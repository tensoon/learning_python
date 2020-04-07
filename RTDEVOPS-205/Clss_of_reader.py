import time
from configparser import ConfigParser
from pathlib import Path
import re
import pandas as pd
from datetime import date, datetime, timedelta
from tabulate import tabulate


from RTD.PythonCore.Logging.Logger import Logger
from RTD.PythonCore.Logging.LoggerToScreenAdapter import LoggerToScreenAdapter
from RTD.PythonCore.Logging.LoggerToSyslogAdapter import LoggerToSyslogAdapter
#from RTD.PythonCore.Version import Version
from RTD.PythonCore.FileSystemHelper import FileSystemHelper

##############################################################
# (C) 2020 Morningstar all rights reserved
##############################################################

class SendstatsChecker:
    
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("config/config.ini")
        self.loggerAdapter = LoggerToScreenAdapter()
        self.loggerAdapter = LoggerToSyslogAdapter(self.config)
        self.logger = Logger([self.loggerAdapter])
        self.day_today = date.today().strftime("%a")
        self.time_now = datetime.now().strftime("%H:%M")
        self.pattern = re.compile(r"FH\_\d+")
        self.feed_section = list(filter(self.pattern.match, self.config.sections()))


# find file created today with file pattern in config file
    def file_finder(self,folder):
        default_name = ["Sendstats.log"]
        try:
            file_name = list(self.config["General"]["file_pattern"].split(","))
            if file_name == ['']:
                file_name = default_name
        except KeyError as error:
            self.logger.ERROR(f"Check config file. Enter Sendstat file name pattern in {error}")
        
        #if file_name is None:
            #file_name = __DEFAULT_FILE_NAME
        
        today = datetime.today().strftime("%Y-%m-%d")
        check = FileSystemHelper.getFiles(folder, file_name)

        for file in check:
            created_date = datetime.fromtimestamp(Path(file).lstat().st_ctime).strftime("%Y-%m-%d")
            if created_date == today:
                return file

# read the file
    def reader(self,folder,fhname,check,lines):
        file = self.file_finder(folder)
        if file == None:
            self.logger.CRIT(f"""Feedhandler={fhname}, Status=Failed, Reason="Sendstats file not found", Folder={folder}.""")
        else:
            df = pd.read_csv(file)
            df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time']) #creating Datetime 
            df.set_index("DateTime", inplace=True) #setting datetime as index

            tail_df = df.tail(lines).filter(["Time", "Messages", "Bytes"]) #tailing last few line set in config file.
            byte = tail_df.where(tail_df["Bytes"] > 0).dropna() # drops all 0 Bytes

            last_time = byte["Time"].tail(1).to_string(index=False,header=False).strip()
            last_msg = byte["Messages"].tail(1).to_string(index=False,header=False).strip()
            last_bytes = byte["Bytes"].tail(1).to_string(index=False,header=False).strip()

            time_ago = (datetime.now() - timedelta(minutes=lines)).strftime("%H:%M") #finding time 10(lines) minutes ago.
            bet_time = tail_df["Time"].between_time(time_ago,self.time_now)
            
            #Check if there was anything written in last 10(lines). If empty will fail the check.
            if len(bet_time) != 0:
                if check == 1: # Initial check PRC1
                    if len(byte) != 0:
                        self.logger.INFO(f"Feedhandler={fhname}, Status=Passed, Time={last_time}, BytesReceived={last_bytes}, No of Message={last_msg}.")
                    else:
                        self.logger.CRIT(f"""Feedhandler={fhname}, Status=Failed. Reason="Data not Received", Folder={folder}""")
                elif check == 2: #Constant update check PRC2
                    byte["TimeDiff"] = pd.to_timedelta(byte["Time"]).diff(1).dt.floor('T').dt.total_seconds()/60 #creating timediff column.
                    max_diff = byte["TimeDiff"].max().astype(int)
                    if max_diff > 1.5: #if time difference is greater than 2 mins
                        self.logger.INFO(f"""Feedhandler={fhname}, Status=Failed, Reason="Sendstat not updated continuously", Folder={folder}, Diff={max_diff} min""")
                    else:
                        self.logger.INFO(f"Feedhandler={fhname}, Status=Passed, Time={last_time}, BytesReceived={last_bytes}, No of Message={last_msg}.")
                elif check == 3: # On Demand check from the menu
                    check3df = tail_df[['Bytes', 'Messages']]
                    print(tabulate(check3df, headers='keys', tablefmt='psql', floatfmt=".0f"))
            else:
                self.logger.CRIT(f"""Feedhandler={fhname}, Status=Failed, Reason="Sendstat not updated in {lines} min" Folder={folder}""")


    def config_checker(self,filename,fhname=None):
        self.logger.INFO(f"Starting Config check for {fhname}.")
        with open(filename, "r") as configfile:
            if 'SendBlocksToMcast=0' in configfile.read():
                self.logger.CRIT(f"""Feedhandler={fhname}, Status=Failed, Reason="SendBlockstoMcast set to 0", File={filename}""")
            else:
                self.logger.INFO(f"Config check complete with no issues for {fhname}.")

            
    def check(self):       
        for options in self.feed_section:
            try:
                fhname = self.config[options]["Feedhandler_Name"]
                days = self.config[options]["days"]
                check_1 = self.config[options]["Initial_check"]
                check_1_lines = int(self.config[options]["Initial_check_lines_to_read"])
                check_2 = self.config[options]["Continuous_check"]
                check_2_lines = int(self.config[options]["Continuous_check_lines_to_read"])
                folder_to_check = self.config[options]["Folder"]
                config_file = self.config[options]["config_file"]

            except KeyError as error:
                self.logger.ERROR(f"Empty value found for options in Config file for {error}")

            try:
                if (self.day_today in days) and (self.time_now == check_1):
                    self.logger.INFO(f"Starting Initial Sendstats Check for {fhname} in {folder_to_check}.")

                    self.reader(folder_to_check,fhname,1,check_1_lines)
                    self.config_checker(config_file,fhname)

                elif (self.day_today in days) and (self.time_now == check_2):
                    self.logger.INFO(f"Starting Continuous Sendstats Check for {fhname} in {folder_to_check}.")

                    self.reader(folder_to_check,fhname,2,check_2_lines)
            except UnboundLocalError as error:
                self.logger.ERROR(f"Check config file. {error}")




if __name__ == "__main__":
    s = SendstatsChecker()
    s.check()

    

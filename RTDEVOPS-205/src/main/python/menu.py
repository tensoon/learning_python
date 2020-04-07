import time
import sys
from Clss_of_reader import *
import schedule
import os
from threading import Thread
import win32console, win32gui, win32con

#Hide console x[close] button to stop accidentally closing
hwnd = win32console.GetConsoleWindow()
if hwnd:
   hMenu = win32gui.GetSystemMenu(hwnd, 0)
   if hMenu:
       win32gui.DeleteMenu(hMenu, win32con.SC_CLOSE, win32con.MF_BYCOMMAND)

ssc = SendstatsChecker()

def call_checks(menu_item, fh_item): #Checks to run
    if menu_item == 1:
        ask = int(input("Enter minutes to check: "))
        folder = ssc.config["FH_" + str(fh_item)]["Folder"]
        fhname = ssc.config["FH_" + str(fh_item)]["Feedhandler_Name"]
        ssc.reader(folder, fhname, 3, ask)
        os.system('pause')
    elif menu_item == 2:
        ssc.config_checker(ssc.config["FH_" + str(fh_item)]["config_file"], ssc.config["FH_" + str(fh_item)]["FeedHandler_Name"])
    elif menu_item == 3:
        reader = ConfigParser()
        configfile = ssc.config["FH_" + str(fh_item)]["config_file"]
        reader.read(configfile)
        mcast_name = re.compile(r"MCastSend|MCast")
        mcast_section = list(filter(mcast_name.match, reader.sections()))

        for items in mcast_section:
            mcast_ip = reader[items]["DataIpAddress"]
            local_ip = reader[items]["LocalIpAddress"]
            port = reader[items]["IpPort"]
        print(f"McastSend setting for {ssc.config['FH_' + str(fh_item)]['FeedHandler_Name']}\n")
        print(f"DataIpAddress={mcast_ip}\nLocalIpAddress={local_ip}\nIpPort={port}")
        os.system('pause')
           
def sub_menu(menu_item): #Displays list of feedhandlers to run checks on
    if menu_item == 4: #Quit
            ask = input("Are you sure you want to close the application? Type 'YES' to close the app.  ")
            if ask==str("YES"):
                ssc.logger.INFO("Sendstats checker stopped.")
                time.sleep(2)
                sys.exit()
            else:
                main_menu()

    fh_n = [(ssc.config[options]["Feedhandler_Name"]) for options in ssc.feed_section]
    return_num = (len(fh_n) + 1)
    
    while True:
        print("========Select FeedHandler==========")
        for index, options in enumerate(fh_n, 1):
                print(f"""\t{index}. {options}""")
        print("\t" + str(return_num)  + ". Return to Main menu")
        try:
            fh_item = int(input("Enter option:  "))
        except ValueError:
            continue
        except UnboundLocalError:
            continue
        if fh_item == return_num:
            main_menu()
        elif fh_item > return_num:
            continue
        else:
            call_checks(menu_item, fh_item)

# Display main menu
def main_menu(): 
    menu = [
        "Check last few minutes of sendstats", 
        "Check SendBlocksToMcast setting for FeedHandler",
        "Lookup Mcast and Local IP address set for Feedhandler",
        "Quit"
    ]
    while True:
        print("============Sendstat Check Menu========================")
        for index, items in enumerate(menu,1):
            print(f"\t{index}. {items}")
            
        try:
            check_id = int(input("Enter option:  "))
            if check_id > len(menu):
                continue
            else:
                sub_menu(check_id)
        except ValueError:
            continue












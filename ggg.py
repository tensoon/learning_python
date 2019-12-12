from ftplib import FTP
import csv

src = r'the path to your credentials and hostname'

with open(src, 'r') as creds:
    reader = csv.DictReader(creds)
    for line in reader:
        host = str(line['host'])
        username = str(line['username'])
        password = str(line['password'])

# Connect and list contents.
ftp = FTP(host=host)
ftp.login(user=username, passwd=password)
list_cont = ftp.nlst()

# The below will create a list form list_cont only containing the items we are concerned with.
# This is so that we can then sort the new list and always download the most recent item.
substr = 'part of filename to filter for'
final_list = list(filter(lambda s: substr in s, list_cont))
final_list.sort()
file_to_get = final_list[-1]

# Download happens here:
def grab_file(fname):
    print(f"Downloading {fname}")
    ftp.retrbinary('RETR ' + fname, open(fname, 'wb').write, 2400)
    print(f"Successfully downloaded {fname}")
    ftp.quit()

grab_file(file_to_get)
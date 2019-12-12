import csv

src = r'C:\Users\balin\Desktop\Source\credentials.csv'

with open(src, 'r') as creds:
    reader = csv.DictReader(creds)
    for line in reader:
        host = str(line['host'])
        username = str(line['username'])
        password = str(line['password'])


print(host, username, password)
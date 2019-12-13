from configparser import ConfigParser

src = r"C:\Users\balin\Desktop\Source\config.ini"

config = ConfigParser()

config.read(src)
host = config['FTP']['host']
username = config['FTP']['username']
password = config['FTP']['password']

print(host, username, password)

'''config['FTP'] = {
    'host': 'mft.coppclark.com',
    'username': 'Morningstar',
    'password': '9a-6L7Rh'
}

with open('config.ini', 'w') as f:
    config.write(f)'''
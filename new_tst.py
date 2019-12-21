from configparser import ConfigParser

src = r"/path/to/config/file"

config = ConfigParser()

config.read(src)
host = config['FTP']['host']
username = config['FTP']['username']
password = config['FTP']['password']

print(host, username, password)

'''config['FTP'] = {
    'host': 'url.goes.here',
    'username': 'username',
    'password': 'password'
}

with open('config.ini', 'w') as f:
    config.write(f)'''

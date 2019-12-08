from ftplib import FTP

ftp = FTP(host='url goes here')
ftp.login(user='username', passwd='password')
list_cont = ftp.nlst()

substr = 'ExchangeTrading'
exchange_trading = list(filter(lambda s: substr in s, list_cont))
exchange_trading.sort()
file_to_get = exchange_trading[-1]


def grabFile(fname):
    print(f"Downloading {fname}")
    ftp.retrbinary('RETR ' + fname, open(fname, 'wb').write, 2400)
    print(f"Successfully downloaded {fname}")
    ftp.quit()

grabFile(file_to_get)
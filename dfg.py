ftp_dir_list = ['CentreChangeReport_20190919.txt', 'CentreChangeReport_20191114.txt', 'ExchangeSettlement_20190919.txt', \
     'ExchangeSettlement_20191003.txt', 'ExchangeSettlement_20191017.txt', 'ExchangeSettlement_20191031.txt', \
         'ExchangeSettlement_20191114.txt', 'ExchangeTrading_20200106.txt', 'ExchangeSettlement_20191128.txt', 'ExchangeTrading_20190919.txt', \
             'ExchangeTrading_20191003.txt', 'ExchangeTrading_20191017.txt', 'ExchangeTrading_20191031.txt', \
                 'ExchangeTrading_20191114.txt', 'ExchangeTrading_20191128.txt', 'ExchangeTrading_20191206.txt', 'THR_20190920.csv.zip', \
                     'THR_20191018.csv.zip', 'THR_20191122.csv.zip']

#print(ftp_dir_list)
substr = 'ExchangeTrading'
res = list(filter(lambda s: substr in s, ftp_dir_list))

res.sort()

file_to_get = res[-1]

print(file_to_get)
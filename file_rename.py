import os

#src = r'/datastore/nas/Downloads'
src = r'\\10.20.30.26\nas\Downloads'

for root, subdirs, files in os.walk(src):
    for file in files:
        print(file)
        '''if file[-3] == '.str':
            print('It exists.')
        else:
            print('Not found.')'''

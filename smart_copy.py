import os
import re
import shutil

''' 
The below code isn't pretty but it does the job.
I would like to improve this by adding some copy confirmation and a progress status.
Probably also create actual functions that will perfom these operations.
'''
username = input(str('Provide a username: '))
password = input(str('And a password: '))

# src = os.getcwd()
src = input('Provide a source dir: ')
#src_files = os.listdir(src)
# src = r'Your source goes here'
pattern = r'[\w]{2}-[\w]{3}-[\w]{3}-[\d]\w*'
d_sl = r'\\'
dest_fin = r'c$\ticker\in'

for file_name in os.listdir(src):
    result = re.search(pattern, file_name)
    dest_srv = result.group(0)
    full_file_name = os.path.join(src, file_name)
    dest = os.path.join(d_sl, dest_srv, dest_fin)
    if os.path.isfile(full_file_name):
        dest = os.path.join(d_sl, dest_srv, dest_fin)
        os.system(f"net use {dest} /user:{username} {password} 2>&1>null")
        shutil.copy(full_file_name, dest)
        print(f"{file_name} copied to {dest_srv}")
        os.system("net use * /delete /y 2>&1>null")


# A version using slicing below:

'''for file_name in os.listdir(src):
    dest_srv = file_name[14:-4] # This will also work and produce the same result as the regex*.
    full_file_name = os.path.join(src, file_name)
    dest = os.path.join(d_sl, dest_srv, dest_fin)
    if os.path.isfile(full_file_name):
        dest = os.path.join(d_sl, dest_srv, dest_fin)
        os.system(f"net use {dest} /user:{username} {password} 2>&1>null")
        shutil.copy(full_file_name, dest)
        print(f"{file_name} copied to {dest_srv}")
        os.system("net use * /delete /y 2>&1>null")'''
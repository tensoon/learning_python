import os, time, sys

folder_path = r"C:\Users\balin\OneDrive\Documents\Rockstar Games\Red Dead Redemption 2\Settings"
starts_with = r"sga"

for file in os.listdir(folder_path):
    file_full_path = os.path.join(folder_path,file)
    if file.startswith(starts_with):
             os.remove(file_full_path)
             print ("File Removed: " , file_full_path)
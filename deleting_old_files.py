import os, time, sys

folder_path = r"C:\Users\nbalinsk\Downloads"
# file_ends_with = ".txt" < -- Specific file type to be deleted
days = 1

now = time.time()
only_files = []

for file in os.listdir(folder_path):
    file_full_path = os.path.join(folder_path, file)
    if os.path.isfile(file_full_path):  # and file.endswith(file_ends_with):
        # Delete files older than x days
        if os.stat(file_full_path).st_mtime < now - days * 86400:
            os.remove(file_full_path)
            print("File Removed: ", file_full_path)

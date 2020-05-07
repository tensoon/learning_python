import os
import time
import glob

here = os.getcwd()

g_there = r"c:\**\*"
there = r"\\10.20.30.9\nas\Movies\**\*h264*"
start = time.time()


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


files = glob.glob(f"{there}", recursive=True)
print(files)
end = time.time()
print(end - start)

""" print(getListOfFiles(there))
end = time.time()
print(end - start) """

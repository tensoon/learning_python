import os

BasePath = input("Where do you want to make your folder?: ")
FolderFiles = input("Enter the file name to refer: ")
SubFolder = input("Is there any subfolders you want to create: ")
x = SubFolder.split(",")


with open(FolderFiles, "r") as f:
    mklst = f.read().splitlines()
    for servers in mklst:
        try:
            os.makedirs(os.path.join(BasePath, servers))
        except OSError:
            pass
        for folder in x:
            try:
                os.makedirs(os.path.join(BasePath, servers, folder))
            except OSError:
                pass

from pathlib import Path
import os

class CRUDFile:

    #For working in user preffered folder
    # def __init__(self, folder_name = None):
    #      # Allow user to set custom folder or default to 'File Handling Project'
    #     if not folder_name:
    #         folder = "File Handling Project"
    #     self.base_path = Path(folder)
    #     self.base_path.mkdir(exist_ok = True)               #ensures the folder exists

    def readFileAndFolder(self):
        # p = Path('base_path')                                   #For working in user preffered folder
        p = Path('')
        items = list(p.rglob('*'))
        for i in items:
            print(i)

    def createFile(self):
        self.readFileAndFolder()
        name = input("Enter your file name: ")
        # p = self.base_path / name                                #For working in user preffered folder
        p = Path(name)
        if p.exists():
            print("File Already exists!")
        else: 
            with open(p, 'w') as fs:
                data = input("Enter the data that you want to enter in your file: ")
                fs.write(data)
                print("Data written succesfully!")

    def readFile(self):
            self.readFileAndFolder()
            name = input("Enter your file name you want to read: ")  
            p = Path(name)
            if not p.exists():
                print("File Not Found!")
            else: 
                with open(p) as fs:
                    print(fs.read())

    def updateFile(self):
        self.readFileAndFolder()
        name = input("Enter your file name you want to update: ")
        p = Path(name)
        if not p.exists():
            print("File not exists!")
        else: 
            with open(p, 'a') as fs:
                data = input("Enter the data that you want to append in your file: ")
                fs.write(data)
                print("Data written succesfully!")

    def deleteFile(self):
        self.readFileAndFolder()
        name = input("Enter your file name you want to delete: ")
        p = Path(name)
        if not p.exists():
            print("File not exists!")
        else: 
            os.remove(name) 

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for appending the file")
print("Press 4 for deleting the file")

#For working in user preffered folder
# folder = input("Enter the folder that you want to work with (deafult folder: File Handling Projects): ")
# ope = CRUDFile(folder_name = folder)

ope = CRUDFile()
check = int(input("Enter your response: "))

if check == 1:
    ope.createFile()

if check == 2:
    ope.readFile()

if check == 3:
    ope.updateFile()

if check == 4:
    ope.deleteFile()
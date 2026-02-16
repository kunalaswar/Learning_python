# #! Creating the folder
#* 1)
# import os
# try:
        
#     os.mkdir("Maharastra")
#     print("Folder is Created successfully ---verify ")
# except FileExistsError:
#     print("\tFile is Already Exist ")
# except FileNotFoundError:
#     print("File is Not Found Error ")

#^--------------------------------------------------------------------------------------------------
#*2)
#!Creating The folder Hierarchy
# import os
# try:
#     os.makedirs("Maharastra\\Akola")
#     print("FIle is Created Successfully in the file of file--verify")
# except FileExistsError:
#     print("file is already is exist in the file of maharastra ")


# #!Creating The folder Hierarchy 
#* Creating the Folder in the Folder of Akola in HKD
# import os
# try:
#     os.makedirs("Maharastra\\Akola\\HKD")
#     print("Folder  is Created Successfully in the file of file--verify")
# except FileExistsError:
#     print("file is already is exist in the file of maharastra ")

#^--------------------------------------------------------------------------------------------------
#
#Creating Folders Hierarchy
#OSCreateFoldersHierarchy.py
# import os
# try:
#     os.makedirs("D:\\PYTHON FULL STACK\\Practice\\OSMODULE\\Apple\\Mango\\Kiwi")
#     print("Folders Hierarchy Created--verify")
# except FileExistsError:
#     print("Folders Hierarchy Alerady Exist")

#^--------------------------------------------------------------------------------------------------
#!Creating the Folder Hierarchy 
#* Creating the Folder of the IN side of the Akola -Again Created
# import os
# try:
#     os.makedirs("Maharastra\\Akola\\Telhara")
#     print("Folder is  Created Successfully in the File of Akola --Again ")
# except FileExistsError:
#     print("Folder already exist in the Akola folder --Try again in another Name please ")    

#^--------------------------------------------------------------------------------------------------
#! Creating the Folder Hierarchy 
#* Creating the Folder of the In Side of the root Folder of Maharastra Again
# import os
# try:
#     os.makedirs("TS")
#     print("Folder is created in the main Root file That is TS")
# except FileExistsError:
#     print("Folder is Already Exist")

#^--------------------------------------------------------------------------------------------------

#! Write a program to Remove the Single Folder

# import os
# try:
#     os.rmdir("D:\\PYTHON FULL STACK\\Practice\\OSMODULE\\Maharastra\\Akola\\Telhara")
#     print("folder is Remove Successfully --verify")
# except FileNotFoundError:
#     print("FIle is not Found here HOW I CAN REMOVE")

#^--------------------------------------------------------------------------------------------------
# ! Write a program to Remove the  Folder Hierarchy in the file 
# D: \\PYTHON FULL STACK\\Practice\\OSMODULE\\Maharastra\\Akola\\Telhara"

# import os
# try:
        
#     os.removedirs("D:\\PYTHON FULL STACK\\Practice\\OSMODULE\\Apple\\Mango\\Kiwi")
#     print("Folder is Remove Successfully ---verify")
# except FileNotFoundError:
#     print("File is not found in the Directory How i can remove folder is not found")    

# # except FileExistsError    
#^--------------------------------------------------------------------------------------------------
#! Remove file name from folder 
# import os
# try:
#     os.remove("Maharastra\\Akola\\File1.data")
#     print("File is remove the Current folder --- Verify")
# except FileExistsError:
#     print("File is already Exist ")

# except FileNotFoundError:
#     print("File is not found from this folder")

#^--------------------------------------------------------------------------------------------------

#! Rename a file from the folder
# import os
# try:
#     # os.rename("Apple\\Banana","Apple\\KUNAL")
#     os.rename("Apple\\KUNAL","Apple\\Banana")
#     print("File Nmae is changed Try to --Verify")
# except FileNotFoundError:
#     print("File is not found How to Modify/ Rename the Folder name")    
#^--------------------------------------------------------------------------------------------------

#! Rename the FILE NAME from the folde name
# import os
# try:
#     # os.rename("Maharastra\\File1.data","Maharastra\\RENMAE.data")
#     os.rename("Maharastra\\RENMAE.data","Maharastra\\File1.data")
#     print("FILE is rename successfully check ---Verify")
# except FileNotFoundError:
#     print("File is not Found Error This file is Not in the file")    
# except FileExistsError:
#     print("File is alreday exist")    














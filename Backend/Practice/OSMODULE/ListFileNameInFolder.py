
#^----------------------------------------------------------------------------------------------------
#! Program Listing the Files in Folder
# import os
# # try:
# filedata=os.listdir("D:\\PYTHON FULL STACK\\Core python\\Class Notes on 20TH NOV 2024-20240812T114336Z-001")
# print(filedata,end="")


#^----------------------------------------------------------------------------------------------------
#!program Listing the file in folder
# import os
# # filedata=os.listdir("Maharastra")
# filedata=os.listdir("D:\\PYTHON FULL STACK")
# print(filedata)

#^----------------------------------------------------------------------------------------------------
#!Program Listing the Files in Folder
#ListFilesEx2.py

# import os
# FilesList=os.listdir(".")
# print("-----------------------------------")
# for filename in FilesList:
#     print("\t{}".format(filename))
# print("-----------------------------------")

#^----------------------------------------------------------------------------------------------------
#!Program Listing the Files in Folder
#ListFilesEx3.py
# import os
# FilesList=os.listdir(".")
# print("Total  Number of Files=",len(FilesList))
# print("-----------------------------------")
# nopf=0
# for filename in FilesList:
#     if(filename.endswith(".py")):
#         print("\t{}".format(filename))
#         nopf=nopf+1
# print("-----------------------------------")
# print("Number of Python Files=",nopf)
# print("-----------------------------------")
#^----------------------------------------------------------------------------------------------------

# import os
# #filedata=os.listdir(".")
# filedata=os.listdir("D:\\PYTHON FULL STACK\\Core python\\Class Notes on 20TH NOV 2024-20240812T114336Z-001")
# print("Total number file=",len(filedata))
# print("-----------------------------------")
# nopy=0
# for val in filedata:
#     if val.endswith(".py"):
            
#         print(f"\t{val}")
#         nopy=nopy+1

# print("-----------------------------------")
# print("Number of python file ONLY =",nopy)

#^----------------------------------------------------------------------------------------------------
   #!Program Listing the Files in Folder
# import os
# filedata=os.listdir(".")   
# print("TOTAL Number of file =",filedata)
# print("---------------------------------")
# datafile=filter(lambda filename:filename.endswith(".data"),filedata)
# x=list(datafile)
# for val in x:
#     print(val)

#^----------------------------------------------------------------------------------------------------

# import os   
# filedata=os.listdir(".")   
# # print("TOTAL Number of file =",len(filedata))
# # print("---------------------------------")
# datafile=list(filter(lambda filename:filename.endswith(".py"),filedata))
# for val in datafile:
#     print(val)
    
# print("Total number of file  with ( .data )=",datafile)

#^----------------------------------------------------------------------------------------------------














#^----------------------------------------------------------------------------------------------------

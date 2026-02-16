# try:
#     with open("stud2.data","x") as fp:
#         print("\tInside of with open() as Indantation---------")
#         print("\tWRITE THE DATA FROM FILE SUCCESSFULLY")
#         print("\tFILE MODE = ",fp.mode)
#         print("\tFile NAME = ",fp.name)
#         print("\t WE CAN READ DATA FORM FILE = ",fp.writable())
#         print("\t WE CAN WRITE DATA FORM FILE = ",fp.readable())
#         print("\t IS FILE CLOSED =", fp.closed)
#         print("-----------------------------------------")
        
#     print("WE ARE COME OUT FROM INDENTATION BLOCK")    
#     print("\t IS FILE CLOSED =", fp.closed)
# except FileExistsError:
#     print("\tFile Already Exits")    

#^--------------------------------------------------------------------------------------------------
#* IF FILE IS ALREADY CREATED CREATED THEN IT'S PROVIDE AN ERROR FILE ALREADY EXIST
# try:
#     with open("stud3.data","x") as fp:
#         print("WE ARE INSIDE OF INDEBTATION BLOCK")
#         print("FILE NAME = ",fp.name)
#         print("FILE MODE = ",fp.mode)
#         print("WE CAN WRITE DATA FROM FILE = ",fp.writable())
#         print("WE CAN READ DATA FROM FILE = ",fp.readable())
#         print("IS FILE CLOSED = ",fp.closed)
#     print("WE ARE COME FROM WITH OPEN( ) AS INDENTATION BLOCK = ",fp.closed)    
# except FileExistsError:
#     print("\t\tFile is already exist")    

#^--------------------------------------------------------------------------------------------------
try:
    with open("sample.py","x+") as fp:
        print("WE ARE INSIDE OF INDEBTATION BLOCK")
        print("FILE NAME = ",fp.name)
        print("FILE MODE = ",fp.mode)
        print("WE CAN WRITE DATA FROM FILE = ",fp.writable())
        print("WE CAN READ DATA FROM FILE = ",fp.readable())
        print("IS FILE CLOSED = ",fp.closed)
    print("WE ARE COME FROM WITH OPEN( ) AS INDENTATION BLOCK = ",fp.closed)    
except FileExistsError:
    print("\t\tFile is already exist")    




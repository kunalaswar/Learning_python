 
#! write a python program which will validate mobile number by using Regular Expression
#^-----------------------------------------------------------------------------------------------
# import re 
# import sys
# while(True):
#     mno = input("Enter  a a Mobile number :")
#     if (len(mno)==10):
#         res = re.search("\d{10}",mno)
#         if res!=None:
#             print(f"{mno} is valid Mobile number ")
#             break
#             # sys.exit()
#         else:
#             print(f"{mno} is Invalid Mobile number ")    
    
#     else:
#         print(f"{mno} is Invalid Mobile number Due to its Invalid Length Try- Again")

#^-----------------------------------------------------------------------------------------------
#!we have to Mobile number start with 98 99 88 89 

# import re
# while (True):
#     mno =input("Enter a Mobile number :")
#     if len(mno) ==10:
#         res = re.search("[98]\d{8}",mno)
#         if res!=None:
#             print(f"{mno} is valid Mobile number ")
#             break
#         else:
#             print(f"{mno} is Invalid Mobile number ")    
    
#     else:
#         print(f"{mno} is Invalid Number Due to its Invalid Length Try- Again")    

#^-----------------------------------------------------------------------------------------------
#! write a python program Which will Extract name of the student from the Given data  
# program from Extracting name of the students from Given Text data
# import re
# gd = "Rossum is the developer of python, Travis is the developer of numpy,Kinnet is developer of pandas,Ritche is the developer of the c language "
# nameslist = re.findall("[A-Z][a-z]+",gd)
# print(nameslist)
# for val in nameslist:
#     print(val)

#^-----------------------------------------------------------------------------------------------
#! program for Extracting the name and marksof the students from given text data
# import re
# gd = "Rossum is the developer of python got 56, Travis is the developer of numpy got 68,Kinnet is developer of pandas got 59,Ritche is the developer of the c language got 62"
# nameslist = re.findall("[A-Z][a-z]+",gd)  
# print(nameslist)
# print("Names List :")
# for val in nameslist:
#     print(f"\t{val}")

# markslist = re.findall("\d{2,3}",gd)
# print(markslist)
# print("Marks List :")
# for val in markslist:
#     print(f"\t{val}")

#* ANOTHER WAY 

# nameslist = re.findall("[A-Z][a-z]+",gd)  
# markslist = re.findall("\d{2,3}",gd)
# print("--------------------------------")
# print(f"\tnames\tmarks")
# print("--------------------------------")
# for names ,marks in zip(nameslist,markslist):
#     print(f"\t{names} \t{marks}")
# print("--------------------------------")

#! write a python program for Extracting the students names,marks where the information present is file (student.data) by using regular Expression
# import re

# try:
#     with open("","r") as fp:  #^ Put it File location
#         filedata = fp.read() #read() function return the value into the str
#         nameslist = re.findall("[A-Z][a-z]+",filedata)
#         markslist = re.findall("\d{2,3}",filedata)
#         print("---------------------------------")
#         for names,marks in zip(nameslist,markslist):
#             print(f"\t{names}\t{marks}")
#         print("-----------------------------------")
# except FileNotFoundError:
#     # print("FIle is not Found ")
#     print("File does Not Exist")


#! write a python program which will retrive mail ids from the Given data where it is present in file
#^ Do it from your side 





#! Sub() function Example 
# import re
# txt = "The rain in spain"
# x = re.sub("\s","9",txt)
# print(x)  #todo- O/P ---> The9rain9in9spain
#^-----------------------------------------------------------------------------------------------














#^-----------------------------------------------------------------------------------------------
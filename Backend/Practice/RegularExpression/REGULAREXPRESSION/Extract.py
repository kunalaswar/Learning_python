
#^===============================================================================================
#! Program for extracting the Names from Given Text Data
#! NamesExtractEx1.py
# import re
# gd = "Rossum is dev of Python , Gosling the dev of java ,Travis is the dev of numpy and Kinney is the dev of pandas"
# sp = "[A-Z][a-z]+"
# names = re.finditer(sp,gd)
# for name in names:
#     print(f"start Value{name.start()} \tEnd Value {name.end()}\tGroup value {name.group()}")

#^===============================================================================================
# import re

# gd = "Rossum is dev of python , Gosling the dev of java ,Travis is the dev of numpy and Kinney is the dev of pandas Kvr is the trainer of python"
# sp = "[A-Z][a-z]+"
# names = re.findall(sp,gd)
# print("List of Name :")
# # print(names)
# for val in names:
#     print(val)
#^===============================================================================================

#!write a Which Will Extract Marks of Students 
#! Program for extracting the Names and marks from Given Text Data
#! NamesMarksExtractEx1.py
# import re
# gd="Rossum got 88 marks , Gosling got 66 marks , Ritche got 65 marks , Travis got 99 marks and Hinter got 56 marks and Kvr got 11 marks"
# sp = r"\d{2}"
# marklist = re.findall(sp,gd)
# print("MArklist")
# print(marklist)

#^===============================================================================================
#! Program for extracting the Names and marks from Given Text Data
#! NamesMarksExtractEx1.py
# import re
# gd="Rossum got 88 marks , Gosling got 66 marks , Ritche got 65 marks , Travis got 99 marks and Hinter got 56 marks and Kvr got 11 marks"
# msp = r"\d{2}"
# nsp = r"[A-Z][a-z]+"
# marklist= re.findall(msp,gd)
# namelist= re.findall(nsp,gd)
# print(marklist)
# print(namelist)

# print("\tnames \t Marks")
# print("-----------------------")
# for name,mark in zip(marklist,namelist):
#     print(f"\t{name} \t{mark}")

#^===============================================================================================
#! Program for extracting the Names and marks from Given Text Data which is Present in File
#! NamesMarksExtractEx2.py

# import re
# try:
        
#     with open("D:\\PYTHON FULL STACK\\Practice\\RegularExpression\\REGULAREXPRESSION\\data.txt","r") as fp:
#         filedata = fp.read()
#         print(filedata)
#         namelist = re.findall(r"[A-Z][a-z]+",filedata)
#         marklist = re.findall("\d{2}",filedata)
#         # print(namelist)
#         # print(marklist)
#         print("-------------------------------")
#         for name,marks in zip(namelist,marklist):
#             print(f"\t{name} \t{marks}")

        #*Apply the Regular Expression
# except FileNotFoundError:
#     print("File Does not Exist :")
#^===============================================================================================
#! Program for extracting the Names and marks from Given Text Data which is Present in File
#! NamesMarksExtractEx3.py
# #todo - Mails 
# import re
# try:
#         with open("D:\\PYTHON FULL STACK\\Practice\\RegularExpression\\REGULAREXPRESSION\\data2.txt","r") as fp:
#             filedata = fp.read()
#             namelist = re.findall(r"[A-Z][a-z]+",filedata)
#             mailslist  = re.findall(r"\S+@\S+",filedata)
#             for n,m in zip(namelist,mailslist):
#                    print(f"{n} \t {m}")

# except FileNotFoundError:
#         print("File Does not Exist")        

#^===============================================================================================



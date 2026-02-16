
#^--------------------------------------------------------------------------------------------------
#!#Program for Demonstrating Dict Data to JSON Str Data.
#DictDataToJsonStrData.py
# d={"EmpNo":100,"Name":"travis","sal":5.6,"author":"Scientist"}
# print(d,type(d))
# jsonstrdata=str(d)
# print(jsonstrdata,type(jsonstrdata))

#^--------------------------------------------------------------------------------------------------
#!program to demonstrating the json Data convert str 
# import json
# jsonstr='{"EmpNo":100,"Name":"travis","sal":5.6,"author":"Scientist"}'
# print(jsonstr,type(jsonstr))
# #*to convert a json data into str format
# print("-"*50)
# strobj=json.loads(jsonstr)
# print(strobj,type(strobj))

# for k in strobj:
#     print(f"{k}--->{strobj[k]}")

#^--------------------------------------------------------------------------------------------------
#!Program for Saving Dict Object Data into the JSON File
#!To Save Dict Object Data into JSON File, we use  json.dump(dictobj,FilePointer)
#DictObjectToJsonFile.py
# import json
# dictobj={"EmpNo":100,"Name":"Travis","Sal":5.6,"Author":"Scientist"}
# with open("D:\\PYTHON FULL STACK\\Practice\\JSON\\emp.json","w") as wp:
#     json.dump(dictobj,wp)
#     print("Dict object data saved in json file ")
#^--------------------------------------------------------------------------------------------------
#! data in the from of dict with in dict to the file
#! DictObjectToJsonFile.py
#! Dict of dict Data into the File of Name data.json is saved 
# import json
# dictobj={"data1":{"EmpNo":100,"Name":"Travis","Sal":5.6,"Author":"Scientist"},
#          "data2":{"EmpNo":200,"Name":"aniket","Sal":5.6,"Author":"Software Enginner"}}
# with open("D:\\PYTHON FULL STACK\\Practice\\JSON\\data.json","w") as wp:
#     json.dump(dictobj,wp)
#     print("Dict of dict Data into the File of Name data.json is saved ")



# #^--------------------------------------------------------------------------------------------------

#!Program for Reading JSON File Data into Dict Object 
#!To Read JSON File Data into Dict Object , we use  dictobject=json.load(FilePointer)
#!JsonFileToDictObj1.py
# import json
# try:
# 	with open("E:\\KVR-PYTHON FOR DSC\\KVR-PANDAS-EXCLUSIVE\\DATAFRAME\\DATA SETS\\data.json","r") as fp:
# 			dictobj=json.load(fp)
# 			print("Dict Object Data={}".format(dictobj))
# 			print("--------------------------------------------------------------------")
# 			for k ,v in dictobj.items():
# 				print("{}".format(k))
# 				for key,val in v.items():
# 					print("\t{}---->{}".format(key,val))
# 			print("--------------------------------------------------------------------")
# except FileNotFoundError:
# 	print("File does not Exist")
#!

# import json
# try:
#     with open("D:\\PYTHON FULL STACK\\Practice\\JSON\\data.json","r") as rp:
#         dictobj=json.load(rp)
#         for k,v in dictobj.items():
#             print(f"{k}--->{v}")
#             for j,k in v.items():
#                 print(f"{j}--->{k}")

# except FileNotFoundError:
#     print("File Not found Error please check the file")
#^--------------------------------------------------------------------------------------------------
#Program for Reading JSON File Data into Dict Object 
#To Read JSON File Data into Dict Object , we use  dictobject=json.load(FilePointer)
#JsonFileToDictObj.py
# import json
# try:
#     with open("D:\\PYTHON FULL STACK\\Practice\\JSON\\emp.json","r") as rp:
#         dictobj=json.load(rp)
#         for k in dictobj:
#             print(f"{k}--->{dictobj[k]}")

# except FileNotFoundError:
#     print("FIle Not found there")
    
#^--------------------------------------------------------------------------------------------------







#^--------------------------------------------------------------------------------------------------
# import json
# # Take the json data
# jsondata  = '{"sno":"100","sname":"harsh","mark":"33.35","cname":"SCK"}'
# print(jsondata,type(jsondata))
# # Convert Json data into dict type data
# dictdata = json.loads(jsondata)
# print(dictdata,type(dictdata))
# print("------------------------------")
# for k,v in dictdata.items():
#     print(f"\t{k}\t{v}")
# print("------------------------------")


# import json
# dictobj = {"eno":"100","ename":"Rossum","sal":45.67,"cname":"psf"}
# print(dictobj,type(dictobj))
# #Open the Json file into the write mode
# with open("emp1.json","w") as fp:
#     json.dump(dictobj,fp)
#     print("Dict Object data saved into json file --- Verify ")


# program for Converting  JSON file data to Dict object data ---json.load()
# json File data to dict file data 
# import json
# try:
#     with open("emp1.json","r") as fp:
#         dictobj=json.load(fp)
#         print(dictobj,type(dictobj))
#         print("----------------------------------")
#         for k , v in dictobj.items():
#             print(f"\t{k}\t{v}")
#         print("----------------------------------")    
# except FileNotFoundError:
#     print("File does not Exits ")
 #!
 #^-----------------------------------------------------------------------------------------------------
# try:
        
#     fp=open( "stud1.data","w")

# except FileExistsError:
#     print("File is already exist")    

# else:
#     print("Type of file pointer ",type(fp))   
#     print("FIle is open in write mode ") 
#     print("Is file is closed = ",fp.closed) #todo Attribute 

# finally:
#     print("I am form filnally block and my main perpose is that to CLOSE THE FILE BEACUSE THE FILE IS OPEN IS OPEN MODE AAAND TO CLOSED THE FILE IN  FINLLY BLOCK")
#     print("file is close",fp.closed)
#     fp.close()
#     print("file is close = ",fp.closed)


 #^-----------------------------------------------------------------------------------------------------
#!
# try:

#     fp=("stud1.data","r")
# except FileNotFoundError:
#     print("file is not found How i  read ")    

# else:
#     print("type of file",type(fp))
#     print("file is opening mode",fp.mode)
#     print("FLE NAME ",fp.name)
# finally:
# #
#     print("file is closed =",fp.closed)
#     print("file is closed =",fp.opened)
#     # print("file is ")
#     fp.close()
#     print("file is close",fp.close)

 #^-----------------------------------------------------------------------------------------------------
#^ CHAT GPT

# try:
#     fp = open("stud1.data", "r")
# except FileNotFoundError:
#     print("File is not found. How can I read?")
#     fp = None  # Initialize fp to avoid reference errors
# else:
#     print("Type of file:", type(fp))
#     print("File opening mode:", fp.mode)
#     print("File name:", fp.name)
# finally:
#     if fp is not None:  # Check if fp was successfully opened
#         print("File is closed before closing:", fp.closed)
#         fp.close()
#         print("File is closed after closing:", fp.closed)
#     else:
#         print("File is not open, so no need to close.")

#^-----------------------------------------------------------------------------------------------------
#!
# try:
        
#     with open("stud1.data","r")as fp:
#         print("Inside the Indentation block open")
#         print("File is closed = ",fp.closed)
#         print("FIle Name = ",fp.name)
#         print("FIle Opening  Mode ",fp.mode)
#         print("Can we read the data from the file ",fp.readable())

#     print("out of Indentation block")
#     print("FIle is closed = ",fp.closed)
  
# except FileNotFoundError:
#     print("FIle is not found Error")

#! THIS FILE IS OPEN IN X+ MODE THAT WAY WE CAN NOT RECREATE THE FILE
# try:
#     with open("sample.py","x+")as fp:
#         print("INside the Indentation block")
#         print("FIle name",fp.name)
#         print("IS file is closed",fp.closed)
#         print("File is readABLE = ",fp.readable())
#         print("FIle is writeABLE =",fp.writable())
#     print("COME OUT OF INDENTATION BLOCK !")    

#     print("FIle iss closed ",fp.closed)        
#     # print("File is READABLE ",fp.readable())
# except FileExistsError:
#     print("File IS already Exitst ")    

#!
#todo - IF file is not exist then create it 
# with open("tech.data","w")as fp:
#     print("File is open in write mode ",fp.mode)
#     print("IS File is readable",fp.readable())
#     print("IS file is writeable ",fp.writable())
# print("COme out the Indentation block")    
# print("FIle is closed to the file",fp.closed)
  
#! write the data to the file  

# with open("stud1.data","w")as fp:
#     # fp.write(f"\t1000")
#     # fp.write(f"\tkunal")
#     # fp.write(f"\t23")
#     print("--------------")
#     fp.write(str(1000)+"\t")
#     fp.write("sagar"+"\t")
#     fp.write(str(23)+"\t")

# print("Write the data to the file SEE Successfully")    

#! with the use of the WriteLines function

# x=[100,"kunal",50]
# with open("tech.data","w") as fp:
#     print("FIle is open write the data to the file")
#     # fp.writelines(str(x))
#     # fp.writelines(f"{x} \t")
#     fp.writelines(f"{x}")
#     print("DATA IS WRITE IN THE FILE CHECK IT")

#! program for reading the employee data and writing to the file

# while True:
#     sno=int(input("ENter a sno"))
#     sname=input("ENter a students name")
#     marks=float(input("Enter a students marks"))
#     with open("tech.data","w")as fp:
#         print("FIle is open in the write mode :")
#         fp.writelines(f"{sno},{sname},{marks}")
#         print("data is inserted Successfully")
#     print("write the data into the file successfully")    
#     ch=input("Do you want to Enter  another record ").lower()
#     if ch=="no":
#         break    
        
#!

# with open("tech.data","w")as fp:
#     print("FIle is open in write mode ")
#     print("is this file is writeABLE",fp.writable())
#     print("is this file is readable ",fp.readable())
#     print("file open in mode",fp.mode)
#     print("FIle name",fp.name)
#     print("fille is closed",fp.closed)
#     fp.write(f"{100} {"kunal"} {90}\n")
#     fp.write(f"{200},{"sagar"} {99}\n")
#     fp.write(f"{300} {"paa"} {90}\n")
#     fp.write(f"{400} {"harsh"} {80}")

#     print("DATA is write successfully ")

# # print("FIle is closed",fp.cloesd)    
# print("FIle is cloesd automatically ")


#!
# try :
#     with open("tech.data","r")as fp:
#         print("File is readable",fp.readable())
#         # print("File is writeable",fp.writable())
#         # print("FIle opening mode",fp.mode)
#         filedata=fp.readline()
#         print(filedata,type(filedata))


#     print("COme out of INDENTATION BLOCk")    

# except FileNotFoundError:
#     print("FILe is not found")


#!
# with open("tech.data", "r") as fp:
#     print("file is open mode",fp.mode)
#     filedata=fp.read()
#     print(filedata)

# print(" file  is read Successfully")    
#!

# filename=input("Enter a file file to read the data  to the file ")
# with open(filename,"r") as fp:
#     print("FIle is read check it ")
#     filedata=fp.read()
#     print(filedata)

# print("file is read and come out of indentation block ")

#!
# try :
#     filename=input("Enter a file name :")
#     with open(filename,"a")as fp:
#        fp.write(f"\n{600} {"kfh"} {89}")


#     print("come out of indentation blo;ck")     
#     print("FIle data us write ")

# except FileNotFoundError:
#     print("FIle noot found eree")

#!

# filename=input("Enter a file name :")
# print("ENter a youe file daata and and until your press @")
# with open(filename,"a")as fp:
#     while True:  
#         filedata=input()
#         if filedata !="@":
#             fp.write(filedata +"\n")
#         else:
#             break    

#!
# try:
#     sf=input("ENter a Source file name :")
#     with open(sf,"r") as rp:
#         filedata = rp.read()
#         ds=input("Enter a destination file :")
#         with open(ds,"a")as wp:
#             wp.write(filedata+"\n\n")
            # print("FIle copy sucessfully")
# except FileNotFoundError:
#     print("FIle not found error")

#!
# import pickle
# with open("stud.pick","ab")as fp:
#     print("FIle is open in write mode check it ")
#     sno=int(input("Enter a studentsnumber :"))
#     sname=input("Enter a student nnmse :")
#     marks=float(input("Enter s students marks :"))
#     lst=[]
#     lst.append(sno)
#     lst.append(sname)
#     lst.append(marks)
#     pickle.dump(lst,fp)
#     print("DATA write into the file successfilly")



# import pickle
# with open("stud.pick","rb") as fp:
#     print("Open the file in read mode ")
#     filedata=pickle.load(fp)
#     print(filedata)

#!

# with open("stud1.data","r")as fp:
#     print("FIle is open it write mode")
    
#     filedata=fp.readlines()
#     print(filedata)

#     nl=0
#     nw=0
#     nc=0 
#     # print(filedata)
#     for line in filedata:
#         # print(i)
#         nl=nc + 1
#         nw=nw + len(line.split())
#         nc=nc +len(line)
#     print(nl)  
#     print(nw)
#     print(nc)

# import pickle 
# with open("stud.pick","wb")as fp:
#     # print()
#     # filedata = fp.write()
#     lst=[1,2,3,4,5,6,7,8,9]
#     pickle.dump(lst,fp)
#     print("DATA saved into the file")
    
# # import pickle 
# # with open("stud.pick","rb")as fp:
    
# #     try:
# #         record=pickle.load(fp)
# #         print(record)
# #         # print("DATA saved into the file")
# #         print("DATA read into the file")
# #     except EOFError:
# #         print("FIle is eof Erreo")
    
# #!

#todo - important program 
#todo--------------------------------------------------------------------------------------------------
#! LinearSearchwithOOPs.py
# class Linear:
#     def readvals(self):
#         nov=int(input("Enter How Many Values:"))
#         if(nov<=0):
#             return []
#         else:
#             lst=[]
#             for i in range(1,nov+1):
#                 val=float(input("Enter {} Value:".format(i)))
#                 lst.append(val)
#             else:
#                 return lst
#     def search(self,lst):
#         #Sort the Data of lst
#         lst.sort()  # [-4.0, 1.0, 11.0, 23.0, 45.0]
#         skey=float(input("Enter the search Key:"))
#         sp=-1
#         for i in range(0,len(lst)):
#             if(lst[i]==skey):
#                 sp=i
#                 break
#         if(sp==-1):
#             print("{} does not exist in list of values".format(skey))
#             print("Search is Un-Sucessful")
#         else:
#             print("{} Found at {} Postion".format(skey,sp))

# #Main Program
# lo=Linear()
# lst=lo.readvals()
# if(len(lst)==0):
#     print("List is empty")
# else:
#     lo.search(lst)






# def fun(val,lst):
#     print(val in lst)


# ls1 = [3,4,5,6,7,8]
# v = fun(int(input("Enter val :")),ls1)
# # print("Value is present : ",v)

#todo--------------------------------------------------------------------------------------------------
# import csv
# with open("kunal.csv" ,"r") as fp:
#     csvr=csv.reader(fp)
#     for record in csvr:
#         # print(record)
#         for val in record:
#             print(val)



# with open("kunal.csv" ,"r")as fp:
#     filedata = fp.read()
#     # print(filedata)
#     for val in filedata:
#         print(val,end="")
#     print()

# import csv
# with open("kunal.csv","r")as fp:
#     print("FIle data is read successfully")
#     filedata = csv.DictReader(fp)
#     # print(filedata)
#     for record in filedata:
#         # print(record)
#         for k,v in record.items():
#             print(f"{k} ---> {v}")
        
#! write the data to the to the  file 

# import csv
# ncol=int(input("Enter how many how many column do you want to enter :"))
# if ncol<0:
#     print("INVALID INPUT ")
# else:
#     column=[]
#     for i in range(1,ncol+1):
#         val=input(f"Enter {i} column name :")
#         column.append(val) 
        
#     else:
#         nr = int(input("ENter a how many record do you want to enter :"))
#         if nr<0:
#             print("Invalid input !")
#         else:
                    
#             for val in range(a,nr+1):
#                 val=input(f"ENter a {val} record ")

# # print(column)

# import csv
# ncol=int(input("Enter a how nmay record do you want lto enter :"))
# if ncol<0:
#     print("INVALID INPUT ")
# else:
#     column=[]
#     for i in range(1,ncol+1):
#         val =input(f"ENter a {i} column name :")
#         column.append(val)
               
#     else:
            
#         main_record=[]        
#         nor=int(input("ENter how many recod you want :"))
#         if nor<0:
#             print("INVALID INPUT ")
#         else:
#             record=[]
#             for i in range(1,nor+1):
#                 # val=input("Enter  ")
#                 print(f"ENter {i} record: ")
#                 for k in range(len(column)):
#                     val =input(f"ENter a value for {column[k]}")
#                     record.append(val)
#                 else:
#                     main_record.append(record)    
#             else:
#                 while(True):
                        
#                     filename = input("Enter filename :")            
#                     if filename.endswith(".csv"):
#                         with open(filename,"a")as fp:
#                             # filedata = 
#                             csvr = csv.writer(fp)
#                             csvr.writerow(column)
#                             csvr.writerows(main_record)
#                             print("CSV FILE IS CREATE SUCCESSFULLY ")
#                     else:
#                         print("INVALID FILE NAME TO THE FILE CHECK IT FROM YOUR SIDE ")        
#                         break
                

# import csv
# ncol=int(input("Enter  HOW MANY NUMBER OF COLUMN YOU WANT TO ENTER :"))
# if ncol<0:
#     print("INVALID INPUT ")
# else:
#     column=[]    
#     for i in range(1,ncol+1):
#         val=input("Enter a colume :")
#         column.append(val)
# # print(column)   
#     else:
#         main_record=[]
#         nor=int(input("Enter a to MANY RECORD TO YOU WNAT  TO ENTER : :"))     
#         for i in range(1,nor+1):
#             print(f"Enter {i} vlaue")  
#             if nor<0:
#                 print("INVLAID INPUT ")
#             else:
#                 record={}
#                 for k in range(len(column)):
#                     val=input(f"Enter   a  {column[k]}")   
#                     record[column[k]] = val
#                 else:
#                     main_record.append(record)    
# # print(main_record)                
#         else:
#             while(True):
#                 filename=input("Enter file name:")    
#                 if filename.endswith(".csv"):
#                     with open(filename,"w") as fp:
#                         csvdwr = csv.DictReader(fp,fieldnames=column)
#                         csvdwr.writeheader()
#                         csvdr.writerows(main_record)
#                 else:
#                         print("csv file is saved and recod save succeccfully")


        
#!
# import pickle

        
# with open("stud.pick","rb") as fp:
   
#         # print("File is Created successfully ")
#     while True:
#         try:
#             filedata = pickle.load(fp)
#             # print(filedata)
#             for val in filedata:
#                 print(val)

#         except EOFError:
#             print("EOF ERROR ")


#! create the file 
# import pickle
# def savedata():
#     with open("aa.pick","ab") as fp:
#         x=[10,"paa",90]
#         pickle.dump(x,fp)
#         print("STUDENTSS DATA IS SAVED SUCCESSFULLY")


# savedata()


#!see the data to the file
# import pickle 
# with open("aa.pick","rb") as fp:
#     while True:
#         try:
                    
#             record = pickle.load(fp)
#             # record1 = pickle.load(fp)
#             print(record)
#             # print(record1)
#             # for val in record:
#                 # print(val)
             
#         except EOFError:
#             # print("FIle ")
#             print("-------EOF ERROR ----------------------")
#             break


# import pickle 
# with open ("aa.pick","ab") as fp:
#     print("File is created successfullly")
#     lst=[]
#     sno=int(input("ENter a studentds numbeer :"))
#     name=input("Entre a students name :")
#     marks=float(input("Enter sudents marks :"))
#     lst.append(sno)
#     lst.append(name)
#     lst.append(marks)
#     pickle.dump(lst,fp)
#     print("FIle data is inserted check it ")

    
#!JSON DATA
#todo - convert the json data to the dict data
#* Main memory 
# import json
# jsondata='{"sno":100, "name":"sagar","mark":78}'
# print(jsondata)

# dict = json.loads(jsondata)
# # print(dict,type(dict))
# for k,v in dict.items():
#     print(k,v)


#*main memory 
#todo - to convert the json data into  the str data
# dict={"sno":100, "name":"sagar","mark":78}
# print(dict,type(dict))
# strjson=str(dict)
# print(strjson,type(strjson))

#! to save the data to the  file

# import json
# dict={"sno":100,"name":"KA","mark":90}
# # print(dict)
# # filedata=
# with open("emp.json","a") as fp:
#     json.dump(dict,fp)
#     print("Check it ")


# import json
# with open("emp.json","r") as fp:
#     print("File is open in read mode ")
#     dictobj=json.load(fp)
#     print(dictobj)
#     print(dictobj,type(dictobj))
#     for k,v in dictobj.items():
#         print(f"{k}---{v}")
        
#!

# import csv  
# nc=int(input("Enter how many number of column you want :"))
# if nc < 0:
#     print("Invlaid input ")
# else:
#     column = []
#     for val in range(1,nc+1):
#         value=input("ENter a first column name :")
#         column.append(value)

#     # print(lst)    
#     else:
#         nor=int(input("Enter a how record do you wnat to Enter :"))
#         if nor < 0:
#             print("INVALID INPUT ")
#         else:
#             main_record=[]
#             for i in range(1,nor+1):
#                 print(f"enter {i} RECORD INTO ")    
#                 record=[]
#                 for k in range(len(column)):
#                     values=input(f"Enter a value for {column[k]}")
#                     record.append(values)
#                 # print(record)     
#                 else:
#                     main_record.append(record)    
#                     print(main_record)
                    


#*
# import threading    
# def welcome():
#     print(f"Welcome Executed by {threading.current_thread().name}")


# def hello():
#     print(f"Hello Executed by {threading.current_thread().name}")

# def hi():
#     print(f"Hi Executed by {threading.current_thread().name}")    


# #Main program     
# print("EXecution Started ",threading.current_thread().name)
# welcome()
# hello()
# hi()
# print("EXecution Ended ",threading.current_thread().name)


#* 
# import threading
# def welcome():
#     print(f"Welcome Executed by {threading.current_thread().name}")

# def hello():
#     print(f"hello Executed by {threading.current_thread().name}")

# #main program    
# t1 = threading.Thread(target=welcome)
# t1.name = "harshal"
# t2 = threading.Thread(target=hello)
# t2.name = "Ankit"

#Dispatch the thread
# t1.start()
# t2.start()

# import threading
# print("Active thread name =",threading.current_thread().name)
# noat = threading.active_count()
# print("number of threads which are actively running = ",noat)

# import threading
# t = threading.current_thread()
# print(t.name,type(t))

import threading























































































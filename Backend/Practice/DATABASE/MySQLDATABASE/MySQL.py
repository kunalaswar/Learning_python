# #^---------------------------------------------------------------------------------------------------
#!update From user input on the bases of sno
# import mysql.connector as mc
# while True:

        
#     try:
#         conn = mc.connect(host="localhost",user="root",passwd="kunal123456",database="batch9am")
#         print("COnnected successfully")
#         cur=conn.cursor()
#         sno=int(input("Enter a students number for update Record:"))
#         sname=input("Enter new NAME :")
#         mark=float(input("Enter a New Marks :"))

#         uq=f"update students set sname='{sname}',mark={mark} where sno={sno}"
#         cur.execute(uq)
#         conn.commit()
#         if cur.rowcount >0:
#             print(f"{cur.rowcount} is Modify record")
#         else:
#             print("Record Does not exist")    

#         ch=input("Do you wnat to inter another record")    
#         if ch=="no":
#             print("Tnx for using this program")
#             break
#         elif ch not in ["yes","no"]    :
#             print("You enter invalid input try---again")
#     except mc.DatabaseError as db:
#         print("problem with your code ",db)        
#     except ValueError:
#         print("Dont enter Str Symbols ")    
# #^---------------------------------------------------------------------------------------------------


#! Reding the data from the database

# import mysql.connector as mc
# try:
#     conn=mc.connect(host="localhost",user="root",passwd="kunal123456",database="batch9am")
#     print("connected ")
#     cur=conn.cursor()
#     sq="select * from students"
#     cur.execute(sq)
#     print("READING THE DATA FROM DATABASE")
#     # conn.commit()
#     metadata = cur.description
#     # print(metadata)
#     print("---------------------------------------")
#     for val in metadata:
#         print(val[0],end="\t\t")
#     print()
#     print("---------------------------------------")

#     records=cur.fetchall()
#     # print(records)
#     for record in records:
#         for val in record:
#             print(val,end="\t\t")
#         print()    
#     print("---------------------------------------")

# except mc.DatabaseError as db:
#     print("problem with your python code")

#^--------------------------------------------------------------------------------------------------
#!program for read the column name from database

# import mysql.connector as mc
# try:
#     conn = mc.connect(host="localhost",user="root",passwd="kunal123456",database="batch9am") 
#     print("connected")
#     cur=conn.cursor()
#     print("Cursor object is created")
#     sq="select * from students"
#     cur.execute(sq)
#     # conn.commit()
#     print("-----------------------------------------------")
#     records=cur.description
#     for record in records:
#         print(record[0],end="\t\t") 
#     print()    
#     print("-----------------------------------------------")
# except mc.DatabaseError as db:
#     print("Problem with your code check it",db)    
#^--------------------------------------------------------------------------------------------------
#!#Program for Getting the Records from any Table along with Col Names
#MySQLSelectRecordEx.py
# import mysql.connector as mc
# try:
#     conn=mc.connect(host="localhost",user="root",passwd="kunal123456",database="batch9am")
#     cur=conn.cursor()
#     # print("----------")
#     sq="select * from students"
#     cur.execute(sq)
#     # conn.commit()
#     records=cur.fetchall()
#     # print(records)
#     for record in records:
#         # print(record)
#         for val in record:
#             print(val,end="\t")
#         print()    
# except mc.DatabaseError as db:
#     print("problem with database conenction",db)

#^--------------------------------------------------------------------------------------------------
# ! program for getting the record with column name"select * from students order by mark asc"

# import mysql.connector as mc
# try:
#     conn=mc.connect(host="localhost",user="root",passwd="kunal123456",database="batch9am")
#     # print("connection")
#     cur=conn.cursor()
#     sq="select * from students order by mark asc"
#     # sq="select * from students order by skill asc"
#     cur.execute(sq)
#     print("DATA is READ ")
#     metadata=cur.description
#     print("------------------------------------------")
#     for colinfo in metadata:
#         print(colinfo[0],end="\t")
#     print()    
#     print("------------------------------------------")
#     records=cur.fetchall()
#     for record in records:
#         for val in record:
#             print(val,end="\t")
#         print()    

# except mc.DatabaseError as db:
#     print("problem  with database ")

# #^---------------------------------------------------------------------------------------------------
#!program

import mysql.connector as mc
try:
        
    conn=mc.connect(host="localhost",user="root",passwd="kunal123456",database="batch9am")
    print("connection")
    cur=conn.cursor() 
    sq="select sname,mark form students"
    cur=conn.cursor(sq)
    records=cur.description
    # print(records,end=" \n")
    for val in records:
        print(val[0],end="\t\t")

    
except mc.DatabaseError as db:
    print("problem  with database ")















# #^---------------------------------------------------------------------------------------------------










# #^---------------------------------------------------------------------------------------------------













# #^---------------------------------------------------------------------------------------------------
# #^---------------------------------------------------------------------------------------------------
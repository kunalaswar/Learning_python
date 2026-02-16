
#^-----------------------------------------------------------------------------------------------------
#!program for obtaining a connection with oracle  

# import oracledb 
# try:
#     conn=oracledb.connect("system/tiger@localhost/orcl")
#     print("Oracle connection is created Successfully")
# except oracledb.databaseError as db:
#     print("Python program with oracle problem ",db)

#^-----------------------------------------------------------------------------------------------------
#!program for creating connection from oracle DB
#* DNS
# import oracledb as orc
# try:
#     conn=orc.connect("system/tiger@localhost/orcl")
#     print("oracle connection is created Successfully")

# except orc.databaseError as db:
#     print("Python Program with oracle DB problem",db)    

#*IP Address 127.0.0.1 is the IP Address
# import oracledb as orc
# try:
#     conn=orc.connect("system/tiger@127.0.0.1/orcl")
#     print("oracle connection is created Successfully")

# except orc.databaseError as db:
#     print("python program with oracle DB problem Check your oracle database",db)
#^-----------------------------------------------------------------------------------------------------
# import oracledb as orc
# try:
#     conn=orc.connect("system/tiger@localhost/orcl")
#     print(type(conn))  #<class 'oracledb.Connection'>
#     print("your connection with oracle database is successfully connect")

# except orc.DatabaseError as db:
#     print("python problem with oracle DB check your oracle database ",db)
#^-----------------------------------------------------------------------------------------------------
# import oracledb as orc
# try:
#     conn=orc.connect ("system/tiger@localhost/orcl")
# except orc.DatabaseError :
#     print("python program with oracle DB check oracle database ---")
#     print("=======================================================")
    
# else:
#     print("your connection with oracle database is successfully connect")
#     print(type(conn))   #<class 'oracledb.Connection'>
#     print("---------------------------------")
#     cur=conn.cursor()
#     print("python program is created with cursor object")
#     print(type(cur))   #<class 'oracledb.Cursor'>
#     print("---------------------------------")
    
# finally:
#     try:
            
#         print("I am from finally block")    
#         conn.close()
#         print("python database connection is closed")
#     except NameError:
#         print("Connectio is not to established ---no need to closed")
#^-----------------------------------------------------------------------------------------------------
# import oracledb as orc
# try:
#     conn=orc.connect("system/tiger@localhost/orcl")
#     print("Created a connection successfully ")
# except orc.DatabaseError as db:
#     print("python program with connection problem")    

# else:
#     print("----------------------------------------")
#     print(type(conn))
#     print("----------------------------------------")
#     print("your program with connected")
#     cur=conn.cursor()
#     print(type(cur))
# finally :
#     try:
#         print(" I am from finallly block")    
#         conn.close()
#         print("connection is closed")
#     except NameError:
#         print("Connectioin is Not established")    

#^-----------------------------------------------------------------------------------------------------
#!program for creating table
# import oracledb as orc #step -1
# try:
#     conn=orc.connect("system/tiger@localhost/orcl") #step-2
#     cur=conn.cursor() #step -3
#     stq="create table stud (sno Number(2) primary key,sname varchar2(10) not null)"
#     print("Table created Sucessfully--verify") # Step-5
#     cur.execute(stq)

# except orc.DatabaseError as db:
#     print("python program with connection problem",db)    

#!
# import oracledb  #step -1
# try:
#     conn=oracledb.connect("system/tiger@localhost/orcl") #step -2
#     print("Connection is created successfully")
#     cur=conn.cursor()     #step-3
#     stq="create table kvr(sno Number(2) primary key,sname varchar2(10) not null)"
#     cur.execute(stq) 
#     print("Table is created successfully ")
# except oracledb.DatabaseError :
#     print("python  program with connection  problem ")    

#! 

# import oracledb
# try:
#     conn=oracledb.connect("system/tiger@localhost/orcl")
#     print("connection is created Successfully ")
#     cur=conn.cursor()
#     stq="create table kvr2(sno Number(2) primary key,sname varchar2(10) not null)"
#     cur.execute(stq)
#     print("Table is created successfully")
# except oracledb.DatabaseError:
#     print("python program with connection problem")    

#^-----------------------------------------------------------------------------------------------
#!program for creating table with Dynamic
# import oracledb
# try:
        
#     conn = oracledb.connect("system/tiger@localhost/orcl")
#     print("Connection is created successfully")
#     cur = conn.cursor()
#     ctq = "create table aniket(sno number(2) primary key,sname varchar2(10) not null)"
#     cur.execute(ctq)
#     print("Table is created successfully")
# except oracledb.DatabaseError:
#     print("problem with your python program")    

#^-----------------------------------------------------------------------------------------------
#!program for creating table with Dynamic
# import oracledb
# try:
        
#     conn=oracledb.connect("system/tiger@localhost/orcl")
#     print("Connection is creted successfully")
#     cur=conn.cursor()
#     stq=input("Enter a Query")
#     cur.execute(stq)

# except oracledb.DatabaseError   :
#     print("problem with your python program")    

#^-----------------------------------------------------------------------------------------------

# import oracledb
# conn=
# cur=conn.cursor()
# query=
# cur.execute(query)
#^-----------------------------------------------------------------------------------------------
# import oracledb #step -1
# conn=oracledb.connect("system/tiger@localhost/orcl") #step-2
# cur=conn.cursor()
# ctq="create table harshal(sno number(2)primary key,sname varchar2(10),marks number(3))"
# cur.execute(ctq)
# print("Table is creted Successfully")

#^-----------------------------------------------------------------------------------------------
#!program for adding the new modify the column
# import oracledb as orc
# try:
        
#     conn=orc.connect("system/tiger@localhost/orcl")
#     cur=conn.cursor()
#     altq="alter table kunal modify (sno number(10),sname varchar(50),marks number(5,2))"
#     cur.execute(altq)
#     print("Alter table Successfully check it for your side")
# except orc.DatabaseError:
#     print("problem in your python code write properly ")


#^-----------------------------------------------------------------------------------------------
# #!program for adding the New  modify column
import oracledb as orc
try:
        
    conn=orc.connect("system/tiger@localhost/orcl")
    cur=conn.cursor()
    altq="alter table kunal modify (sno number(20),sname varchar(60),marks number(3,2))"
    cur.execute(altq)
    print("Alter Table Successfully check  ")
except orc.DatabaseError:
    print("problem in python program check it ")

#^-----------------------------------------------------------------------------------------------
#!program for adding The new Colunm from Dynmaic type
# import oracledb as orc
# try:
#     conn=orc.connect("system/tiger@localhost/orcl")
#     print("oracle database is connected Successfully ")
#     cur=conn.cursor()
#     altq=input("Enter a Alter OR modify Query :")
#     cur.execute(altq)
#     print("ALter Table successfully Check it from Your side")
# except orc.DatabaseError:
#     print("problem with python program check it ")    

# ^-----------------------------------------------------------------------------------------------
#!program from adding the new column with the Help of add not a modify
#* New tabel is added successfully
# import oracledb as orc
# try:
        
#     conn=orc.connect("system/tiger@localhost/orcl")
#     print("oracle database is connected successfully ")
#     cur=conn.cursor()
#     altq="alter table kunal add(sparent varchar2(10))"
#     cur.execute(altq)
#     print("Alter table is added the new column successfully")
# except orc.DatabaseError:
#     print("problem with your program check it")    



# ^-----------------------------------------------------------------------------------------------
# !program for inserting  the data into Table 
# import oracledb as orc
# # try:
        
# conn = orc.connect("system/tiger@localhost/orcl")
# print(" oracle database Connection is successfully")
# cur=conn.cursor()
# iq="insert into kunal values(100,'paa',90,)"
# cur.execute(iq)
# conn.commit()
# print("insert into successfully check it column")
# # except orc.DatabaseError:
#     # print("problem is your python program check it")

#^-----------------------------------------------------------------------------------------------
#! program for inserting  the data into Table 
# import oracledb as orc
# try:
#     conn = orc.connect("system/tiger@localhost/orcl")
#     print("oracle database connection is successfully ")
#     cur=conn.cursor()
#     iq="insert into student values(70,'pratik',20)"
#     cur.execute(iq)
#     conn.commit()
#     print("Insert into successfully check it column")
# except orc.DatabaseError:
#     print("problem is your python program")    

#^-----------------------------------------------------------------------------------------------
#!Delete the entire table
# import oracledb
# conn=oracledb.connect("system/tiger@localhost/orcl")
# print("connection is created successfully")
# cur=conn.cursor()
# dq="drop table sagar"
# cur.execute(dq)
# print("table is drop successfully")

#^-----------------------------------------------------------------------------------------------

#!Dynamic table 
# import oracledb
# while(True):

        
#     try:
#         conn=oracledb.connect("system/tiger@localhost/orcl")
#         print("oracle database connection is successfully")
#         cur=conn.cursor()
#         # iq="insert into student values(100,'ani',80)"
#         iq=input("Enter a query :")
#         cur.execute(iq)
#         conn.commit()
#         print("Insert into suceesfully check it column")
#     except oracledb.DatabaseError as db:
#         print("Error : ",db)
#     except NameError:
#         print("Dont Enter a Str alnum str and special sysbols")
#     ch=input("Do you Enter a another rocord into the table ").lower()        
#     if ch=="no":
#         break
#     else:
#         if ch not in ["yes","no"]:
#             print("your input is invalid Try to Enter proper record")


#^-----------------------------------------------------------------------------------------------
#!Delete the single row from the table
# import oracledb as orc
# try:
#     conn=orc.connect("system/tiger@localhost/orcl")
#     cur=conn.cursor()
#     dq="delete from student where sno=10"
#     cur.execute(dq)
#     conn.commit() #this function to save the Changes with the use of commit()
#     print("Record is delected check from your side")
# except orc.DatabaseError:
#     print("problem in your python program check it propery")
#     # print(e)

#^-----------------------------------------------------------------------------------------------
#!Delete the record  

# import oracledb as orc
# while(True):
#     try:
            
#         conn=orc.connect("system/tiger@localhost/orcl")
#         print("Connection of the data is connected successfullly")
#         cur=conn.cursor()
#         dq="delete table kunal where sno=50"
#         cur.execute(dq)
#         print("One record is delected ")
#     except orc.DatabaseError:
#         print("problem is in your python code")    
#     ch=input("enter your choice here :").lower()
#     if ch=="no":
#         break
#     if ch not in ["yes","no"]:
#         print("Invalid input please the enter properry")    

#* Dynamic Deletion

# import oracledb as orc
# while(True): 
#     try:
#         conn=orc.connect("system/tiger@localhost/orcl")
#         cur=conn.cursor()
#         sno=int(input("Enter a student  sno which you want to delete :"))
#         dq=f"delete from student where sno={sno}"
#         cur.execute(dq)
#         conn.commit()

#         print("Deleted Successfully record ")
#     except orc.DatabaseError:
#         print("----------------------------------------")
#         print("problem in your python coed check it properly ")    
#         if cur.rowcount>0:
#             print("Delected your Record check it from your side")
#         else:
#             print("Record does not exist ib the code")    
#         print("----------------------------------------")
#     ch=input("Do you want delete another record in  (yec/no):") .lower()       
#     if ch=="no":
#         break
#     elif ch not in ["yes","no"]:
#         print("Your input choice is wrong take care about it")

#^-----------------------------------------------------------------------------------------------
#! program for updating marks of student by 10%
# import oracledb as orc
# try:
        
#     conn=orc.connect("system/tiger@localhost/orcl")
#     cur=conn.cursor()
#     upq = "update student set smarks = smarks*10/100"
#     cur.execute(upq)
#     conn.commit()  #to save the upadate record into it
#     print("Update the record from datasbase check it")
# except orc.DatabaseError:
#     print("problem into your python  Check it ")
    
# import oracledb as orc
# try:
#     conn=orc.connect("system/tiger@localhost/orcl")
#     cur=conn.cursor()
#     # upq="update student set samrks=smarks*10/100"
#     cur.execute("update student set smarks=smarks*20/100")
#     conn.commit()
#     print("Update the record from database check it ")
# except orc.DatabaseError:
#     print("problem with your python code check it properly")    
#^-----------------------------------------------------------------------------------------------
#! 

# import oracledb as orc
# while(True):
#     try:
#             conn=orc.connect("system/tiger@localhost/orcl")
#             cur=conn.cursor()
#             sno=int(input("Enter students  Sno to update the marks  or Sname :"))
#             sname=input("Enter Sname :")
#             smarks=float(input("Enter a students marks :"))

#             nq=f"insert into student(sno,sname,smarks) values({sno},'{sname}',{smarks})"
#             cur.execute(nq)
#             conn.commit()

#             print("table is update  successfully check it")
#             print(f"{cur.rowcount} is insert sucessfully ")

#     except orc.DatabaseError as db:
#             print("problem with your python code check it from your side",db)    
#     except NameError:
#         print("Dont Enter alnum str ,special symbols")
#     ch=input("Do you want to insert another (yes/no):")
#     if ch=="no":
#         print("Tnx for using this program")
#         break
#     elif ch not in ["yes","no"]:
#         print("Invalid input Enter try again")
# ^-----------------------------------------------------------------------------------------------
#sagar

# import oracledb
# while True: 
#  try:
#       con = oracledb.connect("system/tiger@localhost/orcl")
#       cur = con.cursor()
#       sno = int(input("Enter Student number : "))
#       sname= input("Enter Name of Student :")
#       smarks = float(input("Enter Marks of Student : "))
#       iq = f"insert into student(sno,sname,smarks) values ({sno},'{sname}',{smarks})"
#       cur.execute(iq)
#       con.commit()
#       print(f"{cur.rowcount}  Student Record Inserted Successfully : ")
#  except oracledb.DatabaseError as db:
#       print("Problem in Oracle : ",db)
#  except ValueError:
#       print("Dont enter alnums,alphabets, symbols  for sno , sname ")
#  ch = input("Do You Want To Enter Another Student Record :  ").lower()
#  if ch == "no" :
#      break
#  if ch not in ["yes","no"]:
#      print("You have Enter Invalid input")



#^-----------------------------------------------------------------------------------------------
#! Program for updating student,Name,Marks based on sno
# import oracledb as orc
# while(True):
        
#     try:
#         conn=orc.connect("system/tiger@localhost/orcl")
#         cur=conn.cursor()
#         # sno=int(input("Enter a students Number to Update students,Name,marks "))
#         # uq=" update student set sname='john',smarks=88 where sno=15; "
#         sno = int(input("Enter Student Number :  "))
#         sname = input("Enter New Name : ")
#         smarks = float(input("Enter New Marks : "))
#         upq= f"update student set  sname = '{sname}',smarks = {smarks} where sno = {sno}"
#         cur.execute(upq)
#         conn.commit()
#         if cur.rowcount >0:
#             print(f"record {cur.rowcount} is updated")
#         else:
#             print("Record does not exist ")    

#     except orc.DatabaseError as db:
#         print("oracle database problem ",db)    
#     except NameError:
#         print("Dont Enter alnum special symbols ")   


#     ch=input("Do you want Enter a another record (yes/no)").lower()
#     if ch=="no":
#         print("Thx for using this program ")
#         break
#     elif ch not in ["yes","no"]:
#         print("YOur input is INVALID please input properly")

#^-----------------------------------------------------------------------------------------------------
#^ CHAT GPT 
# import oracledb as orc

# try:
#     # Step 1: Establish a connection (outside the loop)
#     conn = orc.connect(user="system", password="tiger", dsn="localhost/orcl")
#     cur = conn.cursor()

#     while True:
#         # Step 2: Input from user (optional if static update)
#         sno = int(input("Enter the student number (Sno) to update: "))
#         sname = input("Enter the new name for the student: ")
#         smarks = float(input("Enter the new marks for the student: "))

#         # Step 3: Update query with parameterized inputs
#         uq = "UPDATE student SET sname = :sname, smarks = :smarks WHERE sno = :sno"
#         cur.execute(uq, {"sname": sname, "smarks": smarks, "sno": sno})
#         conn.commit()  # Commit the transaction

#         # Step 4: Inform user of success
#         if cur.rowcount > 0:
#             print("Record updated successfully.")
#         else:
#             print("No record found with the given student number.")

#         # Step 5: Ask user if they want to update another record
#         ch = input("Do you want to update another record? (yes/no): ").strip().lower()
#         if ch == "no":
#             print("Thanks for using this program.")
#             break
#         elif ch not in ["yes", "no"]:
#             print("Your input is INVALID. Please input 'yes' or 'no'.")
# except orc.DatabaseError as db:
#     print("Oracle database problem:", db)
# finally:
#     # Step 6: Close resources
#     if 'cur' in locals():
#         cur.close()
#     if 'conn' in locals():
#         conn.close()
#^----------------------------------------------------------------------------------------------------


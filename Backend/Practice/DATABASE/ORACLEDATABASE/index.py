# #! checking oracle version 
# import oracledb
# print(oracledb.__version__)

#^---------------------------------------------------------------------------------------------
#! checking oracle version
# import oracledb
# print(oracledb._version_)
#^----------------------------------------------------------------------------------------------
#!Program for Obtaining Connection from Oracle DB
#* DNS
# import oracledb as orc
# try:
#  conn = orc.connect("system/1234@localhost/orcl")
#  print(type(conn))      #<class 'oracledb.Connection'>
#  print("orcle database conncected successfully ")
# except orc.DatabaseError as db:
#   print("Problem with Oracle :",db)


#*IpAddres
# import oracledb as orc
# try:
#  conn = orc.connect("system/1234@127.0.0.1/orcl")
#  print(type(conn))                                   #<class 'oracledb.Connection'>
#  print("orcle database conncected successfully ")
# except orc.DatabaseError as db:
#   print("Problem with Oracle :",db)

#^----------------------------------------------------------------------------------------------
#! Program for Demonstrating the Cursor Object Creation
# import oracledb
# try: 
#  conn = oracledb.connect("system/1234@localhost/orcl")
#  print("Connection Created Successfully ")
# except oracledb.DatabaseError as db:
#  print("Problem with oracle : ",db)
# else: 
#    print("Python Program got connection from Oracle Database")
#    print("Type of conn=", type(conn))
#    print("---------------------")
#    cur = conn.cursor()                         #<class 'oracledb.Cursor'>
#    print("Cursor object created succesfully ")
#    print(type(cur))
# finally :
#   try :
#    print("----------------------------------")
#    print("i am from finally block")
#    conn.close()
#    print("Program closed succesfully ")   
#   except NameError:
#     print("Connection is not estblished no need to close ")
# import oracle
# try:
#     conn = oracledb.connect("system/1234@localhost/orcl")
#     print("Connection created successfully")
# except oracledb.DatabaseError as db:
#     print("Problem with Connection ")


#^----------------------------------------------------------------------------------------------
#! Program for creating a table 
#* Syntax - 1
# import oracledb  # step-1
# try:
#  conn = oracledb.connect("system/1234@localhost/orcl") #step-2
#  cur = conn.cursor()  #step-3
#  #step - 4
#  ctq = "create table employee(sno number(3) primary key,sname varchar(2) not null,smarks number(5,2))"
#  cur.execute(ctq)  
#  print(" Tabel created succesfully ")
# except oracledb.DatabaseError as db:
#  print("Proble with conncting database  : ",db)

#* Syntax - 2
# import oracledb 
# try:
#  conn = oracledb.connect("system/1234@localhost/orcl").cursor().execute("create table jay(sno number(3) primary key,sname varchar(2) not null,smarks number(5,2))")
#  print(" Tabel created succesfully ")
# except oracledb.DatabaseError as db:
#  print("Proble with conncting database  : ",db)


#*taking dynamic query
# import oracledb
# try:
#  conn = oracledb.connect("system/1234@localhost/orcl")
#  cur = conn.cursor()
#  ctq = input("Enter A Query : " )
#  cur.execute(ctq)
#  print("Table created successfully : ")
# except oracledb.DatabaseError as db:
#  print("Problem in oracle : ",db)
#^----------------------------------------------------------------------------------------------
#! Program For Adding New Column 
#* Dynmaic Query
# import oracledb 
# try:
#  conn = oracledb.connect("system/1234@localhost/orcl")
#  cur = conn.cursor()
#  ctq = input("Enter A Query for altering table : ")
#  cur.execute(ctq)
#  print("Table altered successfully")
# except oracledb.connect as db:
#  print("Problem in to Eatablish the connection : ",db)


#^----------------------------------------------------------------------------------------------
#! Program for deleting one record 
# import oracledb
# conn = oracledb.connect("system/1234@localhost/orcl")
# cur = conn.cursor()
# ctq = input("Enter your Query :  ")
# cur.execute(ctq)
# print("")
#^----------------------------------------------------------------------------------------------
#! Program inserting data in table


#^----------------------------------------------------------------------------------------------
#! Program For Adding or Modify New Column 
#* Dynmaic Query
# import oracledb 
# try:
#  conn = oracledb.connect("system/1234@localhost/orcl")
#  cur = conn.cursor()
#  ctq = input("Enter A Query for altering table : ")
#  cur.execute(ctq)
#  print("Table altered successfully")
# except oracledb.connect as db:
#  print("Proble in oracle : ",db)
#^----------------------------------------------------------------------------------------------
#! Program inserting data in table
#* syntax-1
# import oracledb
# try:
#  conn = oracledb.connect("system/1234@localhost/orcl")
#  cur = conn.cursor()
#  iq = "insert into employee values(1,'karan',11.44)"
#  cur.execute(iq)
#  conn.commit()
#  print("EMployee record inserted successfully  ")
# except oracledb.DatabaseError as db:
#  print("Problem in Oracle : ",db)

#* syntax-2
# import oracledb
# try:
#  conn = oracledb.connect("system/1234@localhost/orcl")
#  cur = conn.cursor()
#  iq = input("Enter Query for insertion :  ")
#  cur.execute(iq)
#  conn.commit()
#  print("EMployee record inserted successfully  ")
# except oracledb.DatabaseError as db:
#  print("Problem in Oracle : ",db)


#*Dynamic insertion
# import oracledb
# while True: 
#  try:
#       con = oracledb.connect("system/1234@localhost/orcl")
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
#^----------------------------------------------------------------------------------------------
#^---------------------------------------------------------------------------------------------

#*Dynamic insertion
# import oracledb
# while True: 
#  try:
#       con = oracledb.connect("system/1234@localhost/orcl")
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
#^----------------------------------------------------------------------------------------------
#! Program for deleting Query Salary
# import oracledb
# try:
#  con = oracledb.connect("system/1234@localhost/orcl")
#  cur  =con.cursor()
#  dq = "delete from student where sno=50"
#  cur.execute(dq)
#  con.commit()
#  print(f"{cur.rowcount} record is deleted : ")
# except oracledb.DatabaseError as db:
#  print("Problem in oracle ",db)
#^----------------------------------------------------------------------------------------------

#* Dynamic Deletion
# import oracledb
# while True:
#  con = oracledb.connect("system/1234@localhost/orcl")
#  try:
#   cur = con.cursor()
#   sno = int(input("Enter Student Number : "))
#   dq = f"delete from student where sno={sno}"
#   cur.execute(dq)
#   con.commit()
#   if cur.rowcount > 0:
#     print(f"{cur.rowcount} record is delted ")
#   else:
#    print("Record does not exist ")
#  except oracledb.DatabaseError as db:
#   print("Problem in oracle : ", db)
#  ch = input("Do you want to delete another student record - (yes / no) : ").lower()
#  if ch == "no":
#   break
#  if ch not in ["yes", "no"]:
#   print("You have Enter Invalid input")
#   break
#^----------------------------------------------------------------------------------------------
#! program for updating marks of student by 10%
# import oracledb
# try:
#      con = oracledb.connect("system/1234@localhost/orcl")
#      cur = con.cursor()
#      upq = "update student set smarks = smarks*10/100"
#      cur.execute(upq)
#      con.commit()
#      print(f"{cur.rowcount} record updated : ")
# except oracledb.DatabaseError as db:
#      print("Problem in Oracle :",db)

# import oracledb
# try:
#      con = oracledb.connect("system/1234@localhost/orcl")
#      cur = con.cursor()
#      upq = "update student set smarks = smarks * 10 / 100 where sno = 5"
#      cur.execute(upq)
#      con.commit()
#      print(f"{cur.rowcount} record updated : ")
# except oracledb.DatabaseError as db:
#      print("Problem in Oracle :",db)
#^----------------------------------------------------------------------------------------------
#! Program for updating studen,Name,Marks based on sno
# import oracledb
# while True:
#  try :
#   con = oracledb.connect("system/1234@localhost/orcl")
#   cur = con.cursor()

#   sno = int(input("Enter Student Number :  "))
#   sname = input("Enter New Name : ")
#   smarks = float(input("Enter New Marks : "))
#   upq= f"update student set  sname = '{sname}',smarks = {smarks} where sno = {sno}"
#   cur.execute(upq)
#   con.commit()
#   if cur.rowcount>0:
#    print(f"{cur.rowcount} Record Updated Successfully ")
#   else:
#    print("Record does not exitst ")
#  except oracledb.DatabaseError as db:
#   print("Problem in Oracle :",db)
#  except ValueError:
#   print("Dont enter alnums , alphabest , symbols for sno , marks")
#  ch = input("Do you want update another another student record - (yes/no) :").lower()
#  if ch == "no":
#   print("Thanks for using this program  ")
#   break

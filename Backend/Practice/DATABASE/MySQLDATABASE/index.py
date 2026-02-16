# import mysql.connector
# print(mysql.connector.__version__)
# ^----------------------------------------------------------------------------------------------------
#!program to connectes the mysql database 
# import mysql.connector
# try:
        
#     conn = mysql.connector.connect(host="localhost",user="root",passwd="kunal123456")
#     print(conn,type(conn))
#     print("connection is done with MySQL DB")
#     cur=conn.cursor()
#     # print(cur)
# except mysql.connector.DatabaseError as db:
#     print("problem in mysql Connection ")
# ^----------------------------------------------------------------------------------------------------

# import mysql.connector
# try:
#     conn=mysql.connector.connect(host="127.0.0.1",user="root",passwd="kunal123456")
#     print("connection from  mysql is coneerted Successfully")
# except mysql.connector.DatabaseError as db:
#     print("problem with your connection is DB")

# ^----------------------------------------------------------------------------------------------------
#! program is not Running in this stage
# import mysql.connector #Step -1
# conn=mysql.connector.connect(host="127.0.0.1",user="root",passwd="kunal123456",database="sakila")
# cur=conn.cursor() #Step -3
# sq="select * from sakila"
# print("python program is created the cursor object")

# ^----------------------------------------------------------------------------------------------------
#!program To create the database batch9am
# import mysql.connector
# try:
        
#    conn=mysql.connector.connect(host="localhost",user="root",passwd="kunal123456")  
#     cur=conn.cursor()
#     dc="create database batch9am"
#     cur.execute(dc)
#     print(" Database is created successfully")
# except mysql.connector.DatabaseError:
#     print("COnnection is fail  check connection ")
# ^----------------------------------------------------------------------------------------------------
#!program for create the database employee

# import mysql.connector
# try:
        
#     conn = mysql.connector.connect(host="localhost",user="root",passwd="kunal123456")
#     print("connection is database ia connected ")
#     cur=conn.cursor()
#     sq="create database employee"
#     print("Database created successfully ---verify")
    

# except mysql.connector.DatabaseError:
#     print("python database is not connected into the database")


# ^----------------------------------------------------------------------------------------------------
#!program for create database student DATABASE IS NOT CREATED PLEASE CHECK IT 
# import mysql.connector as mc
# try:
        
#     conn = mc.connect(host="localhost",user="root",passwd="kunal123456")
#     print("Connection is connected with database")
#     cur=conn.cursor()
#     sq="create database if not exist student"
#     print("Database is created Successfully ---plaese check verify")
# except mc.DatabaseError:
#     print("problem with your Database ")    
    
#^ CHAT GPT CODE 

# import mysql.connector as mc

# try:
#     # Establish the connection
#     conn = mc.connect(host="localhost", user="root", passwd="kunal123456")
#     print("Connection is established with the database.")

#     # Create a cursor object
#     cur = conn.cursor()

#     # SQL query to create the database
#     sq = "CREATE DATABASE IF NOT EXISTS student"
#     cur.execute(sq)
#     print("Database is created successfully — please verify.")

# except mc.Error as e:  # Catch any MySQL-related errors
#     print("There was a problem with the database:", e)

# finally:
#     # Ensure the connection is closed properly
#     if 'conn' in locals() and conn.is_connected():
#         conn.close()
#         print("Connection closed.")
# ^----------------------------------------------------------------------------------------------------
#!program for creating table form database 

# import mysql.connector as mc
# try:
        
#     conn=mc.connect(host="localhost",user="root",passwd="kunal123456",database="batch9am")
#     print("Connection of the database is connected successfully---verify or check it")
#     cur=conn.cursor()
#     print("cursor object is created successfully ")
#     cq="create table students(sno int primary key,sname varchar(20)not null,mark real not null)"

#     cur.execute(cq)
#     print("Table is created successfully ")
# except mc.Error as e:
#     print("Problem with your mysql database ",e)

# ^----------------------------------------------------------------------------------------------------
#!program for modify the  record into the table

# import mysql.connector as mc
# try:
        
#     conn=mc.connect(host="localhost",user="root",passwd="kunal123456",database="batch9am")
#     cur=conn.cursor()
#     iq="ALTER TABLE students CHANGE sname sname VARCHAR(40) NOT NULL" #Query take form chatgpt
#     cur.execute(iq)
#     print("alter table sname is alter check it ")
# except  mc.DatabaseError as db:
#     print("problem with your database check it ",db)

# ^----------------------------------------------------------------------------------------------------
#!program to add the Extra column into existing table 
# import mysql.connector as mc
# try:
        
#     conn = mc.connect(host="localhost",user="root",passwd="kunal123456",database="batch9am")
#     print("connection is conncted siccessfully check it")
#     cur=conn.cursor()
#     acq="alter table students ADD skill VARCHAR(50);"
#     cur.execute(acq)
    #   conn.commit()  
#     print("Add  the column into it(skill column) check from it")

# except mc.DatabaseError as db:
#     print("problem with your mysql databse check it ")


# ^----------------------------------------------------------------------------------------------------
#!program to insert the table data into it

# import mysql.connector as mc
# try:

#     conn = mc.connect(host="localhost",user="root",passwd="kunal123456",database="batch9am")
#     print("connection is conncted siccessfully check it")
#     cur=conn.cursor()
#     inq="insert into students values(100,'pratik',90,'chatgpt coder' )"
#     cur.execute(inq)
#     conn.commit()
#     print("data is inserted")

# except  mc.DatabaseError as db:
#     print("problem with database code check ir from your  side check out")

# ^----------------------------------------------------------------------------------------------------
#!program to insert the table data into it
#*Dynamic input user and insert into the table 

# import mysql.connector as mc
# while(True):
        
#     try:

#         conn = mc.connect(host="localhost",user="root",passwd="kunal123456",database="batch9am")
#         print("connection is conncted siccessfully check it")
#         cur=conn.cursor()
#         sno=int(input("Enter a students number "))
#         sname=input("Enter a students name ")
#         mark=float(input("Enter a Marks "))
#         skill=input("Enter a skill ")
#         iq="insert into students values(%d,'%s',%f,'%s')"
#         cur.execute(iq %(sno,sname,mark,skill)) # Step-5
#         conn.commit()
#         print("DATA is inserted successfully")

#     except ValueError:
#         print("Dont Enter a Str symbols please Enter properly")

#     except mc.DatabaseError as db:
#         print("problem with your code check it ",db)
#     ch=input("Enter a choice here Do you want to Enter a another record (yes/no) ").lower()
#     if ch=="no":
#         print("Tnx for using this program")
#         break
#     elif ch not in ["yes","no"]:
#         print("Your input choice is wrong")
#         break
#!

# import mysql.connector as mc
# while(True):
#     try:
            
#         conn = mc.connect(host="localhost",user="root",passwd="kunal123456",database="batch9am")
#         print("mysql database is connected successfully")
#         cur=conn.cursor()
#         sno=int(input("Enter a students number "))
#         sname=input("Enter a students name ")
#         mark=float(input("Enter a Marks "))
#         skill=input("Enter a skill ")
#         iq="insert into students values(%d,'%s',%f,'%s')"
#         cur.execute(iq %(sno,sname,mark,skill)) # Step-5

      
#         conn.commit()
#         print("inserted successfully ")

#         ch=input("Do you  Enter  another record (yes/no):")
#         if ch=="no":
#             print("Tnx for using this program")
#             break
#         elif ch not in ["yes","no"]:
#             print("Your Invalid input Enter pproperly")
#             break
#     except mc.DatabaseError as db:
#         print("problem with your connection ",db) 
#     except ValueError:
#         print("Dont ENter a str Alnum or special symbols")

# ^----------------------------------------------------------------------------------------------------
# !program for delete the record from table 
# import mysql.connector as mc
# while True:
        
#     try:
            
#         conn = mc.connect(host="127.0.0.1",user="root",passwd="kunal123456")
#         print("Connection of the data is connected successfully ")
#         cur=conn.cursor()
#         print("Cursor object is Created Successfully you can pass a query ")
#         sno=int(input("Enter a S number for Remove the RECORD :"))
#         dq=f"delete from students where sno = {sno}" 
#         print("YOur input record is deleted check it ")
#         cur.execute(dq)
#         conn.commit()
#         if cur.rowcount>0:
#             print(f"{cur.rowcount} is deleted 1")

    

#         ch=input("Do you want to enter anohter record (yes/no):")
#         if ch=="no":
#             print("Tnx for using this program ")
#             break
#         elif ch not in ["yes","no"]:
#             print("INVALID INPUT ENTER PROPERLY :")
            

#     except mc.DatabaseError as db:
#         print("problem with your mqsql database check ti")    
#     except ValueError:
#         print("Dont Enter a str or anum and special symbols :")

# ^----------------------------------------------------------------------------------------------------
# !program for delete the record from table 
# import mysql.connector as mc
        
# while True:
#     try:
#         conn=mc.connect(host="localhost",user="root",passwd="kunal123456",database="batch9am")
#         print("connection is Connected successfully")
#         cur=conn.cursor()
#         dq="delete from students where sno= 800"
#         cur.execute(dq)
#         print("record is delete from it")
#         conn.commit()

#         if cur.rowcount >0:
#             print(f"{cur.rowcount} is deleted successfully") 
#         else:
#             print("Record is not Exist") 
#         ch=input("Do you want to enter a another Record (yes/no):").lower()
#         # if ch=="no":
#         #     print("Tnx for using this program")
#         #     break
#         # elif ch not in [ "yes","no"]:
#         #     print("Dont Invalid input")
#         #     break

#     except NameError:
#         print("Dont enter str and special symbols")
#     except mc.DatabaseError as db:
#         print("Problem with Your mysql database")            
# ^----------------------------------------------------------------------------------------------------
# !program for delete the record from table  
#* Dynamic input taking from user
# import mysql.connector as mc
# while True:
    
#     try:
            
#         conn=mc.connect(host="localhost",user="root",passwd="kunal123456",database="batch9am")
#         print("connection With database is connected Successfull")
#         cur=conn.cursor()
#         sno=int(input("Enter a Students number :"))
#         dq=f"delete from students where sno={sno}"
#         cur.execute(dq)
#         print("Deleted Successfully form your side")

#         if cur.rowcount >0:
#             print(f"{cur.rowcount} is deleted successfully")
#         else:
#             print("Record is not Exist ")    
#         conn.commit()
#         ch=input("Do you want to Enter enter another Reocord (Yes / no)").lower()    

#         if ch=="no":
#             print("Thank for using this profram")
#             break    
#         elif ch not in ["yes","no"] :
#             print("Invalid input Try---again")

#     except mc.DatabaseError as db:
#         print("Problem with your code check it")
# ^----------------------------------------------------------------------------------------------------






            







# ^----------------------------------------------------------------------------------------------------






# ^----------------------------------------------------------------------------------------------------




# ^----------------------------------------------------------------------------------------------------




# ^----------------------------------------------------------------------------------------------------
















# ^----------------------------------------------------------------------------------------------------














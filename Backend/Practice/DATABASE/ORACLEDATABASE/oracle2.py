
#^----------------------------------------------------------------------------------------------------
#!program for Adding the data from user 
# import oracledb as orc
# try:
        
#     conn=orc.connect("system/tiger@localhost/orcl")
#     print("oracel database is connected successfully ")
#     cur=conn.cursor()
#     eno=int(input("Enter a Emp Number "))
#     ename=input("Enter a Emp Name ")
#     esal=float(input("Enter a Emp SAl "))
#     ecomp=input("Enter Comp name of Emp ")
#     inq=f"insert into employee(eno,ename,esal,ecomp)values({eno},'{ename}',{esal},'{ecomp}')"
#     cur.execute(inq)
#     conn.commit()
#     print("table data is insert properly ")

# except orc.DatabaseError as db:
#     print("Oracle Connection problem ",db)

#^----------------------------------------------------------------------------------------------------
# import oracledb as orc
# try:
        
#     conn=orc.connect("system/tiger@localhost/orcl")
#     print("oracel database is connected successfully ")
#     cur=conn.cursor()
  
#     inq=f"insert into employee values(1,'sagar',6.9,'lfgh')"
#     cur.execute(inq)
#     conn.commit()
#     print("table data is insert properly ")

# except orc.DatabaseError as db:
#     print("Oracle Connection problem ",db)

#^----------------------------------------------------------------------------------------------------
#!delect the record from the table based on employee eno
# import oracledb as orc
# try:
        
#     conn=orc.connect("system/tiger@localhost/orcl")
#     # delete from employee  where eno = 
#     cur=conn.cursor()
#     dq="delete from employee where eno =1"
#     cur.execute(dq)
#     print("Delete one record deleted ")
#     conn.commit()
#     if cur.rowcount>0:
#         print(f"{cur.rowcount} is deleted successfully")    
#     else:
#         print("Record is not Exist ")    
# except orc.DatabaseError as db:
#     print("problem with your oracle connection check it")    

#^----------------------------------------------------------------------------------------------------
#!program for update a salary from employee table by 10 % hike
# import oracledb as orc
# while(True):
        
#     try:
#         conn=orc.connect("system/tiger@localhost/orcl")
#         print("connection is created successfullly")
#         cur=conn.cursor()
#         upq="update  employee set esal = esal+esal*10/100"
#         cur.execute(upq)
#         conn.commit()
#         if cur.rowcount>0:
#             print(f"{cur.rowcount} is  update successfully") 
#             break
#         else:
#             print("Record is not Exist")    
#     except orc.DatabaseError as db:
#         print("problem with oracle database to connect",db)        

#^----------------------------------------------------------------------------------------------------

#!update the salary and company name based on the empployee eno
import oracledb as orc
try:
    conn=orc.connect("system/tiger@localhost/orcl")
    cur=conn.cursor()
    eno=int(input("Enter a employee Number :"))
    esal=int(input("Enter a New salary of the Employee:"))
    ecomp=input("Enter a New company name:")
    upq=f"update employee set esal = {esal},ecomp='{ecomp}'   where eno={eno}"
    cur.execute(upq)
    conn.commit()
    print("updated check from your side check it")
    if cur.rowcount>0:
        print(f"{cur.rowcount} is Update successfully")
    else:
        print("Record is not Exist ")    
except orc.DatabaseError as db:
    print("problem with  your oracle database ",db)    
except NameError:
    print("Dont Enter  ALnum special symbols ")    
#^----------------------------------------------------------------------------------------------------
#! 
# import mysql.connector

# # Connect to MySQL
# try:
#     connection = mysql.connector.connect(
#         host="localhost",  # Replace with your MySQL host
#         user="root",  # Replace with your MySQL username
#         password="kunal123456",  # Replace with your MySQL password
#         database="school"  # Replace with your database name
#     )

#     if connection.is_connected():
#         print("Connected to MySQL database")

#         # Create a cursor object
#         cursor = connection.cursor()
#         cursor.execute("SELECT DATABASE();")

#         # Fetch the current database name
#         db_name = cursor.fetchone()
#         print("You're connected to database:", db_name[0])

#         # Example query execution
#         cursor.execute("SHOW TABLES;")
#         for table in cursor.fetchall():
#             print("Table:", table)

# except mysql.connector.Error as e:
#     print(f"Error connecting to MySQL: {e}")
# finally:
#     if 'connection' in locals() and connection.is_connected():
#         connection.close()
#         print("MySQL connection closed.")

#^----------------------------------------------------------------------------------------------------




















#^----------------------------------------------------------------------------------------------------
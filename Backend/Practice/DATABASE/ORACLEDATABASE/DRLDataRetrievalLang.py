#^---------------------------------------------------------------------------------------------------
#! #Program for Reading the Records from employee table--by using fetchone()
#OracleSelectRecordEx1.py
# import oracledb as orc
# def selectrecord():
        
#     try:
            
#         conn=orc.connect("system/tiger@localhost/orcl")
#         cur=conn.cursor()
#         # print(cur,type(cur))
#         sq="select * from employee"
#         cur.execute(sq)
#         print(" select Query executed")
#         # print(cur,type(cur))
#         while(True):
#          record=cur.fetchone()
#         #  print(record)
#          if record:
#           print(record)
#          else:
#             break

#         # for record in:
#         #     print(record)
#         # print()    
#     except orc.DatabaseError  as db:
#         print("problem with your python program")   
# selectrecord()

#^---------------------------------------------------------------------------------------------------

# import oracledb as orc
# try:
#     conn=orc.connect("system/tiger@localhost/orcl")
#     cur=conn.cursor()
#     sq="select * from employee"
#     cur.execute(sq)
  

#     while(True):
#         record=cur.fetchone()
#     # print(record)
#         if record!=None:
#     #   print(record,end="\t")
#             for i in record:
#                 print(i,end="\t\t")
#             print()
        
#         else:
#             break

# except orc.DatabaseError as db:
#     print("problem with your python program")    
#^---------------------------------------------------------------------------------------------------
# import oracledb as orc
# try:
#     conn=orc.connect("system/tiger@localhost/orcl")
#     print("Connection od the database is coonect successfully")
#     cur=conn.cursor()
#     sq="select * from employee"
#     cur.execute(sq)
#     while(True):
#         record=cur.fetchone()   
#         if record!=None :
#             for val in record:
#                 print(val,end="\t")
#             print()    
#         else:
#             print("------------------------------")   
#             break
  
# except orc.DatabaseError as db:
#     print("problem with an oracle db connection ")

#^---------------------------------------------------------------------------------------------------
#!#Program for Reading the Records from employee table--by using fetchmany()
#OracleSelectRecordEx2.py
# import oracledb as orc
# try:
        
#     conn=orc.connect("system/tiger@localhost/orcl")
#     cur=conn.cursor()    
#     sq="select * from employee"
#     cur.execute(sq)
#     records=cur.fetchmany(4)
#     # print(record)
#     for record in records:    
#         # print(record)
#         for val in record:
#             print(val,end="\t\t")
#         print()    

# except orc.DatabaseError as db:
#     print("problem with oracle connection")
#^---------------------------------------------------------------------------------------------------
#!#Program for Reading the Records from employee table--by using fetchall()
# #OracleSelectRecordEx3.py
# import oracledb as orc
# try:
#     conn=orc.connect("system/tiger@localhost/orcl")
#     cur=conn.cursor()
#     sq="select * from employee"
#     cur.execute(sq)
#     records=cur.fetchall()
#     # print(records)
#     for record in records:
#         # print(record)
#         for val in record:
#             print(val,end="\t\t")
#         print()    


# except orc.DatabaseError as db:
#     print("problem with your python code check it form your side")
#^---------------------------------------------------------------------------------------------------
#!#Program for Getting the Column Names of table
#OracleColumnNames.py
# import oracledb as orc
# try:
#     conn=orc.connect("system/tiger@localhost/orcl")
#     cur=conn.cursor()
#     sq="select * from employee "
#     cur.execute(sq)
#     metadata=cur.description
#     # print(metadata)
#     for colinfo in metadata:
#         print(colinfo[0],end="\t\t")
#     print()
#         # for val in colinfo:
#         #     print(val,end="\t")
#     # print()    
# except orc.DatabaseError as db:
#     print("problem with your code check it",db)
#^---------------------------------------------------------------------------------------------------
#!#Program for Getting the Records from any Table along with Col Names
#OracleColumnsWithRecords.py
# import oracledb as orc
# try:

#     conn=orc.connect("system/tiger@localhost/orcl")
#     cur=conn.cursor()
#     sq="select * from employee"
#     cur.execute(sq)
#     metadata=cur.description
#     print("------------------------------------------------------------")
#     for colinfo in metadata:
#         print(colinfo[0],end="\t\t")
#     print()    
#     print("------------------------------------------------------------")
#     record1=cur.fetchall()
#     for rec in record1:
#         for val in rec:
#             print(val,end="\t\t")
#         print()    
# except orc.DatabaseError as db:
#     print("problem With your python code check it ")

#^---------------------------------------------------------------------------------------------------
#!Program for Getting the Records from any Table along with Col Names
#OracleColumnsWithRecordsByOrder.py
# import oracledb as orc
# def columnwithrecord():
        
#     try:
#         conn=orc.connect("system/tiger@localhost/orcl")
#         print("oracle database connected successfullly ")
#         cur=conn.cursor()
#         # sq="select * from employee order by eno "
#         sq="select * from employee order by eno desc"
#         cur.execute(sq)
#         print("------------------------------------------")
#         metadata=cur.description
#         for colinfo in metadata:
#             print(colinfo[0],end="\t\t")
#         print()    
#         print("------------------------------------------")
#         records=cur.fetchall()
#         for record in records:
#             for val in record:
#                 print(val,end="\t\t")
#             print()    

#         print("------------------------------------------")


#     except orc.DatabaseError as db:
#         print("problem with your python problem",db)
# columnwithrecord()

#^---------------------------------------------------------------------------------------------------



























#^---------------------------------------------------------------------------------------------------
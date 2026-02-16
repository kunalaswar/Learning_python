#!Program for Reading Student Data from KBD and Save them in Student Table by using Classes and Obejcts
#*Example-11
#*Syntax-1
# import sys
# import oracledb  # noqa: F401
# sys.path.append("D:\\PYTHON FULL STACK\\Practice\\Exception_Handling\\NameValidation_1")
# from NameExcept import InvalidNameError,ZerolengthError,SpaceNameError
# from NameValidation import validation

# class student:
#     def readstud(self):
#         try :
                
#             self.sno=int(input("ENTER A STUDENTS NUMBER :"))
#             self.sname=validation(input("ENTER STUDENTS NAME :"))
#             self.marks=float(input("ENTER STUDENTS MARKS :"))
#         except ValueError:
#             print("Dont Enter Str alnum and Special symbols")    
#         except SpaceNameErrer:
#             print("Dont Enter space :")   
#         except InvalidNameError:
#             print("INVALID INPUT PLEASE ENTER PROPERLY")    
#         except ZerolengthError:
#             print("ENTER SOMETHING DONT LEAVE IT")    
#     def dispstuddata(self):
#         print("STUDENTS NUMBER",self.sno)        
#         print("STUDENTS NMAE",self.sname)
#         print("STUDENTS MARKS",self.marks)

#     def savestuddata(self):
#         try:
#             conn=oracledb.connect("system/tiger@localhost/orcl")    
#             print("COnnectio is connected successfully")
#             cur=conn.cursor()
#             iq=(f"insert into students (sno,sname,marks) values({self.sno},'{self.sname}',{self.marks})")
#             cur.execute(iq)
#             conn.commit()
#             print(f"{cur.rowcount} is inserted successfully")
#         except oracledb.DatabaseError as db:
#             print("Connection  with your DB check it ",db)    
# s1=student()            
# s1.readstud()
# s1.dispstuddata()
# s1.savestuddata()

#^-----------------------------------------------------------------------------------------------------
#!Program for Reading Student Data from KBD and Save them in Student Table by using Classes and Obejcts
#*Example-12
#*Syntax-1
# import sys
# import oracledb  # noqa: F401
# sys.path.append("D:\\PYTHON FULL STACK\\Practice\\Exception_Handling\\NameValidation_1")
# from NameExcept import InvalidNameError,ZerolengthError,SpaceNameError
# from NameValidation import validation

# class student:
#     def readstud(self):
#         try:
                
#             self.sno=int(input("Enter a Students number :"))
#             self.sname=input("Enter a students Name :")
#             self.marks=float(input("Enter a Students Marks :"))
#         except ValueError:
#             print("Dont Enter a str alnum and special symbols")
#         except InvalidNameError:
#             print("Invlaid input Enter properly")    
#         except ZerolengthError:
#             print("ENTER SOMETHING DONT LEAVE IT")    
#         except SpaceNameError:
#              print("Dont Enter space :")
#     def dispstuddata(self):
#         print("STUDENTS NUMBER ",self.sno)    
#         print("STUDENTS NAME ",self.sname)    
#         print("STUDENTS MARKS ",self.marks)  
#     def savestuddata(self):
#         try:
                
#             conn=oracledb.connect("system/tiger@localhost/orcl")      
#             print("oracle database is connected successfully")
#             cur=conn.cursor()
#             iq=(f"insert into students(sno,sname ,marks) values({self.sno},'{self.sname}',{self.marks})")
#             cur.execute(iq)
#             conn.commit()
#             if cur.rowcount<0:
#                 print("Not inserted ")
#             else:
#                 print(f"{cur.rowcount} record is inserted successfully ")    

#         except oracledb.DatabaseError as db:
#             print("DATABASE CONNECTION PROBLEM ",db)


# s1=student()
# s1.readstud()
# s1.dispstuddata()
# s1.savestuddata()
#^-----------------------------------------------------------------------------------------------------
#!





































#^-----------------------------------------------------------------------------------------------------
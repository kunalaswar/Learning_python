# class InvalidNameError(Exception):pass
# class ZeroLengthError(BaseException):pass
# class SpaceNameError(Exception):pass
# def validation(name):
#     if len(name)==0:
#         raise ZeroLengthError
#     elif name.isspace():
#         raise SpaceNameError    
#     else:
#         words=input.split()    
#         res=True
#         for word in words:
#             if not word.isalpha():
#                 res=False
#                 break    
#         if res:
#             return name    
#         else:
#             raise InvalidNameError     


# # name=input("ENter a name here :")
# # res=validation(name)
# # print(res)


# import oracledb as orc
# class InvalidNameError(Exception):pass
# class ZeroLengthError(BaseException):pass
# class SpaceNameError(Exception):pass
# def validation(name):
#     if len(name)==0:
#         raise ZeroLengthError
#     elif name.isspace():
#         raise SpaceNameError    
#     else:
#         words=input().split()    
#         res=True
#         for word in words:
#             if not word.isalpha():
#                 res=False
#                 break    
#         if res:
#             return name    
#         else:
#             raise InvalidNameError     

# class students:
#     def readstud(self):
#         try :
                
#             self.sno=int(input("Emter a Students number :"))
#             self.sname=validation(input("ENter a Students Name :"))
#             self.marks=float(input("Enter  students marks"))

#         except ValueError:
#             print("Dont Enter a alnum and special symbol")     
#         except InvalidNameError:
#             print("Dint enter a INVALD INPUT")    
#         except ZeroLengthError:
#             print("ENter your Name ")    
#         except SpaceNameError:
#             print("Dont Enter like this Enter Somethings")    

#     def dispstuddata(self):
#         print("STUDENTS NUMBER ",self.sno)
#         print("STUDENTS NAME ",self.sname)
#         print("STUDENTS MARKS   ",self.marks)

#     def savestuddata(self):
#         try:
#             conn=orc.connect("system/tiger@localhost/orcl")
#             print("COnnection od database is successfully connected")
#             cur=conn.cursor() 
#             print("Cursor object Creation")
#             iq="insert into  students values(%d,'%s',%f)"
#             cur.execute(iq %(self.sno,self.sname,self.marks))
#             conn.commit()
#             print(f"students{cur.rowcount} record inserted sucessfully")
#         except orc.DatabaseError as db:
#             print("problem with your atabse conection ",db)    
# #main program            
# s=students()
# s.readstud()
# s.dispstuddata()
# s.savestuddata()

            



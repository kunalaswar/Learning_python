#^----------------------------------------------------------------------------------------
#!Program for Reading Student Data from KBD and Save them in Student Table by using Classes and Obejcts
#*Example-11
#*Syntax-1
# import sys
# import oracledb  # noqa: F401
# sys.path.append("E:\\FULL STACK PYTHON\\PythonPrograms\\ExceptionHandling\\NameValidation")
# from NameExecpt import InvalidNameError, ZerolenError,SpaceError
# from NameValidation import validation

# class student():

#      def readstud(self):
#       try:
#           self.sno = int(input("Enter Student Number : "))
#           self.name = validation(input("Enter Student Name : "))
#           self.marks = float(input("Enter Student Marks : "))
#       except ValueError:
#          print("Dont Enter alnums,strs, symbols for sno,marks")
#       except InvalidNameError:
#           print("INVALID NAME - PLEASE ENTER VALID NAME ")
#       except ZerolenError:
#          print("PLEASE ENTER NAME - DONT LEAVE EMPTY ")
#       except SpaceError:
#         print("DONT ENTER SPACE")


#      def dispstud(self):
#           print(f"Student Number : {self.sno} : ")
#           print(f"Student Name : {self.name}")
#           print(f"Student Marks : {self.marks} ")
     
#      def savestud(self):
#        try:
#         con = oracledb.connect("system/1234@localhost/orcl")
#         cur = con.cursor()
#         iq = f"insert into student (sno,name,marks) values({self.sno},'{self.name}',{self.marks})"
#         cur.execute(iq)
#         con.commit()
#         print(f"{cur.rowcount} Student Record Inserted")
#        except oracledb.DatabaseError as db:
#           print("Problem in Oracle ",db)


# s = student()
# s.readstud()
# s.dispstud()
# s.savestud()

#^----------------------------------------------------------------------------------------
#*Syntax-2
# import sys
# import oracledb  # noqa: F401
# sys.path.append("E:\\FULL STACK PYTHON\\PythonPrograms\\ExceptionHandling\\NameValidation")
# from NameExecpt import InvalidNameError, ZerolenError,SpaceError
# from NameValidation import validation

# class student():

#      def readstud(self):
#       try:
#           self.sno = int(input("Enter Student Number : "))
#           self.name = validation(input("Enter Student Name : "))
#           self.marks = float(input("Enter Student Marks : "))
#       except ValueError:
#          print("Dont Enter alnums,strs, symbols for sno,marks")
#       except InvalidNameError:
#           print("INVALID NAME - PLEASE ENTER VALID NAME ")
#       except ZerolenError:
#          print("PLEASE ENTER NAME - DONT LEAVE EMPTY ")
#       except SpaceError:
#         print("DONT ENTER SPACE")
#       else:
#          s.dispstud()


#      def dispstud(self):
#           s.savestud()
#           print(f"Student Number : {self.sno} : ")
#           print(f"Student Name : {self.name}")
#           print(f"Student Marks : {self.marks} ")
     
#      def savestud(self):
#        try:
#         con = oracledb.connect("system/1234@localhost/orcl")
#         cur = con.cursor()
#         iq = "insert into student values(%d,'%s',%f)"
#         cur.execute(iq%(self.sno,self.name,self.marks))
#         con.commit()
#         print(f"{cur.rowcount} Student Record Inserted")
#        except oracledb.DatabaseError as db:
#           print("Problem in Oracle ",db)


# s = student()
# s.readstud()
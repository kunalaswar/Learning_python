# def getrecord():
#   con = oracledb.connect("system/1234@localhost/orcl")
#   cur = con.cursor()
#   sq= "select * from student"
#   cur.execute(sq)
#   num = int(input("Enter Student Number Whose Data You Want To View : "))
#   # print("-"*50)
#   # metadata = cur.description
#   # for col in metadata:
#   #   print(col[0],end="\t\t")
#   # print()
#   # print("-"*50)
#   records = cur.fetchall()
#   res = False
#   for record in records:
#       if record[0]==num:
#          res = True
#   if res:
#     print(f"Student Number : {record[0]}")
#     print(f"Student Name : {record[1]}")
#     print(f"Student Marks {record[2]}")
#   else:
#     print("Record Does Not Exist ")


#!-----------------------------------------------------------------------------------------------------


#^-----------------------------------------------------------------------------------------------------
#! Program for Demonstrating the Need of Class Level Data Members
 #* inside of class
# class student:
#    crs = "python"           
#    city= "Hydrabad"    #todo - Here crs and city are called class level data member


# s1 = student()
# # s2 = student()
# # print(type(s1),id(s1))  <class '_main_.student'> 2736275793168
# # print(f"The content of s1 : {s1._dict_}")    #Class Level Data Members are Not available with Object and not part of object 
# #todo - Access the value of class level data members

# print(f"Student course : {s1.crs}")
# print(f"Student city : {s1.city}")
# # print(f"Student course : {s2.crs}")
# # print(f"Student city : {s2.city}")
# print("--------------or-----------------")
# print(f"Student Course : {student.crs}")   # todo - we can access class level data members by objcect and class name also
# print(f"Student City : {student.city}")


# class students:
#     def readstud(self,objinfo):
#         # print("this is an Instance Method ",id (self))
#         print("Current object of that ",id(self))



# s1=students()        
# # s2=students()
# s1.readstud("first")
# print("student reference of s1",id(s1))
# # print("")
# # s2.readstud("second")

#! Program for Demonstrating the Need of Class Level Data Members
# class students:
#     csr="python"
#     city="hyderabad"



# s1=students()    
# s2=students()
# print(id(s1))
# print(id(s2))
# print(f"Content of s1 {s1.__dict__}")
# print(f"content if s2 {s2.__dict__}")
# print("Students courese :",s1.csr)
# print("Students city :",s1.city)

# print("Students course",students.csr)        
# print("Students City",students.city)



#^-----------------------------------------------------------------------------------------
#! Program for Demonstrating the Need of Class Level Data Members
#* inside of main program
# class student : pass

# student.crs = "Python"
# student.city = "Hyd"

# s = student()
# print(f"Content of s : {s._dict_}") #Class Level Data Members are Not available with Object and not part of object 

# print(f"Student Course = {student.crs}")
# print(f"Student City : {student.city}") # todo - we can access class level data members by objcect and class name also

# print("---------or------------")

# print(f"Student Course : {s.crs}")
# print(f"Student City : {s.city}")

#^--------------------------------------------------------------------------------------------------
#!#Program for Demonstrating the Need of Class Level Data Members
#*Example -1 - direct print
# class Student:pass

# s1 = Student()   #todo - type(s1) <class '_main_.student'>
# s2 = Student()

# s1.sno = 100
# s1.name = "Pankaj"
# s1.marks= 58.54


# s2.sno=200
# s2.name="Travis"
# s2.marks=77.77

# print("Content of S1 Object ")
# print(f"Student Number : {s1.sno}")
# print(f"Student Name : {s1.name}")
# print(f"Student Marks : {s1.marks}")
# print("-"*50)

# print("Content of S1 Object ")
# print(f"Student Number : {s2.sno}")
# print(f"Student Name : {s2.name}")
# print(f"Student Marks : {s2.marks}")

#!#Program for Demonstrating the Need of Class Level Data Members
#*Example -1 - direct print
# class students:
#     pass

# s1=students()
# s2=students()

# s1.sno=78
# s1.sname="kunal"
# s1.marks=72

# s2.sno=34
# s2.sname="paa"
# s2.marks=56

# # print("")
# print(s1.sno)
# print(s1.sname)
# print(s1.marks)
# print("----------------------")

# print(s2.sno)
# print(s2.sname)
# print(s2.marks)  
# print("----------------------")

#^--------------------------------------------------------------------------------------------------
#! Program for Demonstrating the Need of Class Level Data Members
#* Example-2 - printing with _dict_ (magic variable , dunder variale)
# class Student:pass

# s1 = Student()
# s2 = Student()
# print(f"Content of s1 : {s1._dict_}")
# print(f"Content of s2 : {s2._dict_} ")
# print(f"Lenght of s1 :  {len(s1._dict_)}")
# print(f"Lenght of s2 : {len(s1._dict_)} ")

# #todo - Place Instance Data Members in S1
# s1.sno = 100
# s1.name = "karan"
# s1.marks = 78.33  #todo - Here sno,name and marks are called Instance Data Members

# #todo - Place Instance Data Members in S2
# s2.sno = 877
# s2.name = "jay"
# s2.marks = 88.85

# print("-"*100)
# print(f"Content of s1 : {s1._dict_}")
# print(f"Content of s2 : {s2._dict_} ")
# print(f"Lenght of s1 :  {len(s1._dict_)}")
# print(f"Lenght of s2 : {len(s1._dict_)} ")
# print("-"*100)

# for val in s1._dict_:
     # print(val,"-->",s1._dict_[val])
     # print(val,"-->",s1._dict_.get(val))
# print("-"*100)

#todo - or
# for k,v in s2._dict_.items():
     # print(f"{k}-->{v}") 
#todo - or
# for k in s2._dict_.keys():
#      print(f"{k}-->{s2._dict_[k]}")


#! Program for Demonstrating the Need of Class Level Data Members
#* Example-2 - printing with _dict_ (magic variable , dunder variale)
# class students:
#      pass

# s1=students()
# s2=students()
# print("content of s1",s1.__dict__)   
# print("Content of s2",s2.__dict__)
# print("length of Students",len(s1.__dict__))
# print("length of Students",len(s2.__dict__))

# s1.sno=int(input("Enter a students number :"))
# s1.sname=input("Enter a students name")
# s1.marks=float(input("Enter a students marks "))
# print(s1.sno)
# print(s1.sname)
# print(s1.marks)

# for v,k in s1.__dict__.items():
#      print(v,"--->",k)
     
#^--------------------------------------------------------------------------------------------------
#! Program for Demonstrating the Need of Class Level Data Members
#*Dynamic input
# class student : pass

# s1 = student()
# s2 = student()

# s1.sno = int(input("Enter student number : "))
# s1.sname = input("Enter student name  : ")
# s1.marks = float(input("Enter student Marks  : "))
# print("-"*50)
# print(f"Student no  : {s1.sno}")
# print(f"Student name : {s1.sname}")
# print(f"Student marks  : {s1.marks}")
# print("-"*50)
# print(f"Content of s1  - {s1._dict_}")
# print("-"*50)

# for k,v in s1._dict_.items():
#      print(f"{k}-->{v}") 
# print("-"*50)

# s2.sno = int(input("Enter student number : "))
# s2.sname = input("Enter student naem  : ")
# s2.marks = float(input("Enter student Marks  : "))
# print("-"*50)
# print(f"Student no  : {s2.sno}")
# print(f"Student name : {s2.sname}")
# print(f"Student marks  : {s2.marks}")
# print("-"*50)
# print(f"Content of s2  - {s2._dict_}")
# print("-"*50)
# for val in s2._dict_:
#      print(val,"-->",s2._dict_[val])

#^-------------------------------------------------------------------------------------------
#! program for Reading and Displaying the Deatils students by using Classes and Objects

# class student:
#      def readstudent(self):
#           print(f"Current Object Reference In Instance Method : {id(self)}")

# s1 = student()
# print(f"Content of S1 before reading : {s1._dict_}")
# print(f"Memory id of S1 in Main Program : {id(s1)}")
# s1.readstudent()                   #todo calling instace method
# print("-----------------")
# s2 = student()
# print(f"Content of S2 before reading : {s2._dict_}")
# print(f"Memory address of S1 in Main Program : {id(s2)} ")
# s2.readstudent()       #todo calling instace method     
#^-------------------------------------------------------------------------------------------
#! program for Reading and Displaying the Deatils students by using Classes and Objects
# class student:
#     def readstudent(self,objinfo):
#      print(f"Enter {objinfo} Student Data : ")
#      self.sno = int(input("Enter Student Number : "))
#      self.sname = input("Enter Student Name : ")
#      self.marks = float(input("Enter Student Marks "))

# s1 = student()
# s2 = student()

# s1.readstudent("First")
# s2.readstudent("Second")


# print("Display the content of S1")
# for dmn,dmv in s1._dict_.items():
#    print(dmn,"-->",dmv)

# print("---------------")

# print("Display the content of S1")
# for dmn in s2._dict_:
#    print(dmn,"-->",s2._dict_[dmn])
#^-------------------------------------------------------------------------------------------

#! program for Reading and Displaying the Deatils students by using Classes and Objects
# class student:
#      def readstudent(self,objinfo):
#           print(f"Enter {objinfo} Student Data : ")
#           self.sno = int(input("Enter Student Number : "))
#           self.sname = input("Enter Student Name : ")
#           self.marks = float(input("Enter Student Marks : "))
#      def displaydata(self,objinfo):
#           print(f"display {objinfo} Student Data")
#           print(f"Student Number : {self.sno}")
#           print(f"Studen Name : {self.sname}")
#           print(f"Student Marks  : {self.marks}")

# s1 = student()
# s2 = student()
# #read the Student Object Data by using Instance Methods
# s1.readstudent("First") # calling Instance Method
# s2.readstudent("Second") # calling Instance Method
# print("--------------")
# s1.displaydata("First") 
# s2.displaydata("Second") 
#^-------------------------------------------------------------------------------------------

# class student:
#     def readstudent(self,objinfo):
#      print(f"Enter {objinfo} Student Data : ")
#      self.sno = int(input("Enter Student Number : "))
#      self.sname = input("Enter Student Name : ")
#      self.marks = float(input("Enter Student Marks "))
#     def displaydata(self,objinfo):
#         print(f"display {objinfo} Student Data")
#         for dmn,dmv in self._dict_.items():
#                print(dmn,"-->",dmv)


# s1 = student()
# s2 = student()
# #read the Student Object Data by using Instance Methods
# s1.readstudent("First") # calling Instance Method
# s2.readstudent("Second") # calling Instance Method
# print("--------------")
# s1.displaydata("First") 
# s2.displaydata("Second")

#^-------------------------------------------------------------------------------------------



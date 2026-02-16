# #! program for reading and displaying the Details Students by USING class and object
#* ONLY REFERENCE RELEATED PART ONLY
# class students:
    
#     def readstud(self):
#         print("Current object REF in Instance Method ",id(self))


# s1=students()
# print( "content of s1 beffore reading ",s1.__dict__)
# print("Memory Address of the S1",id(s1))
# s1.readstud()

#^---------------------------------------------------------------------------------------------------

#! 
# class students:
#     def readstud(self):
#         self.sno=100
#         self.sname="pranva"
#         self.marks=45


# s1=students() 
# print("COntent of s1 Before reading ",s1.__dict__)   
# print("Memory Address of the s1",id(s1))
# s1.readstud()
# print("COntent of s1 Before reading ",s1.__dict__)   
# s2=students()
# s2.readstud()
# print("COntent of s2 Before reading ",s2.__dict__)   

#^---------------------------------------------------------------------------------------------------
#!
# class student:
#     def readstud(self):
#         self.sno=int(input("Enter a Students number :"))
#         self.sname=input("ENter a Students NAME  :")
#         self.marks=float(input("Enter a  students marks :"))


# s1=student()        
# print("Students content ",s1.__dict__)

# s1.readstud()
# print("Students content ",s1.__dict__)
# for k,v in s1.__dict__.items():
#     print(f"{k} ---> {v}")

#^---------------------------------------------------------------------------------------------------
#!

# class student:
#     def readstud(self,objinfo):
#         print(f"Content of {objinfo} student")
#         print("------------------------------------------")
#         self.sno=int(input("Enter a students sno :"))
#         self.sname=input("Enter a Students Name : ")
#         self.marks=float(input("Enter a Students marks :"))
#         print("------------------------------------------")
#     def dispstud(self,objinfo):
#         print("Students number ",self.sno)
#         print("Students Name ",self.sname)
#         print("Students Marks ",self.marks)


# s1=student() 
# s2=student()   
# s1.readstud("first")
# s2.readstud("second")
# s1.dispstud("name")
# print("content of Students",s1.__dict__)
# print("content of Students",s2.__dict__)

#^---------------------------------------------------------------------------------------------------
#!
# class student:
#     def readstud(self,objinfo):
#         self.sno=int(input("ENter a STUDENTS Number :"))
#         self.sname=input("Enter a STUDENTS Name")
#         self.marks=float(input("Enter STUDENTS Marks :"))

#     def dispstud(self,objinfo):
#         print("Student Number :",self.sno)    
#         print("Student Name :",self.sname)    
#         print("Student marks :",self.marks)    

# s1=student()        
# s2=student()
# #read the data form readstud function
# s1.readstud("first")
# s2.readstud("second")

# #write the data form readstud function
# s1.dispstud("first")
# s2.dispstud("second")
# # s2.dispstud("second")

#^---------------------------------------------------------------------------------------------------
#!
# class student:
#     def readstud(self):
#         self.sno=int(input("Enter a Students Number :"))    
#         self.sname=input("Enter  a Students Name")
#         self.marks=float(input("Enter  a students Marks "))
#     def dispdata(self):
#         print("STUDENTS NUMBER",self.sno)    
#         print("STUDENTS NAME ",self.sname)
#         print("STUDENTS MARKS ",self.marks)


# s1=student()
# s2=student()
# s1.readstud()
# s1.dispdata()
# print("Content of the STUDENTS",s1.__dict__)
# print("CONTENT OF THE STUDENTS",s2.__dict__)
# for val in s1.__dict__:
#     print(f"{val} ---> {s1.__dict__.get(val)}")

#^---------------------------------------------------------------------------------------------------
#todo - TODAY 02-12-2024
#!
# class student:
#     def readstud(self):
#         self.sno=int(input("Enter a STUDENTS NUMBER :"))
#         self.sname=input("Enter a STUDENTS NAME ")
#         self.marks=float(input("Enter a STUDENTS MARKS :"))

#     def dispstud(self):
#         print("="*50)
#         print("STUDENTS NUMBER :",self.sno)    
#         print("STUDENTS NAME",self.sname)
#         print("STUDENTS MARKS",self.marks)
#         print("="*50)

# s1=student()
# s2=student()

# s1.readstud()
# s1.dispstud()
# s2.readstud()
# s2.dispstud()

#^---------------------------------------------------------------------------------------------------
#!
# class students:
#     def readval(self):
#         self.sno=int(input("ENTER A STUDENTS NUMBER "))
#         self.sname=input("ENTER A STUDENTS NAME")
#         self.marks=float(input("ENTER A STUDENTS MARKS :"))
#     def dispstud(self):
#         print(self.sno)
#         print(self.sname)
#         print(self.marks)

# #* MAIN PROGRAM
# # print("STUDENTS CONTENT = ",s1.__dict__)

# s1=students()        
# s2=students()
# print("STUDENTS CONTENT = ",s1.__dict__)
# print("-"*50)
# s1.readval()
# s1.dispstud()
# print("STUDENTS CONTENT = ",s1.__dict__)
# print("-"*50)
# s2.readval()
# s2.dispstud()
# print("STUDENTS CONTENT = ",s2.__dict__)

#^---------------------------------------------------------------------------------------------------
#!

# class students:
#     def read(self,objinfo):
#         print(f"{objinfo} of the current object :")
#         self.sno=int(input("Enter  a stuents NUMBER :"))
#         self.sname=input("Enter a students NAME :")
#         self.marks=float(input("Enter a students marks :"))

#     def dispstud(self):
#         print("Students number ",self.sno)    
#         print("Enter sudents name",self.sname)
#         print("Enter a students marks",self.marks)

# s1=students()
# s2=students()
# print("_"*50)
# s1.read("first")
# s1.dispstud("second")
# print("Students CONTENT ",s1.__dict__)
# for k,v in s1.__dict__.items():
#     print(f"{k}--->{v}")

# print("_"*50)

# print("Students CONTENT ",s2.__dict__)
# s2.read()
# s2.dispstud()
# print("Students CONTENT ",s2.__dict__)
# for k ,v in s2.__dict__.items():
#     print(f"{k}--->{v}")
# print("_"*50)

#^---------------------------------------------------------------------------------------------------
#!

# class student:
#     def readstud(self):
#         self.sno=int(input("Enter  a stuents number :"))
#         self.sname=input("Enter a students Nmae :")
#         self.marks=float(input("Enter a students marks :"))
#     def disp(self):
#         print(self.sno)    
#         print(self.sname)
#         print(self.marks)
# s1=student()    #todo -object creation
# s2=student()
# s1.readstud()
# s1.disp()
# print("STUDENTS CONTENT",s1.__dict__)
# for val in s1.__dict__.keys():
#     print(f"{val}--->{s1.__dict__.get(val)}")

# s2.readstud()
# s2.disp()
# print("STUDENTS CONTENT",s2.__dict__)
# for val in s2.__dict__.keys():
#     print(f"{val}--->{s2.__dict__.get(val)}")


#!
#^---------------------------------------------------------------------------------------------------

# class student:
#     def readstud(self):
#         self.sno=int(input("Enter a STUDENTS NNUMBER  :"))
#         self.sname=input("Enter  a STUDENTS NAME :")
#         self.marks=float(input("Enter a students marks :"))

#     # def dispstud(self):
#     #     print("students NUMBER ",self.sno)    
#     #     print("students name",self.sname)
#     #     print("students marks",self.marks)
# s1=student()        
# s2=student()
# print("STUDENTS CONTENT ",s1.__dict__)
# s1.readstud()
# print("STUDENTS CONTENT ",s1.__dict__)
# # s1.dispstud()
# print("STUDENTS CONTENT ",s2.__dict__)
# s2.readstud ()
# print("STUDENTS CONTENT ",s2.__dict__)
# # s2.dispstud()

#!

#^---------------------------------------------------------------------------------------------------
# class student:
#     crs="python"
#     city="HYD"

# s1=student()
# s2=student()
# # print(s1.{sno:10,sname:"kunal",marks:100})
# print(s1.__dict__)
# for k,v in student.__dict.items():
#     print(f"{k}--->{v}")

#^---------------------------------------------------------------------------------------------------
#!

# class student:
#     def readstud(self,objinfo):
#         print(f"{objinfo}STUDENTS CONTENT")
#         self.sno=int(input("Enter a STUDENTS NUMBER :"))
#         self.sname=input("ENTER A STUDENTS NAME :")
#         self.marks=float(input("ENTER A STUDENTS MARKS :"))
#     def dispstud(self,objinfo):
#         print(f"{objinfo} STUDENTS CONTENT ")
#         print("students NUMBER ",self.sno)
#         print("STUDENTS NAME ",self.sname)
#         print("STUDENTS MARKS",self.marks)

   
# s1=student()        
# s2=student()

# s1.readstud("first")
# s1.dispstud("first")
# s2.readstud("second")
# s2.dispstud("second")

# # print(type(self.sno))
# for k,v in s1.__dict__.items():
#     print(f"{k}--->{v}")

# for val in s2.__dict__.keys():
#     print(f"{val} --->{s2.__dict__[val]}")


#^---------------------------------------------------------------------------------------------------
# todo - 02-12-2024

#!program for reading the students Details by using the class and object
# class student:
#     def readstud(self, objinfo):
#         self.sno=int(input("Enter a students Number"))
#         self.sname=input("Enter a students name")
#         self.marks =float(input("Enter a students marks"))
#     def dispstud(self,objinfo):
#         print(self.sno)    
#         print(self.sname)
#         print(self.marks)


# s1=student()   #* creation of data   
# s2=student()   #* creation of data
# s1.readstud("first")
# s1.dispstud("first")
# print("-"*50)
# s2.readstud("second")
# s2.dispstud("second")
# print("-"*50)

#^---------------------------------------------------------------------------------------------------
#! program for Reading and Displaying the Deatils students by using Classes and Objects
#InstanceMethodEx5.py
# class student:
#     def readstud(self,objinfo):
#         print("-------------------------------------------")
#         self.sno=int(input("Enter a students number :"))
#         self.sname=input("Enter a students name :")
#         self.marks=float(input("Enter a students marks :"))
#         self.dispstud(objinfo) #todo - calling Instance Method by using self
        
#         print("-------------------------------------------")
#     def dispstud(self,objinfo ):
#         print("STUDENTS NUMBER",self.sno)   
#         print("STUDENTS NAME ",self.sname)
#         print("STUDENTS MARKS",self.marks)
# s1=student()        
# s2=student()
# s1.readstud("first")
# s2.readstud("second")


#^---------------------------------------------------------------------------------------------------
#! Program for Finding Sum of Two Numbers by using Classes and Objects
# #InstanceMethodEx6.py
# class sum():pass

# s=sum()
# s.a=int(input("Enter a first value :"))
# s.b=int(input("Enter a  second value :"))
# s.c=s.a+s.b
# print("sum = ",s.c)
# print(f"{s.a} + {s.b} = {s.c}")

#^---------------------------------------------------------------------------------------------------
#!#! Program for Finding Sum of Two Numbers by using Classes and Objects
# #InstanceMethodEx7.py
# class sum:
#     def readvalues(self):
#         self.a=int(input("Enter a first number :"))
#         self.b=int(input("Enter a second number :"))
#     def addval(self):
#         self.c=self.a + self.b
#         return self.c
#     def disp(self):
#         print("Sum = ",self.c)

# s1=sum()        
# s1.readvalues()
# s1.addval()
# s1.disp()
# print("---------")

#!
# class sum:
#     def readvalue(self):
#         self.a=float(input("Enter a first number :"))
#         self.b= float(input("Enter a second number :"))

#     def addval(self):
#         self.c=self.a+self.b    

#     def disp(self):
#         print("first values ",self.a)    
#         print("second values ",self.b)
#         print("SUM = ",self.c)

# s1=sum()        
# s1.readvalue()
# s1.addval()
# s1.disp()
#^---------------------------------------------------------------------------------------------------

#!#Program for Finding Sum of Two Numbers by using Classes and Objects
#InstanceMethodEx8.py
# class sum:
#     def readstud(self):
#         self.a = int(input("ENter a first number :"))
#         self.b = int(input("ENter a second number :"))
#     def addval(self):
#         self.c = self.a+ self.b    

#     def dispstud(self):
#         self.readstud() # calling Instnace Method from another Instance Method
#         self.addval() # calling Instnace Method from another Instance Method
#         print("FIRST NAME ",self.a)    
#         print("SECOND NAME ",self.b)    
#         print("SUM = ",self.c)

# s1=sum()        
# s2=sum()
# s1.dispstud()
# print("--------------")

#!#Program for Finding Sum of Two Numbers by using Classes and Objects
#InstanceMethodEx8.py
# class sum:
#     def readvalue(self):
#         self.a=int(input("ENter A first NUMBER :"))
#         self.b=int(input("Enteer a second number "))

#     def addval(self):
#         self.c=self.a + self.b

#     def dispval(self):
#         self.readvalue()    
#         self.addval()
#         print("FIRST VLAUE :",self.a)
#         print("SECOND VLAUE :",self.b)
#         print("SUM =  ",self.c)
# s1=sum()
# s1.dispval()


#^---------------------------------------------------------------------------------------------------   
#! Program for Finding Sum of Two Numbers by using Classes and Objects
#InstanceMethodEx9.py
# class sum:
#     def readval(self):
#         self.a=int(input("Enter a first value"))
#         self.b=int(input("ENter a second value"))
#     def addval(self):
#         c=self.a+self.b
#         return c
#     def dispval(self):
#         self.readval()    
#         kvr=self.addval()
#         print("FIRST VALUE",self.a)
#         print("SECOND VLAUE ",self.b)
#         print("SUM = ",kvr)
# s1=sum()    #object creation     
# s1.dispval()  #Calling instance method with respect to object name  

#^---------------------------------------------------------------------------------------------------   
#!#Program for Cal Factorial of a Number
#InstanceMethodEx10.py

# class factorial:
#     def readval(self):
#         try:
#            self.n=int(input("ENTER a number for calculate factorial :"))        
#         except ValueError:
#             print("DOnt Enter str alnum and special symbols")
#     def calfact(self):
#             if self.n<0:
#                 print(f"INVALID INPUT {self.n}")   
#             else:
#                 fact=1
#                 for i in range(1,self.n+1):
#                     fact=fact*i 
#                 else:
#                     return fact   
#     def dispfact(self,res):            
#         print(f"{self.n}--->{res}")   

# s1=factorial()         
# s1.readval()
# res=s1.calfact()
# s1.dispfact(res)

#!

# class factorial:
#     def readval(self):
#         try:

#             self.n=int(input("ENter a number to get Factoforial :"))
#         except ValueError:
#             print("Dont Enter str str alnum and special")    
#     def calfact(self):
#         if self.n<0:
#             print("INVALID INPUT")        
#         else:
#             fact=1    
#             for i in range(1,self.n+1):
#                 fact=fact*i
#             else:
#                 return fact    
#     def dispfact(self,res):
#         print(res)


# s1=factorial()
# s1.readval()
# res=s1.calfact()
# s1.dispfact(res)

#! program 

# class factorial:
#     def read(self):
#         try:
#             self.n=int(input("Enter a number of to get factorial : "))
#         except ValueError:
#             print("Dont Enter an str Alnum and special symbols")    
#     def calfact(self):
#         if self.n <0:
#             print("INVALID INPUT OT ENTER ")       
#         else:
#             fact=1    
#             for i in range(1,self.n+1):
#                 fact=fact*i 
#             else:
#                 print(fact)    
#     # def           



# s1=factorial()
# s1.read()
# s1.calfact()
# # res=s1.calfact()
# # print(res)


#^---------------------------------------------------------------------------------------------------   
#! 
# class factorial:
#     def read (self):
#         try:
#             self.n=int(input("ENter a number for getting the factoiral "))
#         except ValueError:
#             print("Dont Enter a str alnum and special ")    
#     def calfact(self):
#         if self.n<0:
#             print("DOnt Enter str special symbol and sting")        
#         else:
#             fact=1    
#             for i in  range(1,self.n+1):
#                 fact=fact*i
#             else:
#                 return fact    
#     def dispfact(self,res):
#         print(f"{self.n} --->{res}")
# s1=factorial()        
# s1.read()
# res=s1.calfact()
# # print(res)
# s1.dispfact(res)
#^---------------------------------------------------------------------------------------------------   
#* REPEATE THE PROGRAM FOR ME 
# class factorial:
#     def read(self):
#         try:
#             self.n=int(input("ENter a number for factorial of number :"))
#         except ValueError:
#             print("Dont Enter a str alnum  and special character ")    

#     def calfact(self):
#         if self.n<0:
#             print("Invalid input ")
#         else:
#             fact=1
#             for i in range(1,self.n+1):
#                 fact=fact*i    
#             else:
#                 return fact    
#     def dispfact(self,res):
#         print(res )
# s1=factorial()        
# s1.read()
# res=s1.calfact()
# s1.dispfact(res)

#^---------------------------------------------------------------------------------------------------   
#!Program for Cal Fctorial of a Number
#InstanceMethodEx10.py
# class factoiral:
#     def read(self):
#         try:
#             self.n=int(input("ENter a number to get factoiacal"))
#         except ValueError:
#             print("DOnt enter a Str alnum and special symbol")    
#         res=s1.calfact()
#         s1.dispfact(res)
#     def calfact(self):
#         if self.n<0:
#             print("DONt  Enter special sumbol nad str ")        
#         else:
#             fact=1    
#             for i in range(1,self.n+1):
#                 fact=fact*i
#             else:
#                 return fact    
#     def dispfact(fact,res)            :
#         print(res)

# s1=factoiral()        
# s1.read()


#^---------------------------------------------------------------------------------------------------   
#todo- Program for Reading Student Data from KBD and Save them in Student Table by using Classes and Obejcts
#& StudentOopWithOracle.py














#^---------------------------------------------------------------------------------------------------





#^---------------------------------------------------------------------------------------------------   






#^---------------------------------------------------------------------------------------------------








































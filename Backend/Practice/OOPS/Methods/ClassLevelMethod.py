 #!CLassLevelMethod.py
# class Employee:
#     @classmethod 
#     def getvals(cls): #class level method
#         cls.compname = "IBM"
#         cls.city = "HYD"

# #main program
# Employee.getvals()
# print("company name",Employee.compname)
# print("comapany city",Employee.city)

# #* OR 
# eo=Employee()
# print("Content ot oe",eo.__dict__)
# print("comp name",eo.compname)
# print("Comp city",eo.city)

#^-----------------------------------------------------------------------------------------------------
# #! #!CLassLevelMethod2.py 
# class Employee:
#     @classmethod 
#     def getcomp(cls):
#         cls.compname="IBM"
#     @classmethod    
#     def getcity(cls):
#         cls.city="HYD"

# Employee.getcomp()        
# Employee.getcity()
# print("comp name",Employee.compname)
# print("comp city",Employee.city)
# print("----------------------")
#^-----------------------------------------------------------------------------------------------------

# #! ClassLevelMethodEx3.py
# class Employee:
#     @classmethod
#     def getcomp(cls):
#         cls.compname = "IBM"

#     @classmethod 
#     def getcity(cls):
#         Employee.city="HYD"    

# Employee.getcomp()        
# Employee.getcity()
# print("company name",Employee.compname)
# print("Company city",Employee.city)

#^-----------------------------------------------------------------------------------------------------
#!
#* syntax -1

# class Employee:
#     @classmethod
#     def getcomp(cls):
#         cls.compname="IBM"
#     @classmethod
#     def getcity(cls):
#         cls.city = "HYD"    
# Employee.getcomp()        
# Employee.getcity()
# print("COMPANY name = ",Employee.compname)
# print("company city",Employee.city)     
# print("----------------------")

# e=Employee()
# e.getcomp()
# e.getcity()
# e.compname
# e.city

#^-----------------------------------------------------------------------------------------------------
#!
#* syntax -2
# class Employee:
#     @classmethod
#     def getcomp(cls):
#         cls.compname="IBM"
#     @classmethod 
#     def getcity(cls):
#         cls.city = "HYD"    

# Employee.getcomp()        
# Employee.getcity()
# print("company name",Employee.compname)
# print("Company city",Employee.city)

#^-----------------------------------------------------------------------------------------------------
#!
# class Employee:
#     @classmethod
#     def getcomp(cls):
#         cls.compname="ibm"
#         # Employee.getcity()
#         cls.getcity()
        
#     @classmethod    
#     def getcity(cls):
#         cls.city="HYD"
# Employee.getcomp()        
# print("Comp name",Employee.compname)
# print("Comp city ",Employee.city)
# print("---------------")

#^-----------------------------------------------------------------------------------------------------

#! ClassLevelMethodEx4.py

#* syntax-1
# class Employee:
#     @classmethod
#     def getcomp(cls):
#         cls.compname = "ibm"
#        
#     @classmethod
#     def getcity(cls):
#         cls.city="HYD"

#     def getempdetails(self):
#         self.eno=int(input("Enter a Emp number :"))        
#         self.name=input("Enter a Emp name :")
#         self.sal=float(input("Enter a emp sal :"))
#         
#     def dispempvals(self):
#         print("------------------------")
#         print("Employee number",self.eno)    
#         print("Employee Name",self.name)
#         print("Employee sal",self.sal)
#         print(" EMPLOYEE COMPANY NAME",self.compname)
#         print("EMPLOYEE COMP CITY",Employee.city)
# Employee.getcomp()        
# Employee.getcity()
# e=Employee()
# e.getempdetails()
# e.dispempvals()
#!
#^-----------------------------------------------------------------------------------------------------
#* syntax-2
# class Employee:
#     @classmethod
#     def getcomp(cls):
#         cls.compname="IBM"
#         # cls.getcity() 
#         Employee.getcity() 
#     @classmethod
#     def getcity(cls):
#         cls.city = "hyd"
        
#     def getemp(self):
#         self. eno=int(input("Enter a Emp  number :"))   
#         self.name=input("Enter a Emp name ")
#         self.sal=float(input("Enter a salary :"))
#         self.dispemp()
#     def dispemp(self):
#         print("EMPLOYEE number",self.eno)    
#         print("EMPLOYEE name",self.name)    
#         print("EMPLOYEE sal",self.sal)    
#         # print("EMPLOYEE ")    
#         print("\tEMPLOYEE COMP ",Employee.compname)    
#         print("\tEMPLOYEE ",self.city)    

# Employee.getcomp()
# e=Employee()
# e.getemp()


#!
#^-----------------------------------------------------------------------------------------------------
#*syntax-3

# class Employee:
#     @classmethod
#     def getcomp(cls):
#         cls.compname = "ibm"
#     @classmethod
#     def getcity(cls):
#         cls.city = "hyd"    
#     def getemp(self):
#         self.eno=int(input("Enter a employee number"))     
#         self.name=input("Enter a Employee  Name ")
#         self.sal=float(input("Enter a emp sal "))
#     def dispemp(self):
#         print("Employee number ",self.eno)    
#         print("Employee name",self.name)
#         print("Employee sal",self.sal)
#         print("\t EMPLOYEE COMP NAME",self.compname)
#         print("\tEMPLOYEE CITY ",self.city)

# Employee.getcomp()        
# Employee.getcity()
# e=Employee()
# e.getemp()
# e.dispemp()

#!

#^-----------------------------------------------------------------------------------------------------
#! ClassLevelMethodEx5.py
#* syntax -1
# class Employee:
#     @classmethod
#     def getcomp(cls):
#         cls.compname="IBM"
#         cls.getcity()
#     @classmethod
#     def getcity(cls):
#         cls.city = "hyd"    

#     def getempdetails(self):
        
#         self.sno=int(input("Enter  a Emp number :"))    
#         self.name=input("Enter a Emp name :")
#         self.sal=float(input("Enter a Emp sal "))
#         self.dispempvals()
        
        
#     def dispempvals(self):
        
#         print("-"*50)
#         Employee.getcomp()
#         print("EMPLOYEE NUMBER ",self.sno)    
#         print("EMPLOYEE Name ",self.name)    
#         print("EMPLOYEE sal ",self.sal)    
#         # print("EMPLOYEE  ",)    
#         print("\tEMPLOYEE Comp name ",Employee.compname)    
#         print("\tEMPLOYEE NUMBER ",Employee.city)    
#         print("-"*50)

# Employee.getcomp()
# e=Employee()
# e.getempdetails()
# #?============================
# #* Another syntax 
# Employee().getempdetails()

#^-----------------------------------------------------------------------------------------------------
#!#ClassLevelMethodEx6.py
# class Employee:
#     @classmethod
#     def getcomp(cls):
#         cls.compname="IBM" 
#         cls.getcity()
        
#     @classmethod 
#     def getcity(cls):
#         cls.city="HYD"    
#         Employee().getempdetails()        

#     def getempdetails(self):
      
        
#         # e.dispempvals()
#         self.sno=int(input("Enter a emp no:"))
#         self.name=input("Enter a Emp name :")
#         self.sal=float(input("Enter a Emp sal :"))
#         self.dispempvals()
#     def dispempvals(self):
#         print("="*50)
#         print("Employee number ",self.sno)    
#         print("Employee name ",self.name)    
#         print("Employee sal ",self.sal)    
#         print("\tEmployee comp name  ",self.compname)    
#         print("\tEmployee city ",self.city)    
#         print("="*50)
        
# #main program        
# Employee.getcomp()
# # e=Employee()


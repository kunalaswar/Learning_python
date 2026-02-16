  #! #Non-DestEx1.py
  #^--------------------------------------------------------------------------------------------------
# class employee:
#     def __init__(self):
#         print("I am form parametrrized constructor ")
#         self.eno=int(input("ENter a Emoloyee number :"))
#         self.name=input("Enter a Employee Name :")
#         print("Emp number ",self.eno)
#         print("Emp name ",self.name)

# e1=employee()
#^----------------------------------------------------------------------------------------------------
#!
# class employee:
#   def __init__(self):
#     print("I am from parametetized contructor ")
#     self.sno=int(input("Enter  a employee number :"))
#     self.name =input("ENter a Employee name :")
#     print("Employee number ",self.sno)
#     print("Employee name",self.name)
#     print("------------------------------------")

# e1 = employee()    
# # e1 = employee() there is no parameter value 

#^----------------------------------------------------------------------------------------------------
#!
# class employee:
#   def __init__(self,sno ,name):
#     print("I am from parameterzed constructor ")
#     self.no=sno
#     self.sname=name
#     print("Employee numbeer ",self.no)
#     print("Employee Name ",self.sname)
# # s1  = employee()     
# s1 = employee(10,"RS")


#^----------------------------------------------------------------------------------------------------
# #! DestEx1.py

# class employee:
#     def __init__(self,sno,sname):
#         print(f"I am from parameterized constuctor and  ID {id(self)}")
#         self.sno=sno
#         self.sname=sname
#         print("Employee number ",self.sno)
#         print("Employee name ",self.sname)  
#         print("")

#     def __del__(self):
#         print(f"GS calls __del__() for de-allocating the memory space of the current object { id(self)}" )    




# e1=employee(10,"KA")
# e2=employee(20,"TR")
# e3=employee(30,"RS")

#^----------------------------------------------------------------------------------------------------
#!DecEX.1
# class employee:
#     def __init__(self,sno,sname):
#         print("IT is an parameterized constructor :")
#         self.sno = sno
#         self.name = sname
#         print("Emoloyee number ",self.sno)
#         print("Emloyee Name ",self.name)
        

# e1 = employee(10,"TS")         

#^----------------------------------------------------------------------------------------------------
#!
# import time
# class Emoloyee:
#     def __init__(self,sno,sname):
#         self.sno = sno #int(input("Enter a emloyee number :"))
#         self.sname= sname #input("Enter employee name :"    
#         print("emoloyee number ",self.sno)
#         print("Emoloyee name ",self.sname)
#     def __del__(self):
#         print(f"GC Class __del__() for de-allocating the memory the memory of current object {id(self)}")


# e1=Emoloyee(10,"kunal")
# e2=Emoloyee(20,"sagar")
# e3=Emoloyee(30,"aniket")
# time.sleep(3)
#^----------------------------------------------------------------------------------------------------
#!DestEx2.py

# import time ,sys
# class employee:
#     def __init__(self,eno,ename):
#         print("I am from Parameterized constructor ",id (self))
#         self.eno = eno
#         self.name = ename
#         print(f"Emp number {self.eno}")
#         print(f"Emp name {self.name}")
#         print("----------------------------------")
#     def __del__(self):
#         print("GC Calls __del__() for de-allocating the memory space of current object:{}".format(id(self)))
#         global memspace 
#         memspace = memspace-sys.getsizeof(self)
#         print("\t Now memory space =",memspace)    



# e1=employee(10,"KS")
# e2=employee(20,"bb")
# e3=employee(30,"aa")
# memspace =sys.getsizeof(e1)+sys.getsizeof(e2)+sys.getsizeof(e3)  
# # print(memspace)
# print("Total Memory space of all object ",memspace)

# time .sleep(1)

#^----------------------------------------------------------------------------------------------------
#! 
# import sys,time
# class employee:
#     def __init__(self,sno,sname):
#         self.sno = sno
#         self.sname=sname
        
#         print("emoloyee Number ",self.sno)    
#         print("emoloyee name ",self.sname)    
#         # print("---------------------------")

#     def __del__(self):
#         global memspace
#         print("GS calls __del__() it is call at a last")    
#         memspace =memspace - sys.getsizeof(self)
#         print(memspace)


# e1=employee(10,"fd")
# e2=employee(20,"ss")
# e3=employee(30,"ds")
# memspace = sys.getsizeof(e1)+sys.getsizeof(e2)+sys.getsizeof(e3)
# print(memspace)
#^----------------------------------------------------------------------------------------------------
#! DestEx3.py

# import time
# class employee:
#     def __init__(self,sno,sname):
#         print("-----------------------------------")
#         self.sno = sno
#         self.sname = sname
#         print("Emloyee number ",self.sno)
#         print("Emoloyee name",self.sname)
#         print("-------------------------------------")

#     def __del__(self):
#         print("GC Calls __del__() for de-allocating the memory space of current object:")

# e1 = employee(10,"tt")
# print("NO longer Interesed  to use object e1")
# time.sleep(2)
# e1=None  #* GC calls Destructor Forcefully
# e2 = employee(20,"aa")
# print("NO longer Inteereated to use object e2")
# time.sleep(2)
# e2 = None
# e3 = employee(30,"ff")
# print("NO longer Interested to use object e3")
# time.sleep(2)
# e3 = None
# e4 = employee(40,"dd")
#^----------------------------------------------------------------------------------------------------
#! DestEx4.py
# import time
# class employee:
#     def __init__(self ,sno,sname):
#         print("I am a parameterised constructor")
#         self.sno = sno
#         self.sname = sname
#         print("employee numner ",self.sno)     
#         print("Emoloyee name",self.sname)
#         print("--------------------------------")

#     def __del__(self):
#         print("Garbage collector call __del__() for de- allocating the memery space of memory  object ")     

# e1=employee(10,"aaa")        
# print("No Longer Interested to use object e1")

# time.sleep(2)
# del e1
# e2=employee(20,"bbb")
# print("No Longer Interested to use object e2")
# time.sleep(2)
# del e2
# e3=employee(30,"ccc")
# print("No Longer Interested to use object e2")
# time.sleep(2)
# del e3
#^----------------------------------------------------------------------------------------------------
#!#DestEx5.py
# class employee:
#     def __init__(self,sno,sname):
#         print("I am from parameterized constructor ")
#         self.sno = sno
#         self.sname = sname
#         print("employee number ",self.sno)
#         print("employee name ",self.sname)
#         print("---------------------------")
#     def __del__(self):
#         print("i am Destructor that is call by Garbage collector ")

# #Main program
# e1 = employee(10,"aaa") 
# e2=e1 #todo Deep copy 
# e3=e1 #todo Deep copy

# print(e1.__dict__)
# print(e2.__dict__)
# print(e3.__dict__)
# e1.__dict__['sname'] = "kunal"  #todo - it is a updation part it is an a dict
# print(e1.__dict__)

#^----------------------------------------------------------------------------------------------------

#! DestEx6.py
# import time
# class employee:
#     def __init__(self,sno,sname):
#         self.sno = sno
#         self.sname = sname
#         print("Employee number ",self.sno)
#         print("Employee name",self.sname)
#     def __del__(self):
#         print("GC Calls __del__() for de-allocating the memory space of current object:")

# #main program
# print("program Execution Started ")
# e1=employee(10,"ppp")
# e2 = e1 #Deep copy
# e3 = e1 #Deep copy
# print("No longer Intersted to use object e1")
# time.sleep(1)
# e1= None
# print("NO longer intersted to use object e2")
# time.sleep(1)
# e2=None
# print("NO longer Interseted to use object e3")
# time.sleep(1)
# e3=None


# print()



 #! StaticlevelMethodEx.1
#^----------------------------------------------------------------------------------------------------
# class emp:
#     def getempvals(self):
#         self.eno=int(input("ENter a employee number :"))
#         self.name=input("Enter a emoployee name")
#         self.sal=float(input("Enter a employee salary "))

# class student:
#     def getstudvals(self):
#         self.sno=int(input("Enter  a Student snumber :"))    
#         self.name=input("ENter students name ")
# class teacher:
#     def getteachervals(self):
#         self.tno=int(input("ENter a teacher number :"))
#         self.name=input("Enter a teacher name :")
#         self.exp=float( input("ENter a teacher Experience :"))
#         self.sub=input("Enter a teacher Subject:")

# class hyd:
#     @staticmethod
#     def dispobjdata(obj,objinfo):
#         print(objinfo)        
#         print("----------")
#         for k,v in obj.__dict__.items():
#             print(f"{k}--->{v}")


# e=emp()        
# s=student()
# t=teacher()
# e.getempvals()
# s.getstudvals()
# t.getteachervals()
# h=hyd()
# # hyd.dispobjdata(e,"employee")
# # hyd.dispobjdata(s,"student")
# # hyd.dispobjdata(t,"teacher")

# h.dispobjdata(e,"employee")
# h.dispobjdata(s,"student")
# h.dispobjdata(t,"teacher")

#^----------------------------------------------------------------------------------------------------
#!#StaticMethodEx2.py

# class emp:
#     def getvalemp(self):
#         self.eno=int(input("Enter a employee number :"))
#         self.name = input("Enter a employee name :")
#         self.sal=float(input("Enter employee salary :"))
# class student:
#     def getvalstudent(self):
#         self.sno=int(input("Enter a students number :"))        
#         self.name=input("ENter a students name :")
        
# class teacher:
#     def getteachervals(self):
#         self.tno=int(input("ENter a teacher number :"))        
#         self.name=input('Enter a teacher name :')
#         self.exp=float(input("Enter a teacher Exp :"))
#         self.sub=input("Enter a teacher subject :")
# class hyd:
#     @staticmethod
#     def dispobjdata(obj, objinfo):
#         print("------------------------")
#         print(f"{objinfo} object informmation ")
#         for k,v in obj.__dict__.items():
#             print(f" {k}--->{v}")

# e=emp()
# e.getvalemp()
# print("---------------")
# s=student()
# s.getvalstudent()
# print("---------------")
# t=teacher()
# t.getteachervals()
# h=hyd()
# h.dispobjdata(e,"employee")
# h.dispobjdata(s,"students")
# h.dispobjdata(t,"teacher")

#^----------------------------------------------------------------------------------------------------
#!#StaticMethodEx3.py
# class emp:
#     def getempvals(self):
#         self.eno=int(input("ENter a enployee number "))
#         self.name=input("ENter a enployee name ")
#         self.sal=float(input("ENter a enployee sal "))

#         hyd.dispobjdata(e,"employee")

# class student:
#     def getstudvals(self):
#         self.sno=int(input("ENter a student number :"))    
#         self.sname=input("Enter a student name :") 
        
#         hyd.dispobjdata(s,"student")
# class teacher:
#     def getteachervals(self):
#         self.tno=int(input("Enter a teacher number :"))         
#         self.name=input("Enter a teacher nmae :")
#         self.exp=float(input("Enter a teacher exp :")) 
#         self.sub=input("Enter a teacher subject :")

#         hyd.dispobjdata(t,"teacher")
# class hyd:
#     @staticmethod
#     def dispobjdata(obj,objinfno):
#         for k,v in obj.__dict__.items():
#             print(f"{k}--->{v}")        

# e=emp()
# s=student()
# t=teacher()
# e.getempvals()
# s.getstudvals()
# t.getteachervals()

# ch=input("Enter your choice here :")
# match(ch):
#     case 1:

#^----------------------------------------------------------------------------------------------------
#!ArithmeticCalOops1.py
# class Calculator:
#     def getvals(self):
#         self.a=int(input("Enter a first value :"))
#         self.b=int(input("Enter a second value :"))
#         self.op=input("Enter a operator ")
# class result:
#     def displayvals(ao):
#         match(ao.op):                
#             case "+":
#                 print(f"sum ({ao.a} {ao.b}) = {ao.a + ao.b} ")
#             case "-":
#                 print(f"sub {ao.a} {ao.b} = {ao.a-ao.b}")    
#             case "*":
#                 print(f"Mul {ao.a} {ao.b} = {ao.a * ap.b} ")    
#             case "/":
#                 print(f"div {ao.a} {ao.b} = {ao.a / ao.b}")    
#             case "//":
#                 print(f"floDiv {ao.a} {ao.b} = {ao.a // ao.b}")    
#             case "%":
#                 print(f"mod {ao.a} {ao.b} = {ao.a % ao.b }")    
#             case "**":
#                 print(f"pow {ao.a} {ao.b} = {ao.a ** ao.b}")    
#             case _:
#                 print(f"{ao.op} is not arithmetic operator ")    


# co= Calculator()    
# while(True):
        
#     try:
            
#         co.getvals()

#         result.displayvals(co) 
#     except ValueError:
#         print("Don't Enter str alnum and special symbols ")
#     else:
#         break

#^ -------------------------------------------------------------------------------------------------        
#^ tempory program        
# class emp:
#     def getval(self):
#         self.sno=int(input("Enter a student number :"))
#         self.name=input("Enter a Name :")
#     def dispvals(self):
#         print(e1.__dict__["sno"])
#         print(e1.__dict__.get("sno"))
#         print(e1.__dict__.keys())
        
#         # for k,v in e1.__dict__.items():
#         #     print(k,"- >",v)
# e1=emp()
# e1.getval()
# e1.dispvals()
# # print(e1.__dict__)
# # for k,v in e1.__dict__.items():
# #     print(k,"- >",v)
#^ -------------------------------------------------------------------------------------------------        
#!ArithmeticCalOops2.py
# class Calculator:
#     def getval(self):
#         self.a=int(input("Enter a first value :"))
#         self.b=int(input("Enter a second value :"))
#         self.op=input("Enter a Arithmetic operator :")
# class Result:
#     def cal(ao):
#         match(ao.__dict__["op"]):
#             case "+":
#                 print(f"sum {ao.__dict__['a']} {ao.__dict__['b']} = {ao.__dict__["a"] + ao.__dict__['b']}")
#             case "-":
#                 print(f"sub {ao.__dict__.get('a')} {ao.__dict__.get('b')} = {ao.__dict__.get('a') - ao.__dict__.get('b')}")       

#             case "*":
#                 print(f"mul {ao.__dict__.get("a")} {ao.__dict__.get("b")} = {ao.__dict__.get("a") * ao.__dict__.get("b")}")

#             case "/":
#                 print(f" div{ao.__dict__['a']} {ao.__dict__['b']} = {ao.__dict__['a'] / ao.__dict__[b]}")
#             case "//":
#                 print(f"floordiv {ao.__dict__['a']} {ao.__dict__['b']} = {ao.__dict__['a'] //ao.__dict__['b']}")  
#             case "%":
#                 print(f"modulo {ao.__dict__['a']} {ao.__dict__['b']} = {ao.__dict__['a'] % ao.__dict__['b']}")  
#             case "**":
#                 print(f"power  {ao.__dict__['a']} {ao.__dict__['b']} = {ao.__dict__['a'] ** ao.__dict__['b']}")  
#             case _:
#                 print(f"({ao.__dict__['op']}) ARE NOT IN ARITHMETIC OPERATOR PRESENT ")        



# ao = Calculator()

# try:
#     ao.getval()
#     Result.cal(ao)
    
# except ValueError:
#     print("Don't Enter str ALNUM STR AND SPECIAL SYMBOLS")    
# else:pass    

#^----------------------------------------------------------------------------------------------------
#!pickling
# from Employee import emp
        
# import pickle
# class emppick:
#     def saveempdata(self):
#         with open("oopsemp.pick","ab") as fp:
#             try:
                    
#                 eno=int(input("Enter  a employee number :"))
#                 ename=input("Enter a Employee Name :")
#                 sal=float(input("Enter a Employee Salary :"))
#                 eo = emp()     
#                 eo.getvals(sno,ename,sal)
#                 eo.displayvals()
#                 print("create an object of employee module that import from Employee ")
#                 pickle.dump(eo ,fp)
#                 print("Employee Record save the file Successfully ")
#             except ValueError:
#                 print("DON'T ENTER STR ALNUM AND STING ")
#             except NameError:
#                 print("check it Now from your side ")    



# eo=emppick()
# eo.saveempdata()

#^----------------------------------------------------------------------------------------------------
#!umpickling
# import pickle
# with open("oopsemp.pick","rb")as fp:
#     # try:
            
#         print("FIle is open successfully ")
#         filedata=pickle.load(fp)
#         print(filedata)
    


#^----------------------------------------------------------------------------------------------------
#!LinearSearch

# class Linears:
#     def getvals(self):
#         lst=[val for val in input().split()]
#         return lst

#     def search(self,lst):
#         lst.sort()
#         print(lst)
#         skey=int(input("ENter a number which you want to search :"))
#         sp=-1
#         for i in range(0,len(lst)):
#             if lst[i]==skey:
#                 sp=i
#                 break
#         if skey==-1:
#             print(f"{skey } is not present into the list :")           
#             # print("U")
#         else:
#             print(f"{skey} is in the list with index {sp}")    
#             print("search is successfull") 

    
# lo=Linears()
# lst=lo.getvals()
# # print(lst)
# if len(lst)==0:
#     print(f"list is Empty :{lst}")
# else:
#     lo.search(lst)    

































































#^----------------------------------------------------------------------------------------------------
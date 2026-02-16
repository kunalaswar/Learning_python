
#! #Non-ConstEx.py
# class student:
#     def  getstudvals(self):
#         self.sno=100   
#         self.name="RS"   

# s = student()    
# print("Content of s=",s.__dict__)
# s.getstudvals()
# print("Content of s=",s.__dict__)
# for k,v in s.__dict__.items():
#     print(f"{k} --- {v}")

#^----------------------------------------------------------------------------------------------------
#!#DefaultConsEx1.py
# class test:
#     def __init__(self):  #todo - default constructure
#         self.sno=10
#         self.name="RS"
#         print(self.sno)    
#         print(self.name)


# t=test()        
#^----------------------------------------------------------------------------------------------------
#!
# class test:
#     def __init__(self):
#         self.sno=10
#         self.name="RS"
#         print(f"\tval of sno =",self.sno)
#         print(f"\tval of name =",self.name)
# # I want create three object of three  test classes 
# # initialised the object with same vlaue

# t=test()
# t=test()
# t=test()
#^---------------------------------------------------------------------------------------------------
#!#ConstEx1.py
# class student:
#     def __init__(self):
#         self.sno=100
#         self.name="TS"    

#todo  Initlize all 1 objects with same values 1 and 2 and other Object with Different Values
# #main program        
# s1=student() #* Object creation --makes  the PVM to call constructor Automatically or implicitally
# print("COntent of students",s1.__dict__)
# s2=student()
# print("COnent of students",s2.__dict__)
# s3=student()
# print("COntent of students",s3.__dict__)


#^---------------------------------------------------------------------------------------------------

#TODO - PARAMETERIZED CONSTRUCTOR 

# #!#ConstEx2.py
# class student:
#     def __init__(self,sno,name):
#         print("I am from Deafult constructor")
#         self.sno=sno
#         self.name=name

#^ getting Different value to all 
# #main program        
# s1=student(100,"rss") #todo -Object Creation ---makes the PVM to call automitacally or implicitily
# print("content os s1 = ",s1.__dict__)
# s2=student(200,"ts") #todo -Object Creation ---makes the PVM to call automitacally or implicitily
# print("Content value",s2.__dict__)
# s3=student(300,"SS")  #todo -Object Creation ---makes the PVM to call automitacally or implicitily
# print("COntent value ",s3.__dict__)
#^---------------------------------------------------------------------------------------------------
#! 
# class students:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#         print("VALUE OF A ",self.a)
#         print("VALUE OF B ",self.b)
# s1 = students()   #todo - Object Creation--Makes the PVM to call Default Constructor
# s2 = students()   #todo - Object Creation--Makes the PVM to call Default Constructor
# s3 = students()  #todo - Object Creation--Makes the PVM to call Default Constructor

#^---------------------------------------------------------------------------------------------------
#! DEFAULT CONSTRUCTOR 
# class students:
#     def __init__(self):  #* Default constructer
#         print("It is  aDefaul constructor ")
#         self.a = 10
#         self.b = 20
#         print(f"a={self.a} b={self.b}")

# s1=students()
# s2=students()
# s3=students()        

#^---------------------------------------------------------------------------------------------------
#! Parametetized constructor
#!    1)
# class students:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print("\t value of a ",self.a)
#         print("\t value of b ",self.b)
#         print("----------------------")
       

# s1=students(10,20)        
# s2=students(100,200)
# # #s3=students(100) #typeError is this



#! Parametetized constructor
#!    2)
# class student:
#     def __init__(self,a =1 ,b =2):
#         self.a =a
#         self.b =b
#         print(f" a = {self.a}  b = {self.b}")
# s1=student() # Deafult parameter        
# s1= student(10)
# s3=student(20)
# s4=student(10,30)
# s5=student(b=70,a=60)
# s6=student(b=1000)

#!
# #ParameterizedConstEx1.py
# class Test:
#     def __init__(self,k,v):
#         print("I am from Parameterized Constructor")
#         self.a=k
#         self.b=v
#         print("\tVal of a={}".format(self.a))
#         print("\tVal of b={}".format(self.b))
#         print("-------------------------------")

# #Main Program
# #I want Create three objects of test class and
# # Initlize all 3 objects with Different values
# t1=Test(10,20) # Object Creation--Makes the PVM to call Parameterized Constructor
# t2=Test(100,200) # Object Creation--Makes the PVM to call Parameterized Constructor
# t3=Test(1000,2000) # Object Creation--Makes the PVM to call Parameterized Constructor

#^---------------------------------------------------------------------------------------------------
#! ReverseWordsInLine.py
# class LineWithWords:
#     def __init__(self):
#         self.line=input("Enter a line of Text:")
#     def reversewords(self):
#         x = self.line.split()
#         # print(x)
#         lst=[]
#         for val  in x:
#             # print(val)
#             lst.append(val[::-1])
#         # print(lst)        
#         s=" ".join(lst)
#         print(s)



# line=LineWithWords()
# line.reversewords()

#^---------------------------------------------------------------------------------------------------
# ! program which will accept line of text both numerical and non-numerical value and display only unique value wuth out using set and set function 

# class fun1:
#     def getlist(self):
#         n=input("Enter a list of value seperated by comma : ")
#         self.lst=[val for val in n.split()]
#         # print(lst)
#     def uniqueval(self):
#         new_lst=[]
#         for val  in self.lst:
#             if val not in new_lst:
#                 new_lst.append(val) 
#         print(new_lst)    


# f1=fun1()
# f1.getlist()
# f1.uniqueval()

#^---------------------------------------------------------------------------------------------------
#! program which will accept list of value and display it's Factorial
# class fun1:
#     def Factorial(self):
#         n=int(input("Enter a number to get its factorial :"))
#         fact=1
#         for i in range(1,n+1):
#             # print(i)
#             fact=fact*i
#         print(fact)
# f=fun1()            
# f.Factorial()

#^---------------------------------------------------------------------------------------------------
#! program which will accept a line of text and display the length of each word

# class fun1:
#     def lengthword(self):
#         self.word =[val for val in input("Enter : ").split()]
#         # print(self.word)
#         lengths=0
#         for val in range(0,len(self.word)):
#             # print(self.word[val])
#             print(f"{self.word[val]}--->  {len(self.word[val])}")


# f=fun1()        
# f.lengthword()

#^---------------------------------------------------------------------------------------------------


























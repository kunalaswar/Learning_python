 #ALL NOTES PRACITAL

#A,B="2",3
#txt="@"
#print((A+txt)*B)
#a,b=2,3
#c=4
#print(a+b*c)
#a,b=10,5.0
#c=a*b
#print(c)
#a,b=-5,2
#c=a%b 
#print(c)
#a,b=5,2
#c=a%b
#print(c)
#a,b=5,-2
#c=a%b
#print(c)
#making input fron  & printing it 
#name =input ("name:")
#age=int(input("age:" ))
#print(name)
#print("my name is a",name,"and my age is: " ,    age )
#age=int(input("enter a age"))
#if (age >=18):
 #   print("eligible for vote!!")
#else:
 #   print("Not eligible for vote")   
# colour=(input("Enter a colour  :"))  
# if colour==("red"):
#     print("STOP")
# elif colour=="green":
#     print("GO")
# else:
#     print("LOOK")        
# food =input("food: ")
# eat ="yes" if food =="cake" else "no"
# print(eat)
# a=int(input("a: "))
# b=int(input("b: "))
# c=a+b
# # print(c)
# a=int("2")
# b=4.25
# print(type(a))
# # print(a+b)
# a=3.14
# b=str(a)
# print(type(a))
# side=float(input("enter square side : "))
# print("area = ",side*side)
# a=int(input("enter a value for a :"))
# b=int(input("enter avalue for b :"))
# if a>=b:
#     print("a is a big value")
# else:
#     print("b is a big value")    
# a=int(input("enter first :"))
# b=int(input("enter second :"))
# print(a>=b)
# str1="This is a sting. we are creating it is python"
# print(len(str1))
# ch=str1[0]
# print(ch)
# print(str1[3])
# str1="harshal"
# str2="kunal"
# final_str=(str1+str2)
# print(final_str)
# # print(len(final_str))
# str="This is a string"
#  print(str.startswith("This"))
# str=input("enter a first name: ")
# print(len(str))
# number=int(input("Enter a number: "))
# if number%7==0:
#      print("multiple of 7")
# else:
#      print("it is not multiple of 7")
    
# a=int(input("enter a first"))
# b=int(input("enter a second"))
# c=int(input("enter a third"))
# if(a>=b and a>=c):
#     print("A is biggest",a)
# elif(b>=a and b>=c):
#     print("B is biggest",b)
# elif(c>=a and c>=b):
#     print("C is biggest",c)    
# marks=[94.4, 87.5, 95.2, 66.4, 45.1]
# print(marks)
# print(type (marks))
# print(len(marks))
# print(marks[6])
# tup=(2,1,3,4)
# s=sum(tup)
# print(s)
# print(tup[1])
# tup[0]=5
# print(tup)
# movies=[]
# a=input("Enter a three first movie name: ")
# b=input("Enter a three second movie name: ")
# c=input("Enter a three third movie name: ")
# movies.append(a)
# movies.append(b)
# movies.append(c)
# print(movies)

# PALIDROME PROGARM
# list1=[1,2,3]
# copy_list1=list1.copy()
# copy_list1.reverse()

# if(copy_list1==list1):
#     print("palidrome")
# else:
#     print("not palidrome")    
# list1=[1,3,2,5,4,6]
# list1.sort()
# print(list1)
#DICTONARY CONCEPT
# info={
#     "name":"kunal",
#     "subjects":"python",
#     "age":19,
#     "marks":90.6
#      }
# info["name"]="harshal"
# info["subject"]="java"
#  print(info)
# null_dict={}
# null_dict["name"]="aniket"
# print(null_dict)
# NESTED DICTIONARY
# students={
#     "name":"kunal aswar",
#     "subject":{
#         "phy":97,
#         "chem":98,
#         "math":95
#     }
# }
# print(students.keys())
# print(students)
# SETS CONCEPT
# set1={1,2,3,"kunal","aniket"}
# print(type(set1))
# print(set1)
# set1.add(5)
# print(set1)
# set1.remove(5)
# print(set1)
# set1.clear()
# print(set1)
# set1.pop()
# # print(set1.pop())
# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2))
# # print(set1.intersection(set2))
# subjects={"python","java","c++","python","javascript",
#      "java","python","java","c++","c"}
# # print(len(subjects))
#*** marks={}
# x=int(input("enter a phy: "))
# marks.update({"phy":x})

# x=int(input("enter a chem: "))
# marks.update({"chem":x})

# x=int(input("enter a math: "))
# marks.update({"math":x})
# print(marks)
# #LOOPS CONCEPT:-
# i = 1
# while i<=5:
#     print(i)
#     i+=1
# i=100 
# while i>=1:
#     print(i)    
#     i=i-1
# n=int (input("enter a number: "))
# i=1
# while i<=10:
#     print(n*i)
#      i=i+1
# nums=[1,4,9,16,25,36,49,64,81,100]
# x=36
# i=0
# while i<len(nums) :
#      if(nums[i]==x):
#         print("FOUND",i)

#      i+=1
# list1=[1,4,9,16,25,36,49,64,81,100]
# x=16
# for i in list1:
#     if (list1[i]==x):
#         print("found",i)
# seq= range(11)
# for i in range(10):
#     print(i)
# for i in range(2,100,2):
#     print(i)
# BY USING A RANGE FUNCTION
# n=int(input("Enter a number: "))  
# for i in range(1,11):
#     print(n*i)
# for i in range(5):
#     if i>=5:
#         print(i)
# print ( "sum important works")
# n=int(input("Enter anumber: "))
# n=6
# sum=0
# for i in range(1,n+1):
#     sum +=i
# print("total sum",sum)
# n=9
# fact=1
# for i in range(1,n+1):
#     fact *= 1
# print("factorial= ",fact)    
# FUCTION CONCEPT:
# def sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# sum(2,10)
# sum(2,5)
# def cal_fact(n):
#     fact=1
#     for i in range (1,n+1):
#         fact*=i
#     print(fact)
# cal_fact(8)   
# def converter(usd_val):
#     inr_val=usd_val *83
#     print(usd_val," USD= ",inr_val,"INR")     

# converter(100)
# def sum(kunal):
#     num=int(input("Enter a number: "))
#     if num%2==0:
#          print("even")
#     else:
#          print("Odd")    
# sum(5)   
#RECURSION  CONCEPT:
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(9)   
#program 
# n=int(input("Enter a number:  "))
#  if age>=18:
#      print("vote")     
#  else:
#      print("Not vote")   
#program 
# if n>0:
#     print("positive")
# elif n<0:
#     print("negative")    
# else:
#     print("zero ")  
#program  
# year=int(input("Enter a year:  "))
# if year%4:
#     print("Leap year")
# else:
#     print("not a leap year") 
# i=1
# while i<=5:
#     print(i)
#     i+=1
# WRONG PROGRAM 
# i=1
# sum=0
# while i<=100:
#     sum=sum+i
#     print(sum) 
#     i=i+2
# num1=5
# num2=10
# print(num1+num2)
# def maximum(a,b):
#     if a >= b:
#         print("a is big")
#     else:
#         print("b is big")



# for num in range(1,21):
#     if num % 2==0:
#         if num==10:
#             continue
#         print(num)
# num1=int(input("Enter a numner: "))
# num2=int(input("Enter a numner: "))
# num3=int(input("Enter a numner: "))
# half_num1=num1*0.5
# half_num2=num2*0.5
# half_num3=num3*0.5

# print(num1,"is",half_num1)
# print(num2,"is",half_num2)
# print(num3,"is",half_num3)

# num1=int(input("Enter a  first number"))
# num2=int(input("enter a second number"))
# sum=num1+num2
# sub=num1-num2
# mul=num1*num2
# div=num1%num2
# print(sum)
# print(sub)
# print(mul)
# print(div)
# score=80
# passed = score >= 75 
# print(passed)
# tuple=("kunal","aniket","harshal",[1,2,3,"kunal"])
# print(tuple[3][1])
#important 
# l1=["kunu",17,55.75,"shyam"]
# print(l1)
# for i in range(len(l1)):
#     print(l1[i])


# a=int(input("enter a number"))
# b=int(input("enter a number"))
# if a<b:
#     while a<=b:
#         print(a,end="  ")
#         a=a+1
# else:
#     while b>=a:
#         print(b,end="  ")
#         a-=1        
    #class concept 
# class students:
#     name="amar"

# s1=students()
# print(s1.name)
    #concustor concept

# class students:

#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname

# s1=students("karan","s")
# print(s1.fname,s1.lname)

# s2=students("raj","i")
# print(s2.fname,s2.lname)


# class information:
#     name="roshan"
#     age=20
#     name="aman"
#     age=30
    
# obj1=information()
# obj2=information()
# print(obj1.name,obj1.age)
# print(obj2.name ,obj2.age)
#class program:
# class sample:
#     x=0
#     y=0 
#     def get(self):
#         self.x=int(input("Enter a number"))
#         self.y=int(input("Enter a   number"))

#         def show(self):
#             print(f"data are{self.x}{self.y}")
# obj=sample()
# obj.get()
# obj.show()
# class students:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def get_avg(self):
#             sum=0
#             for val in self.marks:
#                 sum=sum+val
#             print("hi",self.name,"total avg score  ",sum/3)
# s1=students("kunal harshal",[99,98,97])
# s1.get_avg()
            
# a=int(input("Enter a current number"))
# b=int(input("Enter a previous number"))
# # print(a+b)
# def maximun( a,b,c):
#     if (a>=b)and(a>=c):
#         largest = a
#     elif(b>=a)and(b>=c):
#         largest = b
#     else:
#         largest = c 
#     return largest
# a=int(input("Enter a number : "))
# b=int(input("Enter a number : "))            
# c=int(input("Enter a number : "))

# print(maximun (a,b,c))

# def myfunc(n):
#     for i in range(0,n):
#         for j in range(0,i+1):
#             print("*",end="")
#     print("\r")
# n=5
# myfunc(n)

class employees:
    salary=89
    def get_salary(self):
        return self.get_salary
E1=employees()
print(E1.salary)    
#! write a program to find max of two integer number
# a=int(input("Entre a number :"))
# b=int(input("Entre a number :"))
# c=a if a>b else b
# print(f"the max value is {c}")
#?===================================================================================================
#! write a program to find the number is even or odd
# a=int(input('entre a number :'))
# print(f"{a} is even" if a%2==0 else print(f"{a} is odd"))

#?===================================================================================================
# print( print("True") if False else print("False"))
# print( 10 if False else print("False"))

#?===================================================================================================
# sub1=int(input("Entre a first sub marks")) #* and operator is used
# sub2=int(input("Entre a second sub marks"))
# if sub1>=50 and sub2>=50:
#     print("Pass")
# else:
#     print("Do more study")    

#?===================================================================================================
# sub1=int(input("Entre a first sub marks")) #* or operator is used
# sub2=int(input("Entre a second sub marks"))
# if sub1>=50 or sub2>=50:
#     print("Pass")
# else:
#     print("Do more study")    
#?===================================================================================================
#! Login Application /program
# uname=input("USERNAME : ")
# pwd=input("PASSWORD : ")
# print("WELCOME") if uname=="kunal" and pwd=="k123" else print("Invalid username or password try-again ")
#?===================================================================================================
#!program to find max of three number
# a=int(input("Entre a number"))
# b=int(input("Entre a number"))
# c=int(input("Entre a number"))
# print(a if a>b and a>c else b if b>a and b>c else c if c>a and c>b else "Equal" )

#?===================================================================================================
# for i in range(1,5):
#     print("*")
#     for j in range(i):
#         print("*",end="")

# for i in range(1,6):
#     print(i*"*")
# print("Code", "Chef")
# print(5,5)
# print("Python","Programming")
#?===================================================================================================
#!wite a program to input name ,sub1,sub2 and find grade based average 
#*write in conditional operator in one line 
# name=input("Enter a your name :")
# sub1=int(input("Enter a sub1 marks :"))
# sub2=int(input("Enter a sub2 marks :"))
# avg=sub1+sub2/2
# print(avg)
# if avg>90:
#     print("A")
# elif avg>80<=90:
#     print("B+")    
# elif avg>70<=80:
#     print("B")     
# elif avg>60<=70    :
#     print("C")
# else:
#     print("PASS")    
#*

#!write a python program to calculate  commission  based sales
#sales>6000--->10%
#sales>=4000<6000--->5%
# sales>4000--->0
# sales=int(input("Entre a sales :"))
# comm = sales*10/100 if sales>=60000 else sales*5/100 if sales>40000 and sales<60000 
# print(sales)
# print(comm)

#?===================================================================================================
# print(0 and 200)
# print(0 or 200)
# print(100 and 200 and 300)
# print(True or False)
# print(False or True)
# print(True or True)
# print(False or False)

#?===================================================================================================
#! write a program  to find the input character  is vowel or not 
# vowel =input("Entre a vowel : ").lower()
# if vowel in "aeiou":
#     print("it is vowel ")
# else:
#     print("it is not vowel ")  

# ch =input("Enter a character :").lower()
# print("Vowel") if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" else print( "Not vowel")

#?===================================================================================================
# ch=input("Enter a line of text :")
# for i in ch:
#     print(i)

# ch=input("Enter a line of text :")
# if ch in "aeiou":
#     print("Vowel")
# else:
#     print("NOt vowel")    




#?===================================================================================================
# a=5
# a=a+5
# print(a)

#!add two varible without using +operator 
# a=5
# b=4
# print(a+b)

# num=input("Enter a number :")
# s=0
# for  i in num:
#     res=int(i)%10
#     s=int(s)+int(i)
#     num=int(num)//10
# print(s)    
#?===================================================================================================
#!add two varible without using +operator 
# a=int(input("Enter a first  number :"))
# b=int(input("Enter a second number"))
# c=(a & b)<<1
# # w=a^b
# print(c)     #print(c,w)



#?===================================================================================================
#!swap a two number without using third varible



#?===================================================================================================
#! Reversed by using reversed() this is applicable both of the Data Types list,tuple
# tpl=(1,2,3,4,5,6)
# t1=reversed(tpl)
# print(t1)
# for val in t1:
#     print(val)
#?===================================================================================================
#! identity operator
# a=10
# b=10
# c=10
# print(a,id(a),b,id(b),c,id(c))
# print(a is b is  c)

# x=1.5
# y=1.5
# print(x,id(x),y,id(y))
# print(x is y)
#! walrus operator 
# a=10
# b=20
# c=(d:=a+b)*(e:=a-b)
# print(c ,d ,e)
# #! we can used this as a part of Expression 
# c=(d:=5+2)-(e:=5-2)
# print(c ,d , e)


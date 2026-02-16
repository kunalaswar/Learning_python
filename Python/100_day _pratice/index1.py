# #  find the square root
# import math as m
# print(m.sqrt(90))

# # Calculate the Area of a Triangle
# base = int(input("Enter a number : "))
# height = int(input("Enter a number : "))
# area = 0.5 * base * height
# print(area)

#Swap Two Variables
# a = 12
# b = 13
# temp = a
# print(temp)
# a = b
# print(a)
# b =temp
# print(b)
# print("We are swap the to number :", a ,b)


# Generate a Random Number
# import random as r
# k = r.randint(1000,10000)
# print(k)

# Convert Kilometers to Miles

# km = float(input("Enter a number in kilometers  : "))
# miles =  km * (0.621371)
# print( f" {km} kilometers of the mile is : {miles}")

# Convert Celsius To Fahrenheit
# celsius = float (input("Enter a temperture value: "))
# fahrenheit = (c*(9/5)) + 32 
# print(f"{celsius} the faharanite of this number is {fahrenheit}")


# Check if a Number is Positive, Negative or 0
# num = int(input("Enter a number : "))
# if (num>0):
#     print("positive number :",num)
# elif(num<0):
#     print("Negative number : ",num )
# else:
#     print("Zero : ",num) 
# 

# Check if a Number is Odd or Even   =>
# num = int(input("Enter a number :" ))
# if(num%2==0):
#     print("Even number is ",num)    
# else:
#     print("odd number is ",num)  

#Check Leap Year

# year = int(input("Enter a year : "))
# if year % 4==0:
#     print(" the quesent of this is ",year/4)
#     print(f"thi is  leap year {year}")
# else:
#     print(" the quesent of this is ",year/4)
#     print(f"this is not leap year {year}")

#Find the Largest Among Three Numbers 
# a = int(input("Enter a number :"))
# b = int(input("Enter a number :"))
# c = int(input("Enter a number :"))
# if(a>b)and(a>c):
#     print("the greatest number is",a)
# elif(b>a)and(b>c):
#    print("the greatest number is",b) 
# else:
#      print("the greatest number is",c)     


# num = int(input("Enter a number : "))
# for i in range(1,11):
#     print(f" {num} X {i} = {num * i} ")

  
#Check Prime Number
# num =int(input("Enter a number : "))
# if num==1:
#     print("it is not prime number ")
# if num>1:
#      for i in range(2,num):
#          if num % i ==0:
#              print("it is A not prime number")
#              break
#      else:
#          print("it is A prime number ")
    
# num = int(input("Enter a number "))
# for i in range(1, num +1 ):
#     print(i)

# num = int(input("enter a number : "))
# i=1
# while(i<=num):
#     print("value of i",i)
#     i=i+1

# n =int(input("Enter a number "))
# i=1
# while(i<=10):
#     print(f"{n}is muntiply {i} => {i*n}")
#     i=i+1

# n =int(input("Enter a number:"))
# for i in range(1,11):
#     print(i*n)



# n = int(input("Enter a number :"))
# if(n<0):
#     print("negative number")
# elif(n>0):
#     if(n<10):
#         print("it is single Digit number")
#     elif(n<100):
#         print(" it is two digit number")
#     else:
#         print("it is three digit number")
# else:
#     print("it is Zero")                    

# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter a number :  "))
# if(num1>num2):
#     print(f"the greatest number is {num1}")
# elif(num1<num2):
#     print(f"thee greatest number is {num2}")   
# else:
#     print("both nunber is same")   





#  print the Fibonacci sequence
# num=10
# num1=0
# num2=1
# temp=0
# for i in range(0,num):
#    temp =num1+num2
#    num1=num2
#    num2=temp
#    print(temp)


# Print the Fibonacci sequence
# a=0
# b=1
# num=int(input("Enter a number to obtain a fibonacci to obtain : "))
# if num==0:
#     print(a)
# else:
#     print( "value of a ",a)
#     print("value of b",b)
#     for i in range(1,num):
#         c=a+b
#         a=b    



# a = int(input("Enter a number : "))
# b = int(input("Enter a number : "))
# c = int(input("Enter a number : "))
# d = a + b + c
# if(d==180):
#     print("it is form an triangle")
# elif(d==360):
#     print("it form an circle")
# else:
#     print("it is not any type or None")        

# num = int(input("Enter a number : "))
# for i in range(1,num):
#     if(num%2==0):
#         print(f"Even number")
#         break
#     else:
#         print(f"odd number")   
#         break
 
 
#  Find the Factorial of a Number using for loop
# num = int(input("Enter a number : "))
# fact= 1
# if(num<0):
#     print("factorial of the number is not ")
# if(num==0):
#     print(f"factorial of the {num} is is 1  ")    
# if(num>0):
#    for i in range(1, num+1):
#         fact= (fact*i)
# print( "the factorial of the given number is ",fact)


#  Find the Factorial of a Number using Recursion  
# function calling itself

# def fact(a):
#     if a==0:
#         return 1
#     else :
#         return ((a)*fact(a-1))

# num=int(input("Enter a number : "))
# result = fact(num)
# print("factorial of the given number is :",result) 




        
#  Check Armstrong Number
# num= int(input("Enter a number :"))
# total = 0
# i = num
# while(i>0):
#     r = i%10#3 ,5 ,
#     print("r is",r)
#     total = total + (r*r*r)
#     print(total)
#     i = i//10#15
# print("total",total)
# if total == num:
#     print("it is Armstrong num ")
# else:
#     print("it is not Armstrong num")

#   Check Armstrong Number
# num=int(input("Enter a number : "))
# temp=num
# total =0
# while(temp>0):
#     digit = temp%10 # 3
#     total=total*(digit**3)
#     sum = sum + total
#     temp//10


# the Question in for loop 
# num=int(input("Enter a number :"))
# total=0
# for i in range(num,0,-1):
#     r=i%10
#     print(r)
#     total=total+(r*r*r)
#     i=i//10
#     print(total)

#  Find Numbers Divisible by Another Number
# 1) By using for loop
# for i in range(1,100):
#     if i % 13==0:
#         print(i)

# Convert Decimal to Binary, Octal and Hexadecimal
# a =10
# b=bin(a)
# print(b,type(b))

# a=0o17
# b=hex(a)
# print(b,type(b))




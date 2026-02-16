# import random
# print(help(random))
# print

# print(0b1010)
# print(0x1)
# print(0xac)
# print(0xaccer) #error
# print(0xacce)

# None=10
# print(None)


# a= 2+3j
# print(a)
# print(a.real)
# print(a.imag)

# word=input("Entera  number :")
# for i in range(len(word)):
#     print(i)

# s="python"
# for i in range(1,10):
#    print(i)
#    print(s)

# word=input("Enter a word :")
# for i in range(len(word)):
#     print(word[i])


# list=["kunal","python","paa"]
# for i in list:
#     print(i)


#1 2 3 4 5 6 7 8 9 10
# n= int(input("Entera number"))
# i=1
# while(i<=n):
#     print(i)
#     i=i+1


#9 8 7 6 5 4 3 2 1
# n=int(input("Enter a  number :"))
# i=n
# while(i>=0):  
#     print(i)
#     i=i-1

#Even number 2,4,6,8,10
# n= int(input("Enter a  number :"))
# i=0
# while(i<=n):
#     print(i)
#     i=i+2

#odd number 1,3,5,7,9
# n=int(input("Enter a  number :"))
# i=1
# while(i<=n):
#     print(i)
#     i=i+2

# word="python"
# print(len(word))

# word=input("Entera word :")
# i=0
# while(i<=len(word)-1):
#     print(word[i])
#     i=i+1

# s="python"
# print(s[0])
# print(s[10])



#multiplication table using for loop
# n= int(input("Enter a number:"))
# for i in range(1,11):
#     print(n*i)

#multiplication table using while loop
# s=0
# ss=0
# n=int(input("Enter a  number :"))
# i=1
# while(i<=10):
#     print(i*n)
#     i=i+1
#     s=s+i
#     ss= ss+i*n
# print("sum",s)  
# print("multiplicationsum = ",ss)  

# for i in ("python"):
#     print(i)






#program is for loop
# for val in range(0,10,1):
# s=0
# for val in range(1,10,1):
#     print(val) 
#     s=s+val
# print("sum = ",s)  

#program is while loop
# i=0
# while(i<=0):
#     print()




# a=range(10,51,10)
# print(a[3])


# n=int(input("Entera  number :"))
# i=n
# while(i>=1):
#     print(i)
#     i=i+1

#program for finding sum of natural nnumber i=using for loop
# n=int(input("Entera  number :"))
# sum=0
# for i in range(1,n+1,1):
#     print(i)
#     sum=sum+i
# print( "sum => ",sum)    


#program for finding sum of natural nnumber using while loop
# n=int(input("Entera  number :"))
# sum=0
# i=1
# while(i<=n):
#     print(i)
#     sum=sum+i
#     i=i+1
# print("sum = ",sum)

#program for finding sum of n natural number and their square sum also using for loop
# n= int(input("Enter a nunber :"))
# s=0
# squares=0
# for i in range(1,n+1):
#     print(f"{i},  {i*i}")
#     s=s+i
#     squares=squares+i*i
# print("sum = ",s)    
# print("squares = ",squares)    


#program for finding sum of n natural number and their square sum also using while loop
# n= int(input("Enter a  number :"))
# s=0
# squares=0
# i=1
# while(i<=n):
#     print(f"{i},{i*i}")
#     i=i+1
#     s=s+i
#     squares=squares+i*i
# print(f"{s} , {squares}" )   


# Chat history


# Today

# Yesterday
# Previous 7 Days
# You said:
# GIVE me qutions on match case in python
# ChatGPT said:
# ChatGPT
# Here are some questions on the match statement introduced in Python 3.10, which is used for structural pattern matching:

# Basic Questions
# What is the primary purpose of the match statement in Python?

# How does the syntax of the match statement differ from traditional conditional statements like if and elif?

# Can you explain the use of the case keyword in a match statement?
# What types of patterns can be used in the case clauses? Provide examples.
# How do you handle the default case in a match statement?
# Intermediate Questions
# What are “wildcard” patterns in a match statement? How do you use them?
# Explain how to destructure a list or tuple in a case statement. Provide an example.
# How can you match against a dictionary's keys and values using the match statement?
# What are guard conditions in a match statement, and how do they work?
# Can you nest match statements? Provide an example.
# Advanced Questions
# What are some limitations of the match statement compared to traditional if-elif chains?
# How does the match statement handle types in pattern matching?
# Provide an example of using the match statement to perform type checking on a variable.
# Discuss the performance implications of using match versus traditional conditional statements.
# Can you implement a simple state machine using the match statement?
# Practical Questions
# Write a match statement that categorizes an input number as positive, negative, or zero.
# Using the match statement, implement a simple parser for a basic mathematical expression (e.g., 1 + 2, 3 * 4).
# Demonstrate how to use the match statement to handle different error types in exception handling.
# Create a match statement that processes various data types (e.g., integers, strings, lists) and returns a corresponding response.
# Explain how to implement a command pattern using the match statement in a command-line application.
# Feel free to ask for explanations or examples for any of these questions!





# Sent by Copilot:

# Absolutely! Here are some programming questions to challenge your understanding of while loops in Python:

# Basic Loop: Write a while loop that prints the numbers from 1 to 20.

# i=1
# while(i<=20):
#     print(i ,end=" ")
#     i=i+1

#for loop 
# for i in range(1,21):
#     print(i)
# for i in range(21):
#     print(i)

# for i in range(20,1,-1):
#     print(i)




# Sum Calculation: Use a while loop to calculate the sum of all even numbers between 1 and 100.

# n=int(input("Entera  number :"))
# sum=0
# i=0
# while(i<=n):
#     print(i)
#     i=i+2
#     sum=sum+i
# else:
#     print("sum = ",sum)

# Sum Calculation: Use a while loop to calculate the sum of all even numbers between 1 and 100.
#using for loop
# n= int(input("Enter a number :"))
# sum=0
# for i in range(1,n+1):
#     print(i)
#     sum=sum+i
# print("SUM =>",sum)


# Factorial Calculation: Write a while loop to compute the factorial of a given number.
# n=int(input("Enter a number :"))
# fact=1
# i=1
# while(i<=n):
#     print(i)
#     fact=fact*i
#     i=i+1
# print("factorial calculation =>",fact)    


#  Factorial Calculation: Write a for  loop to compute the factorial of a given number.
# n=int(input("Enter a number :"))
# fact=1
# for i in range(1,n+1):
#     print(i)
#     fact=fact*i
# print(f"fact => ",fact)    



# List Manipulation: Given a list of numbers, use a while loop to remove all elements from the list one by one.
# list=[1,2,3,4,5,6]
# i=1
# while(i<=len(list)):
#     print((list[i]).clear())
#     i=i+1

# Pattern Printing: Use nested while loops to print a pyramid pattern of stars.

# Guessing Game: Implement a simple guessing game where the user has to guess a number between 1 and 50. The loop should continue until the user guesses the correct number. while loop
# number=15
# while(True):
#     user_num=int(input("Enter a  number :"))
#     if(user_num==number):
#         break
# print(f"{number}is guess properly {user_num}")


# Guessing Game: Implement a simple guessing game where the user has to guess a number between 1 and 50. The loop should continue until the user guesses the correct number. for loop
# number=15
# for i in range(1,100):
#     user_num=int(input("Enter a number :"))
#     if(user_num==number):
#         break
# print(f"{user_num} is guess prooperly {number}")    



# Prime Number Check: Use a while loop to check if a given number is prime.



# Fibonacci Sequence: Generate the first 10 numbers of the Fibonacci sequence using a while loop.



# Try these out and let me know if you need any hints or further explanations!

# i=1
# while()


# Here are some Python programming questions related to loops:




# Beginner Level:
# Print Numbers from 1 to 10:
# Write a Python program using a for loop to print numbers from 1 to 10.


# Sum of First N Natural Numbers:
# Write a Python program that takes an input n from the user and uses a while loop to calculate the sum of the first n natural numbers.


# Print Even Numbers Between 1 and 20:
# Write a Python program to print all even numbers between 1 and 20 using a for loop.

# Print Multiplication Table:
# Write a Python program that asks the user for a number and prints its multiplication table using a loop.

# Factorial Calculation:
# Write a Python program to calculate the factorial of a number using a for loop.

# Intermediate Level:
# Sum of Digits in a Number:
# Write a Python program that asks the user for a number and uses a while loop to calculate the sum of its digits.

# Reverse a String:
# Write a Python program to reverse a string using a loop.

# Count the Occurrence of a Character in a String:
# Write a Python program that takes a string and a character from the user and counts how many times the character occurs in the string using a loop.

# Print Fibonacci Sequence:
# Write a Python program to print the Fibonacci sequence up to n terms, where n is entered by the user.

# Prime Number Check:
# Write a Python program to check if a given number is prime using a loop.




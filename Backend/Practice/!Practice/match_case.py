# #MatchCaseEx1.py
# print("="*50)
# print("\tArithmetic Operations")
# print("="*50)
# print("\t1. Addtion")
# print("\t2. Substration")
# print("\t3. Multiplication")
# print("\t4. Division")
# print("\t5. Modulo Division")
# print("\t6. Exponentiation")
# print("\t7. Exit")
# print("="*50)

# ch=int(input("Enter  your choice :"))
# match (ch): # int(ch)
#     case 1:
#         print("enter a two number for addition :")
#         a,b= float(input()),float(input())
#         # a= float(input("Enter a first number :"))
#         # b= float(input("Enter a second number :"))
#         print(f"sum({a},{b})={a+b}")
#     case 2:
#         print("Enter atwo number for Substraction :")    
#         a,b= float(input()),float(input())
#         print(f"sub({a},{b})={a-b}")
#     case 3:
#         print("Enter atwo number for multiplication :")    
#         a,b= float(input()),float(input())
#         print(f"mul({a},{b})={a*b}")
#     case 4:
#         print("Enter atwo number for Division :")    
#         a,b= float(input()),float(input())
#         print(f"Div({a},{b})={a/b}")
#         print(f" floor Div({a},{b})={a//b}")
#     case 5:
#          print("Enter atwo number for modulo Division:")    
#          a,b= float(input()),float(input())
#          print(f" Modulo division({a},{b})={a%b}")
     
#     case 6:
#          print("Enter atwo number for  Exponentiation :")    
#          a,b= float(input()),float(input())
#          print(f" Exponentiation({a},{b})={a**b}")
#     case 7:
#         print("THX for using program") 
#     case _:
#         print("User selection operation is wrong-- try again")
# print("program Execution completed")         



# #MatchCaseEx2.py
# print("="*50)
# print("\t")
# print("="*50)
# print("\t1.f to c ")
# print("\t2. f to k ")
# print("\t3. c to f")
# print("\t5.  c to k")
# print("\t6.  k to f")
# print("\t7. k to cExit")
# print("="*50)

# ch=int(input("Enter  your choice :"))
# match (ch): # int(ch)
#     case 1:
#         f=float(input("Enter a number: "))
#         c=



# #MatchCaseEx4.py
# import sys
# s="""=================================================
# 				Area of Different Figures
# =================================================
# 				R. Rectangle
# 				T. Triangle
# 				S. Square
# 				C. Circle
# 				E. Exit
# ================================================="""
# print(s)
# ch=input("Enter Ur Choice:")
# match(ch):
#     case "R"|'r':
#         L,B=float(input("Enter Length:")),float(input("Enter Breadth:"))
#         ar=L*B
#         print("Area of Rect={}".format(ar))
#     case "T"|'t':
#         B, H = float(input("Enter Base:")), float(input("Enter Height:"))
#         at=(1/2)*B*H
#         print("Area of Triangle:{}".format(at))
#         print("--------------OR--------------------------")
#         a,b,c=float(input("Enter Side1:")),float(input("Enter Side2:")),float(input("Enter Side3:"))
#         s=(a+b+c)/2
#         ats=(s*(s-a)*(s-b)*(s-c))**0.5
#         print("Area of Triangle:{}".format(ats))
#     case "S"|'s':
#         s1 = float(input("Enter Side:"))
#         sa = s1*s1
#         print("Area of Square={}".format(sa))
#     case "C"|'c':
#         r = float(input("Enter Radius:"))
#         ca = 3.14*r**2
#         print("Area of Square={}".format(ca))
#     case "E"|'e':
#         print("thx for using Program")
#         sys.exit()
#     case _:
#         print("Ur Selection of Operation is Wrong--try again")



# 1. Simple Calculator with match-case
# Write a Python program that acts as a simple calculator. The user will input two numbers and choose an operation (addition, subtraction, multiplication, division) from a menu. Use the match-case statement to select the correct operation based on the user's choice.

# Requirements:

# If the user enters 1, perform addition.
# If the user enters 2, perform subtraction.
# If the user enters 3, perform multiplication.
# If the user enters 4, perform division.
# If the user enters anything else, display an error message.
# a=float(input("Enter value for a:"))
# b=float(input("Enter value for b:"))
# user=float(input("Enter  your choice :"))
# match(user):
#     case 1:
#         print(f"Addition {a+b}")
#     case 2 :
#         print(f"substraction {a-b}") 
#     case 3:
#         print(f"Multiplication {a*b}")       
#     case 4:
#         print(f"Division {a/b}")       
#     case _:
#         print(f"invalid input please try again !")       

# 2. Day of the Week
# Write a Python program that asks the user to enter a number between 1 and 7 and prints the corresponding day of the week. Use a match-case statement to print the day.
# 1 → "Monday"
# 2 → "Tuesday"
# 3 → "Wednesday"
# ........
# 7 → "Sunday"
# If the user enters a number outside of this range, print "Invalid input."

# user=int(input("enter a value for  related week  day:"))
# match(user):
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("Tues")
#     case 5:
#         print("fri")
#     case 6:
#         print("sat")
#     case 7:
#         print("Sun")

#  3.Grade System
# Write a program that asks the user to input a student's grade as a percentage and then assigns a letter grade based on the percentage using match-case.

# Grading System:

# 90–100 → "A"
# 80–89 → "B"
# 70–79 → "C"
# 60–69 → "D"
# Below 60 → "F"
# Handle invalid inputs if the percentage is outside the range of 0 to 100.


# user=int(input("enter a percentage:"))
# match(user):
#     case user if user>=90 & user<=100:
#         print("A")
#     case user if user>=80 & user<=89:
#         print("B")
#     case user if user>=70 & user<=79:
#         print("C")
#     case _:
#         print("")


# 4. Shipping Cost Calculator
# Create a program where the user enters the shipping region code and the program returns the shipping cost based on the region. Use a match-case statement to implement this.

# Shipping Costs:

# Code 1 → "Domestic Shipping: $5"
# Code 2 → "International Shipping: $15"
# Code 3 → "Express Shipping: $25"
# Code 4 → "Overnight Shipping: $50"
# If the user enters a code that isn't in the list, print "Invalid shipping code."



# my_dict = {"key1": "value1", "key2": "value2"}

# match my_dict:
#     case {"key1": "value1", "key2": "value2"}:
#         print("Dictionary contains expected key-value pairs.")
#     case _:
#         print("Dictionary is not as expected.")


# Question:
#  Write a Python program using match-case to determine if a given number is positive, negative, or zero.
# num=int(input("Enter a numnber :"))
# a =num>0
# b=num<0
# c=num==0
# match (num):
#     case a if num>0:
#         print("positive number")
#     case b if num<0:
#         print("Negative  number")
#     case c if num==0:
        # print("zero number ")
# match (num):
#     case 1 if num>0:
#         print("positive number")
#     case 2 if num<0:
#         print("Negative  number")
#     case 3 if num==0:
#         print("zero number ")
# Example:
# a=(7,3,10)
# match a:
#     case (1,5,8):
#         print(1,5,8)
#     case (2,6,9):
#         print(2,6,9)
#     case (7,3,10):
#         print(7,3,10)
#     case _:
#         print("invalid")
# Output
# 7,3,10
# bytes (immutable)
# b = b'hello'
# # b[0] = 100  # This will raise a TypeError

# # bytearray (mutable)
# ba = bytearray(b'hello')
# ba[0] = 100 + 100 # This will work fine
# # print(ba)  # Output: bytearray(b'dello')
# print(ba[0])
# for val in ba:
#     print(val)









#  Intermediate Level:
# # Question:
# Create a Python function that uses match-case to identify the type of a given object (e.g., integer,
# string, list, dictionary).
# Hard Level:
# # Question:
# Develop a Python program that employs match-case to analyze a text file and count the occurrences of different word lengths.







# intermediate Level (Revised):
# Question:

# Write a Python function that uses match-case to determine the type of a given geometric shape (e.g., square, rectangle, circle, triangle) based on its properties (e.g., sides, angles).

# Hard Level (Revised):
# Question:

# Create a Python program that utilizes match-case to parse a JSON file representing a complex data structure (e.g., a nested dictionary) and extract specific information based on predefined patterns.


# Simple Level: Write a Python program using match-case to determine if a given year is a leap year.
# Intermediate Level: Create a Python function that uses match-case to identify the type of a given geometric shape (e.g., square, rectangle, circle, triangle) based on its properties (e.g., sides, angles).
# Hard Level: Develop a Python program that employs match-case to analyze a text file and identify the most frequently used words and their corresponding frequencies.
# If you have an issue with the provided questions:

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
# Feel free to ask for explanations or examples for any of these question

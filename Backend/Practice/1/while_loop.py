# lst=["Ankit","aniket","sagar"]
# for val in lst:
#     if val.startswith("a") or val.startswith("A"):
#         print(val)
#?======================================================================================================
#! 1 2 3 4 5 
# i=1
# while i<=5:
#     print(i)
#     i=i+1

#!  5 4 3 2 1 
# i=5
# while i>=1:
#     print(i,end=" ")
#     i=i-1  #i-=1

#! 1 4 9  16 25  Thiois is a square  to understand it by  your self
# i=1
# while i<=5:
#     print(i*i)  #*print(i**2) this is a power concept in it
#     i=i+1     #*i+=1

#! 25 16 9 4 1 
# i=5
# while i>=1:
#     print(i**2)
#     i=i-1

#!A B C D E  
#* very important this to know the ascii value 

# i=65
# while i<=69:
#     print(chr(i))
#     i=i+1
#?======================================================================================================

#! write a program to print sum of 10 number
# i=1
# sum=0
# while i<=10:
#     print(i)
#     sum=sum+i
#     i=i+1
# else:
#     print("-"*30)
#     print(f"sum of {sum }")

#!write a program add a 10 value to give the value at a runtime 
# i=1
# sum=0
# while i<=10:
#     num=int(input(f"Enter a {i} number :"))
#     # print(i)
#     sum=sum + num
#     i+=1   
# print(f"sum of input number : {sum}")    

#! write a program to print a table from user input
# num=int(input("Enter a number which you want to table :"))
# i=1
# while i<11:
#     print(f"{num} X {i} = {num*i}")
#     i+=1

# num=int(input("Enter a number which you want :"))
# start=int(input("Enter a number where from you start :"))
# end=int(input("Enter a ending number whrer upto you want table :"))
# while(start<=end):
#     print(f"{start} X {num} = {start*num}")
#     start=start+1

#! write a program to find length of number 
#* with the converting with str but the Question is other 
# s=input("Enter a any value :")
# count=0
# i=0
# while(i<len(s)):
#     print(s[i],end=" ")
#     count=count+1
#     i=i+1
# print()    
# print(f"length = {count}")    

#! write a program to find length of number 
# num=int(input("Enter a number to find its length :"))
# count=1
# i=1
# while i<num:
#     res=num%10
#     count=count+1
#     num=num//10
# print(count)

#*logic-1
# num=int(input("Enter a number :"))
# i=num
# count=0
# while(i>0):
#     count=count+1
#     i=i//10
# print(f"Length of number : {count}")    
#?======================================================================================================
#! write a program to find even digit from an input number
# num=int(input("Enter a number :"))
# print("EVEN number are :")
# # i=num
# while(num>0):
#     r=num%10
#     if(r%2==0):
#         print(r)
#     num=num//10    
   
#! write a program to find odd digit from an input number
# num=int(input("Enter a number :"))
# counteven=0
# countodd=0
# # print("ODD number are :")
# # print("even digit ")
# while(num>0):
#     res=num%10
#     if(res%2!=0):
#         countodd=countodd+1  
#         # print(res)
#     else:
#         counteven=counteven+1 
#         # print(res)   

#     num=num//10 
# print(f"count of odd digit : {countodd}")
# print(f"count of even digit :{counteven}")
#?======================================================================================================
#& THIS ARE THE QUESTION THAT AREE WITHOUT  USING THE PREDEFINED FUNCTION 
#^  IMP PART with out using bin() function 
#! write a program input decimal number and convert into binary string
# num=int(input("Enter a  number :"))
# str1=""
# while num!=0:# and num!=1:
#     reminder=num%2
#     str1=str1+str(num)
#     num=num//10
# str1=str1+str(num)    
# print(str1)    

#?======================================================================================================
#!write a program to convert  decimal  to  octal
# num=int(input("Enter a number :"))
# str1= ""
# while




#?======================================================================================================
#!write a program to convert  decimal  to  Hexadecimal








#?======================================================================================================
#!write a program to reversed a number 
# num=int(input("Enter a  number :"))
# while(num>0):
#     res=num%10
#     print(res,end="")
#     num=num//10

#!write a program to reversed a number 
# num=int(input("Enter a number :"))
# rev=0
# while num>0:
#     r=num%10
#     rev=(rev*10)+r
#     num=num//10
# print(rev)    

#?======================================================================================================
#!write a program to find input number is armstrong or Not 
#* 153
#*length=3
#* 1 pow 3 + 5 pow 3 + 3 pow 3 =sum=153
#*
# num=int(input("Enter a number between 100 to 999 its work only three digit not a 4 or 5 digit  :"))
# #^ if you want to input any digit number then you find the length of the number
# num1=num
# sum=0
# while(num>0):
#     res=num%10
#     sum=sum+(res**3)
#     num=num//10
# if num1==sum:
#     print("Amstrong number")
# else:    
#     print("Not Amstrong number")

#?=====================================================================================================
#! write a program to find input number is prime or not
# num=int(input("Enter a number :"))
# count=0
# i=1
# while(i<=num):
#     r=num%i
#     if r==0:
#         count=count+1
#     i=i+1
# # print(count)
# if count==2:
#     print(f"{num} is prime number ")
# else:
#     print(f"{num} Not prime number ")



#?=====================================================================================================
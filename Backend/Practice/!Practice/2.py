
# ! Write a program to find avg of two input numbers
# a=int(input("Enter a  first number :"))
# b=int(input("Enter a  second number :"))
# avg=(a+b)/2
# print(avg)

# ! write a program to remove last digit of number
# num=int(input("Enter any integer number "))
# # num=abs(num)//10
# # print(num)

# # num = int(input("Enter any integer number: "))

# #! Remove the last digit while maintaining the sign
# if num < 0:
#     num = -(-num // 10)  # Use negative sign for the result if input is negative
# else:
#     num = num // 10

# print("Number after removing the last digit:", num)

# print(10>5<20)
# print(10>5>20)

# ! Write a program to find a person is elg to vote or not
# name=input("Entera a name :")
# age=int(input("Enter a AGE HERE :"))

# if(age>=18):
#     print(f"{name} is Eligible for vote")
# else:
#     print(f"{name} is NOT Eligible for vote")

# !Write a program to check whether a number entered is
# !three digit number or not
# num=int(input("Enter a number :"))
# if(num>100)and(num<1000):
#     print("ti si three")
# else:
#     print("it is two")    

# user=input("Enter a username :")
# pwd=input("Enter a password :")
# if(user=="kunal"):
#     print("Welcome !!")
#     if(pwd=="@12345"):
#         print("correct Password. ")    
#     else:
#         print("invalid Password.")
# else:
#     print("invalid username")        

# ! Write a program to find max of 3 numbers without using and,or operators
# a=int(input("Enter a first number :"))
# b=int(input("Enter a second number :"))
# c=int(input("Enter a third number :"))
# if(a==b==c):
#     print("EQUAL")    
# elif(a>b)and(a>=c):
#     print(a)    
# elif(b>a) and(b>=c):
#     print(b)    
# elif(c>=a) and(c>=b):    
#     print(c)


# !write a program to find length of string (count of characters)
# s=input("Enter a word :")
# count=0
# for _ in s:
#     count=count+1
# print(count)    

# #! Write a program to count alphabets,digits and special
# #! characters in a given string
# s=input("Enter a number :")


# n=int(input("Entera number:"))
# i=n
# while(i>=1):
#     print(i)
#     i=i-1

# word=input("Entera a word:")
# i=0
# while(i<len(word)):
#     print(word[i])
#     i=i+1

# word=input("Enter a word :")
# i=len(word)-1
# while(i>=0):
#     print(word[i])
#     i=i-1

# !Even number with in N
# n=int(input("Enter a number :"))
# i=0
# while(i<=n):
#     print(i)
#     i=i+2
# n=int(input("Entera number :"))
# i=n
# while(i>=0):
#     print(i)
#     i=i-2
# !reverse in N
# n=int(input("Enter a number :"))
# i=1
# while(i<=n):
#     print(i)
#     i=i+2
# n=int(input("Entera number :"))
# i=n
# while(i>=1):
#     print(i)
#     i=i-2

# n=int(input("Entera number :"))
# i=n
# while(i>=1):
#     print(i)
#     i=i-2

# n=int(input("Entera number :"))
# i=1
# while(i<=n):
#     if(i%2==0):
#         print(i)
#     i=i+1

# n=int(input("Entera number :"))
# i=1
# while(i<=n):
#     if(i%2!=0):
#         print(i)
#     i=i+


# n=int(input("Enter a number :"))
# i=n
# while(i>=1):
#     if(i%2==0):
#         print(i)
#     i=i-1    

# n=int(input("Enter a number :"))
# for i in range(10,0,-1):
#     print(i*n)

# word=input("Enter a Word : ")
# for i in range(len(word)):
#     print(word[i])


# word=input("Enter a word:")
# for i in range(0,len(word)):
#     print(word[i])

# word=input("Entera  word:")
# for i in range(-len(word),0):
#     print(word[i])

# !backword Direction

# word=input("Entera word:")
# for i in word:
#     print(i)

# word=input("Entera word:")
# for i in word[::-1]:
#     print(i)

# word=input("Enter a  word :")
# for i in range(len(word)-1,-1,-1 ):
#     print(word[i])

# word=input("Enter a  word :")
# for i in range(-1,-len(word)+1,-1):
#     print(word[i])

# num=int(input("Enter a number:"))
# sum=0
# temp = num
# while(num>0):
#     res=num%10
#     sum=sum+res
#     num//=10
# print(sum)

# n=input("Enter a number :")
# s=0
# for i in n:
#     s=s+int(i)
# print(s)

# n=input("Enter a number:")
# x=n.split()
# # print(x,type(x))
# for i in x[0]:
#     print(int(i))

# n=input("Entera number :")
# lst=list[n]
# # print(lst)
# for i in n:
#     print(int(i))

# s="python"
# print(s,type(s))

# s="python"
# i=0
# while(i<=len(s)-1):
#     print(s[i])
#     i=i+1

# n=int(input("Enter a number :"))
# i=1
# sum=0
# sq_s=0
# while(i<=n):
#     print(i , i*i)
#     sum=sum+i
#     sq_s=sq_s+i*i
#     i=i+1
# print("------------")    
# print(sum,sq_s)    

# n=int(input("Enter a number :"))
# i=1
# sum=0
# sq_s=0
# for i in range(1,n+1):
#     print(i , i*i)
#     sum=sum+i
#     sq_s=sq_s=i*i
# print("-------------------")    
# print(sum , sq_s)    

# ! factorial of given number
# n=int(input("Enter a number :"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)    

# !  program for obtaining Factors of a given number
# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i)

# ! write a program to sum of digit of given number
# num=int(input("Enter a number :")) 
# # i=num
# sum=0
# while(num>0):
#     res=num%10
#     sum=sum+res
#     num=num//10
# print(sum)    


# ! given number given sum of digit or number
# *LOGIC -1
# num = int(input("Enter a number: "))
# sum = 0  # Initialize sum to 0

# while num > 0:
#     res = num % 10  # Get the last digit
#     sum = sum + res  # Add the last digit to sum
#     num = num // 10  # Remove the last digit from num

# print("Sum of the digits:", sum)

# *LOGIC-1
# num=int(input("Enter a number :"))
# sum=0
# while(num>0):
#     res=num%10
#     sum=sum+res
#     num=num//10
# print(sum)  
  
# * LOGIC-3
# n=input("Enter a number :")
# if(int(n)<=0):
#     print("it is the Invalid number :")
# else:
#     sum=0
#     # print(f"Given number :{int(n)}")    
#     digit=n.split()
#     # print("Digits ",digit[0])
#     for digit in digit[0]:
#        sum=sum+int(digit)
#     else:   
#         print(sum)        
#         # print(digit[0])

# s="345678"
# lst=list([s])
# print(lst)

# *logic-4
# num=int(input("Enter a number :"))
# if(num<=0):
#     print("Invalid input --please Enter a valid input")
# else:
#     s=0
#     digit=list[]


# s="23456"
# l=list(s)
# print(l)



# ! write a python program which will a ceespt a line of text and append the palindeome word if any present in the line of text
# word=input("Enter a line / string :")
# if(word==word[::-1]):
#     print("it is palindrome ")
# else:
#     print(" it is not palindeome ")    


# s="kunal"
# list=list([s])
# print(s)

# !write a program to print "pyth" with using slicing and indexing 
# n = "python"    #input("Enter a word :")
# for i in n:
#     print(n[i])

        

#? =========================================================================================================
#!  PROGRAM FOR FINDING SUM OF NATURAL NUMBERS 
# n = int(input("ENTER A NUMBER : "))
# sum = 0
# for i in range(n+1):
#      sum = sum + i 
#      print(f"numbers = {i}  sum = {sum}")
# else:
#      print(f"sum of {n} natural numbers  is {sum}")
     
#!  PROGRAM FOR FINDING SUM OF NATURAL NUMBERS 

# sum=0
# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     print(i)
#     sum=sum+i
# print("-----------")    
# print(sum)    


#? =========================================================================================================
#! PRINTING SUM AND SUM SQUARES OF NATURAL NUMBERS
# 1 s sum is      1    
# 2 and 1 sum is  3     
# 3 and 3 sum is  6     
# 4 and 6 sum is  10    
# 5 and 10 sum is 15     
# ---------------------
#sum of n is natural n is 15  

# 1 s square is 1s
# 2 s square is 4 
# 3 s square is 9 
# 4 s square is 16 
# 5 s square is 25 
# -----------------------
# sum of squares  =  55

#*LOGIC_1
#*LOGIC_1
# n = int(input("ENTER A NUMBER UPTO WHICH YOU WANT SUM AND SUM OF THEIRE SQUARES : "))
# sum = 0
# sum_squres= 0
# for i in range (n+1):
#      sum = sum + i 
#      sum_squres= sum_squres+i*i
#      print(i)
# else:
#      print(f"sum of {n} natural number is {sum} and sum of squres of  natural number is {sum_squres}")

#*LOGIC_2
# n = int(input("ENTER A NUMBER UPTO WHICH YOU WANT SUM AND SUM OF THEIRE SQUARES : "))
# sum = 0
# sum_squres= 0
# for i in range (n+1):
#      sum = sum + i 
#      sum_squres= sum_squres+i**2
#      print(i)
# else:
#      print(f"sum of {n} natural number is {sum} and sum of squres of  natural number is {sum_squres}")

#! PRINTING SUM AND SUM SQUARES OF NATURAL NUMBERS

# n=int(input("Enter a number :"))
# sum=0
# sqr_sum=0
# for i in range(1,n+1):
#     print(i, i*i)
#     sum=sum+i
#     sqr_sum=sqr_sum+i*i
# print("---------------")    
# print(sum ,  sqr_sum)    



# n=input("Enter a number :")
# s=str(n)
# sum=0
# sqr_sum=0
# for i in :
     

#? =========================================================================================================
#!  PROGRAM FOR FINDING PRODUCT OF NATURAL 

# n = int(input("ENTER A NUMBER UPTO WHERE YOU WANT PRODUT : "))
# sum_product = 1
# for i in range(1,n+1):
#      sum_product*= i
#      print(i)
# else:
#      print(f"product of {n} natural number is {sum_product}")

#!  PROGRAM FOR FINDING PRODUCT OF NATURAL 
# n=int(input("Enter a number :"))
# p=1
# for i in range(1,n+1):
#     print(i)
#     p=p*i
# print(p)    


#? =========================================================================================================
#!  PROGRAM FOR FINDING SQAURE OF PRODUCT OF NATURAL 
# n= int(input("ENTER A NUMBER : "))
# sum_product = 1
# product_square  = 1
# for i in range(1,n+1):
#      sum_product = sum_product*i
#      product_square = product_square*i**2
#      print(i)
# else:
#      print(f"product of {n} natural number is {sum_product} and square of product is {product_square} ")

#!  PROGRAM FOR FINDING SQAURE OF PRODUCT OF NATURAL 
# n=int(input("Enter a number :"))
# squ_p=1
# for i in range(1,n+1):
#     print(i)
#     squ_p=squ_p*i*i
# print(squ_p)    


#? =========================================================================================================
#!  PROGRAM FOR FINDING SUM OF PRODUCT OF NATURAL NUMBERS UPTO N

#*LOGIC_1:
# n = int(input("enter a number : "))
# sum = 0
# sum_cubes= 0
# for i in range(n+1):
#      sum = sum+i
#      sum_cubes = sum_cubes+i*i*i
#      print(i)
# else:
#      print(f"sum of {n} natural number is {sum} sum of cube of natural number is {sum_cubes} ")
     
          
#*LOGIC_2:
# n = int(input("enter a number : "))
# sum = 0
# sum_cubes= 0
# for i in range(n+1):
#      sum = sum+i
#      sum_cubes = sum_cubes+i**3
#      print(i)
# else:
#      print(f"sum of {n} natural number is {sum} sum of cube of natural number is {sum_cubes} ")     

#!  PROGRAM FOR FINDING SUM OF PRODUCT OF NATURAL NUMBERS UPTO N

# n=int(input("Enter a number :"))
# sum=1
# for i in range(1,n+1):
#     print(i)
#     sum=sum*i*i*i
# print("-----------")    
# print(sum)


#? =========================================================================================================
# #!  PROGRAM FOR FINDING SUM & SUM OF SQUARE & SUM OF SQUARE CUBE OF NATURAL UMBERS UPTO N
# n = int(input("ENTER A NUMBER "))
# sum=0
# sum_square= 0
# sum_cube = 0
# for i in range(1,n+1):
#      sum = sum + i
#      sum_square = sum_square + i**2
#      sum_cube = sum_cube + i**3
#      print(f"{i},sum={sum}, sum of squares = {sum_square}, sum of cubes = {sum_cube}")
# else:
#      print(f"sum of {n} is {sum} and sum of squares {sum_square} and sum of cube is {sum_cube}")

# #!  PROGRAM FOR FINDING SUM & SUM OF SQUARE & SUM OF SQUARE CUBE OF NATURAL UMBERS UPTO N

# n=int(input("Enter a number :"))
# sum=0
# sqr_sum=0
# cub_sum=0
# for i in range(1,n+1):
#     print(i , i*i , i*i*i)
#     sum=sum+i
#     sqr_sum=sqr_sum+i*i
#     cub_sum=cub_sum + i*i*i
#     i +=1
# print("-------------")    
# print( sum, sqr_sum , cub_sum)    


#? =========================================================================================================\
#! PROGRAM FOR PRINTING SUM OF GIVEN DIGIT 
# #*LOGIC_0
# num = int(input("ENTER A DIGIT WHOSE SUM YOU WANT : "))
# if (num<=0):
#      print("You have entered invalid input ! please enter valid input ")
# else:    
#  sum = 0 
#  temp_num = num
# for digit in str(num):
#       r = num%10 +
#       sum = sum + r
#       num = int(num)//10
# else:
#  print(f"sum of {temp_num} is {sum}")

#*LOGIC_1
# n = input("enter a value ")
# d= n.split()
# print(d,type(d))     
# print(d[0],type(d[0]))
# s = 0
# for i in d[0]:
#     s = s+int(i)
# else:
#      print(f"sum of {n} is {s} ")

#*LOGIC_2     
# n = input("enter a number : "),
# list  = list(n)
# # print(list,type(list))
# sum =  0
# for i in list:
#     sum = sum+int(i)
# else:
#      print(f"sum of {n} is {sum } ")

# *LOGIC_3
# n = int(input("enter a number "))
# sum = 0
# for i in n:
#      sum = sum+int(i)
# else:
#      print(f"sum of {n} is {sum } ")
     
     
#! PROGRAM FOR PRINTING SUM OF GIVEN DIGIT 
#* logic-0 Using while loop
# n=int(input("Enter a value :"))
# temp=n
# if(n<0):
#     print("It is invalid input")
# else:
#     sum=0
#     res=0
#     while(n>0):
#         res=n%10
#         sum=sum + res
#         n //=10  #n=n//10
# print(f"the given digit is that {temp} is  {sum}")             

#*using for loop logic-0
# num=int(input("Enter a number :"))
# temp=num
# if(num<=0):
#     print("It is invalid input")
# else:
#     sum=0
#     for digit in str(num):
#         res=num%10
#         sum=sum+res
#         num=num//10
# print(f"the of given number  {temp}  is  {sum}")  

# # *Logic-1
# n=input("Enter a number :")
# # print(n,type(n))
# d=n.split()
# # print(d,type(d))
# print(d[0],type(d[0]))
# s=0
# for i in d[0]:
#     print(i,end=" ")
#     s=s+int(i)
# print()
# print(s)
# LOGIC------------
# n=input("Enter a number :")   #123
# num=n
# s=0
# for i in n:
#     print(i)
#     s=s+int(i)
# print("------")
# print(s)


#LOGIC-----
# n=input("Enter a number :")    
# d=n.split()
# s=0
# print(d,d[0],type(d))
# for i in d[0]:
#     print(i)
#     s=s+int(i)
# print("------")
# print(s)    


#LOGIC
# n=input("Enter a number :")
# list=list(n)
# # print(list)
# s=""
# s1=str(s)
# for i in list:
#     print(i)
#     s1=s1+i
# print("-------")    
# print(s1)


#LOGIC
# n=input("Enter a number :")
# list=list(n)
# # print(list)
# s=""
# s1=str(s)
# for i in list:
#     print(i)
#     s1=s1+i
# print("-------")    
# print(s1)


#LOGIC
# n=input("Enter a number :")
# list=list(n)
# # print(list)
# s=""
# s1=str(s)
# for i in list:
#     print(i)
#     s1=s1+i
# print("-------")    
# print(s1)

# n=int(input("Enter a number :"))
# s=0
# for i in str(n):
#     print(i)
#     s=s+int(i)
# print("------")    
# print(s)



#? =========================================================================================================\
#!PROGRAM FOR PRINTING ""PYTH"" WITHOUT USING SLICING AND INDEXING

# s = "python"
# for ch in s:
#      if (ch=="o"):
#           break
#      print(ch)
# else:
#      print("it is else block")
#!PROGRAM FOR PRINTING ""PYTH"" WITHOUT USING SLICING AND INDEXING
# n=input("Enter a value :")
# for ch in n:
#     if(ch=="p"):
#         break
#     print(ch)
# else:
#     print("It is else block")

# s="python"
# for ch in s:
#     if(ch=="o"):
#         break
#     print(ch)

# else:
#     print("it is else block")
#? =========================================================================================================\
#! PROGRAM FOR FINDING FACTORIAL OF GIVEN NUMBER
# 5 = 1*2*3*4*5
# 5 = 5*4*3*2*1

#*LOGIC_1:
# n = int(input("enter a number : "))
# fact = 1
# for i in range(1,n+1):
#      fact= fact*i
#      # print(i,fact)
# else:
#      print(f"factorial of {n} is {fact} ")

#*LOGIC_2:
# n  = int(input("enter a number : "))
# fact = 1
# for i in range(n,0,-1):
#      fact = fact*i
#      # print(i,fact)
# else:
#      print(f"factorial of {n} is {fact}")

#! PROGRAM FOR FINDING FACTORIAL OF GIVEN NUMBER

# n=int(input("Enter a number :"))
# fact=1
# for i in range(1,n+1):
#     print(i) 
#     fact=fact*i
# print("------")    
# print(fact)

# for i in range(1,6):
#     print(i)
# for i in range(-1,-6,-1):
#     print(i)

#? =========================================================================================================
#! PROGRAM FOR PRINTING EVEN NUMBER IN GIVEN VALUE 
#*LOGIC_1:
# n = input("enter a number ")
# for i in n:
#      if int(i)%2==0:
#           print(i)

#*LOGIC_2:
# n = input("enter a number ")
# x = n.split()
# for i in x[0]:
#      if int(i)%2==0:
#           print(i)

#*LOGIC_3:
# n = input("enter a number ")
# list = list(n)
# for i in list:
#      if int(i)%2==0:
#           print(i)
          
# !PROGRAM FOR PRINTING EVEN NUMBER IN GIVEN VALUE 
# n=int(input("Enter a number :"))
# for i in str(n):
#     if(int(i)%2==0):
#         print(i)

# n=input("Enter a number :")
# s=0
# list=list(n)
# print(list)
# # print(list,type(list))
# for i in list:
#     s=s+int(i)
# print(s)    

# n=input("Enter a number :")

# x=n.split()
# print(x,type(x))
# for i in list:
#     print(i)


# n=input("Enter a number :")
# s=0
# list=list(n)
# for i in n:
#     s=s+int(i)
# print(s)    


# n=int(input("Enter a number :"))        
# sum=0
# for i in str(n):
#     if(int(i)%2==0):
#         print(i)
#         sum=sum+int(i)
# print("------")        
# print(sum)        

# n=input("Enter a number :")
# s=0
# x=n.split()
# print(x,type(x))
# for i in x[0]:
#     if(int(i)%2==0):
#         print(i)
#     s=s+int(i)
# print(s)        


#? =========================================================================================================
#! PROGRAM FOR PRINTING ODD NUMBER IN GIVEN VALUE 
#*LOGIC_1:
# n = input("enter a number ")
# for i in n:
#      if int(i)%2!=0:
#           print(i)

#*LOGIC_2:
# n = input("enter a number ")
# x = n.split()
# for i in x[0]:
#      if int(i)%2!=0:
#           print(i)

#*LOGIC_3:
# n = input("enter a number ")
# list = list(n)
# for i in list:
#      if int(i)%2!=0:
#           print(i)

#! PROGRAM FOR PRINTING ODD NUMBER IN GIVEN VALUE 

#*LOGIC-0
# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     # print(i)
#     r=n%10
#     if(r%2!=0):
#         print(r ,end="  ")
#     n=n//10   


#*LOGIC-1
# n=input("Enter a number :")
# for i in n:
#     if int(i)%2!=0:
#         print(i)

#*LOGIC-2
# n=input("Enter a number :")
# x=n.split()
# # print(x)
# for i in x[0]:
#     if(int(i)%2!=0):
#         print(i)

# print(int(str(2))%2==0)

#*LOGIC-3
# n=input("Enter a number :")
# list1=list(n)
# for i in list1:
#     if(int(i)%2!=0):
#         print(i)
#!--------------------------------
# n=input("Enter a number")
# n1=list(n)
# print(n1)
#!--------------------------
# k=list("kunal")
# print(k)
#!------------------
# num=input("Enter a number: ")
# k=tuple(num)
# print(k)
#!------------------
# num=input("Enter a number: ")
# k=set(num)
# print(k)
# #!----------------
# num=input("Enter a number: ")
# k=frozenset(num)
# print(k)
#!---------------------------
# num=input("Enter a number: ") #?dict madhe hot nahi
# k=dict({num})
# print(k)









#! 08-10-2024----------sagar dada

#!  PROGRAM FOR FINDING SUM OF PRODUCT OF NATURAL NUMBERS UPTO N
# *LOGIC_1:
# n = int(input("enter a number : "))
# sum = 0
# sum_cubes= 0
# for i in range(n+1):
#      sum = sum+i
#      sum_cubes = sum_cubes+i*i*i
#      print(i)
# else:
#      print(f"sum of {n} natural number is {sum} sum of cube of natural number is {sum_cubes} ")


# *LOGIC_2:
# n = int(input("enter a number : "))
# sum = 0
# sum_cubes= 0
# for i in range(n+1):
#      sum = sum+i
#      sum_cubes = sum_cubes+i**3
#      print(i)
# else:
#      print(f"sum of {n} natural number is {sum} sum of cube of natural number is {sum_cubes} ")
# ? =========================================================================================================
# #!  PROGRAM FOR FINDING SUM & SUM OF SQUARE & SUM OF SQUARE CUBE OF NATURAL UMBERS UPTO N
# n = int(input("ENTER A NUMBER "))
# sum=0
# sum_square= 0
# sum_cube = 0
# for i in range(1,n+1):
#      sum = sum + i
#      sum_square = sum_square + i**2
#      sum_cube = sum_cube + i**3
#      print(f"{i},sum={sum}, sum of squares = {sum_square}, sum of cubes = {sum_cube}")
# else:
#      print(f"sum of {n} is {sum} and sum of squares {sum_square} and sum of cube is {sum_cube}")
# ? ========================================================================================================
#! PROGRAM FOR PRINTING SUM OF GIVEN DIGIT
# *LOGIC_0
# num = int(input("ENTER A DIGIT WHOSE SUM YOU WANT : "))
# if (num<=0):
#      print("You have entered invalid input ! please enter valid input ")
# else:
#  sum = 0
#  temp_num = num
# for digit in str(num):
#       r = num%10 +
#       sum = sum + r
#       num = int(num)//10
# else:
#  print(f"sum of {temp_num} is {sum}")

# *LOGIC_1
# n = input("enter a value ")
# d= n.split()
# # print(d,type(d))
# # print(d[0 ],type(d[0]))
# s = 0
# for i in d[0]:
#     s = s+int(i)
# else:
#      print(f"sum of {n} is {s} ")

# *LOGIC_2
# n = input("enter a number : ")
# list  = list(n)
# # print(list,type(list))
# sum =  0
# for i in list:
#     sum = sum+int(i)
# else:
#      print(f"sum of {n} is {sum } ")

# *LOGIC_3
# n = input("enter a number ")
# sum = 0
# for i in n:
#      sum = sum+int(i)
# else:
#      print(f"sum of {n} is {sum } ")


# ? =========================================================================================================\
#!PROGRAM FOR PRINTING ""PYTH"" WITHOUT USING SLICING AND INDEXING

# s = "python"
# for ch in s:
#      if (ch=="o"):
#           break
#      print(ch)
# else:
#      print("it is else block")
# ? =========================================================================================================\
#! PROGRAM FOR FINDING FACTORIAL OF GIVEN NUMBER
# 5 = 1*2*3*4*5
# 5 = 5*4*3*2*1

# *LOGIC_1:
# n = int(input("enter a number : "))
# fact = 1
# for i in range(1,n+1):
#      fact= fact*i
#      # print(i,fact)
# else:
#      print(f"factorial of {n} is {fact} ")

# *LOGIC_2:
# n  = int(input("enter a number : "))
# fact = 1
# for i in range(n,0,-1):
#      fact = fact*i
#      # print(i,fact)
# else:
#      print(f"factorial of {n} is {fact}")
# ? =========================================================================================================
#! PROGRAM FOR PRINTING EVEN NUMBER IN GIVEN VALUE
# *LOGIC_1:
# n = input("enter a number ")
# for i in n:
#      if int(i)%2==0:
#           print(i)

# *LOGIC_2:
# n = input("enter a number ")
# x = n.split()
# for i in x[0]:
#      if int(i)%2==0:
#           print(i)

# *LOGIC_3:
# n = input("enter a number ")
# list = list(n)
# for i in list:
#      if int(i)%2==0:
#           print(i)


# ? =========================================================================================================
#! PROGRAM FOR PRINTING ODD NUMBER IN GIVEN VALUE
# *LOGIC_1:
# n = input("enter a number ")
# for i in n:
#      if int(i)%2!=0:
#           print(i)

# *LOGIC_2:
# n = input("enter a number ")
# x = n.split()
# for i in x[0]:
#      if int(i)%2!=0:
#           print(i)

# *LOGIC_3:
# n = input("enter a number ")
# list = list(n)
# for i in list:
#     if int(i) % 2 != 0:
#         print(i)

# ? =========================================================================================================
#! 08-10-2024

# s = input(" ENTER A LINE : ")
# x = s.split()
# for i in x:
#     print(i)
#     for ch in i:
#         print(ch)

# list1 = list([])



#!Write a program TO FIND LENGTH OF NUMBER
# num=int(input("Enter a number:"))
# count=0
# while(num>0):
#     num=num//10
#     count=count+1
# print(count)    
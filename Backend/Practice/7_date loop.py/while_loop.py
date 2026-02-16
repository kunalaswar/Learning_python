
#! program for finding the sum of only EVEN number and PRODUCT of odd number
# n=int(input("enter a number :"))               
# evens=0
# oddp=1
# while(n>0):
#     res=n%10
#     if(res%2==0):
#         print(res)
#         evens=evens+res
#     elif(res%2!=0):
#         print(res)    
#         oddp=oddp*res
#     n=n//10    
# print(evens , oddp)        

#! SUBSTRACTION BY -2
# n = int(input("ENTER A NUMBER: "))
# i = n

# while i >= 0:
#     print( i)
#     i -= 2

#? =========================================================================================================
#!  PROGRAM FOR FINDING SUM OF NATURAL NUMBERS 
# n= int(input("ENTER A NUMBER : "))
# if (n<=0):
#      print("invalid input please enter valid input ! ")
# else: 
#      i = 0             #OR YOU CAN START FROM 0 ALSO
#      sum = 0
#      while(i<=n):
#           sum= sum+i
#           print(f"{i}")
#           i=i+1
          
#      else:
#           print(f"sum of {n} natural number {sum} ")
#!  PROGRAM FOR FINDING SUM OF NATURAL NUMBERS 

# n=int(input("Enter a number :"))
# sum=0
# for i in range(1,n+1):
#     print(i)
#     sum=sum+i
# print("------")    
# print(sum)

# n=int(input("Enter a number :"))
# sum=0
# i=1
# while(i<=n):
#     print(i)
#     sum=sum+i
#     i=i+1
# print("-------")    
# print(sum)    
#!reversed order
# n=int(input("Enter a number :"))
# sum=0
# for i in range(n,0,-1):
#     print(i)
#     sum=sum+i
# print("------")    
# print(sum)

# n=int(input("Enter a number :"))
# sum=0
# i=n
# while(i>=0):
#     print(i)
#     sum=sum+i
#     i=i-1
# print("------")    
# print(sum)

#!PROGRAM FOR FINDING SUM OF NATURAL NUMBERS in reversed order
# n=int(input("Entera  number "))
# sum=0
# i=n
# while(i>=1):
#     print(i)
#     sum=sum+i
#     i=i-1
# else:
#     print("sum in reversed order ",sum)

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

#*LOGIC_1:
# n= int(input("ENTER A NUMBER : "))
# if (n<=0):
#      print("invalid input please enter valid input ! ")
# else: 
#      i = 1             
#      sum = 0
#      sum_squares = 0
#      while(i<=n):
#           sum= sum+i
#           sum_squares=sum_squares+i*i
#           print(f"{i}")
#           i=i+1
          
#      else:
#           print(f"sum of {n} natural number {sum} and theire square is {sum_squares}")



# #*LOGIC_2:
# n= int(input("ENTER A NUMBER : "))
# if (n<=0):
#      print("invalid input please enter valid input ! ")
# else: 
#      i = 0             #OR YOU CAN START FROM 0 ALSO
#      sum = 0
#      sum_squares = 0
#      while(i<=n):
#           sum= sum+i
#           sum_squares=sum_squares+i**2
#           print(f"{i}, sum= {sum},sum_squares={sum_squares}")
#           i=i+1
          
#      else:
#           print(f"sum of {n} natural number {sum} and theire square is {sum_squares}")

#! PRINTING SUM AND SUM SQUARES OF NATURAL NUMBERS
# n=int(input("Entera  number "))
# sum=0
# squ_sum=1
# i=1
# while(i<=n):
#     print(i ,i*i)
#     sum=sum+i
#     squ_sum= squ_sum+i*i
#     i=i+1
# else:
#     print(sum,squ_sum)    

#?-----------------

# n=int(input("ENter a number:"))
# i=n
# sum=0
# sqr_sum=0
# while(i>=1):
#     sum=sum+i
#     sqr_sum=sqr_sum + i*i
#     print(i ,i*i)
#     i=i-1
# else:
#     print(sum,sqr_sum)    
#! PRINTING SUM AND SUM SQUARES OF NATURAL NUMBERS
# n=int(input("Enter a number :"))
# i=1
# sum=0
# sqr_s=0
# while(i<=n):
#     print(f"{i}  {i*i}")
#     sum=sum+i
#     sqr_s=sqr_s+i*i
#     i=i+1
# print("------------")    
# print(f"{sum}  {sqr_s}")        

# n=int(input("Entera number :"))
# i=n
# sum=0
# sqr_s=0
# while(i>=0):
#     print(f"{i}  {i*i}")
#     sum=sum+i
#     sqr_s=sqr_s+i
#     i=i-1
# print("----------")    
# print(f"{sum}  {sqr_s}")    

# n=int(input("Entera number :"))
# sum=0
# sqr_s=0
# for i in range(1,n+1):
#     print(i ,i*i)
#     sum=sum+i
#     sqr_s=sqr_s+i*i
# print("------")    
# print(sum , sqr_s )    

# n=int(input("Entera number :"))
# sum=0
# sqr_s=0
# for i in range(n,0,-1):
#     print(i , i*i)
#     sum=sum+i
#     sqr_s=  sqr_s+i*i
# print("------")    
# print(f"{sum} {sqr_s}")


#? =========================================================================================================
#!  PROGRAM FOR FINDING PRODUCT OF NATURAL 
# n= int(input("ENTER A NUMBER : "))
# if (n<=0):
#      print("it is invalid input  ")
# else:     
#   i = 1
#   sum_product = 1
#   while(i<=n):
#      sum_product = sum_product*i
#      print(i)
#      i+=1
#   else:
#      print(f"product of {n} natural number is {sum_product}")

#!  PROGRAM FOR FINDING PRODUCT OF NATURAL 
# n=int(input("Enter a number :"))
# p=1
# i=1
# while(i<=n):
#     p=p*i
#     print(i)
#     i=i+1
# else:
#     print("product",p)

#!  PROGRAM FOR FINDING PRODUCT OF NATURAL 
# n=int(input("Entera number :"))
# p=1
# for i in range(1,n+1):
#     print(i)
#     p=p*i
# print("------")    
# print(p)

#? =========================================================================================================
#!  PROGRAM FOR FINDING SQAURE OF PRODUCT OF NATURAL 
# n= int(input("ENTER A NUMBER : "))
# i = 1
# sum_product = 1
# product_square  = 1
# while(i<=n):
#      sum_product = sum_product*i
#      product_square = product_square*i**2
#      print(i)
#      i+=1
# else:
#      print(f"product of {n} natural number is {sum_product} and square of product is {product_square} ")

#!  PROGRAM FOR FINDING SQAURE OF PRODUCT OF NATURAL in reversed order
# n=int(input("Enter a number "))
# i=n
# squ_p=1
# while(i>=1):
#     squ_p = squ_p *i
#     print(i)
#     i=i-1
# else:
#     print(squ_p)    
#! PROGRAM FOR FINDING SQAURE OF PRODUCT OF NATURAL in reversed order
# n=int(input("Enter a number :"))
# squre_sum=1
# for i in range(n, 0,-1):
#     print(i)
#     squre_sum=squre_sum*i*i
# print("------")    
# print(squre_sum)    

# n=int(input("Enter a number :"))
# i=n 
# sum_product = 1
# product_square  = 1
# while(i>=1):
#     # print(i,i*i)
#     sum_product = sum_product*i
#     product_square  = product_square*i*i
#     # print(i)
#     i=i-1
# print(sum_product,product_square)   

#? =========================================================================================================
#!  PROGRAM FOR FINDING SUM OF CUBE OF NATURAL NUMBERS UPTO N

#*LOGIC_1:
# n = int(input("enter a number : "))
# i = 1
# sum = 0
# sum_cubes= 0
# while(i<=n):
#      sum = sum+i
#      sum_cubes = sum_cubes+i**3
#      print(i)
#      i = i+1
# else:
#      print(f"sum of {n} natural number is {sum} sum of cube of natural number is {sum_cubes} ")     

#*LOGIC_2:
# n = int(input("enter a number : "))
# i = 1
# sum = 0
# sum_cubes= 0
# while(i<=n):
#      sum = sum+i
#      sum_cubes = sum_cubes+i*i*i
#      print(i)
#      i = i+1
# else:
#      print(f"sum of {n} natural number is {sum} sum of cube of natural number is {sum_cubes} ")     


#!  PROGRAM FOR FINDING SUM OF CUBE OF NATURAL NUMBERS UPTO N
# n=int(input("Enter a number :"))
# cs=0
# i=1
# while(i<=n):
#     print(i*i*i)
#     cs=cs+i*i*i
#     i=i+1
# else:
#     print("-----------------")
#     print(cs)

#?================================
# n=int(input("Enter a number :"))
# i=n
# cs=1
# while(i>=1):
#     print(i*i*i)
#     cs=cs+i*i*i
#     i=i-1
# else:
#     print("------------")    
#     print(cs)

#? =========================================================================================================
#!  PROGRAM FOR FINDING SUM & SUM OF SQUARE & SUM OF SQUARE CUBE OF NATURAL UMBERS UPTO N
# n = int(input("ENTER A NUMBER "))
# i = 1
# sum=0
# sum_square= 0
# sum_cube = 0
# while(i<=n):
#      sum = sum + i
#      sum_square = sum_square + i**2
#      sum_cube = sum_cube + i**3
#      print(i)
#      i=i+1
# else:
#      print(f"sum of {n} is {sum} and sum of squares {sum_square} and sum of cube is {sum_cube}")

#!  PROGRAM FOR FINDING SUM & SUM OF SQUARE & SUM OF  CUBE OF NATURAL UMBERS UPTO N
# n=int(input("Enter a number :"))
# i=1
# sum=0
# squ_sum=0
# cub_sum=0
# while(i<=n):
#     print(i ,  i*i ,  i*i*i)
#     sum=sum + i
#     squ_sum=squ_sum+i*i
#     cub_sum=cub_sum+i*i*i
#     i=i+1
# else:
#     print("-------------------------")
#     print(f"{sum} {squ_sum} {cub_sum}")    


#? =========================================================================================================
#! PROGRAM FOR PRINTING SUM OF GIVEN DIGIT 
# num = int(input("ENTER A DIGIT WHOSE SUM YOU WANT : "))
# if (num<=0):
#      print("You have entered invalid input ! please enter valid input ")
# else:    
#     sum = 0 
#     temp_num = num
#     while(num>0):
#       r = num%10 
#       sum = sum + r
#       num = num//10
#     else:
#         print(f"sum of {temp_num} is {sum}")



#! PROGRAM FOR PRINTING SUM OF GIVEN DIGIT 
# num = int(input("ENTER A DIGIT WHOSE SUM YOU WANT : "))
# if (num<0):
#      print("You have entered invalid input ! please enter valid input ")
# else:
#     sum=0
#     while(num>0):
#         r=num%10
#         sum=sum+r
#         num=num//10
# print(sum)    

# num=int(input("Enter a number :"))
# if(num<=0):
#     print("it  is invalid input")
# else:
#     sum=0
#     while(num>0):
#         r=num%10
#         sum=sum+r
#         num=num//10
#     else:
#         print(sum)    




#? =========================================================================================================
#!PROGRAM FOR PRINTING ""PYTH"" WITHOUT USING SLICING AND INDEXING
# s = "python"
# i =0
# while(i<len(s)):
#      if s[i]=="o":
#           break   
#      print(s[i])
#      i = i+1
# else:
#      print("it is else block")

#!PROGRAM FOR PRINTING ""PYTH"" WITHOUT USING SLICING AND INDEXING

# s="python"
# i = 0
# while(i<len(s)):
#     # print(s[i]=="o")
#     if(s[i]=="o"):
#         break
#     print(s[i])
#     i=i+1
# else:
#     print("It is else block")    
#?----------------------------------------------
# s="python"        
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])


#? =========================================================================================================
#! PROGRAM FOR FINDING FACTORIAL OF GIVEN NUMBER
# 5 = 1*2*3*4*5
# 5 = 5*4*3*2*1

#*LOGIC_1:
# n = int(input("enter a number : "))
# fact = 1
# i = 1
# while(i<=n):
#      fact= fact*i
     ## print(i,fact)
#      i= i+1
# else:
#      print(f"factorial of {n} is {fact} ")

#*LOGIC_2:
# n  = int(input("enter a number : "))
# i = n
# fact = 1
# while(i>0):
#      fact = fact*i
#      # print(i,fact)
#      i = i-1
# else:
#      print(f"factorial of {n} is {fact}")

#! PROGRAM FOR FINDING FACTORIAL OF GIVEN NUMBER
# n=int(input("Enter a number :"))
# i=n
# fact=1
# while(i>=1):
#     fact=fact*i
#     i=i-1
# else:
#     print(fact)    


# n=int(input("Enter a number :"))
# i=1
# fact=1
# while(i<=n):
#     fact=fact*i
#     i=i+1
# else:
#     print(fact)    



#? =========================================================================================================
#! PROGRAM FOR PRINTING EVEN NUMBER IN GIVEN VALUE 
#* LOGIC_1
#? IN REVERSE ORDER CAUSE DIVDING RIGHT
# num = int(input("ENTER A NUMBER  : "))
# while(num>0):
#       d = num%10 
#       if d%2==0:
#        print(d)
#       num = num//10

# #* LOGIC_2
# num = int(input("ENTER A NUMBER  : "))
# list = []
# while(num>0):
#       d = num%10 
#       if d%2==0:
#        list.append(d)
#       num = num//10
# else:
#      list.reverse()
#      print(list)

#! PROGRAM FOR PRINTING EVEN NUMBER IN GIVEN VALUE 
#? program for printing the even number in given value
# n=int(input("Enter a number :"))
# # i=n
# while(n>0):
#     r=n%10
#     if(r%2==0):
#         print(r)
#     n=n//10

#* LOGIC-2
# n=int(input("Enter a number :"))
# list=[]
# while(n>0):
#     r=n%10
#     if r%2==0:
#         list.append(r)
#     n=n//10
# else:
#     list.reverse()
#     print(list)

        

# sum of given number

# n=int(input("Enter a number :"))
# i=n
# sum=0
# while(i>0):
#     r=i%10
#     sum=sum+r
#     i = i//10
# print(sum)    

#? =========================================================================================================
#! PROGRAM FOR PRINTING ODD NUMBER IN GIVEN VALUE 


#* LOGIC_1
#? IN REVERSE ORDER CAUSE DIVDING RIGHT
# num = int(input("ENTER A DIGIT : "))
# while(num>1):
#      r = num%10 
#      if r%2!=0:
#        print(r)
#      num = num//10

# #* LOGIC_2
#? Print the even digits in reverse order (original order in number)
# num = int(input("ENTER A NUMBER  : "))
# list = []
# while(num>1):
#       d = num%10 
#       if d%2!=0:
#        list.append(d)
#       num = num//10
# else:
#      list.reverse()
#      print(list)


#! PROGRAM FOR PRINTING ODD NUMBER IN GIVEN VALUE 
# n=int(input("Enter a number :"))
# i=n
# while(i>1):
#     r=i%10
#     if(r%2!=0):
#         print(r)
#     i=i//10


#*LOGIC-2
# n=int(input("Enter a number :"))
# list=[]
# while(n>0):
#     a=n%10
#     if a%2!=0:
#         list.append(a)
#     n=n//10
# else:
#     list.reverse()
#     print(list)

# n=int(input("Enter a number:"))
# i=n
# while(i>0):
#     r=i%10
#     if(r%2!=0):
#         print(r)
#     i=i//10

#! 08-10-2024----------sagar dada

# ? =========================================================================================================
#! PROGRAM FOR PRINTING EVEN NUMBER IN GIVEN VALUE
# * LOGIC_1
# ? IN REVERSE ORDER CAUSE DIVDING RIGHT
# num = int(input("ENTER A NUMBER  : "))
# while(num>0):
#       d = num%10
#       if d%2==0:
#        print(d)
#       num = num//10

# #* LOGIC_2
# num = int(input("ENTER A NUMBER  : "))
# list = []
# while(num>0):
#       d = num%10
#       if d%2==0:
#        list.append(d)
#       num = num//10
# else:
#      list.reverse()
#      print(list)


# ? =========================================================================================================
#! PROGRAM FOR PRINTING ODD NUMBER IN GIVEN VALUE


# * LOGIC_1
# ? IN REVERSE ORDER CAUSE DIVDING RIGHT
# num = int(input("ENTER A DIGIT : "))
# while(num>1):
#      r = num%10
#      if r%2!=0:
#        print(r)
#      num = num//10

# #* LOGIC_2
# ? Print the even digits in reverse order (original order in number)
# num = int(input("ENTER A NUMBER  : "))
# list = []
# while(num>1):
#       d = num%10
#       if d%2!=0:
#        list.append(d)
#       num = num//10
# else:
#      list.reverse()
#      print(list)
# ? =========================================================================================================
# s = "my name is anthony gunajlwsih  "
# x = s.split()
# print(x)
# i = 0
# while(i<len(x)):
#      print(x[i] ,"=",len(x[i]))
#      i= i+1
# s = " ".join(x)

#?------------------------------------------------
#write by me

# s="python is an oop lang"
# x = s.split()
# print(x)
# i=0
# while(i<len(x)):
#     print( x[i])
#     i=i+1
# s=" ".join(x)


# ? =========================================================================================================
#! PROGRAM WHICH WILL PRINT REVERSE A VALUE WITHOUT USING EXTEND AND SLICING
# num = int(input("enter a value : "))
# onum = num
# rn = 0
# while num > 0:
#     digit = num % 10
#     rn = rn * 10 +digit
#     num = num // 10
# print(f"reverse of {onum} is {rn}")

# ? =========================================================================================================
#! WRITE A PYTHON PROGRAM WHICH WILL GET UPPERCASE AND LOWERCASE LETTERS SEPERATELY
# ? =========================================================================================================
#! 08-10-2024
# s = "  PYTHON IS OOP LANG "
# x = s.split()
# # print(x)
# i = 0
# while i < len(x):
#       print(x[i])
#       j = 0
#       while j < len(x[i]):
#        print(x[i][j])
#        j = j + 1
#       i = i + 1
# ? =========================================================================================================
#! PROGRAM WHICH WILL PRINT REVERSE A VALUE WITHOUT USING EXTEND AND SLICING

# revnum = 0
# num=int(input("Enter a value :"))
# while(num>0):
#     r=num%10
#     revnum = (revnum*10) + r
#     num //= 10  # shorthand operator # num = num //10

    
# print(f"Reverse num : {revnum}")

#! WRITE A PYTHON PROGRAM WHICH WILL GET UPPERCASE AND LOWERCASE LETTERS SEPERATELY










# list1=[1,2,3]
# list2=list1+[3]
# print(list2)

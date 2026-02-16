#* LEVEL_1
#! printing 1 to n number
# n = int(input("ENTER A NUMBER : "))
# if(n<=0):
#  print(f"{n} is invalid input")
# else:
#  i = 1
#  while(i<=n):
#      print(i)
#      i=i+1
#  else:
#      print("it is else block")

# =================================
# !printing 1 to n number
# n=int(input("Enter a  number :"))
# i=1
# while(i<=n):
#     print(i)
#     i=i+1

# ------------------------------------------------------------------------------------------------------------
#!printing n to 1 number
# n = int(input("ENTER A NUMBER : "))
# if(n<=0):
#  print(f"{n} is invalid input")
# else:
#  i = n
#  while(i>=1):
#   print(i)
#   i=i-1
#  else:
#      print("it is else block")


#!printing n to 1 number
# n=int(input("Enter a number "))
# i=n
# while(i>=1):
#     print(i)
#     i=i-1



# ? ============================================================================================================
#!printing multiplication table
# n = int(input("ENTER A NUMBER WHOSE MULTIPLICATION YOU WANT : "))
# i = 1
# while(i<=10):
#      print(f'{n}X {i} = {n*i}')
#      i=i+1

#!printing multiplication table
# n=int(input("Enter a number :"))
# i=1
# while(i<=10):
#     print(i*n)
#     i=i+1

# ------------------------------------------------------------------------------------------------------------
#!printing multiplication table upto which you mulplication
# n = int(input("ENTER NUNBER FOR WHICH YOU WANT MULTIPLICATION TABLE : "))
# m = int(input("ENTER NUMBER UPTO WHICH YOU WANT MULTIPLICATION "))
# i = 1
# while(i<=m):
#      print(f" {n} X {i} = {n*i}")
#      i=i+1
# else:
#      print("it is else block")

#!printing multiplication table upto which you mulplication
# n=int(input("ENTER A NUMBER WHICH TABLE YOU WANT TO CREATE: "))
# m=int(input("ENTER A NUNBER UPTO YOU WNAT TABLE: "))
# i=1
# while(i<=m):
#     print(i*n)
#     i=i+1

#!printing multiplication table upto which you mulplication in reverse order
# n=int(input("ENTER A NUMBER WHICH TABLE YOU WANT TO CREATE: "))
# m=int(input("ENTER A NUNBER UPTO YOU WNAT TABLE: "))
# i=10
# while(i>=m):
#     print(i*n)
#     i=i-1

# ------------------------------------------------------------------------------------------------------------
#!printing multiplication table from which to upto which you mulplication
# n = int(input("ENTER NUNBER FOR WHICH YOU WANT MULTIPLICATION TABLE : "))
# i = int(input("ENTER FROM WHERE YOU WANT TO START MULTIPLICATION  : "))
# m = int(input("ENTER NUMBER UPTO WHICH YOU WANT MULTIPLICATION :  "))
# while(i<=m):
#      print(f" {n} X {i} = {n*i}")
#      i=i+1
# else:
#      print("it is else block")

#!printing multiplication table from which to upto which you mulplication
# n=int(input("ENTER A NUMBER WHICH TABLE YOU WNAT TO DO"))
# i=int(input("ENTER A NUMBER WHERE YOU START A TABLE :"))
# m=int(input("ENTER A NUMBER WHERE YOU END A TABLE :"))
# while(i<=m):
#     print(f" {n} X  {i}    {i*n}")
#     i=i+1



# ------------------------------------------------------------------------------------------------------------
#!reverse multiplication table
# n = int(input("ENTER A NUiMBER WHOSE MULTIPLICATION YOU WANT : "))
# i = int(input("where to start "))
# m = int(input("where to end"))
# while(i>=m):
#      print(f'{n}X {i} = {n*i}')
#      i=i-1




#!reverse multiplication table
# n = int(input("ENTER A NUiMBER WHOSE MULTIPLICATION YOU WANT : "))
# i = int(input("where to start  biggest value from end "))
# m = int(input("where to end"))
# while(i>=m):
#     print(f'{n}X {i} = {n*i}')
#     i=i-1

# ------------------------------------------------------------------------------------------------------------
# !reverse multiplication table by taking starting and ending from user
# n = int(input("ENTER A NUMBER WHOSE MULTIPLICATION YOU WANT : "))
# i = int(input("where to start "))
# m = int(input("where to end"))
# while(i>=m):
#      print(f'{n}X {i} = {n*i}')
#      i=i-1


# !reverse multiplication table by taking starting and ending from user
# n = int(input("ENTER A NUMBER WHOSE MULTIPLICATION YOU WANT : "))
# i = int(input("where to start  is biggest from end value"))
# m = int(input("where to end"))
# while(i>=m):
#      print(f'{n}X {i} = {n*i}')
#      i=i-1

# ? ========================================================================================================
#!program for accepting a word a printing its char by char
# -6  -5 -4  -3  -2  -1
# p   y   t   h   o   n
# 0   1   2   3   4   5


# *logic1
# word = input("ENTER A WORD :")
# i = 0
# while(i<len(word)):
#      print(word[i])
#      i = i+1

# ? or

# word = input("ENTER A WORD :")
# i = int(input("from where you want "))
# while(i<=(len(word)-1)):
#      print(word[i])
#      i = i+1


# *logic2
# word= input("enter a word : ")
# i = -len(word)
# while(i<0):  #OR i<=-1 
#      print(word[i])
#      i = i + 1

#! PROGRAM FOR ACCEPTING A WORD A PRINTING ITS CHAR BY CHAR 
# -6  -5 -4  -3  -2  -1
# p   y   t   h   o   n
# 0   1   2   3   4   5

# word=(input("Enter a WORD : "))
# i=0
# while(i<=len(word)-1): #? OR (i<len(word))
#     print(word[i])
#     i=i+1


# word=(input("Enter a word :"))
# i=int(input("from where you want "))
# while(i<len(word)):
#     print(word[i])
#     i=i+1

# word=(input("Enter a word :"))
# i=-len(word)
# while(i<0):
#     print(word[i])
#     i=i+1


# -----------------------------------------------------------------------------------------------------
#! PROGRAM FOR ACCEPTING A WORD A PRINTING ITS CHAR BY CHAR IN REVERSE ORDER
# -6  -5 -4  -3  -2  -1
# p   y   t   h   o   n
# 0   1   2   3   4   5

# * logic1
# word = input("ENTER A WORD : ")
# i = -1
# while(i>-len(word)+1):
#      print(word[i])
#      i = i-1
# else:
#      print("it is else block")

# * logic2
# word = input("ENTER A WORD : ")
# i = (len(word)-1)
# while(i>=0):  #OR i>-1
#      print(word[i])
#      i=i-1


# s="python"
# print(s[-6:6])
#! PROGRAM FOR ACCEPTING A WORD A PRINTING ITS CHAR BY CHAR IN REVERSE ORDER
# -6  -5 -4  -3  -2  -1
# p   y   t   h   o   n
# 0   1   2   3   4   5


# word=input("Enter a word :")
# i=len(word)-1
# while(i>=0):
#     print(word[i])
#     i=i-1


# word=input("Enter a word :")
# i=len(word)-1
# while(i>-1):
#     print(word[i])
#     i=i-1


# ? =====================================================================================================
# ! PROGRAM FOR PRINTING EVEN NUMBERS WITHIN N
# * logic1
# n = int(input("HOW MANY NUMBER YOU WANT TO GENRATE : "))
# i = 0
# while(i<=n):
#      print(i)
#      i = i+2
# else:
#      print("IT IS ELSE BLOCK")


# * logic2
# n = int(input("ENTER A NUMBER : "))
# i = 0
# while(i<=n):
#    if (i%2==0):
#     print(i)
#    i= i+1


# *LOGIC_3:
# n = int(input("Enter a number: "))
# i = 0
# while i <= n:
#     if i % 2 != 0:
#         pass  
#     else:
#         print(i)  
#     i += 1  

# ! PROGRAM FOR PRINTING EVEN NUMBERS WITHIN N
# n=int(input("Enter a number :"))
# i=0
# while(i<=n):
#     print(i)
#     i=i+2

# n=int(input("Enter a number :"))
# i=0 
# while(i<=n):
#     if(i%2==0):
#         print(i)
#     i=i+1


# n=int(input("Enter a number :"))
# i=0
# while(i<=n):
#     if(i%2!=0):
#         pass
#     else:
#         print(i)
#     i=i+1


#? =====================================================================================================
#!PROGRAM FOR PRINTING ODD NUMBER UPTO N
#*LOGIC_1:
# n = int(input("enter a number : "))
# i = 1
# while(i<=n):
#    print(i)
#    i=i+2
# else:
#    print("it is else block")
   
#*LOGIC_2:
# n = int(input("enter a number : "))
# i = 1             #OR 0
# while(i<=n):
#     if i%2!=0:
#       print(i)
#     i=i+1
# else:
#    print("it is else block")

#*LOGIC_3:
# n = int(input("Enter a number: "))
# i = 0                   #OR i = 1
# while i <= n:
#     if i % 2 == 0:
#         pass  
#     else:
#         print(i)  
#     i += 1              #OR i = i + 2

#!PROGRAM FOR PRINTING ODD NUMBER UPTO N
# n=int(input("Enter a number"))
# i=1
# while(i<=n):
#     print(i)
#     i=i+2
   

# n=int(input("Enter a number"))
# i=1
# while(i<=n):
#     if(i%2!=0):
#         print("odd",i)
#     i=i+1    

# n=int(input("Enter a number"))
# i=1
# while(i<=n):
#     if(i%2==0):
#         pass
#     else:
#         print(i)
#     i=i+1    
        

#? =====================================================================================================
#!PROGRAM FOR PRINTING BOTH EVEN AND ODD NUMBER UPTO N
# #*LOGIC_1:
# n= int(input("enter a  number "))
# i = 0
# while(i<=n):
#      if i%2 ==0:
#       print("even",i)
#      else:
#           print("odd",i)
#      i=i+1

#!PROGRAM FOR PRINTING BOTH EVEN AND ODD NUMBER UPTO N
# n=int(input("Enter a number :"))
# i=1
# while(i<=n):
#     if(i%2==0):
#         print("EVEN ",i)
#     else:
#         print("ODD",i)
#     i=i+1        


#? =====================================================================================================
#! PROGRAM FOR PRINTING EVEN NUMBERS IN DECREASING ORDER 
#*LOGIC_1:
# n = int(input("ENTER A NUMBER : "))
# i = n
# while(i>=0):
#      if i%2==0:
#       print("even",i)

          
# #*LOGIC_2:
# n= int(input("ENTER A NUMBER : "))
# i = n
# while(i>=0):
#      if i%2!=0:
#           pass
#      else:
#           print("even",i)
#      i=i-1 

#! PROGRAM FOR PRINTING EVEN NUMBERS IN DECREASING ORDER 
# n=int(input("Entera  number :"))
# i=n 
# while(i<=1):
#     print(i)
#     i=i+2

#?-------------
# n=int(input("Enter a number :"))
# i=n
# while(i>=0):
#     if(i%2!=0):
#         print(i)
#     i=i-1    

#?----------------
# n=int(input("Entera number:"))
# i=n
# while(i>=0):
#     if(i%2==0):
#         print(i)
#     i=i-1    

#? =====================================================================================================
#! PROGRAM FOR PRINTING ODD NUMBERS IN DECREASING ORDER


# #*LOGIC_1:
# n= int(input("ENTER A VALUE : "))
# i = n 
# while(i>=1):
#      if i%2!=0:
#       print(i)     
#      i -=1
# else:
#      print("it is else block ")

# #*LOGIC_2:
# n= int(input("ENTER A VALUE : "))
# i = n 
# while(i>=1):
#      if i%2==0:
#           pass
#      else:
#           print(i)
#      i-=1
# else:
#      print("it is else block ")

#! PROGRAM FOR PRINTING ODD NUMBERS IN DECREASING ORDER
# n=int(input("Enter a nuber :"))
# i=n
# while(i>=0):
#     if(i%2!=0):
#         print(i)
#     i=i-1   


# n=int(input("Enter a number :"))
# i=n
# while(i>=0):
#     if(i%2==0):
#         pass
#     else:
#         print(i)    
#     i=i-1    


#? =========================================================================================================
#! PROGRAM FOR PRINTING BOTH EVEN AND ODD NUMBERS IN DECREASING ORDER 
# n = int(input("ENTER A NUMBER : "))
# i = n
# while(i>=0):
#      if i%2==0:
#       print("even",i)
#      else:
#        print("odd",i)
#      i=i-1


#! PROGRAM FOR PRINTING BOTH EVEN AND ODD NUMBERS IN DECREASING ORDER 
# n=int(input("Enter a number "))
# i=n
# while(i>=0):
#     if(i%2==0):
#         print("EVEN in REVERSED",i)
#     else:
#         print("odd in reversed",i)
#         print()
#     i=i-1        


#! SUBSTRACTION BY -2
# n = int(input("ENTER A NUMBER: "))
# i = n

# while i >= 0:
#     print( i)
#     i -= 


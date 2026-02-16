# *LEVEL_1
# printing 1 to n number
# n= int(input("ENTER A NUMBER : "))
# for i in range(1,n+1):
#      print(i)

# ---------------------------------------------------------------------------------------------------
#! printing n to 1 number 
# n = int(input("ENTER A NUMBER : "))
# for i in range(1 , n+1):
#      print(i)

#? =====================================================================================================
#!printing multiplication table
# n= int(input("ENTER A NUMBER WHOSE MULTIPLICATION TABLE YOU WANT : "))
# S = int(input("ENTER VALUE FROM WHERE YOU WANT TO START TABLE "))
# E = int(input("ENTER VALUE FROM WHERE YOU WANT TO START TABLE "))
# for i in range(S,E+1):
#      print(f"{n}X{i}={n*i}")

# -----------------------------------------------------------------------------------------------------

# n= int(input("ENTER A NUMBER WHOSE MULTIPLICATION TABLE YOU WANT : "))
# S = int(input("ENTER VALUE FROM WHERE YOU WANT TO start TABLE "))
# E = int(input("ENTER VALUE FROM WHERE YOU WANT TO end TABLE "))
# for i in range(S,E-1,-1):
#      print(f"{n}X{i}={n*i}")

#? ====================================================================================================
# ! PROGRAM FOR PRINTING EVEN NUMBERS WITHIN N
#*LOGIC_1:
# n = int(input("ENTER A NUMBER WHERE YOU WANT TO GENERATE EVEN NUMBERS : "))
# for i in range(0,n+1,2):
#      print(i)

#*LOGIC_2:
# n = int(input("ENTER A NUMBER WHERE YOU WANT TO GENERATE EVEN NUMBERS : "))
# for i in range(n+1):
#  if i%2==0:
#     print(i)

#*LOGIC_3:
# n = int(input("ENTER A NUMBER WHERE YOU WANT TO GENERATE EVEN NUMBERS : "))
# for i in range(n+1):
#      if i%2!=0:
#           pass
#      else:
#           print(i)


#? ====================================================================================================
#!  PROGRAM FOR PRINTING ODD NUMBER UPTO N
#*LOGIC_1
# n= int(input("ENTER A NUMBER : "))
# for i in range (1,n+1,2):
#      print(i)

#*LOGIC_2
# n= int(input("ENTER A NUMBER : "))
# for i in range(1,n+1):  #OR 0
#      if i%2!=0:
#           print(i)
# else:
#      print("it is else block")

#*LOGIC_3
# n= int(input("ENTER A NUMBER : "))
# for i in range(1,n+1):
#      if i%2==0:
#           pass
#      else:
#           print(i)
#? ====================================================================================================
#! PROGRAM FOR ACCEPTING A WORD A PRINTING ITS CHAR 
# -6  -5 -4  -3  -2  -1
# p   y   t   h   o   n
# 0   1   2   3   4   5

#*LOGIC_1
# word= input("ENTER A WORD : ")
# for i in word:
#      print(i)

#*LOGIC_2
# word= input("enter a word : ")
# for i in range(0,len(word)):
#      print(word[i])

#*LOGIC_3
# word = input("ENTER A WORD : ")
# for  i in range((-len(word)),0):
#      print(word[i])
#? ====================================================================================================
#! PROGRAM FOR PRINTING BOTH EVEN AND ODD NUMBER UPTO N
# n = int(input("enter a number "))
# for i in range(n+1):
#      if i%2==0:
#           print("even",i)
#      else:
#           print("odd",i)


#? ====================================================================================================
#! PROGRAM FOR PRINTING EVEN NUMBERS IN DECREASING ORDER 
#*LOGIC_1
# n =  int(input("enter a number "))
# for i in range(n,0,-1):
#      if i%2==0:
#           print(i)
#  
     
#*LOGIC_2
# n =  int(input("enter a number "))
# for i in range(n,0,-1):
#      if i%2!=0:
#           pass
#      else:
#           print(i)

#? ====================================================================================================
#! PROGRAM FOR PRINTING ODD NUMBERS IN DECREASING ORDER
#*LOGIC_1
# n =  int(input("enter a number "))
# for i in range(n,1,-1):
#      if i%2!=0:
#           print(i)
 
     
#*LOGIC_2
# n =  int(input("enter a number "))
# for i in range(n,0,-1):
#      if i%2==0:
#           pass
#      else:
#           print(i)
#? ====================================================================================================
#! PROGRAM FOR PRINTING BOTH EVEN AND ODD NUMBERS IN DECREASING ORDER 
#*LOGIC_1
# n =  int(input("enter a number "))
# for i in range(n,0,-1):
#      if i%2==0:
#           print("EVEN",i)
#      else:
#           print("ODD",i)
     


#! SUBSTRACTION BY -2 IN DECREASING ORDER 
# n = int(input("enter a number :  "))
# for i in range(n,0,-2):
#      print(i)

#? ==================================================================================================
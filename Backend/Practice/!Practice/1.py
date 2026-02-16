# print("madam"=="madam"[::-1])
# print("madam"!="madam"[::-1])
# s="java"
# print(len(s))

# s=input("Enter a string : ")
# for i in s[-6:4]:
#     print(i,end= " ")

# r=range(1,6)
# for i in r:
#     print(i)

# for i in str("123"):
#     print(i)

# r=range(10,16,2)
# for i in r:
#     print(i)




# a=0b1111
# print(a,type(a))
# print(bin(15))

# a=0b10000
# print(a,type(a))
# a=0b1010
# b=0b0110
# print(a+b)

# a=19
# print(hex(a))

# a=0o13
# print(a)
# b=0o18          #SyntaxError: invalid digit '8' in octal literal
# print(b)

# a=0xEF
# print(a,type(a))

# a=0b1011
# print(a)
# !==================================================
# d1={1:"one",2:"two",3:"three"}
# for d,n in d1.items():
#     print(d,n)
# !===========================================

# d d1={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six"}
# digit=int(input("Enter a number :"))
# res=d1.get(digit)
# print(res)

# ?================================================


# d1={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six"}
# digit=int(input("Enter a number :"))
# res=d1.get(digit)
# if(res!=None):
#     print(res)
# else:
#     print(digit)    

# !========================================================================================

# d1={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six"}
# digit=int(input("Enter a number :"))
# res=d1.get(digit) if(d1.get(digit)!=None) else "it is number "


# print(2%2==0)
# print(not(2%2==0))
# print(2%2!=0)

# n=int(input("Entera  numnber :"))
# i=1
# while(i<=n):
#     if(i%2!=0):
#         print(i)
#     i=i+1    

# line=input("enter a line :")#.split()
# print(line)
# word=line.split()
# i=0
# while(i<=len(word)-1):
#     print(i , word[i] , len(word[i]))
#     i=i+1
    
#?---------------------------------------------

# word=input("Enter a word :")
# i=0
# while(i<len(word)):
#     print(i,word[i] )
#     i=i+1


# word=input("Enter a word :")
# for i in range(0,len(word)):
#     print(word[i])
#?----------------------------------------------
# s="python"
# i=0
# while(i<=len(s)-1):
#     print(i,s[i])
#     i=i+1

# s="python"
# for i in range(0,len(s)):
#     print(i,s[i])

#?===============================================================
# word=input("Enter a word: ")
# i=0
# while(i<=len(word)-1):
#     print(word[i])
#     i=i+1


# word=input("Enter a word :")
# for i in range(len(word)):
#     print(word[i])

#?========================================================================
#*LOGIC-1

# word=input("Enter a number")
# i=len(word)-1
# while(i>=0):
#     print(word[i])
#     i=i-1 


#*LOGIC-2
# word=input("Enter a word :")
# i=-1
# while(i>=-len(word)):
#     print(word[i])
#     i=i-1



#!===========================================


#-6 -5 -4 -3 -2 -1
# P  Y  T  H  O  N
# 0  1  2  3  4  5

# word=input("Enter a word :")
# for i in word:
#     print(i)

#!--------------------------

# word=input("Enter a word :")
# for i in range(-len(word),0):
#     print(word[i])

#!----------------------------------
# word=input("Enter a word :")
# for i in range(len(word)):
#     print(word[i])

#!---------------------------------
# word=input("Enter a word :")
# for i in range(0,len(word)):
#     print(word[i])

#!---------------------------------
#-6 -5 -4 -3 -2 -1
# P  Y  T  H  O  N
# 0  1  2  3  4  5

#REVERSED OF THE WORD OR VALUE 
# word=input("Enter a word :")
# for i in range(len(word)-1,-1,-1):
#     print(word[i])


# word=input("Enter a word :")
# for i in range( len(word),-1,-1):
#     print(i)


# 1. Print Numbers 1 to 10
# Write a program that uses a while loop to print the numbers from 1 to 10.

# n=int(input("Enter a number :"))
# i=1
# while(i<=n):
#     print(i)
#     i=i+1
#=============================================================
# 2. Even Numbers from 1 to 20
# Write a program that uses a while loop to print all even numbers from 1 to 20.
# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     if(i%2==0):
#         print(i)
#=================================================================
# 3. Sum of First 5 Numbers
# Write a program that uses a while loop to calculate the sum of the first 5 natural numbers (1+2+3+4+5).
# n=int(input("Enter a number :"))
# s=0
# i=0
# while(i<=n):
#     print(i)
#     s=s+i
#     i=i+1
# print(s)
#====================================================
# 4. Counting Down
# Write a program that counts down from 10 to 1 using a while loop.

# n=int(input("Enter a number:"))
# count=0
# i=1
# while(i<=n):
#     count=count+1
#     i=i+1
# print("Count = ",count)    

# 5. Repeat a Word
# Write a program that asks the user to input a word and a number, and then uses a while loop to print the word that many times.





# 6. Number Guessing Game
# Write a program that keeps asking the user to guess a number between 1 and 10 until they guess the correct number (you can hard-code the correct number).
# n=int(input("Enter a number:"))
# while(True):
#     n=int(input("Enter a number:"))
#     if(n==7):
#         print("win")
#         break

# n=7
# while(n==7):
#     n=int(input("Enter a number :"))



# 7. Print "Hello" 5 Times
# Write a program that uses a while loop to print the word "Hello" 5 times.
# i=1
# while(i<=5):
#     print("True")
#     i=i+1

# 8. Add Numbers Until Zero
# Write a program that keeps asking the user for a number and adds them up. The program stops when the user enters 0, and it then prints the total sum.
# s=0
# while(True):
#     n=int(input("Enter a number :"))
#     s=s+n
#     if(n==0):
#         break
# print(s)






# 9. Multiply by 2
# Write a program that starts with the number 1 and uses a while loop to multiply the number by 2 until the number is greater than or equal to 100.
# i=1
# while(i<=100):
#     print(i*2)
#     i=i+1







# 10. Print Odd Numbers
# Write a program that uses a while loop to print all odd numbers from 1 to 15.
# n=int(input("Enter a number "))
# i=0
# while(i<=n):
#     if(i%2!=0):
#         print(i)
#     i=i+1    

# s="python"
# for ch in s:
#     if(ch=="o"):
#         break
#     else:
#         print(ch)

# s="python"
# for ch in s:
#     if(ch=="o" or ch=="n"):
#         continue
#     else:
#         print(ch)


# s="python"
# for ch in s:
#     if(ch=="o"):
#         pass
#     else:
#         continue
# print(ch)

# s="python"
# for ch in s:
#     if(ch=="o"):
#         pass
#     else:
#         break
# print(ch)

# s="python"
# i=0
# while(i<len(s)):
#     if(s[i]=="o"):
#         break
#     else:
#         print(s[i])
#     i=i+1

# s="python"
# i=0
# while(i<len(s)):
#     if(s[i]=="o"):
#         continue
#     else:
#         print(s[i])
#     i=i+1

# s="python"

# s="MISSISSIPPI"
# count=0
# for ch in s:
#     if(ch=="I"):
#         count=count+1
#     if(count==3):
#         break
#     else:
#         print(ch)


# s="MISSISSIPPI"
# count=0
# for ch in s:
#     if(ch=="I"):
#         count=count+1
#     if(count==2):
#         continue    
#     else:
#          print("----------")
#          print(ch)
# print(count)






#^ --------------------------------------------------------------------------------------------`# lst = [45,34,54,33,0,-1,-3,17,29,-36]
# pv = [ val  for val in lst if val>0]
# nv = [val for val in lst if val<0]
# print("positive values  : ",pv)
# print("negative values : ",nv)`
#^ --------------------------------------------------------------------------------------------
#! PROGRAM FOR FINDING GIVEN VALUE IS PRIME OR NOT USING DICT COMPREHENSIOIN 

#^---------------------------------------------------------------
#! PROGRAM FOR FINDING GIVEN VALUE IS PRIME OR NOT USING LIST COMPREHENSIOIN 
# def prime(val):
#     res=True
#     for i in range(2,val):
#         if(val%i==0):
#             res="Not prime"
#     return res        




# lst=input("Enter a comma seperated value").split()
# lst_value=[int(i) for i in lst if(int(i)>1)]
# lst_prime=[val for val in lst_value if prime(val) ]
# print(lst_value)
# print(lst_prime)






#^ --------------------------------------------------------------------------------------------
#! Write a list comprehension to create a list of squares of numbers from 1 to 10.
# lst=[i for i in range(1,11)]
# print(lst)

# n=int(input("Entre a number : "))
# lst=[val for val in range(1,n+1)]
# print(lst)

# lst=[i**2 for i in range(1,11) ]
# print(lst)


#^ --------------------------------------------------------------------------------------------
#! Use a list comprehension to generate a list of even numbers between 1 and 20.
# lst=[val for val in range(1,21) if val%2==0]
# print(lst)
#^ --------------------------------------------------------------------------------------------
#! Write a list comprehension that creates a list of numbers from 1 to 10, but only include numbers greater than 5.
# lst=[val for val in range(1,11) if val>=5]
# print(lst)
#^ --------------------------------------------------------------------------------------------
#! Write a list comprehension to convert all characters in the string "hello world" to uppercase.
# lst="hello world" 
# lst1=[val.upper() for val in lst ]
# print(lst1)
# st="".join(lst1)
# print(st)
#^ --------------------------------------------------------------------------------------------
#! Generate a list of tuples (x, x^2) for x in the range 1 to 10 using a list comprehension.
# lst=[val for val in range(1,11) if ]
# print(lst)
# tpl=tuple(lst)
# print(tpl)
#!Generate a list of tuples (x, x^2) 

# lst=[val for val in range(1,11)]
#^ --------------------------------------------------------------------------------------------
#! Write a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 5 and the values are their cubes.
# lst={val:val**3 for val in range(1,6)}
# print(lst)
# for k,v in lst.items():
#     print(k,v)

#^ --------------------------------------------------------------------------------------------
#! Use a set comprehension to create a set of unique vowels present in the string "comprehension is fun".
# set={i for i in "comprehension is fun" if i in "AEIOUaeiou"}
# print(set)

#^ --------------------------------------------------------------------------------------------
#! Use a list comprehension to flatten the following list of lists: [[1, 2, 3], [4, 5], [6, 7, 8]].
# lst=[[1, 2, 3], [4, 5], [6, 7, 8]]
# lst1=[]
# flatten=[val for val in lst  ]
# lst1.append(val)
# print(lst1)
#*proper logic to access the list 
# flatten=[j for i in lst for j in i]
# print(flatten)



# n=input("Enter a string")
# for ch in n:
    





































































































































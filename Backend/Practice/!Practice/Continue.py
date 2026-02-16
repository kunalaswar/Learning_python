# s="python"
# print(s[0]+s[1]+s[2]+s[4])

#*logic-1
# s=input("Enter a string: ")
# for ch in s:
#     if(ch)=="o":
#         break
#     else:
#         print(f"{ch}")    
# else:
#     print("i am for loop else block")        
# print("i am a other statement in program")    

#*logic-2
# s=input("Enter a string: ")
# i=0
# while(i<len(s)):
#     if(s[i]=="o"):
#         break
#     else:
#         print(f"{s[i]}")    
#     i=i+1    
# else:
#     print("i am for loop else :")        

#!program for prime number
# n=int(input("Enter a number :"))
# i=1
# while(i<=n):
#     if(n%i==0):
#         print("PRIME--->",i)
#     i=i+1  

#!prime number program
# n=int(input("Enter a number :"))
# res="prime"
# for i  in range(2,n):
#     if(n%i==0):
#         res="Not prime"
#         break
# if(res=="prime"):
#     print(n , res)
# else:
#     print(n,res)


# s="python"
# for ch in s:
#     if(ch=="o"):
#         #  print(ch)
#          break
#     else:
#         print(f"value {ch}")    
# else:
#     print("it is for else loop")        

# s="python"
# i=0
# while(i<len(s)):
#     if(s[i]=="o"):
#         break
#     print(s[i])
#     i=i+1  

# s="python"
# i=0
# while(i<len(s)):
#     if(s[i]=="o"):
#         break
#     else:
#         print(f"value { s[i]}")
#     i=i+1    
# else:        
#     print("it is for else ")

#!prime number
# res="prime"
# n=int(input("Enter a number:"))
# for i in range(2,n):
#     if(n%i==0):
#         res="Not prime"
#         break
#     i=i+1
# if(res=="prime"):
#     print(n,  res)
# else:
#     print(n,  res)    

# n=int(input("Entera number:"))
# res="prime"
# for i in range(2,n):
#     if(n%i==0):
#         res="Not prime"
#         break
#     i=i+1
# if(res=="prime"):
#     print( n,  res)        
# else:
#     print(n,   res)    

# n=int(input("Entera number:"))
# res=False
# for i in range(2,n):
#     if(n%i==0):
#         res=True
#         break
#     i=i+1
# if(res==True):
#     print(n,  res)
# else:
#     print(n,   res)    

# n=int(input("Enter a number:"))
# i=2
# res="prime"
# while(i<=n):
#     if(n%i==0):
#         res="Not prime"
#         break
#     i=i+1
# if(res=="prime"):
#     print(f"{n} is prime")    
# if(res=="Not prime"):

#     print(f"{n} is Not prime")  

#* Continue statement

# s="python"
# for ch in s:
#     if(ch=="t"):
#         continue
#     print(ch)


# s="python"
# i=0
# while(i<len(s)):
#     if(s[i]=="t"):
#         i=i+1
#         continue
#     print(s[i])
#     i=i+1


# s="python"
# i=0
# while(i<len(s)):
#        if(s[i]=="y" or s[i]=="t"):
#             i=i+1
#             continue
#         print(s[i])
#         i=i+1
# # else:
# #     print(s[i])
# #     i=i+1

# s="python"
# i=0
# while(i<len(s)):
#     if(s[i]=="t"or s[i]=="h"):
#         i=i+1
#         continue
#     print(s[i])
#     i=i+1

# s="python"
# i=0
# while(i<len(s)):
#     if(s[i] in ["y","h"]):
#         i=i+1
#         continue
#     print(s[i])
#     i=i+1

# n=input("Enter a string  :")
# # list1=[]
# i=0
# while(i<len(n)-1):
#     if(n[i] in ["a","e","i","o","u"]):
#         i=i+1
#         # print(n[i])
#         continue
#     print(n[i])
#     i=i+1

# s="python"
# i=0
# while(i<len(s)):
#     if(s[i]=="y" or s[i]=="o"):
#         i=i+1
#         continue
#     print(s[i])
#     i=i+1

#!program take list of value and display only positive value
# n=int(input("Enter a number :")) #!Wrong
# list1=[1,2,3,4,-9,4,-3,-5,6,-7]
# list2=[]
# i=1
# while(i<len(list1)):
#     if(len(list1)<0):
#         # list1.append(list2)
#         i=i+1
#         continue
#     list1.append(list2)
#     # print(list2)
#     print(list1)
#     i=i+1

#!program take list of value and display only positive value 
# lst=[12,-23,-34,45,67,-8,9,-1]
# for val in lst:
#     if(val<0):
#         continue
#     print(val)
#!program take list of value and display only positive value 
# lst=[12,-23,-34,45,67,-8,9,-1]
# for val in lst:
#     if(val>0):
#         continue
#     print(val)

# lst=[12,-23,-34,45,67,-8,9,-1]
# lst2=[]
# for val in lst:
#     if(val>0):
#         # lst2.append(lst)
#         continue
#     print(val)

#!WAP accept the list of value from keyborad
# n=input("Enter a number :")
# # lst1=list(n)#!Enter a number :12 13 23 34 45 67  ['1', '2', ' ', '1', '3', ' ', '2', '3', ' ', '3', '4', ' ', '4', '5', ' ', '6', '7', ' ']
# # print(lst1)
# lst=n.split()
# print(lst)
# for val in lst:
#     if(int(val)<=0):
#         continue
#     print(val)
# # print(val)




# word=input("enter a word :")
# word.lower()
# for i in word:
#     if i in "aeiou":
#         # print(i,"it is vowel ")
#         print(i)
#         break
#     else:
#         print("it is not Vowel")
        

# text=input("Enter a line of text :").lower()
# for ch in text:
#     if ch not in "aeiou":
#         continue
#     else:
#         print(ch,end=" ")

# line=input("Enter a line of text :")
# for i in line:
#     if i.isalnum():
#         continue
#     else:
#         print(i)
        
# line=input("Enter a line of text :").split()
# print(line)
# for val in line:
#     if len(val)==2 or len(val)==3:  
#         print(val)

#! write a program to print only positive number from user input
# text=input("Enter a line of text seperated by space  :")
# # text.split()
# # print(text)

# for val in text:
#     if int(val)>0:
#         continue
#     else:
#         print(val,end=" ")

# n=int(input('enter a number Whrere you want to generate:'))
# for i in range(2,n+1):
#     # print(i)
#     res="prime"
#     for j in range(2,i):
#         if i%j==0:
#             res="Not prime"
#             break
#     if res=="prime":
#         print(i,"is",res)    
























# #!class with userDefined Execption
# class NumberDivisionError(Exception):pass

# def multi():
                
#     if (b==0):
#         raise NumberDivisionError 

#     else:
#         return a/b


# try:
        
#     a=int(input("Enter a number "))
#     b=int(input("Enter a number "))
#     c=multi(a,b)
#     print("Division =",c)
# except:
#     print("Error")

#* format for single line for code 
#!sagar code

# class InvalidNameError(Exception):pass
# class ZeroLenghtError(Exception):pass
# class SpaceError(Exception):pass
# n = input("Enter Name : ")
# try:
#   if len(n)==0:
#        raise ZeroLenghtError
#   elif n.isspace():
#        raise SpaceError
#   else:
#    lst = n.split()   
#    for word in lst:
#         if not word.isalpha():
#             raise InvalidNameError
#    print(n) 
# except InvalidNameError:
#     print("Please Enter Valid Name  ")
# except ZeroLenghtError:
#     print("Please Enter Name - Dont Leave Empty")
# except SpaceError:
#     print("Dont Enter Spaces ")



# class InvalidNameError (Exception):pass
# class ZerolengthError (Exception):pass
# class SpacesError(Exception):pass
# n=input("Enter a Name :")
# try:
#     if len(n)==0:
#         raise ZerolengthError
#     elif n.isspace():
#         raise SpacesError
        
#     x=n.split()
#     print(x)
#     for val in x:
#         if not val.isalpha():
#             raise InvalidNameError
#         print(n)    
# except ZerolengthError:
#     print("Entre some thing")        
# except SpacesError:
#     print("Space is there put your name")    
# except InvalidNameError:
#     print("Dont Enter Alnum Str  symbols")    



# def fun1(x):
#     lst=x.split()
#     # print(lst)
# # # fun1("121")    
#     # if 
#     for val in lst:
#         # print(val)
#         if val ==val[::-1]:
#            return True
# #     if res:
# #         print(res)
# #     else:
# #         print(res)
# val=input()        
# rv=fun1(val)                     
# print(rv)
# # if res:
# #     print(res)
# # else:
# #     print(res)        



# l1="python is aan oop lang"
# x=l1.split()
# # print(list(x))
# print(x)

#! to find the second max  

# def fun1(lst):
#     s=set(lst)
#     # print(s)
#     s1=sorted(len(s))
#     print(s1)

# lst=[1,2,3,4,4,5,6,6]
# fun1(lst)    


#!Decorator
# def outer(kvr):
#     def inner():
#         n=kvr()
#         # print(n,type(n))
#         # print(kvr,type(kvr))
#         res=n*n
#         return res
#     return inner    



# def getvals():
#     return int(input("Enter a number "))        

# res=outer(getvals)
# s=res()
# print("square = ",s)

#!
# def outer(kvr):
#     def inner():
#         n=kvr()
#         res=n*n
#         return n,res
#     return inner

# @outer   
# def getvals():
#     return int(input("enter a number :"))
# n,res=getvals()    
# print(n,res)

#! reversed the number logic

# def fun1():
#     n=int(input("Enter a number :"))
#     rev=0
#     while(n>0):
#         res=n%10
#         rev=rev*10+res
#         n=n//10
#     print(rev)
# fun1()

#!
# class NumberDivisionError (Exception):pass

# def multi(a,b):
#     if b==0:
#         raise NumberDivisionError 
#     else:
#         return a/b    


# try:
#     a=int(input("Enter a number :"))        
#     b=int(input("Enter a number :"))
#     res=multi(a,b)
#     print(res)

# except NumberDivisionError:
#     print("Dont Enter a Zeor for DEN ")
    
#!    

# class ZeroNumberError(Exception):pass
# class NegNumberError(Exception):pass

# def multi(n):
#     if n==0:
#         raise ZeroNumberError
#     elif n<0:
#         raise NegNumberError  
#     else:
#         i=0
#         for i in range(1,11):
#             print( f"{n} X {i} = {n*i}" )


# try:
#     n=int(input("Enter a number "))
#     multi (n)
# except ZeroNumberError:
#     print("Dont Enter a zero number ")

# except NegNumberError:
#     print("Dont Enter anegative number for i to generated multi table")

#!
# class NonprimeError (Exception):pass

# def prime(n):
#     if n==1:
#         raise NonprimeError
#     else:
#         for val in range(2,n+1):
#             if n%val==0:
#                 raise NonprimeError
#             else:
#                 return ("PRIME NUMBER ")        

# try :
#     n=int(input("Enter a Number :"))
#     res=prime(n)
#     print(res)

# except NonprimeError:
#     print("NUmber is not a prime")    

#& yield keyword

# def kvrrange(n):
#     s=0
#     while(s<n):
#         # s=s+n
#         yield s
#         s=s+1    

# res=kvrrange(5)
# print(res)
# for val in res:
#     print(val)

#todo - NONLOCAL KEYWORD USE

# def outer():
#     x=100
#     y=200
#     def inner1():
#         print(x)       
#         print(y)
#     def inner2():
#         nonlocal x,y
#         x=300
#         y=400
# inner1()        
# inner2()
# inner1()        
# print(x)
# print(y)
# outer()

    
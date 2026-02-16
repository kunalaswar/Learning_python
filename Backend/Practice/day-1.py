# a =10 
# print(a,type(a))
# a = 1.2
# print(a,type(a))

# a = 0b1100
# print(a,type(a))

# a = 15
# print(hex(a),type(a))

# a = 0xbe
# print(a,type(a))

# a =0xbee
# print(a,type(a))

# a =3e6 # e = 10 
# print(a,type(a))

# a = 0.00000000002
# print(a)

# a = 0.00000000004
# print(a,type(a))


# a = 2+3j
# print(a ,type(a))

# a = 2+3j
# b = 2+3j
# c = a+b
# print(a+b)
# print(c)

# a = "kunal" #Lenght always start form 1 and index is always start form 0
# print(a,type(a),len(a))

# a = bytes(13)
# print(a,type(a),len(a))

# a = "python"
# print(a[0:6])
# print(a[-6:0])
# print(a[0:3])
# print(a[9]) # indexError String index out of range 
# len function  is not used in the Fundamental datatype in python  it is totally isude in iterable object
# a = "hyderabad"[2]
# print(a)


# s = "PYTHON"
# # print(s[-10:-1:-1])
# print(s[:3:-1])
# print(s)

# a = "madam"=="madam"[::-1]
# print(a)
# a = "python" == "python"[::-1]
# print(a)

# b = "malayalam" =="malayalam"[::-1]
# print(b)

# p=eval("10")
# print(p,type(p))

# x = eval("1.5")
# print(x,type(x))

#type casting
# a = 12.23
# print(a)
# print(int(a))

# b = int(1.2)
# print(b)

# a = True
# print(a)
# print(int(a))

# b = False
# print(b)
# print(int((b)))

# c = 3+4j
# # print(int(c))
# print(c.real)
# print(int(c.real))
# print(c.imag)
# print(int(c.imag))

# a= "12"
# print(int(a))
# print(float("1.23"))

# a ="12.23" #Because of this there is an . dot pvm is convider as the special symbols
# print(int(a))
 
# b = "True" 
# print(int(b))

# a = 12 #int
# print(float(a))

# a =True
# print(float(a))

# a = 2 + 3j
# # print(float(a))
# print(float(a.real))
# print(float(a.imag))

# a = 2 + 3j
# b = float(a.real)
# print(b,type(b))

# a = 24
# print(bool(a))
# a =-23
# print(bool(a))
# b = 0
# print(bool(b))

# a ="12"
# print(bool(a))
# a = "0"
# print(bool(a))
# b = ""
# print(bool(b))

# c = 2+3j
# print(bool(c))

# a = 10
# print(complex(a))

# b = 23
# print(complex(b))

# c = complex(0)
# print(c,type(c))
# c = complex(3+2)
# print(c,type(c))
# print(complex(5-2))

# a = True
# b = str(a)
# print(b,type(b))
# print(len(b))

# a = 2+3j
# b = str(a)
# print(b)
# print(b,type(b),len(b))

#!Data is in encryption format
# lst = [1,2,33,4,5,6,7,8,9]
# # print(lst,type(lst))
# b = bytes(lst)
# print(b,type(b))
# for val in b:
#     print(val,end=" ")

# lst =[1,2,33,4,5,6,7,8,9,255]
# b = bytes(lst)
# print(b,type(b))
# for val in b:
#     print(val,end=" ")

# lst =[1,2,33,4,5,6,7,8,9,255]
# b = bytes(lst)
# print(b,type(b))
# b[0]= 23 #TypeError: 'bytes' object does not support item assignment
# print(b)
# c = tuple(b)
# print(c,type(c))

# lst =[1,2,33,4,5,6,7,8,9,255]
# b =bytes(lst)
# print(b,type(b))
# print(b[0]) #data is convert 
# print(b[3])
# print(b[0:3]) #data with in the bytes format 


# lst =[1,2,33,4,5,6,7,8,9,255]
# b = bytearray(lst)
# print(b,type(b))
# # for val in b:
# #     print(val,end = " ")
# b[0]=23    
# print(b,type(b))
# for k in b:
#     print(k,end=" ")
# print()    
# # x =b[1]
# # print(b[0:3])

# lst = [12,32,34,45,6,8,98,67]
# b = bytearray(lst)
# print(b,type(b))
# for val in b:
#     print(val,end = " ")

# a = range(10,16)
# print(a,type(a))
# for val in a:
#     print(val)

# for val in range(10):
    # print(val,end=" ")    

# for val in  range(10,21,2)[::-1]:
    # print(val)
# for val in range(-1,-11,-1):
#     print(val)


#!list 

# lst = [10,20,30,40,50,60]
# print(lst,type(lst))
# lst[0] = 100
# print(lst)
# lst[0:3]=["kunal","harshal","aniket","sagar"]
# print(lst)

# s = "python"
# print(list(s))

# lst= [10,20,30,40,50,60]
# print(lst)
# print(lst[2])
# print(lst[0:2])
# lst[0:2]=[100,200,300,400,500]
# print(lst)

#!function in list
# 1 append
# lst= [10,20,30,40,50,60]
# print(lst)
# lst[2]=(100)
# for val in lst:
#     print(val)
# print(lst)
# print(lst.append("kunal"))
# print(lst)

# lst= [10,20,30,40,50,60]
# print(lst,type(lst),id(lst))
# lst.append(100)
# print(lst)
# lst.append([1,2,33,4,5])
# print(lst,id(lst))

# lst = []
# for val in range(1,11):
#     lst.append(val)
# print("value of the list",lst)    

# lst1 = list()
# lst2 = []
# lst1.append([10,20,30,40,50])
# lst2.append(900)
# print(lst1)
# print(lst2)

# lst = [10,"RS",23.45]
# print(lst,type(lst))
# lst.insert(-1,"python")
# print(lst)
# lst.insert(-10,"kunal")
# print(lst)
# lst.clear()
# print(lst)

# lst= [10,20,30,"RS",True]
# print(lst)
# lst.remove("RS")
# print(lst)
# lst.remove(True)
# print(lst)
# lst.remove(10)
# print(lst)

# lst.remove(10)
# print(lst)

# lst = [10,20,30,40,50,60]
# lst.remove(30)
# lst.remove(10)
# lst.remove(20)
# lst.remove(40)
# lst.remove(50)
# lst.remove(60)
# print(lst)


# lst = [10,20,"RS", True]
# print(lst.pop(0))
# print(lst.remove(1))
# print(lst.pop(-1))
# print(lst.pop(100))
# print(lst)

# lst = [10,20,"RS", True]
# print(lst.pop())
# print(lst.pop())
# print(lst.pop())
# print(lst.pop())
# # lst.pop()
# print(lst)

# lst = [10,20,"RS", True]
# del lst[-2]
# del lst[1:2]
# del lst
# print(lst)

# lst =[10,20,30,40,50]
# del lst[::-1]
# print(lst)
# del lst
# print(lst)

# s = "what is your name"
# # del s[1:3] #! the both cases is not done in side this 
# # del s[0]
# del s
# print(s)


# lst = [10,20,30,"RS", True]
# print(lst.index(10))
# print(lst.index(20))
# print(lst.index(30))
# print(lst.index("RS"))
# print(lst.index(True))
# #print(lst.index(False)) #ValueError 
# print(lst)

# enumerate()
# this function isone of the predefined General function

# for val in range(11):
#     print(val,end=" ")
# lst= [10,20,30,40,50,60]
# for index,value in enumerate(lst):
#     print(f"{index} ---> {value}")

# lst= [10,20,30,40,50,60,10]
# for index,value in enumerate(lst):
#     # print(f"{index} --->{value}")
#     if (value ==10):
#         print(index,"--->", value)
    
# s = "MISSISSIPI"
# c = 0
# for index,value in enumerate(s):
#     if value =="I":
#         print(f"{index} --->{value}")
#         c= c+1
# print("Total value of I = ",c)        

# lst1 = [10,20,30,"RS" ,True]
# lst2 = lst1.copy() #!shallow copy
# print(lst1,id(lst1))
# print(lst2,id(lst2))


# lst1 = [10,20,30,"RS" ,True]
# lst2 = lst1
# print(lst1,id(lst1))
# print(lst2,id(lst2))
# lst1.remove(10)
# lst2.append(100)
# lst2.insert(1,"kunal")
# print(lst1)
# print(lst2)
# del lst1[1]
# print(lst1)
# print(lst2)

# count () Function in python
# lst = [10,20,30,10,20,60,50,10,20,40,30]
# print(len(lst))
# print(lst.count(10))
# print(lst.count(20))
# print(lst.count(30))

# print(list("1231231234561").count(1))
# print(list(123123423451).count(1)) #'int' object is not iterable

# print(list([1231231234986758].count(1))) #'int' object is not iterable

# print(list(["kunal"]).count("k"))
# print(list(["kunal"]).count("kunal"))

# lst1 =[10,20,"RS",23.45,True]
# lst2 = lst1.reverse()
# print(lst1,id(lst1))
# print(lst2,id(lst2)) # this return always none 

# lst1 =[10,20,"RS",23.45,True]
# print(lst1,id(lst1))
# lst1.reverse()
# print(lst1)

# lst = [1,2,3,45,6]
# print(lst[::-1])
# lst.reverse()
# print(lst)

# lst2 = []
# lst = [1,2,3,45,6]
# for val in lst:
#     lst2.append(val)
# print(lst2)    

# lst =[10,2,5,3,12,87,65,33,2]
# lst.sort()
# lst.sort(reverse=True)
# print(lst)
# lst.sort(reverse=False)
# print(lst)

# lst = [10,20,True,False]
# lst.sort()
# print(lst)

# lst1 = [10,20,30]
# lst2 = ["TR","RS","DR"]
# lst3 = [1.1,2.2,3.3]
# lst1.extend(lst2)
# lst1.extend(lst3)
# print(lst1)

# lst1 = [10,20,30]
# lst2 = ["TR","RS","DR"]
# lst3 = [1.1,2.2,3.3]
# # print(lst1+lst2+lst3)
# k=lst1+lst2+lst3
# print(k)

lst = [10,"kalesh",[20,16,18],[70,76,65],"JNTU"]
# print(lst)
# for val in lst:
#     print(val,type(val),type(lst))

# print(lst[2])
# for val in lst[2]:
#     print(val)

# lst[2] = ["kunal" ,"sagar","aniket"]
# # # lst[2].append(15)
# # # print(lst)

# (lst[-2].insert(-1,1000))
# print(lst[-2])
# lst[-2].sort()
# print(lst[-2])
# lst[2].sort()
# print(lst[2])

# function of the list
# append()
# insert()
# copy()
# lst1 = lst2
# shallow copy
# deep copy
# clear()
# index()
# list.pop()
# list.copy(1)
# list.extend(lst2)
# list.sort()
# del lst()
# for i,v in enumerate (lst):
#     print(i,v)

# tpl = ()
# tpl1 = tuple()
# print(type(tpl1))

# tpl = (10,20,30,40,50)
# print(tpl[1])
# print(tpl[0:2])

# # tpl[0]=100
# print(tpl)

# t= (10)
# print(t,type(t))
# t= (10,)
# print(t,type(t))
# x = ("python")
# print(x,type(x))

# tup = (10,20,45.56,0,9,-1)
# print("Slicing =",tup[::-1])
# print(tup.count(10))
# print(tup.index(45.56))
# tup = sorted(tup)
# print("sorted() function = ",tuple(tup))

# tup2= tup
# print(tup2) #Deep copy is possible but not shallow copy


# tup = (10,20,45.56,0,9,-1)
# lst = list(tup)
# lst.sort()
# print(lst,type(lst))
# print(tuple(lst),type(lst))



# tuple in tuple 
# tup = (10,"RS",(16,18,17),(67,80,78),"OUCET")
# print(tup)
# for val in tup:
#     print(val,type(val),type(tup))

# tup[0]=13 # TypeError: 'tuple' object does not support item assignment


# def kunal():
#     x = int(input("Enter a number :"))
#     y = int(input("Enter a number :"))
#     c = x+y
#     print(c)

# kunal()    
# # print(z)

# num = int(input("Enter a number :"))
# res = "Prime"
# for i in range(2,num+1):
#     for j in range(2,i):
#         if i%j==0:
#             res = "Not prime"
#             break


# if res == "prime":
#     print("prime")
# else:
#     print("Not prime")    

# n = int(input("Enter a number :"))
# res = "prime"
# for i in range(2,n):
#     if n%i ==0:
#         print("Not prime ")
#         break
# print(f"{res}")    

# n= int(input("Enter a number :"))
# res = "prime"
# i=0
# while(i<=n):
#     if (n%i==0):
#         print("Not prime")
#         break
#     i=i+1
# print(res)    

# n= int(input("Enter a number :"))
# res = True
# for i in range(2,n):
#     if (n%i==0):
#         res = False
#         break
    
# # print(res)    
# x = "prime" if res else "Not Prime"
# print(x)

# n = int(input("Enter a number "))
# if n<=0:
#     print("Invalid input")
# else:
#     for i in range(2,n+1):
#         res = True
#         for j in range(2,i):
#             if i%j==0:
#                 res= False
#                 break
# if res:
#     print("Prime")            
# else:
#     print("Not prime")    


# for val in range(2,2):
#     print(val)

# n = int(input("Enter a number :"))
# i = 2
# while(i<=n):
#     res =True
#     j = 2
#     while(j<i):
#         if i%j==0:
#             res = False
#             break
#         j = j+1
#     if res:
#      print(i,"prime")    
#     else:
#       print(i,"Not prime ") 
#     i=i+1

# lst = [val for val in input().split(",")]
# print(lst)

# lst = [int(val) for val in input("Enter : ").split()]
# print(lst)
# pv = [int(i) for i in lst if i>0]
# print(pv)
# nv = [int(i) for i in lst if i<0]
# print(nv)

# lst = [int(val) for val in input("Enter:").split() if int(val)>0]
# print(lst)
# sqr = {val:val*val for val in lst if val>0}
# print(sqr)
# for key,value in sqr.items():
#     print(f"{key} --->{value}")


# def decideprime(val):
#     res = True
#     for i in range(2,val):
#         if val%i==0:
#             res = False
#             break
#     return res        

# lst = [int(val) for val in input("Enter :").split() if int(val)>0]
# prime = [val for val in lst if decideprime(val)]
# print(prime)

# def decideprime(val):
#     res = True
#     for i in range(2,val):
#         if i%val==0:
#             res = 0
#             break
#     return res
# lst = [int(val) for val in input().split() if int(val)>0 or decideprime(int(val))]    
# print(lst)

# def sumop(a,b):
#     c = a+b
#     return c
# res = sumop(2,3)
# print(res)

# sumop = lambda a,b : a+b 
# res = sumop(2,3)
# print(res)


# sumop = lambda a,b :a+b
# res = sumop(4,5)
# print(res)

# sumop  = lambda a,b: a if a>b else b if a<b else print("Both are equal")
# lst = [int(val) for val in input().split() if int(val>0)]
# res = sumop(4,5)
# print("bigest value = ",res)


# addop = lambda a,b:a+b

# lst  = [int(val) for val in input().split()]
# filobj = list(filter(lambda val:val>0,lst))
# print(filobj)

# def pos(val):
#     if val>0:
#         return True
#     else:
#         return False
# print("Enter list of vlaue seperated by space ")
# lst = [int(val) for val in input().split()]
# obj1 = filter(pos,lst)
# print(list(obj1))

# lst = [int(val) for val in input().split()]
# # print(lst)
# fobj = list(filter(lambda val :val>0 ,lst))
# print(fobj)

# lst = [val for val in input("Enter a string ").split()]
# print(lst)
# filterobj = list(filter(lambda val :val==val[::-1],lst))
# print(filterobj)



# value = int(input("Enter  a number :"))

# res = "Even" if value%2==0 else "Odd"
# print(res)

# val = input("ENTER NUMBER :")
# res = "Palindrome" if val ==val[::-1] else "NOT Palindrome"
# print(res)

# num1 = int(input("Enter a first number :"))
# num2 = int(input("Enter a second number :"))
# num3 = int(input("Enter a third number :"))
# res = num1 if (num2<num1>=num2) else num2 if (num1<num2>=num3) else num3 if (num1<num3>=num2) else "All value EQUAL"

# print("Biggest value is =",res)




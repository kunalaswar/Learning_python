 #! global function 
# a=100
# def fun1():
#     b=10
#     print(a+10)
#     print(b)


# def fun2():
#     c=20
#     print(a+10)

#     print(c)

# fun1()
# fun2()

#! Globol function 
# def incre():
#     global a,b
#     a=a+10
#     b=b+20


# def update():
#     global a,b
#     a=a+1
#     b=b+1



# a=10
# b=20    

# incre()
# update()
# print(a)
# print(b)

# * tuple compresion 
# lst=(int(val) for val in input().split())
# print(lst)     #<generator object <genexpr> at 0x00000223C21FC2B0>
# #todo- to convert inot the tuple we can convert with the help of tuple function
# tup=tuple(lst)
# print(tup)

#
# def kvrmax(lst):  #[ 2,3,4,5]
#     mv=lst[0]
#     for val in lst:
#         if val > mv:
#             mv=val
#     return mv

# def kvrmin(lst): #[ 2,3,4,5,1]
#     minv=lst[0]
#     for val in lst:
#         if val< minv:
#             minv=val
#     return minv    



# findmax=lambda  lst:kvrmax(lst)
# findmin=lambda lst:kvrmin(lst)

# lst=[int(val) for val in input().split() if int(val)>0]
# mv=findmax(lst)
# minv=findmin(lst)
# # print(lst)
# print(mv)
# print(minv)

#!Filter function

# fun=lambda val : val%2==0


# lst=[int(val) for val in input().split()]
# print(lst)
# filobj=list(filter(fun,lst))
# print(filobj)


#!
# def pos(val):
#     if val>0:
#         return True
#     else:
#         return False
        

# lst=[int(val)for val in input().split()]
# # print(lst)

# obj= list(filter(pos,lst))
# print(obj)

#!
# pos=lambda val:val>0

# lst=[int(val) for val in input().split()]
# print(lst)
# obj=list(filter(pos ,lst))
# print(obj)


#! 

# pos=lambda val:val>0
# neg=lambda val:val<0
# n=input("Enter a value with space :")
# lst=[int(val) for val in n.split()]
# # print(lst)
# obj=list(filter(pos,lst))
# print(obj)
# obj1=list(filter(neg,lst))
# print(obj1)

#!
# pal=lambda val :val==val[::-1]

# lst=[val for val in input().split()]
# # print(lst)
# filobj=list(filter(pal,lst))
# print(filobj)

#!program for finding the list of vowels word
# fun1=lambda 

# words=input("Enter a line of  Text :").lower()
# lst=[val.lower() for val in words.split()]
# # print(lst)
# fun1=list(filter(lambda val :"a" in val or "e" in val or "i" in val or "o" in val or "u" in val,lst))
# print(fun1)

#!map function 
# lst=[int(val) for val in input().split()]
# # print(lst)
# mapobj=list(map(lambda val: val*val, lst))
# print(mapobj)

#!program for finding 


# lst=[int(val) for val in input().split()]
# # print(lst)
# hike=list(map(lambda val:val*0.5,lst))
# print(hike)

# lst=[int(val) for val in input().split()]
# # print(lst)
# even=list(filter(lambda val :val%2==0,lst))
# odd=list(filter(lambda val :val%2!=0,lst))
# print(even)
# print(odd)


#!
# dictemp={10:1000,20:2000,30:2500,40:4000}
# mspsal=list(map(lambda val:dictemp[val] + dictemp[val]*50/100,dictemp))
# print(mspsal)
# for k,v in zip(dictemp,mspsal):
#     dictemp[k]=v
# print("new saslary of Employee")
# for k,v in dictemp.items():
#     print(f"{k}--->{v}")

#!
# import sys
# dictemp={}
# while(True):
#     eno=input("Enter a Emp Number :")
#     sal=float(input("Enter a salary "))
#     dictemp[eno]=sal
#     ch=input("Do you want to enter a another Enter into it (YES/NO):").lower()
#     if ch=="no":
#         break
#     if ch not in ["yes","no"]:
#         print("INVALID input")
#         sys.exit()    

# #for k,v in dictemp.items():
# #    # print(k,v)

# modsal=list(map(lambda x:x[1] + x[1]*50/100,dictemp.items()))
# for k,v in zip(dictemp,modsal):
#     dictemp[k]=v
# # print()
# for key,val in dictemp.items():
#     print(key,val)


#!reduce function 
# import functools
# lst=[int(val) for val in input().split()]
# print(lst)
# res=functools.reduce(lambda a,b:a+b,lst)
# print(res)

# import functools
# def res(a,b):
#     c=a+b
#     return c

# lst=[int(val) for val in input().split()]
# # print(lst)
# rudobj=functools.reduce(res,lst)
# print(rudobj)

















































































































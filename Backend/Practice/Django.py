

# t = (5,10,15)
# x,_,y=t
# print(x,y)

#?===========================================================================================
# a = 1_2
# b = a*2
# print(b)

#?===========================================================================================
# x,y = 4,3
# z = (x--x)+(y--y)
# print(z)

#?===========================================================================================
# a = 2
# b = 3
# print(a**b*a**b)

#?===========================================================================================
# print(pow(2,3,5))  # 2**3 = 8%5 = 3

#?===========================================================================================
# print(pow(2,3,5,3))   #* TypeError: pow() takes at most 3 arguments (4 given)

#?===========================================================================================
#If n is divisible by 3, subtract 2 from n.
#If not, subtract 1 from n.
#?===========================================================================================

# n = 6
# while n>0:
#     print(n)
#     n-=2 if n%3==0 else 1
#?===========================================================================================
        
# add = lambda x,y : x+y
# result =add(3,5)*(lambda x:x**2)(2)  # here is (2) is the passing the argument to the lambda function 
# print(result)
#?===========================================================================================

# lst =[1,2,3]
# lst2 =str(lst)
# print(lst2,type(lst2))

#?===========================================================================================
# lst = [11,"bool",54,{},33,[],""]
# print(list(filter(bool,lst)))  # it return only True value not a false

#?===========================================================================================
# l = [1,0,2,0,3,0]
# for i in l:
#     if i==0:
#         l.remove(i)
#         l.append(i)
# print(l)        
#?===========================================================================================
# a = {1,1,1,2,2,6,6,6,6}
# b = list(a)
# print(b)
# print(b[2])
#?===========================================================================================
# s = "python"
# for i in range(len(s)):
#     print(s)
#     s ="a"
#?===========================================================================================

# a = ["a","b","c","d"]
# for i in a:
#     a.append(i.upper())
# print(a)
#?===========================================================================================

# def f1(*,a,b):
#     print(a,b)
# f1(a=10,b=20)
#?===========================================================================================
# def f1(a,b,/):
#     print(a,b)
# f1(10,20)    
#?===========================================================================================
# def f1(*,a,b,c,/):   #* Invalid syntax syntaxerror
#     print(a,b,c)
# f1()    

#?===========================================================================================
# a = ['a','b','c','d']
# for i in a:
#     a.append(i.upper())
# print(a)    #* MemoryError  throw at runtime 

#* then your answer is right
# a = ['a','b','c','d']
# l=[]
# for i in a:
#     l.append(i.upper())
# print(l)    

#?===========================================================================================
#* Alising

# x = [10,20,30,40,50]
# y = x   #* Deep copy
# y[1]=333
# print('x :', x)
# print('y :', y)

#?===========================================================================================
#* cloning
# x = [10,20,30,40,50]
# y = x.copy()
# y[1]=333
# print('x :', x)
# print('y :', y)


# x = [10,20,30,40]
# y = x[:]
# y[1] = 333
# print('x :', x)
# print('y :', y)

# Aliasing and Cloning:
# --------------------------------

# = meant for aliasing
# copy()/[:] meant for cloning

# import copy
# x = [10,20,[30,40],50]
# y = copy.copy(x)
# y[2][0] = 333
# print('x :', x)
# print('y :', y)

# import copy
# x = [10,20,[30,40],50]
# y = copy.deepcopy(x)
# y[2][0]=333
# y[2][2]=444
# print('x :', x)
# print('y :', y)



#?===========================================================================================
# a = {"hello":"world","first":1}
# b = {k:v for k,v in a.items()}
# print(b)

# str1 = 'PYTHON'
# output = [chr(ord(char)-5) for char in str1]
# print(''.join(output)) #KTOCJI
#?===========================================================================================

# ==========================  8-04-2025 =========================
# chapter 4: Working with Models & Databases
# a = 10 #global var
# def f1():
#     a = 333
#     print("f1:",a)
# def f2()    :
#     print("f2:",a)

# f1()
# f2()
#* the main perpose of global varible 
# a = 10 #global
# def f1():
#     global a
#     a = 333 #local
#     print("f1:",a)
# def f2():
#     print("f2:",a)

# f1()
# f2()

#?===========================================================================================
# def outer():
#     print("Hii ")
# f1 = outer # if we dont mension the outer() function paranthesis then it well create an Error

# def outer():
#     print("Hii")
# f1 = outer
# f1() # call by here 

#?===========================================================================================

# def wish():
#     print("Hi good morning")
# greet = wish 
# del wish
# greet()    

#?===========================================================================================
# from faker import Faker
# fakegen = Faker()
# name = fakegen.name()
# print(name)
# fname = fakegen.first_name()
# print(fname)
# lname = fakegen.last_name()
# print(lname)
# date1 = fakegen.date()
# print(date1)
# number = fakegen.random_number(5)
# print(number)
# email1 = fakegen.email()
# print(email1)

# city = fakegen.city()
# print(city)

# print(fakegen.random_int(min=0,max=9999))
# print(fakegen.random_element(elements=("sunny","bunny","vinny","chinny","pinny")))


#?===========================================================================================

# from random import *
# def phonenumber():
#     d1 = randint(6,9)
#     # print( d1)
#     num =   "" +str(d1)
#     for i in range(randint(0,9)):
#         num = str(randint(0,9))
#     return int(num)    
# for i in   range(10):
#     phonenumber()
#?===========================================================================================

#! Date = 16-04-2025

# from faker import Faker
# fake_obj = Faker()
# for i in range(10):
#     phno = fake_obj.phone_number()
#     print(phno)
#?===========================================================================================
# how to add the two dictnaries

#! How to merge 2 dictionaries into a third dictionary 
# print(d1+d2)
#* 1st way
# d1= {100:'sunny',200:'Bunny',300:'Chinny'}
# d2 = {300:'vinny',400:'pinny',500:'ginny'}
# d3 = {**d1,**d2}
# print(d3)

# #* 2nd way
# d3 = d1.copy()
# for k,v in d2.items():
#     d3[k]= v
# print(d3)    


#todo - How to update an existing dict with items of another dict?
#* 3rd way

# d1.update(d2)
# print(d1)

#* 4th way

# d1 |= d2
# print(d1)








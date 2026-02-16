# Approach1:funtion with return type with parameter
# --------------------------------------------------
# #INPUT          : Taking from Function Call
# #PROCESS   : Done inside of Function Body
# #RESULT      : Giving Back to Function Call
# --------------------------------------------------
# def addop(a,b):
#     c=a+b
#     return c

# x=float(input("Enter First Value:"))
# y=float(input("Enter Second Value:"))
# z=addop(x,y) # function call
# print(f"sum({x} {y})={z}")
 

# Approach2:function with no return type and no parameter
# --------------------------------------------------
# #INPUT     : Inside the Function Body
# #PROCESS   : Inside the Function Body
# #RESULT    : Inside the Function Body
# --------------------------------------------------

# def addop():
#     a=float(input("Enter First Value:"))
#     b = float(input("Enter Second Value:"))
#     #Processing
#     c=a+b
#     #Display the Result
#     print(f"sum({a} {b})={c}")

# #Main Program
# addop() # Function Call

# Approach3:function  no return type and with parameter
# --------------------------------------------------
# #INPUT     : Taking from Function Call
# #PROCESS   : Done inside of Function Body
# #RESULT    : Inside the Function Body
# --------------------------------------------------
# def addop(a,b):
#     c=a+b
#     print("sum({},{})={}".format(a,b,c))

# #Main Program
# x=float(input("Enter First Value:"))
# y=float(input("Enter Second Value:"))
# addop(x,y) # Function Call


# Approach4:function with no parameter and with return type
# --------------------------------------------------
# #INPUT     : Inside the Function Body
# #PROCESS   : Inside the Function Body
# #RESULT    : Giving Back to Function Call
# ------------------------------------
# def addop():
#     # Take the Input
#     a = float(input("Enter First Value:"))
#     b = float(input("Enter Second Value:"))
#     # Processing
#     c = a + b
#     #Give the Result Back to Function Call
#     return a,b,c # here return not returns Single Value But also returns More than one value
# #Main Program
# a,b,c=addop() # Function Call with Multi Line assigment
# print("sum({},{})={}".format(a,b,c))
# print("---------------OR---------------------")
# res=addop() # Function Call with Single Line assigment
# #here res is an object of <class, tuple>
# print("sum({},{})={}".format(res[0],res[1],res[2]))
# print("-----------OR----------------")
# print("sum({},{})={}".format(res[-3],res[-2],res[-1]))

#------------------------------------------------------------------------------------------------------------
#calculate simple intersted and total amount to pay
# si=p*r*t
# total=si+p
#----------------------------------------------------------------------------------------------------------------

#approach 1:function with return type and with parameter
#-----------------------------------
# def simpleintersted(p,r,t):
#     si=p*r*t
#     total=si+p
#     return si,total

# p=int(input("Enter a principal Amount: "))
# r=int(input("Enter a rate of intersted : "))
# t=int(input("Enter a time : "))
# si,total=simpleintersted(p,r,t)
# print(f"{p}{r}{t}={si}")
# print(f"{si} + {p}= {total}")

#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def simpleintersted():
#     p=int(input("Enter a principal Amount: "))
#     r=int(input("Enter a rate of intersted : "))
#     t=int(input("Enter a time : "))
#     si=p*r*t
#     print(f"{p}{r}{t}={si}")
#     total=si+p
#     print(f"{si} + {p}= {total}")

# simpleintersted()

#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def simpleintersted(p,r,t):
#     si=p*r*t
#     print(f"{p}{r}{t}={si}")
#     total=si+p
#     print(f"{si} + {p}= {total}")

# p=int(input("Enter a principal Amount: "))
# r=int(input("Enter a rate of intersted : "))
# t=int(input("Enter a time : "))

# simpleintersted(p,r,t)
    
#approach 4:function with  return type and with no  parameter
#--------------------------------------------
# def simpleintersted():
#     p=int(input("Enter a principal Amount: "))
#     r=int(input("Enter a rate of intersted : "))
#     t=int(input("Enter a time : "))
#     si=p*r*t
#     total=si+p
#     return p,r,t,si,total

# res=simpleintersted()
# print(f"{res[0]}{res[1]}{res[2]}={res[3]}")
# print(f"{res[3]} + {res[0]}= {res[-1]}")

#----------------------------------------
#area of rectangle
# area=length*breadth
#-------------------------------------------

#approach 1:function with return type and with parameter
#-----------------------------------
# def rect(l,b):
#     area=l*b
#     return area

# length=int(input("Enter a length of reactangle: "))
# breadth=int(input("Enter a breadth of reactangle: "))
# area=rect(length,breadth)
# print(f"{length}*{breadth}={area}")

#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def rect():
#     l=int(input("Enter a length of reactangle: "))
#     b=int(input("Enter a breadth of reactangle: "))
#     area=l*b
#     print(f"{l}*{b}={area}")

# rect()    

#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def rect(l,b):
#     area=l*b
#     print(f"{l}*{b}={area}")

# l=int(input("Enter a length of reactangle: "))
# b=int(input("Enter a breadth of reactangle: "))     
# rect(l,b)

#approach 4:function with  return type and with no  parameter
#--------------------------------------------
# def rect():
#     l=int(input("Enter a length of reactangle: "))
#     b=int(input("Enter a breadth of reactangle: "))
#     area=l*b
#     return l,b,area

# res=rect()
# print(f"{res[0]}*{res[1]}={res[-1]}")     

#------------------------------------------------------------------------------------------------------------------------
#area of circle
# area=3.14*r*r
#---------------------------------------------------------------------------------------------------------------------------

#approach 1:function with return type and with parameter
#-----------------------------------
# def circle(r):
#     area=3.14*r*r
#     return area

# radius=int(input("enter aradius:"))
# a=circle(radius)
# print(f"3.14 * {radius} * {radius}={a}")

#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def circle():
#     r=int(input("enter aradius:"))
#     area=3.14*r*r
#     print(f"3.14 * {r} * {r}={area}")

# circle()    

#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def circle(r):
#     area=3.14*r*r
#     print(f"3.14 * {r} * {r}={area}")

# radius=int(input("enter aradius:"))
# circle(radius)

#approach 4:function with  return type and with no  parameter
#--------------------------------------------
# def circle():
#     r=int(input("enter aradius:"))
#     area=3.14*r*r
#     return r,area

# res=circle()
# print(f"3.14 * {res[0]}* {res[0]}=  {res[-1]}")


#-----------------------------------------------------------------------------------------------------------------------
#area and perimeter of square
# area=side*side
# perimeter=4*side
#------------------------------------------------------------------------------------------------------------------------

#approach 1:function with return type and with parameter
#-----------------------------------
# def area_square(side):
#     area=side*side
#     return area

# def perimeter_square(side):
#     perimeter=4*side
#     return perimeter

# s=int(input("Enter a side of square: "))

# a=area_square(s)
# print(f"{s} * {s} = {a}")

# p=perimeter_square(s)
# print(f"{s} * 4 = {p}")


#approach 2:function with no return type and with no  parameter
#-----------------------------------------------

#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def area_square(side):
#     area=side*side
#     print(f"{side}* {side}={area}")

# def perimeter_square(side):
#     perimeter=4*side
#     print(f"{side}* 4 ={perimeter}")

# s=int(input("enter a side of square:"))

# area_square(s)

# perimeter_square(s)

#approach 4:function with  return type and with no parameter
#--------------------------------------------

# def area_square():
#     s=int(input("enter a side of square:"))
#     area=s*s
#     return area,s 

# a,b=area_square()
# print(f"{b} * {b} = {a}")
# print("------------------------OR--------------------------------------")
# res=area_square()
# print(f"{res[1]} * {res[1]} = {res[0]}")


#--------------------------------------------------------------------------------------------------------
#!area and perimeter of triangle
# area=1\2 *base *height
# perimeter=length + length + length
#--------------------------------------------------------------------------------------------------------

#approach 1:function with return type and with parameter
#-----------------------------------
#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
#approach 4:function with  return type and with no  parameter
#--------------------------------------------


#! PROGRAM FOR REVERSING WORD AT SAME PLACE

# def reverseword(s):
#     x=s.split()
#     # print(x)
#     lst=[]
#     for i in x:
#         lst.append(i[::-1])
#     print(lst)    



# n=input("Enter a number :")
# reverseword(n)


#?------------------------------------------------------------------------------------------------
# !which will accept a line of words and find length of each word and also find smallest word length calculate roots of quandratic equation
#?------------------------------------------------------------------------------------------------
# given input:     python is an oop lang
# expected output: nohtyp si na poo gnal
#approach 1:function with return type and with parameter
#-----------------------------------
# def reverseword(s):
#     x=s.split()
#     # print(x)
#     lst=[]
#     for i in x:
#         lst.append(i[::-1])

#     p=" ".join(lst)    
#     print(p)

# s=input("Enter a line of text :")
# reverseword(s)

#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def reverseword():
#     s=input("Enter a line of text :")
#     x=s.split()
#     # print(x)
#     lst=[]
#     for i in x:
#         lst.append(i[::-1])
#     print(lst)  
#     k=" ".join(lst)  
#     print(k)

# reverseword()

#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def reverseword(s):
#     x=s.split()
#     print(x)
#     lst=[]
#     for i in x:
#         lst.append(i[::-1])
#     else:

#         k=" ".join(lst)
#         print(k)


# n=input("Enter a line of text :")
# reverseword(n)
#approach 4:function with  return type and with no  parameter
#--------------------------------------------
# def reverseword():
#     n=input("Enter a line of text :")
#     x=n.split()
#     # print(x)
#     lst=[]
#     for i in x:
#         lst.append(i[::-1])

#     print(lst)
#     k=" ".join(lst)
#     return k

# k=reverseword()
# print(k)

#! PROGRAM FOR REVERSING WORD AT SAME PLACE
# def reverseword(x):
#     # print(x)
#     k=x.split()
#     lst=[]
#     for i in k:
#         lst.append(i[::-1])
#     # print(lst)
#     s=" ".join(lst)
#     return s

# n=input("Entre a line of text :")
# res=reverseword(n)
# print(res)

# def reverseword(x):
#     print(x)
#     lst=[]
#     for i in x:
#         # print(i[::-1])
#         lst.append(i[::-1])
#     print(lst)
#     s=" ".join(lst)
#     print(s)
# n=int(input("Entre how many value you wnat to genetare :"))
# for i in range(1,n+1):
#     value=input("Enter a word ")
# reverseword(n)




#!magic number program
# def magic(n):
#     square=n*n
#     print(square)
#     snumber=str(n)
#     ssquare=str(square)
#     if(ssquare.endswith(snumber)):
#         print("magic number")
#     else:
#         print("NOt magic number")



# n=int(input("Enter a number :"))
# magic(n)

#!magic number program
#*approach 1:function with return type and with parameter
#-----------------------------------
# def magicnum(n):
#     square=n*n
#     print(square)
#     ssquare=str(square)
#     snum=str(n)
#     if(ssquare.endswith(snum)):
#         return ("magic number ")
#     else:
#         return ("Not a magic number ")


# n=int(input("Enter a number :"))
# res=magicnum(n)
# print(res)


#*approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def magicnum():
#     n=int(input("Enter a number :"))
#     square=n*n
#     # print(square)
#     ssquare = str(square)
#     snum=str(n)
#     if(ssquare.endswith(snum)):
#         print(f"magic number {snum}")
#     else:
#         print(f" not a magic number {snum}")    
#main program

# magicnum()


#*approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def magicnum(n):
#     square=n*n
#     print(square)
#     ssquare=str(square)
#     snum=str(n)
#     if(ssquare.endswith(snum)):
#         print("magic number")
#     else:
#         print("Not a magic number")    




# n=int(input("Enter a number :"))
# if(n<=0):
#     print("Invalid input ")
# else:
#     magicnum(n)

#*approach 4:function with  return type and with no  parameter
#--------------------------------------------
# def magicnum():
#     n=int(input("Enter a number: "))
#     square=n*n
#     print(square)
#     snum=str(n)
#     ssquare=str(square)
#     if(ssquare.endswith(snum)):
#         return(f"It is magic number {snum}")
#     else:
#         return(f"It is not a magic number {snum}")    
#!main program
# res=magicnum()
# print(res)



#approach 1:function with return type and with parameter
#-----------------------------------
#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
#approach 4:function with  return type and with no  parameter
#--------------------------------------------


#&         Aniket question
#! which will accept a line of words and find length of each word and also find smallest word length
#?----------------------------------------------------------------------------------------------
# def readvalue():
#     n=int(input("enter a how many list of value you want :"))
#     lst=[]
#     for i in range(1,n+1):
#         value=input("Enter a word :")
#         lst.append(value)
#     return(lst) 
   
# def findlength(lst):
#     wordlen=dict()
#     for i in lst:
#         wordlen[i]=len(i)
#     return wordlen
# def  leastlengthword(wordlen):
#     val=wordlen.values()
#     # print(val)
#     mv=min(val)
#     print(mv)
#     for key ,value in wordlen.items():
#         if(value==mv):
#             print(f"{key} {value}")


# lst=readvalue()
# if(type(lst)==str):
#     print(str)
# else:    
#     wordlen=findlength(lst)
#     leastlengthword(wordlen)


#! calculate roots of quandratic equation
#?----------------------------------------------------------------------------------------------


       #*Harshal
#! given input:     python is an oop lang
#! expected output: nohtyp si na poo gnal
#?----------------------------------------------------------------------------------------------
# def reverseword():
#     word=input("Enter  a line of text :")
#     x=word.split()
#     print(x)
#     lst2=[]
#     for i in range(len(x)):
#         lst2.append(x[i][::-1])
#     print(lst2)   
#     return " ".join(lst2)

# print("Reverse string : ",reverseword())











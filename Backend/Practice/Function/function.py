# def sumop():
#     print("this is inside the function")
#     print("Welcome to function")

# sumop()
# print("ths is outside the function")

#*Approach 1
# def sumop():
#     a=int(input("Enter a number :"))
#     b=int(input("Enter a number :"))
#     c=a+b
#     print("sum",c)
# sumop()    

#*Approach 2
# def sumop(a,b):
#     x=int(input("Enter a number"))
#     y=int(input("Enter a number"))
#     z=x+y
#     return z

# res=sumop(5,6)
# print("sum =" ,res)

# def welcome(): # Function Definition
#     print("Welcome to Functions")

# #Main Program
# print("I am before Function Call")
# print("Type of welcome=",type(welcome)) # <class, 'function'>
# welcome() # Function Call
# print("I am after Function Call")

#* Approach1:
# --------------------------------------------------
#INPUT          : Taking from Function Call
#PROCESS   : Done inside of Function Body
#RESULT      : Giving Back to Function Call
# def sumop(a,b):
#     c=a+b
#     return c

# #& main program  
# x=int(input("Enter a  number :"))
# y=int(input("Enter a  number :"))
# z=sumop(x,y)
# print(f"sum({x} + {y}) ={z}")



# * Approach2:
# --------------------------------------------------
#INPUT     : Inside the Function Body
#PROCESS   : Inside the Function Body
#RESULT    : Inside the Function Body
# def sumop():
#     x=int(input("Enter a number :"))
#     y=int(input("Enter a number :"))
#     z=x+y
#     print(f" sum({x} +{y}) ={z}")
# #& main program  
# sumop()    


# --------------------------------------------------
#* Approach3:
# --------------------------------------------------
#INPUT     : Taking from Function Call
#PROCESS   : Done inside of Function Body
#RESULT    : Inside the Function Body

# def sumop(a,b):
#     c=a+b
#     print(f"sum {a} {b} ={c}")

# # #& main program  
# x=int(input("Enter a number :"))
# y=int(input("Enter a number :"))
# z=sumop(x,y)

# --------------------------------------------------
#* Approach4:
# --------------------------------------------------
#INPUT     : Inside the Function Body
#PROCESS   : Inside the Function Body
#RESULT    : Giving Back to Function Call
# def sumop():
#     x=int(input("Enter a number : "))
#     y=int(input("Enter a number : "))
#     z=x+y
#     return x,y,z
# a, b, res=sumop()    
# print(f" sum({a} {b}) ={res}")










# def addop():
#     # Take the Input
#     a = float(input("Enter First Value:"))
#     b = float(input("Enter Second Value:"))
#     # Processing
#     c = a + b
#     #Give the Result Back to Function Call
#     return c # here return not returns Single Value But also returns More than one value
#Main Program
# c=addop() # Function Call with Multi Line assigment
# print(c)
# res=addop() # Function Call with Single Line assigment
#here res is an object of <class, tuple>
# print("sum({},{})={}".format(res[0],res[1],res[2]))

# print("sum({},{})={}".format(res[-3],res[-2],res[-1]))

#^ WAP to  which will calculate  Area of rectangle 

# def areat():
#     l=int(input("Enter a length :"))
#     w=int(input("Enter a width :"))
#     area=l*w
#     print(f" area of rectangle {area}")
# areat()    

#* Approach1:
# --------------------------------------------------
#INPUT          : Taking from Function Call
#PROCESS   : Done inside of Function Body
#RESULT      : Giving Back to Function Call
# def areat(a,b):
#     c=a*b
#     return c



# l=int(input("Enter a lenght : "))    
# w=int(input("Enter a width : "))    
# res=areat(l,w)
# print(f"Area of rectangle => {res}")


#* Approach2:
# --------------------------------------------------
#INPUT     : Inside the Function Body
#PROCESS   : Inside the Function Body
#RESULT    : Inside the Function Body
# --------------------------------------------------
# def areat():
#     l=int(input("Enter a length :"))
#     w=int(input("Enter a width :"))
#     area=l*w
#     print(f" area of rectangle {area}")
# areat() 
        
#* Approach3:
# --------------------------------------------------
#INPUT     : Taking from Function Call
#PROCESS   : Done inside of Function Body
#RESULT    : Inside the Function Body
# --------------------------------------------------
# def areat(a,b):
#     c=a+b
#     print(f"sum {c}")


# l=int(input("Enter a lenght : "))    
# w=int(input("Enter a width : "))    
# areat(l,w)


#* Approach4:
# --------------------------------------------------
#INPUT     : Inside the Function Body
#PROCESS   : Inside the Function Body
#RESULT    : Giving Back to Function Call
# def areat():
#     l=int(input("Enter a lenght : "))    
#     w=int(input("Enter a width : "))    
#     area=l*w
#     return  area
# res=areat( )
# print(f" sum =>{res} ")

#!  Area of circle
# #* Approach1:
#^parameter  with return type
# def circle(r):
#     c=3.14*r**2
#     return c
# #& main program
# x=int(input("Enter a Radius  of the circle : "))  
# res=circle( x)  
# print(res)

#* Approach2:
#^ No parameter with no return type
# def circle():
#     r=int(input("Enter a radius of circle :"))
#     pi=3.14
#     area=pi*r*r
#     print(f"Radius = {area}")
    
# circle()    

#* Approach3:
#^ parameter with no return type
# def circle(r):
#     pi=3.14
#     k=pi*r*r
#     print(f"area => {k}")
    

# r=int(input("Enter a radius of circle :"))
# circle(r)

#* Approach4:
 #^ no p no r
# def circle():
#     pi=3.14
#     r=int(input("Enter a radius of circle :"))
#     k=pi*r*r
#     return k
# k=circle()    
# print(k)
    



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
# print(f"sum({x}{y})={z}")
 

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
#     print("sum({},{})={}".format(a,b,c))

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
# a,b,c=addop() # Function Call with Multi Line assignment
# print("sum({},{})={}".format(a,b,c))
# print("---------------OR---------------------")
# res=addop() # Function Call with Single Line assignment
# #here res is an object of <class, tuple>
# print("sum({},{})={}".format(res[0],res[1],res[2]))
# print("-----------OR----------------")
# print("sum({},{})={}".format(res[-3],res[-2],res[-1]))


#*substraction of two number 
#! Approach1:funtion with return type with parameter
# def subop(a,b):
#     c=a-b
#     return c

# x=int(input("Enter a number :"))    
# y=int(input("Enter a number :"))    
# res=subop(x,y)
# print( f"Sub =>",res)

#! Approach2:funtion with not return type not parameter
# def subop():
#     x=int(input("Enter a number:"))
#     y=int(input("Enter a number:"))
#     z=x-y
#     print(f"sub =>",z)

# subop()   

#! Approach3:funtion not  return type with parameter

# def subop(a,b):
#     c=a-b
#     print("sub =>",c)
#
# x=int(input("Enter a number :"))    
# y=int(input("Enter a number :"))    
# subop(x,y)

#! Approach4:funtion with return type not  parameter

# def subop():
#     a=int(input("Enter  a number"))
#     b=int(input("Enter  a number"))
#     c=a-b
#     return c

# print(subop())
# # print(res)


#!Program for calculating area and perimeter of Square
#SquareAreaPeri.py
# def squarearea():
#     s=float(input("Enter Value of Side for Cal Area of Square:"))
#     sa=s**2
#     print("Area of Square={}".format(sa))

# def squareperi():
#     s = float(input("Enter Value of Side for Cal Perimeter of Square:"))
#     ps = 4*s
#     print("Perimeter of Square={}".format(ps))

# #Main Program
# squareperi()
# squarearea()
#!Program for calculating area and perimeter of Square

#!calculate simple intersted and total amount to pay
# si=p*r*t
# totalamt=si+p
#approach 1:function with return type and with parameter
#-----------------------------------
# def simpleint():
#     p=float(input("ENTER PRINCIPLE Amount : "))
#     r=float(input("ENTER RATE OF INTEREST : "))
#     t=float(input("ENTER TIME : "))
#     si=p*r*t
#     totalamt=si+p
#     print(f"Simple interest is {si}")
#     print(f"total amount is {totalamt}")
# simpleint()    


# def simpleint(p,r,t):
#      si=p*r*t
#      totalamt=si+p    
#      return si, totalamt

# p=float(input("ENTER PRINCIPLE Amount : "))
# r=float(input("ENTER RATE OF INTEREST : "))
# t=float(input("ENTER TIME : "))
# a,b=simpleint(p,r,t)     
# print(f"The simple interest is {a}")
# print(f"Total Amount is {b}")

#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def simpleint():
#        p=float(input("ENTER PRINCIPLE Amount : "))
#        r=float(input("ENTER RATE OF INTEREST : "))
#        t=float(input("ENTER TIME : "))    
#        si=p*r*t
#        totalamt=si+p
#        print(f"simple intrerst is {si}")
#        print(f"Total Amount is {totalamt}")
# simpleint()       

#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def simpleint(p,r,t):
#         si=p*r*t
#         totalamt=si+p
#         print(f"simple interest is {si}")
#         print(f"Total Amount is{totalamt}")

# p=float(input("ENTER PRINCIPLE Amount : "))
# r=float(input("ENTER RATE OF INTEREST : "))
# t=float(input("ENTER TIME : ")) 
# simpleint(p,r,t)

#approach 4:function with  return type and with no  parameter
#--------------------------------------------
# def simpleint():
#     p=float(input("ENTER PRINCIPLE Amount : "))
#     r=float(input("ENTER RATE OF INTEREST : "))
#     t=float(input("ENTER TIME : ")) 
#     si=p*r*t
#     totalamt=si+p
#     return si ,totalamt
# 
# a,b=simpleint()    
# print(f"simple interist is {a}")
# print(f"Total Amount is {b}")


# def simpleint():
#     p=float(input("ENTER PRINCIPLE Amount : "))
#     r=float(input("ENTER RATE OF INTEREST : "))
#     t=float(input("ENTER TIME : ")) 
#     si=p*r*t
#     totalamt=si+p
#     return si ,totalamt

# a=simpleint()    
# # print(f"simple interist is {a}")
# print(f"Simple interest {a[0]}  and Total Amount {a[1]}")

#!==========================================
#!area and perimeter of square
# area=side*side
# perimeter=4*side
#!==========================================

#approach 1:function with return type and with parameter
#-----------------------------------
# def area_square(side):
#     area=side*side
#     return area

# def perimeter_square(side):
#     perimeter=4*side
#     return perimeter

# x=int(input("Enter a side of square :"))

# res=area_square(x)
# print(f"Area of square is =>{res}")

# res=perimeter_square(x)
# print(f"perimeter of square is =>{res}")

#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def area_square():
#     side=int(input("Enter a side of square :"))
#     area=side*side
#     print(f"Area of square is {area}")

# def perimeter_square():
#     side=int(input("Enter a side of square :"))
#     perimeter=4*side
#     print(f"perimeter of square is {perimeter}")

# area_square()
# perimeter_square()

#approach 3:function with  no return type and with  parameter
#--------------------------------------------------

# def area_square(side):
#     area=side*side
#     print(f"Area of square is {area}")

# def perimeter_square(side):
#     perimeter=4*side
#     print(f"perimeter of the square is {perimeter}")

# x=int(input("Enter a side of square :"))
# area_square(x)

# perimeter_square(x)


#approach 4:function with  return type and with no  parameter
#--------------------------------------------
# def area_square():
#     side=int(input("Enter a side of square :"))
#     area=side*side
#     return area

# def perimeter_square():
#     side=int(input("Enter a perimeter of square:"))
#     perimeter=4*side
#     return perimeter
    
# res=area_square()    
# print(f"Area of square is {res}")

# res=perimeter_square()
# print(f"perimeter of the square {res}")


#!======================================
#! area and perimeter of triangle
# area = 1/2 * base * height
# perimeter = length + length + length
#!======================================
#approach 1:function with return type and with parameter
#-----------------------------------
# def area_triangle(base , height):
#     area=1/2* base*height
#     return area

# def perimeter_triangle(length):
#      perimeter = length + length + length
#      return perimeter

#  b=int(input("Enter a base:"))
# h=int(input("Enter a height:"))
# res =area_triangle(b,h)
# print(res)
# l=int(input("Enter a lenght of triangle "))
# var=perimeter_triangle(l)  
# print(f"perimeter of triangle is =>{var}")   

#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def area_triangle():
#     base=int(input("Enter a base:"))
#     height=int(input("Enter a height:"))
#     area=1/2* base*height
#     print(f"area of triangle :{area}")

# def perimeter_triangle():
#      length=int(input("Enter a lenght of triangle "))
#      perimeter = length + length + length
#      print(f"Perimeter of triangle is {perimeter}")

# area_triangle()
# perimeter_triangle()

#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def area_triangle(base, height):
#     area=1/2* base*height
#     print(f"area of triangle is {area}")

# def  perimeter_triangle(length):
#     perimeter = length + length + length
#     print(f"Perimeter of triangle is {perimeter}")

# l=int(input("Enter a lenght of triangle "))
# perimeter_triangle(l)

# b=int(input("Enter a base:"))
# h=int(input("Enter a height:"))
# area_triangle(b,h)


#approach 4:function with  return type and with no  parameter
#--------------------------------------------
# def area_triangle():
#     base=int(input("Enter a base:"))
#     height=int(input("Enter a height:"))
#     area=1/2* base*height
#     return area
# def perimeter_triangle():
#     length=int(input("Enter a length :"))
#     perimeter = length + length + length
#     return perimeter

# res1=perimeter_triangle()    
# print(f"perimeter of triangle is {res1}")
# res=area_triangle()    
# print(f" Area of triangle is {res}")
#?===========================================================================================
#! Calculate area of circle by using function 
#* AREA OF CIRCLE = 3.14*r*r
#?===========================================================================================
#* approach 1:function with return type and with parameter
#-------------------------------------------
# def  area_circle( r):
#      area = 3.14*r*r
#      return area

# x=int(input("Enter a radius :"))
# res=area_circle( x)
# print(f"Area of circle {res}")

#* approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def area_circle():
#     r=int(input("Enter a radius: "))
#     area=3.14*r*r
#     print(f"area of circle is {area}")

# area_circle()    

#* approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def area_circle(r):
#       area=3.14*r*r
#       print(f"area of circle is {area}")

# x=int(input("Enter a radius :"))
# area_circle(x)      

#* approach 4:function with  return type and with no  parameter
#--------------------------------------------
# def area_circle():
#     r=int(input("Enter a radius:"))
#     area=3.14*r*r
#     return area

# k=area_circle()    
# print(f"Area of circle {k}")

#?===========================================================================================
#!calculate area of Rectacgle by using fuction
#*AREA OF RECTANGLE = LENGTH * BREADTH
#?===========================================================================================
# *approach 1:function with return type and with parameter
#-------------------------------------------
# def area_rectangle(length,breadth):
#     area=length*breadth
#     return area
# x=int(input("Enter a length:"))    
# y=int(input("Enter a breadth:"))    
# res=area_rectangle(x,y)
# print(f"Area of restangle is {res} ")

#* approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def area_rectangle():
#     length=int(input("Enter a length:"))
#     breadth=int(input("Enter a breadth"))
#     area=length * breadth
#     print(f"Area of Rectagle {area}")

# area_rectangle()    

#* approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def area_rectangle(length , breadth):
#     area=length*breadth
#     print(f"Area of rectangle {area}")

# x=int(input("Enter a length :"))
# y=int(input("Enter a breadth :"))
# area_rectangle(x,y)    

#* approach 4:function with  return type and with no  parameter
#---------------------------------------------------
# def area_rectangle():
#     length=int(input("Enter a length: "))
#     breadth=int(input("Enter a breadth: "))
#     area=length*breadth
#     return area

# res=area_rectangle()    
# print(f"Area of rectangle is {res}")


#?=======================================================================================
#! Remove 10 from list harshal Question
# lst=[10,20,15,25,10,5,17,5]
# count=0
# for i in lst:
#     if i==10 or count==0:
#         count= count+1
#         if count==1:
#             continue
#     print(i)



#! PROGRAM WHICH WILL ACCPET WORD AND FIND IT IS PALINDEOME OR NOT
#* approach 1:function with return type and with parameter
#-----------------------------------
# def palindrome(word):

#     if(word==word[::-1]):
#         print("it is palindrome word")
#         return word
#     else:
#         print(" it is not a palindeome")
#         return word

# s=input("Enter a word :")
# res=palindrome(s)
# # print(res)

#* approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def palindrome():
#     word=input("Enter a word:")
#     if(word==word[::-1]):
#         print("it is palindeome")
#     else:    
#         print("It is Not palindeome")
# palindrome()        

#* approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def palindrome(word):
#     if(word==word[::-1]):
#         print("It is palindeome")
#     else:
#         print("It is Not palindeome") 
#    
# x=input("Enter a word ")        
# palindrome(x)

#* approach 4:function with  return type and with no  parameter
#--------------------------------------------
# def palindrome():
#     word=input("Enter a word ")
#     if(word==word[::-1]):
#         print("it is palindeome : ")
#         return word
#     else:
#         print("It is Not palindrome : ")    
#         return word
# res=palindrome()        
# # print("res")

#!Program for finding sum and average of list of values
#*SumAvgFunEx1.py
# def findsumavg():
#     n=int(input("Enter How Many Values u want to Enter:"))
#     if(n<=0):
#         print("{} is Invalid Input".format(n))
#     else:
#         lst=[]
#         for i in range(1,n+1):
#             value=int(input(f"Enter a {i} number:"))
#             lst.append(value)
#         print(lst)  
#         s=0  
#         for i in lst:

#             a=int(input("Enter a number :"))
#             b=int(input("Enter a number :"))
#             c=a+b
#             print(f"sum( {a} {b}) ={c} ")

#         print(s)
# findsumavg()

#
# def findsumavg():
#     n=int(input("Enter how many value you to generate :"))
#     if(n<=0):
#         print(f"{n} is invalid number :")
#     else:
#         lst=[]    
#         for i in range(1,n+1):
#             value=int(input("Enter a number :"))
#             lst.append(value)
#         else:
#             print("List of values :")
#             print(lst)    
#         s=0
#         for k in lst:
#             s=s+k
#         else:

#             print(f"sum = {s}")
#             # print(f"Avg = {s/n}")
#             print(f"Avg = {s/len(lst)}")

# findsumavg()

#approach 1:function with return type and with parameter
#-----------------------------------
# def findsumavg():
#     n=int(input("Enter how many value you want to generate :"))
#     if(n<=0):
#         print("Invalid input ")
#     else:
#         lst=[]    
#         for i in range(1,n+1):
#             value=int(input(f"Enter {i} number :"))
#             lst.append(value)
#         else:
#             print("List of value :")    
#             print(lst)

#         s=0
#         for k in lst:
#             s=s+k
#         else:
#             print(f"sum of list of value= {s}") 
#             print(f"Avg = {k/len(lst)} ")   
# findsumavg()            

#approach 1:function with return type and with parameter
#-----------------------------------------------------------------
# def findsumavg(lst):
#     s=0
#     for i in lst:
#         s=s+i
#     else:
#         return s   

# n=int(input("Enter how many value you wnat to genetare :"))
# if(n<=0):
#     print("Invalid input")
# else:
            
#     lst=[]
#     for i in range(1,n+1):
#         value=int(input("Enter a number :"))
#         lst.append(value)
#     else:
#         print("List of values :")    
#         print(lst)
# res=findsumavg(lst)
# print(f"Sum of list = {res}")


#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def findsumavg():
#     n=int(input("Enter a how many value to generate :"))
#     lst=[]
#     for i in range(1,n+1):
#         value=int(input(f"Enter a {i} number :"))
#         lst.append(value)
#     else:
#         print("List of values:")
#         print(lst)    
#         s=0
#     for i in lst:
#         s=s+i
#     else:
#         print("Sum of list",s)
#         print(f"Avg {s/len(lst)}")    

# findsumavg()

#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def findsumavg(lst):
#     s=0
#     for i in lst:
#         s=s+i
#     else:
#         print(f"Sum {s}")    


# n=int(input("Enter how many number you want to generate :"))
# lst=[]
# for i in range(1,n+1):
#     value=int(input(f"Enter a {i} number :"))
#     lst.append(value)
# else:
#     findsumavg(lst)

#approach 4:function with  return type and with no  parameter
#--------------------------------------------
# def findsumavg():
#     n=int(input("Enter how many number you want to generate :"))
#     lst=[]
#     for i in range(1,n+1):
#         value=int(input(f"Enter a {i} number :"))
#         lst.append(value)
#     else:
#         print("list of value :")
#         print(lst)
#     s=0
#     for i in lst:
#         s=s+i
#     else:
#         return s    

# res=findsumavg()
# print(f"sum of list = {res}")

#^=========================================================================================================
#!Program for Finding Length of each word and also find Highest length word
#*WordsLengthFunEx1.py
# def readvalues():
#     nov=int(input("Enter How Many Words u have:"))
#     if(nov<=0):
#         return ("{} is invalid input".format(nov))
#     else:
#         words=[]
#         for i in range(1,nov+1):
#             word=input("Enter {} Word:".format(i))
#             words.append(word)
#         else:
#             return words

# def findlengthwords(words): # words=['Python', 'Java', 'Hyderabad', 'Goa']
#     wordlen=dict() # create empty dict for getting word name as key and its length as value
#     for word in words:
#         wordlen[word]=len(word)
#     return wordlen

#^=========================================================================================================
# def highestlengthword(dictobj):
#     #the values from dict object by using values()
#     vals=dictobj.values()
#     mv=max(vals) # here max() is a general pre-defined function
#     print("-----------------------------------")
#     print("List of Max Length Word(s)")
#     print("-----------------------------------")
#     for key,value in dictobj.items():
#         if(value==mv):
#             print("\t{}".format(key))
#     else:
#         print("-----------------------------------")
# #Main Program
# res=readvalues()
# if (type(res)==str):
#     print(res)
# else:
#     WL=findlengthwords(res) # Function call sending list of words
#     highestlengthword(WL) # Function call sending Dict Object


#^=========================================================================================================
#!        sagar dada
#Program for Finding Length of each word and also find Highest length word
#WordsLengthFunEx1.py
# def readvalues():
#     nov=int(input("Enter How Many Words u have:"))
#     if(nov<=0):
#         return ("{} is invalid input".format(nov))
#     else:
#         lst=[]
#         for i in range(1,nov+1):
#             word=input("Enter {} Word:".format(i))
#             lst.append(word)
#         else:
#              return lst

# def findlengthwords(lst): 
#     wordlen=dict() 
#     for j in lst:
#         wordlen[j]=len(j)
#     return wordlen

# def highestlengthword(wordlen):
    
#     mv=max(wordlen.values()) 
#     print("List of Max Length Word(s)")
#     for key,value in wordlen.items():
#         if(value==mv):
#             print("\t{}".format(key))
# lst=readvalues()    
# if (type(lst)==str):
#     print(lst)
# else:
#     wordlen=findlengthwords(lst) # Function call sending list of lst
#     highestlengthword(wordlen) # Function call sending Dict Object


#^=========================================================================================================
# def readvalues():
#     n=int(input("Enter a number :"))
#     lst=[]
#     for i in range(1,n+1):
#         values=input("Enter a word :")
#         lst.append(values)
#     else:
#         return lst   
# def findlengthwords(lst):
#     wordlen=dict()     
#     for j in lst:
#         wordlen[j]=len(j)
#     else:
#         return wordlen
    
# def highestlengthword(wordlen):
#     value= wordlen.values()       
#     mv=max(value)
#     for key ,value in wordlen.items():
#         if(value==mv):
#             # print(key)
#             return  key  

    
# res=readvalues() 
   
# wordlen=findlengthwords(res)
# kunal=highestlengthword(wordlen)    
# print(kunal)

#^=========================================================================================================



# def readvalues():
#     n=int(input("Enter a number :"))
#     lst=[]
#     for i in range(1,n+1):
#         values=input("Enter a word :")
#         lst.append(values)
#     else:
#         return lst   
# def findlengthwords(lst):
#     wordlen=dict()     
#     for j in lst:
#         wordlen[j]=len(j)
#     else:
#         return wordlen
    
# def highestlengthword(wordlen):
#     value= wordlen.values()       
#     mv=max(value)
#     for key ,value in wordlen.items():
#         if(value==mv):
#             # print(key)
#             return  key  

    
# res=readvalues() 
   
# wordlen=findlengthwords(res)
# key=highestlengthword(wordlen)    
# print(key)

#^=========================================================================================================
# def readvalues():
#     n=int(input("Enter a how many many number to genetare :"))
#     lst=[]
#     for i in range(1,n+1):
#         value=input("Enter a  word :")
#         lst.append(value)
#     return lst 

# def findlengthwords(lst):
#     wordlen=dict()
#     for j in lst:
#         wordlen[j]=len(j)
#     return wordlen    
# def highestlengthword(wordlen):
#    val=wordlen.values()
#    mv=max(val)

#    for key,value in wordlen.items():
#       if(value==mv):
#         print(key)



# lst=readvalues()
# wordlen=findlengthwords(lst)
# lst=highestlengthword(wordlen)    
#^=========================================================================================================

#?==========================================================================
#!write a program which will accept list of word and find the least length word

# def readvalues():
#     lst=[]
#     n=int(input("Enter a how many number you want to generate :"))
#     for i in range(1,n+1):
#         value=input("Enter a word :")
#         lst.append(value)
#     return lst 
#   
# def findlengthwords(lst):
#     wordlen=dict()    
#     for j in lst:
#         wordlen[j]=len(j)
#     return wordlen   
#  
# def highestlengthword(wordlen):
#     val=wordlen.values()
#     mv =min(val)
#     for key ,value in wordlen.items():
#         if(value==mv):
#             print(key)
    

# lst=readvalues()
# wordlen=findlengthwords(lst)
# highestlengthword(wordlen)

#?==============================================================
#!write a program which will accept line of text and get the reverse of the word/sentense at the same place
#*python is an oop lang
#*nohtyp si poo gnal
#?==============================================================
# def readvalue():
#     n=int(input("Enter a how many number you want :"))
#     lst=[]
#     for i in range(1,n+1):
#         value=input("Enter a word :")
#         lst.append(value)
#     return lst

# def findlengthwords(lst):
#     wordlen=dict()
#     for i in lst:
#         wordlen[i]=

# lst=readvalue()

# print("Execute program")


# def readvalue():
#     n=int(input("Enter a how many number you want :"))
#     lst=[]
#     for i in range(1,n+1):
#         value=input("Enter a word :")
#         lst.append(value)
#     return lst

# def findlengthwords(lst1):
#     # wordlen=dict()'
#     for k in lst:
#         lst1[k].reverse()
#     return str(lst1[k])
  

# lst=readvalue()
# k=findlengthwords(lst)
# print(k)

# print("Execute program")












#!Program for Finding Length of each word and also find Highest length word
#*WordsLengthFunEx1.py
#-----------------------------------
#approach 1:function with return type and with parameter
# def readvalue():
#     lst=[]
#     n=int(input("Enter a how many number you want to generate :"))
#     for i in range(1,n+1):
#         value=input(f"Enter a {i} words :")
#         lst.append(value)
#     return lst   
 
# def findlengthwords(lst):  
#     wordlen=dict()
#     for j in lst:
#         wordlen[j]=len(j)
#     return wordlen

# def highestlengthword(wordlen):
#     val=wordlen.values()
#     mv=max(val)
#     for key ,value in wordlen.items():
#         if(value==mv):
#             print(key)
# #main program
# lst=readvalue()

# wordlen=findlengthwords(lst)

# highestlengthword(wordlen)

#approach 1:function with return type and with parameter
#-----------------------------------------------
# def readvalue(n):
#     return lst

# def findlengthword(lst):
#     wordlen=dict()
#     for j in lst:
#         wordlen[j]=len(j)
#     return wordlen
# def highestlengthword(wordlen):  
#     val=wordlen.values()
#     mv=max(val)

#     for key ,value in wordlen.items():
#         if(value==mv):
#             print(key)

# lst=[]
# n=int(input("Enter a how many numnber you want to generate :"))
# for i in range(1,n+1):
#     value=input("Enter a word :")
#     lst.append(value)
# lst=readvalue(n)
  
    
# wordlen=findlengthword(lst)
# highestlengthword(wordlen)


#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# lst=[]
# word_length={}
# def readvalue():
#     n=int(input("Enter a how many number you want to generate :"))
#     for i in range(1,n+1):
#         value=input(f"Enter a {i} word :")
#         lst.append(value)
#     else:
#         print(lst)

# def findlengthword(lst):

#     for j in lst:
#         word_length[j]=len(j)
        
#     print(word_length)

# def highestlengthword(dict):
#     val=word_length.values()           
#     mv=max(val)
#     for key,value in word_length.items():
#         if(value==mv):
#             print(key)

# readvalue()
# findlengthword(lst)
# highestlengthword(word_length)

#approach 3:function with  no return type and with  parameter
#-----------------------------------------------


#approach 4:function with  return type and with no  parameter
#-----------------------------------------------

#! with the help of isinstance function 
# def readvalue():
#     n=int(input("Enter a how many number you want to generate: "))
#     if(n<=0):
#         return("Invalid input")
#     else:
                
#         lst=[]
#         for i in range(1,n+1):
#             value=input(f"Enter a {i} word :")
#             lst.append(value)
#         return lst      

# def findlengthword(lst):
#         wordlen=dict()
#         for j in lst:
#             wordlen[j]=len(j)

#         return wordlen

# def highestlengthword(wordlen):
#         val=wordlen.values()
#         mv=min(val)
#         for key ,value in wordlen.items():
#             if(value==mv):
#                 print(key,value)
# # lst=readvalue()
# lst=readvalue()

# if isinstance(lst, str):
#     print(lst)
# else:
#     wordlen=findlengthword(lst)
#     highestlengthword(wordlen)

#!  
# def readvalue():
#     n=int(input("Enter a how many number you want to generate: "))
#     if(n<=0):
#         return("Invalid input")
#     else:
                
#         lst=[]
#         for i in range(1,n+1):
#             value=input(f"Enter a {i} word :")
#             lst.append(value)
#         return lst      

# def findlengthword(lst):
#         wordlen=dict()
#         for j in lst:
#             wordlen[j]=len(j)

#         return wordlen

# def highestlengthword(wordlen):
#         val=wordlen.values()
#         mv=min(val)
#         for key ,value in wordlen.items():
#             if(value==mv):
#                 print(key,value)
# # lst=readvalue()
# lst=readvalue()

# if isinstance(lst, str):
#     print(lst)
# else:
#     wordlen=findlengthword(lst)
#     highestlengthword(wordlen)
    

#^ 
# def readvalue():
#     n=int(input("Enter a how many number you want to generate: "))
#     while(n<0):
#         print("invalid input")
#         n=int(input("Enter a how many number you want to generate: "))

#         lst=[]
#         for i in range(1,n+1):
#             value=input(f"Enter a {i} word :")
#             lst.append(value)
#         return lst      

# def findlengthword(lst):
#         wordlen=dict()
#         for j in lst:
#             wordlen[j]=len(j)

#         return wordlen

# def highestlengthword(wordlen):
#         val=wordlen.values()
#         mv=min(val)
#         for key ,value in wordlen.items():
#             if(value==mv):
#                 print(key,value)
# # lst=readvalue()
# lst=readvalue()

# # if(type(str)==lst):
# #     print(lst)
# # else:
# wordlen=findlengthword(lst)
# highestlengthword(wordlen)










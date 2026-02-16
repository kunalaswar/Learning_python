# def sumop(a,b):
#     c=a+b
#     return c

# res=sumop(5,10)
# print("sum =>",res)

#!Normal function
# def sumop(a,b): #^function defination
#     c=a+b
#     return c

#*main program
# x,y=int(input("Enter a first value : ")),int(input("Entre  a second value : "))    
# res=sumop(x,y) #^function call
# print("sum => ",res)

#! Working with Anonymous OR Lambda Functions
#* There is no return keyword of this lambda function
# sumop=lambda a,b: a+b  #^ function defination

#*main program
# res=sumop(5,10) #^function call
# print("sum =>",res) 




#!Program for cal addition of Two Numbers by using Anonymous Functions
#*AnonymousFunEx1.py
# def sumop(a,b):
#     c=a+b
#     return c
# #!lambda function
# sumop=lambda a,b:a+b

# x,y=int(input("Enter a first number for normal fun : ")),int(input("Enter a second number for normal fun :"))
# res=sumop(x,y)    
# print("sum =>",res)
# k,v=int(input("Enter a first number for  fun :")),int(input("Entre a second number for  fun : "))
# res=sumop(k,v)
# print("sum =>",res)


# subop=lambda a,b:a-b

# #main p 
# x,y = int(input("Entre : ")),int(input("Entre : "))
# res=subop(x,y)
# print("substraction => ",res)







#!Program for performing Different types of Arithmetic Operations by using Anonymous Function
#*AnonymousFunEx2.py

# from operator import floordiv

# def arithmenu():
#     print("=" * 50)
#     print("\tArithmetic Operations")
#     print("=" * 50)
#     print("\t1. Addtion")
#     print("\t2. Substration")
#     print("\t3. Multiplication")
#     print("\t4. Division")
#     print("\t5. Floor Division")
#     print("\t6. Modulo Division")
#     print("\t7. Exponentiation")
#     print("\t8. Exit")
#     print("=" * 50)

# #Anonymous Functions Definition
# addop=lambda k,v: k+v
# subop=lambda k,v: k-v
# mulop=lambda a,b: a*b
# divop=lambda k,v: k/v
# floordivop=lambda k,v: k//v
# modop=lambda k,v:k%v
# powop=lambda k,v: k**v


# #Main Program
# while(True):
#     arithmenu()
#     ch=int(input("Enter Ur Choice:"))
#     match(ch):
#         case 1:
#             print("Enter Two Values for addition")
#             a, b = float(input()), float(input())
#             res1 = addop(a, b)  # Anonymous  Function Call
#             print("\tsum({},{})={}".format(a,b,res1))
#         case 2:
#             print("Enter Two Values for Substraction")
#             a, b = float(input()), float(input())
#             res1 = subop(a, b)  # Anonymous  Function Call
#             print("\tsub({},{})={}".format(a, b, res1))
#         case 3:
#             print("Enter Two Values for Multiplication")
#             a, b = float(input()), float(input())
#             res1 = mulop(a, b)  # Anonymous  Function Call
#             print("\tmul({},{})={}".format(a, b, res1))
#         case 4:
#             print("Enter Two Values for Normal Div")
#             a, b = float(input()), float(input())
#             res1 = divop(a, b)  # Anonymous  Function Call
#             print("\tdiv({},{})={}".format(a, b, res1))
#         case 5:
#             print("Enter Two Values for Floor Div")
#             a, b = float(input()), float(input())
#             res1 = floordiv(a, b)  # Anonymous  Function Call
#             print("\tsum({},{})={}".format(a, b, res1))
#         case 6:
#             print("Enter Two Values for Mod Div")
#             a, b = float(input()), float(input())
#             res1 = modop(a, b)  # Anonymous  Function Call
#             print("\tmod({},{})={}".format(a, b, res1))
#         case 7:
#             a, b = float(input("Enter Base:")), float(input("Enter Power:"))
#             res1 = powop(a, b)  # Anonymous  Function Call
#             print("\tpow({},{})={}".format(a, b, res1))

#         case 8:
#             print("Thx for using this program")
#             break
#         case _:
#             print("Ur Selection of Operation is wrong-try again")

#!program 
# def arithmenu():
#     print("=" * 50)
#     print("\tArithmetic Operations")
#     print("=" * 50)
#     print("\t1. Addtion")
#     print("\t2. Substration")
#     print("\t3. Multiplication")
#     print("\t4. Division")
#     print("\t5. Floor Division")
#     print("\t6. Modulo Division")
#     print("\t7. Exponentiation")
#     print("\t8. Exit")
#     print("=" * 50)

# #Anoymous function Defination
# addop=lambda k,v: k+v
# subop=lambda k,v: k-v
# mulop=lambda a,b: a*b
# divop=lambda k,v: k/v
# floordivop=lambda k,v: k//v
# modop=lambda k,v:k%v
# powop=lambda k,v: k**v


# while(True):
#     arithmenu()
#     ch =int(input("Entre a choice :"))
#     match(ch):
#         case 1:
#             x,y=int(input("Entre a first num :")),int(input("Entre a first num :"))
#             res1=addop(x,y)
#             print(f"sum = {res1}")
#         case 2:
#             x,y=int(input("Entre a first num :")),int(input("Entre a first num :"))
#             res=subop(x,y)
#             print(f"sub = {res}")
#         case 3:
#             x,y=int(input("Entre a first num :")),int(input("Entre a first num :"))
#             res=mulop(x,y)
#             print(f"mul = {res}")
#         case 4:
#             x,y=int(input("Entre a first num :")),int(input("Entre a first num :"))
#             res=divop(x,y)
#             print(f"Division = {res}")       
#         case 5:    
#             x,y=int(input("Entre a first num :")),int(input("Entre a first num :"))
#             res=floordivop(x,y)
#             print(f"Floor division= {res}")
#         case 6:
#             x,y=int(input("Entre a first num :")),int(input("Entre a first num :"))
#             res=mudop(x,y)
#             print(f"modulus = {res}")    
#         case 7:
#             x,y=int(input("Entre a first num :")),int(input("Entre a first num :"))
#             res=powop(x,y)
#             print(f"power of  = {res}")    
#         case 8:
#            print("Thank for using program !")
#            break
#         case _:
#             print("wrong input you selected Try- Again")   

#?================================================================================================

#!Program for finding Biggest of Three Nums by using Anonymous Functions
#*AnonymousFunEx3.py

# findbig=lambda k,v,r: k if k>=v and k>r else v if v>k and v>=r else r if r>=k and r>v else "ALL VALUES ARE EQUAL"

# #Main Program
# print("Enter Three Numbers:")
# a,b,c=float(input()),float(input()),float(input())
# res=findbig(a,b,c) # Anonymous Function Call
# print("Big({},{},{})={}".format(a,b,c,res))

# findbig=lambda k,v,r:k if k>=v and k>r else v if v>k and v>=r else r if r>=k and r>v else "All value are Equal"

# a,b,c=int(input("Enter first value")),int(input("Enter second value")),int(input("Enter third value"))
# res=findbig(a,b,c)
# print("Big value =",res)




#?================================================================================================
#!Program for finding Biggest of Three Nums by using Anonymous Functions
#*AnonymousFunEx4.py

# findbig=lambda k,v,r:k if v<=k>r else v if k<v>=r else r if k<=r>v else "ALL VALUES ARE EQUAL"

# #Main Program
# print("Enter Three Numbers:")
# a,b,c=float(input()),float(input()),float(input())
# res=findbig(a,b,c) # Anonymous Function Call
# print("Big({},{},{})={}".format(a,b,c,res))

#!program
# findbig=lambda k,v,r: k if v<=k>r else v if r<=v>k else r if k<=r>v else "All value are equal"

# print("Entre a three value")
# a,b,c=int(input()),int(input()),int(input())
# res=findbig(a,b,c)
# print("Big =",res)

#?================================================================================================
#! PROGRAM FOR CALCULATING AREA OF DIFFRENT FIGURES LIKE CIRCLES , RECTANGLE ,SQUARES AND TRAINGLE

# def areamenu():
#      print("""
                  
#               1. CIRCLE 
#               2. RECTANGLE 
#               3. SQUARE
#               4. TRAINGLE
#               5. EXIT 
           
# """)
# circle=lambda r: 3.14*r*r      
# rect=lambda l, b : l*b 
# square=lambda s:s*s
# triangle=lambda b,h:0.5*b*h

# while(True):
#       areamenu()
#       ch=int(input("Entre a choice :"))
#       match(ch):
#             case 1:
#                   r=int(input("Entre  a radius :"))
#                   area=circle(r)
#                   print("area of circle ",area)
#                   print("*"*20)

#             case 2:
#                   l,b=int(input("Entre length : ")),int(input("Entre breadth :"))
#                   area=rect(l,b)
#                   print("Area of rectangle=",area)
#                   print("*"*20)
#             case 3:
#                   s=int(input("Enter a side "))      
#                   side=square(s)
#                   print("square of area = ",side)
#                   print("*"*20)
#             case 4:
#                   b,h=int(input("Entre a base")),int(input("Entre height"))      
#                   area=triangle(b,h)
#                   print(" Area of triangle=",area)
#                   print("*"*20)
#             case _:
#                   print("Invalid input Try- again")      
#                   print("*"*20)


#^ --------------------------------------------------------------------------------------------
#! PROGRAM FOR CALCULATING DIFFRENT TEMPRATURE CONVERSION USING ANONYMOUS FUNCTION 

# def temeraturemenu():
#       print(
#         """
#         1. Celsius to Fahrenheit 
#         2. Fahrenheit to Celsius
#         3. Celsius to Kelvin
#         4. Kelvin to Celsius
#         5. Fahrenheit to Kelvin:
#         6. Kelvin to Fahrenheit
#         """)
# C_F=lambda c : (9/5) * c + 32
# F_C=lambda f : (5/9) * (f - 32)
# C_K=lambda c : c + 273.15
# K_C=lambda k : k - 273.15
# F_K=lambda f : (5/9) * (f - 32) + 273.15
# K_F=lambda k :  (9/5) * ( - 273.15) + 32

# while(True):
#       temeraturemenu()
#       ch=int(input("Entre a your choice :"))      
#       match(ch):
#             case 1:
#                   c=int(input("Entre a Celsius : "))
#                   res = C_F(c)
#                   print("Fahrenheit ",res)
#                   print("*"*50)
#             case 2:
#                 f=int(input("Entre a Fahrenheit :"))      
#                 res = F_C(f)
#                 print("celsius",res)
#                 print("*"*50)
#             case 3:
#                 c=int(input("Entre a celsius :"))
#                 res=C_K(c)
#                 print("Fahrenheit  ",res)
#                 print("*"*50)
#             case 4:
#                 k=int(input("Enter kelvin :"))    
#                 res=K_C(k)
#                 print(res)
#                 print("*"*50)
#             case 5:
#                 f=int(input("Enter a Fahrenheit "))    
#                 res=F_K(f)
#                 print("Fahrenheit ",res)
#                 print("*"*50)
#             case _:
#                 print("Invalid input please Try-again")    
#                 print("*"*50)
                
#?====================================================================================================

#! write a program to find Smallest among three value
# var1=lambda a,b,c:a if a<b and a<=c else b if b<a and b<=c else c if c<=a and c<b else "all value are equal"

# a,b,c=int(input("Enter a first value")),int(input("Enter a first value")),int(input("Enter a first value"))
# res=var1(a,b,c)
# print("Smallest value = ",res)

#?====================================================================================================

#! write a program which will find biggest and smallest of two numerical value
# bv=lambda a,b: a if a>b else b if b>a else "both are equal"
# sv=lambda a,b: a if a<b else b if b<a else "both are equal"

# a=int(input("Entre a number :"))
# b=int(input("Entre a number :"))
# big=bv(a,b)
# print("Big value =",big)

# small=sv(a,b)
# print("small value =",small)


#! 





































































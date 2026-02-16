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
# # ------------------------------------
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
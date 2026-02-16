# from Division import divop
# from NumberDivisionError import NumberDivisionError
# try:
#     a=int(input("enter a first number "))
#     b=int(input("enter a second number "))
#     try:
#         res=divop(a,b) #function call ---gives either Result or exception  EXCEPTION CREATING STATEMENT
#     except:
#         print("\tDONT ENTER ZERO FOR DEN...")

#     else:
#         print(res)
# except ValueError:
#     print("\tDon't enter alnum ,str and Digits !")
    
            
from Division import mutli
from NumberDivisionError import NumberDivisionError

a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
c=multi(a,b)
print(c)


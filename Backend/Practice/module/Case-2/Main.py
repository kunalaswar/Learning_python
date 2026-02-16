from menu import menu
from circle import Circlearea
from square import squarearea
from rect import area
menu()
n=int(input('Enter your choice :'))
# match(n):
#     case 1:
#         area()
#     case 2:    
#         Circlearea()
#     case 3:    
#         squarearea()
#     case _:
#         print("U choice of input is Wrong ")    

#!with the help of if... elif...
if n==1:
    area()
elif n==2:
    Circlearea()    
elif n==3:
    squarearea()    
else:
    print(" Invalid input Please try again")    


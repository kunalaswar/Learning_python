from AopMenu import menu
from Aopimplementation import sumop,subop,mulop,divop,Modulodivop,Expoentiationop
n=int(input("Enter your Choice :"))
match(n):
    case 1:sumop()
    case 2:subop()
    case 3:mulop()
    case 4:divop()
    case 5:Modulodivop()
    case 6:Expoentiationop()
    case 7:print("thx for using this program")
    case _:
        print("U input choice is not proper :")
menu()
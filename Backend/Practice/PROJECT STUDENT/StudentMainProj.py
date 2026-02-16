from StudentMenu import menu
from StudentAdd import savestuddata
from StudentViews import getallrecords ,getrecord

while(True):
    menu()
    try:
        ch=int(input("Enter your Choice :"))
        match(ch):
            case 1:
                savestuddata()
            case 2:
                getallrecords()
            case 3:
                getrecord()
            case 4:pass
            case 5:pass
            case 5:pass
            case 6:pass
            case 7:
                print("Tnx for your this APP")
                break
            case _:
                print("U your Selection operation is wrong -Try again")
    except ValueError:
        print("Dont Enter Str Alnum and Symbols ")            
        




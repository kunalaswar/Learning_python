from StudentMenu import menu
from StudentAdd import addstudentrecord
from StudentViews import getallrecords ,getrecord
from StudentDelete import deleterecord
from StudentUpdate import updaterecord
from StudentSearch import searchrecord

while(True):
    menu()
    ch=int(input("Enter a choice here:"))
    match (ch):
        case 1:
            addstudentrecord()  
             
        case 2:
            getallrecords()
		    
        case 3:
              getrecord()       
        case 4:
            deleterecord()    
        case 5:
            updaterecord()    
        case 6:
            searchrecord()  
        case 7:
            print("INVALID INPUT your input not in CHOICE ") 
            break      


    

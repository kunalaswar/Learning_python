from NameExcept import InvalidNameError,ZerolengthError,SpaceNameError
from NameValidation import validation
try:
    name=input("Enter a your Name :")
    res=validation(name)
except InvalidNameError:
    print("Invalid Name ---Try Again")
except ZerolengthError:
    print("Try to Enter your Name")
except SpaceNameError:
    print("Dont Enter  a space Enter properly ")   
    
else:
    print(f"{name} is valid Name ")


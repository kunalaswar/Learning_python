from MulExcept import ZeroError,NegativeNumberError
from Multable import table

try:
    num=int(input("Enter a number for table :"))
    res=table(num)
except (ZeroError,NegativeNumberError,ValueError):
    print("\tDont Enter Zero ")
    print("\tDont Enter str,special ")
    print("\t Dont Enter Negative Number ")
else:
    
    print(res)
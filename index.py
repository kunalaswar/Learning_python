# print("Hello Python")
from sys import argv 
print(type(argv))
print("Number of command line args",len(argv))
print("the List of command line args",argv)
for val in argv:
    print(val)
    
    
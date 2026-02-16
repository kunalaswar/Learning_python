a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
d = int(input("Enter a number : "))

if(a>b)&(a>c):
 print(f"{a} is greater ")
elif(b>c)&(b>d):
   print(f"{b} is greater ")
elif(c>d)&(c>a):
    print(f"{c} is greater ")
else:
    print(f"{d} is greater ")            
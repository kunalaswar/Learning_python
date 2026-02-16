# def greatest(a, b, c):
#     if(a>b or a>c):
#         print(f"the greater number is:  {a}")
#     elif(b>c or b>c):
#         print(f"the greater number is:  {b}") 
#     else:
#         print(f"the greater number is:  {c}")        

# # greatest(5,100,0)
# print(greatest(5,100,0))

# def greatest(a, b, c):
#     if(a>b or a>c):
#         return a
#     elif(b>c or b>c):
#         return b
#     elif(c>a or c>b):
#         return c

# a=1
# b=2
# c=3    
    
# print(greatest(a, b, c)) 
   
a =int(input("Enter a number : "))
b =int(input("Enter a number : "))
c =int(input("Enter a number : "))
if(a>b and a>c):
    print(f"the greater number is:  {a}")
elif(b>c and b>c):
    print(f"the greater number is:  {b}") 
else:
    print(f"the greater number is:  {c}")



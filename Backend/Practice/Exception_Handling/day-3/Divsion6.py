try:
    s1=input("Enter a number: ")
    s2=input("Enter a number: ")
    a=int(s1)   
    b=int(s2)   
    c=a/b
except ValueError as ve:
    print(ve)

except ZeroDivisionError as z:
    print(z)
else:
    print("First value",a)
    print("Second value",b)
    print("Div = ",c)    
finally:
    print("-------------finally-------------")



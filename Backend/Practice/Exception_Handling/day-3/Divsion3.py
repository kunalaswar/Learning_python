try:
    s1=input("Enter a first value :")
    s2=input("Enter a second value :")
    a=int(s1)
    b=int(s2)
    c=a/b
except (ValueError,ZeroDivisionError):
    print("Dont enter a almun special symbol or pure str")    
    print("Dont Enter a zero for DEN...")    
else:
    print(c)
finally:
    print("I am finally block !!!")    
try:
    s1=input("Enter first number :")
    s2=input("Enter second number :")
    a=int(s1)
    b=int(s2)
    c=a/b
    # print("Div = ",c) 
except ValueError:
    print("Dont's Enter alnum or special symbol")    
except ValueError:
    print("Dont's Enter alnum or special symbol")    
except ZeroDivisionError:
    print("Dont's Enter a Zero in DEN.......")    
else:
      print("Div = ",c)     

finally:
    print("I am always Executed I am finally block !")
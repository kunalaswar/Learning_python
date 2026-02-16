# #todo -  This is not a proper code to write exception

try:
    s1=input("Enter a number :")
    s2=input("Enter a number :")
    a=int(s1)
    b=int(s2)
    c=a/b

except :
    print("Oooop some thing Went wrong ") 
else:
    print("Div = ",c)

finally:
    print("-------------finally--------------------")

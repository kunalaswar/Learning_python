
#!Program for Finding Square for Every Value of list of values
#*DictComprehensionEx1.py
# lst=[3,13,12,9,17,4,3]
# d={val:val**2 for val in lst }
# print(d,type(d))

# lst=[3,13,12,9,17,4,3]
# d = { val : val**2 for val in lst }
# print(d,type(d))



#!program for Finding Square Root for +Ve Numbers from List of Numerical Values
#*DictComprehensionEx2.py

# print("Enter List of Values separated by comma:")
# sqrtvals={float(val):round(float(val)**0.5,2)  for val in input().split(",")  if float(val)>0 }
# print("="*50)
# print("Given Value\t\tSquareRoot Value")
# print("="*50)
# for val1,val2 in sqrtvals.items():
#     print("\t{}\t\t{}".format(val1,val2))
# print("="*50)

# sqrtvals={int(val):round(int(val)**0.5,2) for val in input("Enter list of values seperated by comma").split(",") if(int(val)>0)}
# print(sqrtvals)
# print("Given Value\tSquareRoot Value")
# for val1,val2 in sqrtvals.items():
#     print(f"{val1}--->\t\t\t{val2}")















































































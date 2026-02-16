  #! Write a python program which will read Emp details from keyboard save then i file as record ---BY using pickling
  #^---------------------------------------------------------------------------------------------------

import pickle  
with open("D:\\PYTHON FULL STACK\\Practice\\Files\\Pickling-unPickling\\emp.pick","ab") as fp:
  try:  
    empno=int(input("Enter a number :"))
    empname=input("Enter your name :")
    empsalary=float(input("Enter your salary :"))
    lst=[]
    lst.append(empno)
    lst.append(empname)
    lst.append(empsalary)
    pickle.dump(lst, fp)
  except FileNotFoundError:
    print("FILE NOT FOUND ERROR :")  
print("EMPDATA saved in file succeccfully")


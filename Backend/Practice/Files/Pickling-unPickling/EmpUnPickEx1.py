  #!write a python program which will read the record from Emp file  ---BY using Unpickling Operation
  #^--------------------------------------------------------------------------------------------------
import pickle
with open("emp.pick","rb") as fp:
  while(True):
    try:
      record=pickle.load(fp)
      print(record)
    except EOFError:
      break
      
    
    








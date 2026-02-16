# #!program for creating the file in Write mode  
try:
    fp=open("stud1.data","w")
   
except FileExistsError:
    print("File is Exist ")    
else:
    print("file is create and open in write mode")
    print(fp,type(fp))    


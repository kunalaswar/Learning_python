# # #! program for writing the  data in the file
# #Program for Writing the Data to the File----write()
# #FileWriteEx1.py  #! with the a mode is to give data Append
# try:
        
#     fp=open("stud11.data","a")
   
# except TypeError:
#     print("Dont's Enter data in int,float BE like a programmer")    
# else:

#     fp.write("harshal\t")
#     fp.write("aniket\t")
#     fp.write(str(200)+"\n")
#     print("Data written to the file ---Verify your file ")
#     fp.close()

            #^with open() as
# #! program for writing the  data in the file
#Program for Writing the Data to the File----write()
#FileWriteEx1.py  #! with the a mode is to give data Append
try:
        
    with open("stud11.data","a") as fp:
        fp.write("harshal\t")
        fp.write("aniket\t")
        fp.write(str(200)+"\n")
        print("Data written to the file ---Verify your file ")
    
except TypeError:
    print("Dont's Enter data in int,float BE like a programmer")    

    
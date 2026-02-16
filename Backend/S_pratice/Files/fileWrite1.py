# # #! program for writing the  data in the file
# #Program for Writing the Data to the File----write()
# #FileWriteEx1.py  #! with the w mode is to give data Overlapped
# try:
        
#     fp=open("stud11.data","w")
   
# except TypeError:
#     print("Dont's Enter data in int,float BE like a programmer")    
# else:
#     # fp.write("kunal aswar"+"\t")
#     # fp.write("harshal kharabe\t")
#     # fp.write("aniket paa\t")
#     # fp.write(str(100)+"\n")
#     fp.write("kunal "+"\t")
#     fp.write("harshal\t")
#     fp.write("aniket\t")
#     fp.write(str(200)+"\n")
#     print("Data written to the file ---Verify your ")
#     fp.close()

            #^with open() as
# #! program for writing the  data in the file
#Program for Writing the Data to the File----write()
#FileWriteEx1.py  #! with the w mode is to give data Overlapped
try:
        
    with open("stud11.data","w") as fp:
        # fp.write("kunal aswar"+"\t")
        # fp.write("harshal kharabe\t")
        # fp.write("aniket paa\t")
        # fp.write(str(100)+"\n")
        fp.write("kunal "+"\t")
        fp.write("harshal\t")
        fp.write("aniket\t")
        fp.write(str(200)+"\n")
        print("Data written to the file ---Verify your ")
   
except TypeError:
    print("Dont's Enter data in int,float BE like a programmer")    

   
# # #! How to open a file 
# try:
#     fp=open("stud3.data","r") #* r mode is default mode We write it or not write it
   
# except FileNotFoundError:
#     print("File Does not Exist----------- ")

# else:
#     print("files open in read moad in Current directory or folder")
#     print("open file in read mode ")
#     print("Is File closed =",fp.closed)

# finally:
#     print("I am finally block ")
#     print("Is File closed in finally block ",fp.closed)
#     fp.close()
#     print("Is File closed in finally block ",fp.closed)
    

#!
#! How to open a file 
try:
    fp=open("stud3.data","r") #* r mode is default mode We write it or not write it
   
except FileNotFoundError:
    print("File Does not Exist----------- ")

else:
    print("files open in read moad in Current directory or folder")
    print("open file in read mode ")
    print("Is File closed =",fp.closed)

finally:
    print("I am finally block ")
    try:
        print("Is File closed in finally block ",fp.closed)
        fp.close()
        print("Is File closed in finally block ",fp.closed)
    except:
        print("file is UNABLE to open there is no need to CLOSED the file")
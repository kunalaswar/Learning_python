# #! Program 1

# try:
#     fp=open("stud.data","r")
#     print(fp)
# except FileNotFoundError:
#     print("File Not found ")    
#^----------------------------------------------------------------------------------------------------
#!program 2

# try:
#     # fp=open("stud1.data","r")
#     fp=open("stud3.data","r")
    
# except FileNotFoundError:
#     print("file Not found")

# else:
#     print(fp)
#     print("File Opened in Read mode")    
#     print("Is file closed :",fp.closed)
# finally:
#     print("I am finally  block")  
#     try:  
#         print("Is File is closed in finally block :",fp.closed)
#         fp.close()
#         print("Is File is closed in finally block :",fp.closed)
#     except NameError:
#         print("File is Not present")
#         print("File unable to open --there is no need to close")

#^----------------------------------------------------------------------------------------------------

# try:
#     with open("D:\\PYTHON FULL STACK\\Practice\\Files\\FileOpen\\stud.data","r") as fp:
#         print("IS FILE IS OPEN IN WHICH MODE = ",fp.mode)
#         print("IS FILE IS READABLE = ",fp.readable())
#         print("IS FILE IS WRITEABLE = ",fp.writable())
#     print("file open in read mode = ",fp.closed)            

# except FileExistsError:
#     print("File Already Exist ")        

# finally:
#     print("I AM FINALLY BLOCK ")
#     print("Finally block not to write in it ")



#^----------------------------------------------------------------------------------------------------
try:
    with open("D:\\PYTHON FULL STACK\\Practice\\Files\\FileOpen\\stud.data","r") as fp:
        print("FILE OF THIS NAME = ",fp.name)
        print("FILE OF THIS MODE = ",fp.mode)
        print("IS THIS FILE IS READABALE = ",fp.readable())
        print("IS THIS FILE IS WRITEABLE = ",fp.writable())
except FileNotFoundError:
    print("FILE IS NOT FOUND ")



# from socket import *
# # import socket
# def kunal():
#     host = gethostname()
#     # host = "localhost"
#     # print(host)
#     port = 8088
#     s = socket()
#     s.binds((host,port))
#     print("Server is Running ")
#     s.listen(5)
#     c,add = s.accept()
#     print("Connection estiblished")

# kunal()    

#! write a python program which will impliment the following 
#! A] write a server side program in such a way that it should a number fron client program ,square it and give the result back to the client side program 

#! B] write a client program in such way that it should  accept an number from keyboard and get its square fron the server side program 

#serverSquare.py
import socket  #step 1
#step 2
s = socket.socket()
s.bind(("localhost",8888))
s.listen(2)  #step 3
print("Server side program is ready to Accept  any Client side program ")
while(True):
    try :
            
        cside,clientadd = s.accept() #step 4
        #step 5
        csval = float( cside.recv(1024).decode())
        print(f"val of client :{csval}")
        res = csval**2
        cside.send(str(res).encode()) #step 6
    except ValueError:
        cside.send("Dont's Enter Alnum,symbols and Strs".encode())
        




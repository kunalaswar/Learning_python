
# import socket
# while(True):
#     s = socket.socket()
#     s.connect(("localhost",8808))
#     cspmsg =input("Students --->")
#     if cspmsg .lower()=="bye":
#         s.send(cspmsg .decode())
#         break
#     else:
#         s.send(cspmsg.encode())
#         sermsg = s.recv(1024).decode()
#         print(f"KVR---> {sermsg}")


#!write a python program for Emolitation the folling

#! A] write an server side program in such way that use Batch 9pm  in such way that it should accept students number from Client side program and give student scomplete result to the client side  program 

#! write a client side program in such way that its shuold  students number from Keyboard, send to the server side program and gets the complete result  from the students 

#serverResultDataBasesEx.py
import socket
import mysql.connector
s = socket.socket()
s.bind(("localhost",8808))
s.listen(2)
while(True):
    try:
        clientSocket,clientadd = s.accept()
        sno = int(clientSocket.recv(1024).decode())
        # PDBC code 
        conn = mysql.connector.connect(host = "localhost",
                                user = "root",
                                passwd = "kunal123456",
                                database = "batch9am")
                                               
        cur = conn.cursor()       
        cur.execute("select * from result where sno = %d"% mark)
        record = cur.fetchone()
        clientSocket.send(str(record).encode())


    except ValueError:
        clientSocket.send =("Don't Enter alnum,strs and symbols for students Number ".encode())    

    except mysql.connector.DatabaseError as db:
        clientSocket.send (("problem in Mysql DB :",db).encode())
    except :
        clientSocket.send(("Oops something Went wrong ").encode())
         


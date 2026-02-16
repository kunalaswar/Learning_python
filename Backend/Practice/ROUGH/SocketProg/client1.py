# from socket import * 
# def main():
#     host = gethostname()
#     portno =8088
#     s = socket()
#     s.connect((host,portno))
#     s.send("Hello")
#     s.close()

# main()    


#! B] write a client program in such way that it should  accept an number from keyboard and get its square fron the server side program 

import socket #step 1
# step 2
s =socket.socket()
s.connect(("localhost",8888))
print("Client side program obtain Connection fron server side program ")
    # step 3
n = input("Enter a value for Getting it square :") 
s.send(n.encode())
 #step 4
res = s.recv(1024).decode() 
print(f"square {n,res }")
print("*"*30)

 



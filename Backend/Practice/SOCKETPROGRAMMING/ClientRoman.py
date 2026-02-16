
import socket
s = socket.socket()
s.connect(("localhost",8888))
print("Client side program connected to server side program ")
print("--------------------------------------------------------")
n = input("Enter number for getting its ROMAN EQL")
s.send(n.encode())
rv=s.recv(1024).decode()
print(f"Roman {n} = {rv}")




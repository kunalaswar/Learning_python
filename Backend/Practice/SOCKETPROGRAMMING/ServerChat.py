import socket
s = socket.socket()
s.bind(("localhost",8558))
# s.bind(("127.0.0.1",8558))
s.listen(2)
while(True):
    cs,ca = s.accept()
    csdata = cs.recv(1024).decode()
    print(f"Students --->{csdata}")
    sdata = input("KVR --->")
    cs.send(sdata.encode())

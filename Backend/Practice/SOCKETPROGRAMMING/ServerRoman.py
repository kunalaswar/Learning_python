
import socket 
s = socket.socket()
s.bind(("localhost",8888))
s.listen(2)

print("Server side is ready to accept any client side program request ")

while(True):
    cs,ca = s.accept()
    csdata =cs.recv(1024).decode()
    print("Client data at server",csdata)
    n = int(csdata) #    32767 -ve 0
    try:
            
        if (n<=0):
            cs.send(str("Does not have Roman Eqv",n).encode())
        else:
            rn = ""
            while(n>=1000):
                rn = rn+"M"
                n = n-1000
            # print(rn)    
            if (n>=900):
                rn =rn+"CM" 
                n = n-900
            if (n>=500)    :
                rn = rn+"D"
                n = n-500
            if (n>=400):
                rn = rn+"CD"
                n = n-400
            while(n>=100):
                rn = rn+"C"
                n = n-100    
            if n>=90:
                rn = rn +"XC"    
                n = n-90
            if (n>=50)    :
                rn = rn+"L"
                n = n-50
            if (n>=40):
                rn = rn+"XL"    
                n = n-40
            while(n>=10):
                rn = rn+"X"
                n = n-10
            if (n>=5):
                rn = rn+"V"
                n = n-5
            if (n>=4):
                rn = rn+"IV"    
                n = n-4
            while(n>=1):
                rn = rn+"I"    
                n = n-1
                break
    except ValueError:
        cs.send("Dont Enter Alnum and Symbols and strs".encode())            








    

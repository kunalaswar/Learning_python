 #!SynchBankWithDrawFunEx.py
#todo - First number  
#todo    VERY IMPORTANT EXAMPLE --->
# import threading , time 
# def checkclear(camt): #checkamount

#     lobj.acquire() #step -2 
#     global vmbal
#     if vmbal<camt:
#         print(f"Dear Customer : { threading.current_thread().name} your Check of INR {camt} is Bounce -contact source ") #Check Bounce
#     else:
#         vmbal = vmbal - camt
#         print(f"Dear Customer : { threading.current_thread().name} your Check of INR {camt} is Bounce clear ")
#         time.sleep(1)
#         print("Available Balance :",vmbal)

#         print("-------------------------------------")

#     lobj.release() #Step -3 

# #todo - Main program 
# #VM Account balance 
# vmbal = 10000  #original Balance 
# #create an object of Lock class 
# lobj = threading.Lock() #Step -1 

# t1 = threading.Thread(target=checkclear ,args=(10000,))
# t1.name = "aaa"
# t2 = threading.Thread(target=checkclear,args=(90000,))
# t2.name = "bbb"
# t3 = threading.Thread(target=checkclear,args=(7000,))
# t3.name = "ccc"
# t4 = threading.Thread(target=checkclear,args = (5000,))
# t4.name = "ddd"
# t5 = threading.Thread(target=checkclear,args=(2000,))
# t5.name = "eee"

# #Dipatch the sub thread 
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()

#^-------------------------------------------------------------------------------------------------
#! SynchBankWithDrawOopsEx.py
#todo - Second  number  
#todo    VERY IMPORTANT EXAMPLE --->

# import threading,time 
# class Browers:
#     @classmethod
#     def getlock(cls):
#         #create the object of lock class
#         cls.lobj = threading.Lock()
#         Browers.getaccbal()
#     @classmethod    
#     def getaccbal(cls):
#         #VM Account Bal    
#         cls.vmbal= 110000
#     def __init__(self,camt):
#         self.camt = camt    
#     def checkclear(self): #checkamount
#         #release the object of Lock object 
#         Browers.lobj.acquire() 
#         # global vmbal  #todo - Need not to write a global keyword 
#         if self.camt > Browers.vmbal:
#             print(f"Dear Customer : { threading.current_thread().name} your Check of INR {self.camt} is Bounce -contact source ") #Check Bounce
#             time.sleep(1)
#         else:
#             Browers.vmbal = Browers.vmbal-self.camt
#             print(f"Dear Customer : { threading.current_thread().name} your Check of INR {self.camt} is Bounce clear ")
#             time.sleep(1)
#             print("\tAvailable Balanace in VM Account:{}".format(Browers.vmbal))

#             print("-------------------------------------")
#         Browers.lobj.release() #Step -3 
    
# #Main program     
# #call Class Level Methods of Borower Class
# Browers.getlock()

# t1 = threading.Thread(target= Browers(10000).checkclear)        
# t1.name = "aaa"
# t2 = threading.Thread(target= Browers(9000).checkclear)        
# t2.name = "bbb"
# t3 = threading.Thread(target= Browers(8000).checkclear)        
# t3.name = "ccc"
# t4 = threading.Thread(target= Browers(7000).checkclear)        
# t4.name = "ddd"
# t5 = threading.Thread(target= Browers(1000).checkclear)        
# t5.name = "eee"

# #Dispatch the sub thread 
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
#^-------------------------------------------------------------------------------------------------
#!ReservationAppFun.py
#todo - Third number 
import threading , time     
def Reservation(nos):  #nos = Number of seat
    lobj.acquire()
    global totseats
    if (nos > totseats):
        print(f"\tDear Passenger:'{threading.current_thread().name}', {nos} Seats are not Available-better luck next time")
        time.sleep(1)
    else:
        totseats = totseats-nos
        print("\tDear Passenger:'{}', {} Seats are Reseved Happy Journey ".format(threading.current_thread().name,nos))
        time.sleep(1)
        print("Available seat  = ",totseats)
        if (totseats ==0):
            print("\t BUS IS FULL ")
        print("-------------------------------------------------------------------")    
        lobj.release()    

#main program 
#create an object of Lock     
lobj = threading.Lock()
#number of seats in Buses 
totseats = 12
# t1 = threading.Thread(target = Reservation, args = (14,))
t1 = threading.Thread(target = Reservation, args = (4,))
t1.name = "pavan"
t2 = threading.Thread(target = Reservation, args = (4,))
t2.name = "pratik"
t3 = threading.Thread(target = Reservation, args = (4,))
t3.name = "ankit"
t4 = threading.Thread(target = Reservation, args = (4,))
t4.name = "sai"
#Dispatch all the threads 
t1.start()
t2.start()
t3.start()
t4.start()

#^-------------------------------------------------------------------------------------------------




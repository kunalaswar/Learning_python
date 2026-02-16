#joinEx1.py 

# import threading,time
# def welcome(val):
#     print(f"{val} Good morning {threading.current_thread().name}")
#     time.sleep(1)
# #main program     

# print("Program Execution Started by ",threading.current_thread().name)
# t1 = threading.Thread(target=welcome,args=("harshal",))
# t1.name = "kunal"
# print("Execution status of sub thread t1 = ",t1.is_alive())
# #todo  - Dispatch the sub thread     <---
# t1.start()
# print("Execution Status of Sub thread t1 = ",t1.is_alive()) 
# #todo - Make the Mainthread to wait until subthread joins to the mainthread
# t1.join() # todo  <---
# print("Execution Status of Sub thread t1 after join() = ",t1.is_alive()) 
# print("Program Execution Ended by ",threading.current_thread().name)

#^----------------------------------------------------------------------------------------------
#! write a python program which will generated 1 to n number After Each and Every second by using thread 

# import threading,time
# def Numbergen(n):
#     if(n<=0):
#         print(f"{threading.current_thread.name} ")
#     else:
#         for val in range(1,n+1):
#             print(f"val is {threading.current_thread().name} --->{val}")    
#             time.sleep(0.10)


# #Main program     
# t1 = threading.Thread(target=Numbergen,args=(10,))
# t1.start()

#^----------------------------------------------------------------------------------------------

# import threading ,time 
# def numbergen(n):
#     if (n<=0):
#         print(f"{threading.current_thread().name}--->{n}")
#     else:
#         for i in range(1,n+1):
#             print(f"{threading.current_thread().name} ---> value of i {i}")    
#             time.sleep(0.10)

# #Main program 
# n = int(input("Enter a How many number you want to Enter "))
# t1 = threading.Thread(target=numbergen,args=(n,))
# #todo - Dispatch the Thread 
# t1.start()

#^----------------------------------------------------------------------------------------------
#! By using OOPS Object oriented programming 

# import threading ,time 
# class kunal:
#     def numbergen(n):
#         if n<=0:
#             print(f"number is invalid {threading.current_thread().name}") 
            
#         else:
#             for i in range(1,n+1):
#                 print(f"value {threading.current_thread().name} ---> value of i {i}")    
#                 time.sleep(0.10)
# #Main program 
# n = int(input("Enter How many number  you want to generated "))
# t1 = threading.Thread(target=kunal.numbergen,args=(n,))
# #todo Dispatch the Sub thread 
# t1.start()

#^----------------------------------------------------------------------------------------------
# import threading ,time
# class kunal:
#     def __init__(self,n):
#         self.n = n
#     def numbergen(self):
#         if (self.n<=0):
#             print("Invliad input",threading.current_thread().name)    
#         else:
#             for val in range(1,n+1):
#                 print (f"{threading.current_thread().name} ---> value of i {val}  ")    
#                 time.sleep(0.10)

# #Main program 
# n = int(input("Enter a how many number You want to generated  "))
# no =kunal(n)
# t1 = threading.Thread(target=no.numbergen)
# #todo - Dispatch the sub thread
# t1.start()

#?===============================================================================================
   #todo   17-12-2024
#?===============================================================================================
#! Write a thread based  application which will generated odd number seperatedly and Even number seperatedly 
# import threading, time
# def odd(n):
#     if n<=0:
#         print(f"{n} Invlaid input {threading.Thread().name}")
#     else:
#         for val in range(1,n+1):
#             if val%2!=0:
#                 print(f"\t\t\todd number = {val}")    
#                 time.sleep(0.25)
# def even(n):  
#     if n<=0:
#         print(f"{n} Invlaid input {threading.Thread().name}")
#     else:
#         for val in range(1,n+1):
#             if val%2==0:
#                 print(f"\t\t\teven number = {val}")                
#                 time.sleep(0.25)

# #Main program 
# #Create two sub thread for performiong the operation
# print("Program Execution Started ",threading.current_thread().name)
# t1 = threading.Thread(target=odd,args=(10,))
# t2 = threading.Thread(target=even,args=(10,))
# print(f"Number of thread Which are running --->{threading.active_count()}")

# #todo - Dispatch the Thread 
# t1.start()
# t2.start()
# print(f"Number of thread Which are running --->{threading.active_count()}")

# t1.join()
# t2.join()
# print("Program Execution Ended ",threading.current_thread().name)


#^---------------------------------------------------------------------------------------------
#! 
# import threading, time
# def odd(n):
#     if n<=0:
#         print(f"{n} Invlaid input {threading.Thread().name}")
#     else:
#         for val in range(1,n+1):
#             if val%2!=0:
#                 print(f"\t\t\todd number = {val}")    
#                 time.sleep(0.25)
# def even(n):  
#     if n<=0:
#         print(f"{n} Invlaid input {threading.Thread().name}")
#     else:
#         for val in range(1,n+1):
#             if val%2==0:
#                 print(f"\t\t\teven number = {val}")                
#                 time.sleep(0.25)

# #Main program 
# #Create two sub thread for performiong the operation
# print("Program Execution Started ",threading.current_thread().name)
# t1 = threading.Thread(target=odd,args=(int(input("Enter a How many Odd number You want to generated")),))
# t2 = threading.Thread(target=even,args=(int(input("Enter a How many Even number You want to generated")),))
# print(f"Number of thread Which are running --->{threading.active_count()}")

# #todo - Dispatch the Thread 
# t1.start()
# t2.start()
# print(f"Number of thread Which are running --->{threading.active_count()}")

# t1.join()
# t2.join()
# print("Program Execution Ended ",threading.current_thread().name)

#^---------------------------------------------------------------------------------------------
#! OOPS 
# import threading , time 
# class kunal :
#     def odd(self,n):
#         if n<=0:
#             print(f"invalid input {threading.current_thread().name}")
#         else:
#             for i in range(1,n+1,2):
#                 print(f"{threading.current_thread().name}--->  Odd number : {i}")   
#                 time.sleep(0.25) 
#     def even(self,n):
#         if n<=0:
#             print(f"invalid input {threading.current_thread().name}")
#         else:
#             for i in range(2,n+1,2):
#                 print(f"{threading.current_thread().name}--->  Even number : {i}")   
#                 time.sleep(0.25) 

# #Main Program 
# print(f"program Execution Started : {threading.current_thread().name}")
# # no = kunal()
# t1 = threading.Thread(target=kunal().odd,args=(int(input("Enter how many number you want to generated")),))
# t2 = threading.Thread(target=kunal().even,args=(int(input("Enter how many number you want to generated")),))

# #todo - Dispatch sub thread 
# t1.start()
# t2.start()

# t1.join()
# t2.join()
# print(f"program Execution Ended : {threading.current_thread().name}")

#?--------------------------------------------------------------------------------------------
#?--------------------------------------------------------------------------------------------
#!synchronization  Dead lock Concept

# import threading ,time
# def multable (n):
#     l.acquire() #step 2
#     if(n<=0):
#         print(f" invalid input {n}")
#     else:
#         for i in range(1,11):
#             print(f"{threading.current_thread().name}  {i} X {n} ={n*i} ")    
#             time.sleep(0.25)
#     l.release() #step 3
            

# #main program
# #Creating the object of lock class of threading
# l=threading.Lock() #step 1
# t1 = threading.Thread(target=multable , args=(5,))
# print("------------")
# t2 = threading.Thread(target=multable , args=(9,))
# print("------------")
# t3 = threading.Thread(target=multable , args=(12,))
# t4 = threading.Thread(target=multable , args=(10,))

# #todo - Dispatch the sub thread
# t1.start()
# t2.start()
# t3.start()
# t4.start()


#!OOPS

# import threading ,time
# class kunal:
        
#     def multable (self,n):
#         l.acquire() #step 2
#         if(n<=0):
#             print(f" invalid input {n}")
#         else:
#             for i in range(1,11):
#                 print(f"{threading.current_thread().name}  {i} X {n} ={n*i} ")    
#                 time.sleep(0.25)
#         l.release() #step 3
                

# #main program
# #Creating the object of lock class of threading
# l=threading.Lock() #step 1

# t1 = threading.Thread(target=kunal().multable , args=(5,))
# print("------------")
# t2 = threading.Thread(target=kunal().multable , args=(9,))
# print("------------")
# t3 = threading.Thread(target=kunal().multable , args=(12,))
# t4 = threading.Thread(target=kunal().multable , args=(10,))

# #todo - Dispatch the sub thread
# t1.start()
# t2.start()
# t3.start()
# t4.start()

#!OOPS with other method OR some Changes

# import threading ,time
# class kunal:
#     def __init__(self,n):
#             self.n = n
#     def multable (self):
        
#         l.acquire() #step 2
#         if(self.n<=0):
#             print(f" invalid input {self.n}")
#         else:
#             for i in range(1,11):
#                 print(f"{threading.current_thread().name}  {i} X {self.n} ={self.n*i} ")    
#                 time.sleep(0.25)
#         l.release() #step 3
                

# #main program
# #Creating the object of lock class of threading
# l=threading.Lock() #step 1

# t1 = threading.Thread(target=kunal(5).multable)
# print("------------")
# t2 = threading.Thread(target=kunal(9).multable )
# print("------------")
# t3 = threading.Thread(target=kunal(12).multable )
# t4 = threading.Thread(target=kunal(10).multable )

# #todo - Dispatch the sub thread
# t1.start()
# t2.start()
# t3.start()
# t4.start()
#^------------------------------------------------------------------------------------------------
# import threading,time
# class table:
#     def __init__(self,k):
#         self.k = k
#     def multable(self):
#         l.acquire() #step 2
#         if self.k<=0:
#             print(f" Invalid input {k}   {threading.current_thread().name}")
#         else:
#             for i in range(1,11):
#                 print(f"{threading.current_thread().name}  {self.k} X {i} = {self.k*i}")    
#                 time.sleep(0.25)
#         l.release() #step 3

# #Main program  
# l = threading.Lock() #step 1
# print("Program Execution Started ",threading.current_thread().name)               
# t1 = threading.Thread(target=table(5).multable)
# t2 = threading.Thread(target=table(10).multable)

# #Dispatch the sub thread
# t1.start()
# t2.start()

# print("Program Execution Ended ",threading.current_thread().name)               
# #join the sub thread 
# # t1.join()
# # t2.join()


#^------------------------------------------------------------------------------------------------
#!synchBankWithDrawFun 
# import threading ,time 
# def checkclear(camt):
#     l.acquire() #step 2
#     global vmbal
#     if camt> vmbal:
#         print(f"Dear customer {threading.current_thread().name} UR check of INR Is Bounced - Contant source")
#         time.sleep(1)
#     else:
#         vmbal = vmbal-camt    
#         print(f"Dear customer {threading.current_thread().name} UR check in Cleared {camt}")
#         time.sleep(1)
#         print(f"Avalible Balance in VM Account {vmbal}")
#     print("-----------------------------------")
#     l.release()#step 3

# #Main program 
# #VM Account Balance 
# vmbal  = 10000
# #Create the lock Class object 
# l = threading.Lock() #step 1
# t1 = threading.Thread(target=checkclear,args=(10000,))
# t1.name = "AAA"
# t2 = threading.Thread(target=checkclear,args=(1000,))
# t2.name = "BBB"
# t3 = threading.Thread(target=checkclear,args=(2000,))
# t3.name = "CCC"
# #Dispatch the sub thread 
# t1.start()
# t2.start()
# t3.start()

#^------------------------------------------------------------------------------------------------
#! Same Example with OOPS
# import threading ,time 
# class bank:
        
#     def checkclear(self,camt):
#         l.acquire() #step 2
#         global vmbal
#         if camt> vmbal:
#             print(f"Dear customer {threading.current_thread().name} UR check of INR Is Bounced - Contant source")
#             time.sleep(1)
#         else:
#             vmbal = vmbal-camt    
#             print(f"Dear customer {threading.current_thread().name} UR check in Cleared {camt}")
#             time.sleep(1)
#             print(f"Avalible Balance in VM Account {vmbal}")
#         print("-----------------------------------")
#         l.release()#step 3

# #Main program 
# #VM Account Balance 
# vmbal  = 10000
# #Create the lock Class object 
# l = threading.Lock() #step 1
# t1 = threading.Thread(target=bank().checkclear,args=(10000,))
# t1.name = "AAA"
# t2 = threading.Thread(target=bank().checkclear,args=(1000,))
# t2.name = "BBB"
# t3 = threading.Thread(target=bank().checkclear,args=(2000,))
# t3.name = "CCC"
# #Dispatch the sub thread 
# t1.start()
# t2.start()
# t3.start()



# import threading ,time 
# class bank:
#     @classmethod     
#     def getlock(cls):
#         #Create the lock Class object 
#         cls.l = threading.Lock() #step 1
#         bank.getaccbal()
#     @classmethod    
#     def getaccbal(cls):
#         #VM Account Balance 
#         cls.vmbal  = 11000
#     def __init__(self,camt):
#         self.camt = camt
        
#     def checkclear(self,camt):
#         bank.l.acquire() #step 2
#         global vmbal
#         if self.camt> bank.vmbal:
#             print(f"Dear customer {threading.current_thread().name} UR check of INR Is Bounced - Contant source")
#             time.sleep(1)
#         else:
#             bank.vmbal = bank.vmbal-self.camt    
#             print(f"Dear customer {threading.current_thread().name} UR check in Cleared {camt}")
#             time.sleep(1)
#             print(f"Avalible Balance in VM Account {vmbal}")
#         print("-----------------------------------")
#         bank.l.release()#step 3

# #Main program 

# t1 = threading.Thread(target=bank(10000).checkclear)
# t1.name = "AAA"
# t2 = threading.Thread(target=bank(1000).checkclear)
# t2.name = "BBB"
# t3 = threading.Thread(target=bank(2000).checkclear)
# t3.name = "CCC"
# #Dispatch the sub thread 
# t1.start()
# t2.start()
# t3.start()


#^------------------------------------------------------------------------------------------------
import threading ,time
def reservation(nos):
    global totseats
    l.acquire() #step 2
    if nos>totseats:
        
        print(f"DEAR Passenger {threading.current_thread().name} Seat are Not  Avaliable Better Luck Next time {nos}")
        time.sleep(1)
        
    else:
        totseats = totseats - nos    
        print(f"DEAR Passenger {threading.current_thread().name}Seats are Available Happy Jurney GO ---> {nos}  ")
        time.sleep(2)
        print("Avaliable Seats ",totseats)    
    l.release()#step 3    
#Main program 
l = threading.Lock() #step 1
#Number of Seat in the bus 
totseats =12 
#Create MUltiple Passenger Threads 
t1 = threading.Thread(target=reservation,args=(5,))
t1.name = "Kunal"
t2 = threading.Thread(target=reservation,args=(6,))
t2.name = "Ankit"
t3 = threading.Thread(target=reservation,args=(9,))
t3.name = "Harshal"

#Dispatch the threads 
t1.start()
t2.start()
t3.start()


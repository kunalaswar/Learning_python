 #todo -write the thread Based application to Genetated ODD number  seperatelly and EVEN number Seperatelly  
 #! write the program to Generating ODD and Even Number Seperatelly 

# import threading ,time  
# def odd(n):
#     if n<=0:
#         print(f"Invalid input {threading.current_thread().name}")
#     else:
#         for i in range(1,n+1):
#             print(f"{threading.current_thread().name}  odd: {i}")
#             time.sleep(1)
# def even (n):
#     if n<=0:
#         print(f"Invalid input {threading.current_thread().name}")
#     else:
#         for i in range(2,n+1,2):
#             print(f"{threading.current_thread().name} Even : {i}")
#             time.sleep(1)

# #main program 
# print(f"Program Execution Started By :{threading.current_thread().name}")
# #Create to sub thread for performing Two operations 

# t1 =threading.Thread(target=odd,args=(int(input("Enter how many ODD number U Generated : "
# )),))
# t2 =threading.Thread(target=even,args=(int(input("Enter how many ODD number U Generated : "
# )),))
# print(f"Number of thread which are running before start  = {threading.active_count()}")
# #Dispatch the two sub thread 
# t1.start()
# t2.start()
# print(f"Number of thread which are running After start  = {threading.active_count()}")
# #Join the sub threads
# t1 .join()
# t2.join()
# print(f"Number of thread which are rinning after joining  {threading.active_count()}   ")
# print(f"Program Execution Ended By :{threading.current_thread().name}")


#^-----------------------------------------------------------------------------------------------
#! write the program to Generating ODD and Even Number Seperatelly 
#todo - OOP
#& Created two class seperatedly
# import threading ,time
# class Numbers:
#     def odd(self,n):
#         if n <=0:
#             print(f"{threading.current_thread().name} is Invalid Number {n}")
#         else:
#             for val in range(1,n+1,2):
#                 print(f"{threading.current_thread().name} ODD :{val }")       
#                 time.sleep(1)
#     def even(self,n):            
#         if n <=0:
#             print(f"{threading.current_thread().name} is Invalid Number {n}")
#         else:
#             for val in range(2,n+1,2):
#                 print(f"{threading.current_thread().name} EVEN :{val }")       
#                 time.sleep(1)
# #Main program 
# print(f"Program Execution Started by {threading.current_thread().name}")
# t1 = threading.Thread(target=Numbers().odd,args=(int(input("Enter a How many number you Wnat Generate :")),))
# t2 = threading.Thread(target=Numbers().even,args=(int(input("Enter a How many number you Wnat Generate :")),))

# #Dispatch the sub thread 
# t1.start()
# t2.start()
# #Join the sub thread 
# t1.join()
# t2.join()
# print("Number Threads which are running after joining={}".format(threading.active_count()) )# 1

# print(f"Program Execution Ended  by {threading.current_thread().name}")


#^-----------------------------------------------------------------------------------------------
#! write the program to Generating ODD and Even Number Seperatelly 
#todo - OOP Created a sepeated Class TWO METHOD 
#& Created 1 Class and combine both method in to the single class 
# import threading ,time
# class oddnumber:
#     def odd(self,n):
#         if n<=0:
#             print(f" {threading.current_thread().name} invalid input {n}")
#         else:
#             for val in range(1,n+1,2):
#                 print(f" {threading.current_thread().name} ODD={val}")     
#                 time.sleep(1)

# class evennumber:
#     def even(self,n):
#         if n<=0:
#             print(f" {threading.current_thread().name} invalid input {n}")
#         else:
#             for val in range(2,n+1,2):
#                 print(f" {threading.current_thread().name} EVEN= {val}")     
#                 time.sleep(1)
# #main program 
# print(f"Program Execution Stated by {threading.current_thread().name} ")

# t1 = threading.Thread(target=oddnumber().odd,args=(int(input("Enter a How many number you want to generated :")),))
# t2 = threading.Thread(target=evennumber().even,args=(int(input("Enter a How many number you Want to Genetared ")),))
# time.sleep(1)
# #Dispatch the sub Thread 
# t1.start()
# t2.start()
# #Join the two sub thread 
# t1.join()
# t2.join()
# print(f"Program Execution End by {threading.current_thread().name} ")

#^-----------------------------------------------------------------------------------------------
#!Program for Demonstrating the Occurence of Dead Lock 
#todo - DeadLockFunEx1.py with only function 
# import threading,time
# def multable(n):
#     if n<=0:
#         print(f"invlaid input {n}")
#     else:
#         for i in range(1,11):
#             print(f"{threading.current_thread().name} ---> {n} X {i} = {n*i}")    
#             time.sleep(0.25)
#         print("------------------------------------")    
# #main program         
# t1 = threading.Thread(target=multable,args=(int(input("Which table you Want ")),))
# t2 = threading.Thread(target=multable,args=(int(input("Which table you Want ")),))
# t3 = threading.Thread(target=multable,args=(int(input("Which table you Want ")),))
# t4 = threading.Thread(target=multable,args=(int(input("Which table you Want ")),))
# #dispatch the Sub threads 
# t1.start()
# t2.start()
# t3.start()
# t4.start()

# # t1.join()
# # t2.join()
# # t3.join()
# # t4.join()

#^-----------------------------------------------------------------------------------------------
#!Program for Demonstrating the Occurence of Dead Lock 
#todo - DeadLockFunEx2.py with only CLASS OOP  
# import threading ,time 
# class table:
#     def multable(self,n):
#         if n<=0:
#             print(f"{n} is invalid input ")
#         else:
#            for i in range(1,11):
#             print(f"{threading.current_thread().name} ---> {n} X {i} = {n*i}")    
#             time.sleep(0.25)
#         print("------------------------------------")      


# #main program 
# t1 = threading.Thread(target=table().multable,args=(int(input("ENter a Table number :")),))
# t2 = threading.Thread(target=table().multable,args=(int(input("ENter a Table number :")),))
# t3 = threading.Thread(target=table().multable,args=(int(input("ENter a Table number :")),))
# t4 = threading.Thread(target=table().multable,args=(int(input("ENter a Table number :")),))

# # Dispatch the sub thread
# t1.start()
# t2.start()
# t3.start()
# t4.start()

#^-----------------------------------------------------------------------------------------------
#! Program for Demonstrating the Elimination of Dead Lock with Synchronization.
# SynchFunEx1.py

# import threading,time
# def multable(n):
#     L.acquire()
#     if n<=0:
#         print(f"{n} is invalid input ")
#     else:
#         for i in range(1,11):
#             print(f"{threading.current_thread().name} ---> {n} X {i} = {n*i}")    
#             time.sleep(0.25)
#         print("------------------------------------")      
#     L.release()

# #Main Program
# #Create an object of Lock class of threading
# L=threading.Lock() # Step-1
# #Create sub threads
# # t1 = threading.Thread(target=multable ,args=(int(input("Which number of table you want :"))))
# # t2 = threading.Thread(target=multable ,args=(int(input("Which number of table you want :"))))
# # t3 = threading.Thread(target=multable ,args=(int(input("Which number of table you want :"))))
# # t4 = threading.Thread(target=multable ,args=(int(input("Which number of table you want :"))))

# t1 = threading.Thread(target=multable ,args=(12,))
# t2 = threading.Thread(target=multable ,args=(2,))
# t3 = threading.Thread(target=multable ,args=(5,))
# t4 = threading.Thread(target=multable ,args=(6,))

# # Dispatch the sub thread 
# t1.start()
# t2.start()
# t3.start()
# t4.start()

#^-----------------------------------------------------------------------------------------------
#! Program for Demonstrating the Elimination of Dead Lock with Synchronization.
#todo - SynchOopsEx1.py
#todo  - OOP Concept 

# import threading,time
# class Table:
# 	def MulTable(self,n):
# 		#Get the lock
# 		L.acquire() #todo - Step-2
# 		if(n<=0):
# 			print("{}--> {} is Invalid Input".format(threading.current_thread().name,n))
# 		else:
# 			print("-"*50)
# 			print("Mul Table for:{}".format(n))
# 			print("-"*50)
# 			for i in range(1,11):
# 				print("\t{}---->{} x {}={}".format(threading.current_thread().name,n,i,n*i))
# 				time.sleep(0.125)
			
# 		print("-------------------------------------------------------------")
# 		#release the lock
# 		L.release() # todo -Step-3

# #Main Program
# #Create an object of Lock class of threading
# L=threading.Lock() #todo - Step-1
# #Create sub threads
# t1=threading.Thread(target=Table().MulTable,args=(19,))
# t2=threading.Thread(target=Table().MulTable,args=(17,))
# t3=threading.Thread(target=Table().MulTable,args=(-9,))
# t4=threading.Thread(target=Table().MulTable,args=(14,))
# #dispatch the sub threads
# t1.start()
# t2.start()
# t3.start()
# t4.start()















#^-----------------------------------------------------------------------------------------------
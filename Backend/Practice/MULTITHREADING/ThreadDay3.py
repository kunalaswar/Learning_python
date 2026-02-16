  #!Program for Demonstrating the need of join() of Thread class
#todo - JoinEx1.py

# import threading,time 
# def welcome(val):
#     print(f"{threading.current_thread().name} {val}")
#     time.sleep(2)
#     print(f"\t\tComing out from sleep {threading.current_thread().name}")


# #Main program     
# print(f"Program Execution Statted from main program :{threading.current_thread().name}")
# t1 = threading.Thread(target = welcome,args= ('Rossum',))
# print("Execution Status of the Sub Thread t1 Before start()",t1.is_alive())
# t1.start()
# print("Execution Status of the Sub Thread t1 after Start ()",t1.is_alive())
# t1.join()
# print("Program Execution Ended From main program ",t1.is_alive())
# print("Program Execuiton Ended by :",threading.current_thread().name)

#^-----------------------------------------------------------------------------------------------------

#!#Program for generating 1 to N numebrs by using threads
#NumberGenFunEx1.py

# import threading ,time  #Step -1 
# def generator(n): #Step -2
#     if n<=0:
#         print(f"Invalid input {threading.current_thread().name}")
#     else:
#         for i in range(1,n+1):
#             print(f"{threading.current_thread().name} is value {i}")
#             time.sleep(0.25)

# #Main program             
# n= int(input("How Many number you Wnat to Generate "))
# t1 = threading.Thread(target = generator,args = (n,))  #Step -3
# t1.start() #Step - 4

#^---------------------------------------------------------------------------------------------------
#!#Program for generating 1 to N numebrs by using threads
#NumberGenOopsEx1.py

# import threading , time
# class numbers:
#     def numgenerator(self,n):
#         if (n<=0):
#             print("Invalid input ",threading.current_thread().name)
#         else:
#             for val in range(1,n+1):
#                 print(f"{threading.current_thread().name} value is i= {val}")    
#                 time.sleep(2)
# #Main Program 
# n = int(input("Enter How many number you Wnat to Generated :"))
# no = numbers()
# t1 = threading.Thread(target = no.numgenerator,args= (n,))
# t1.start()

#^---------------------------------------------------------------------------------------------------
#!#Program for generating 1 to N numebrs by using threads
#NumberGenOopsEx2.py

# import threading,time
# class number:
#     def numgenerator(self,n):
#         if n<=0:
#             print(f"invalid input {threading.current_thread().name}  {n}")
#         else:
#             for val in range(1,n+1):
#                 print(f"{threading.current_thread().name} is Value= {val}")    
#                 time.sleep(1)  

# #Main program 
# t1 = threading.Thread(target = number().numgenerator,args=(int(input("ENTER A HOW MANY NUMBER YOU WANT TO GENERATE :")),))
# t1.start()
#^---------------------------------------------------------------------------------------------------
#! #Program for generating 1 to N numebrs by using threads
#todo - NumberGenOopsEx3.py

# import threading ,time
# class number :
#     def gennumber(self,n):
#         if n <= 0 :
#             print("Invalid input ",threading.current_thread().name)
#         else:
#             for val in range(1,n+1):
#                 print(f"{threading.current_thread().name} value  is i= {val}")    
#                 time.sleep(0.25)   

# #Main program                 
# n =int(input("Enter a number number :"))
# threading.Thread(target = number().gennumber, args=(int(input("Enter How many number you want to Generated ")),)).start()

#^---------------------------------------------------------------------------------------------------
#!#Program for generating 1 to N numebrs by using threads
# todo - NumberGenOopsEx4.py

# import threading , time 
# class number:
#     def __init__(self,n):
#         self.n = n
#     def gennumber(self):
#         if n<=0:
#             print(f"{threading.current_thread().name} is Invalid input {self.n}")
#         else:
#             for i in range(1,self.n+1):
#                 print(f"{threading.current_thread().name } Value is {i}")    
#                 time.sleep(0.25)

# #Main program                 
# n = int(input("Enter a number u want to Generate :"))
# no =number(n)
# t1 =threading.Thread(target=no.gennumber)
# t1.start()

#^---------------------------------------------------------------------------------------------------
#!Program for generating 1 to N numebrs by using threads
#NumberGenOopsEx5.py

# import threading , time
# class number:
#     def __init__(self ,n):
#         self. n = n

#     def numgenerator(self):
#         if(self.n<= 0 ):
#             print(f"{threading.current_thread().name} is Invalid input {self.n}")
#         else:
#             for val in range(1,self.n+1):
#                 print(f"{threading.current_thread().name} value is  i = {val}")
#                 time.sleep(1)

# #Main program 
# n = int(input("Enter how Many number you want to generated :"))
# t1 = threading.Thread(target=number(n).numgenerator)

# t1.start()
#^---------------------------------------------------------------------------------------------------
# !Program for generating 1 to N numebrs by using threads
# todo - NumberGenOopsEx5.py


#^---------------------------------------------------------------------------------------------------
#!Program for generating 1 to N numebrs by using threads
#NumberGenOopsEx6.py

# import threading ,time
# class number:
#     def __init__(self,n):
#         self. n = n
#     def gennumber(self):
#         if (self.n<0):
#             print(f"Invliad input {threading.current_thread().name}  is {self.n}")    
#         else:
#             for val in range(1,self.n+1):
#                 print(f"{threading.current_thread().name} value of i =  {val}")    
#                 time.sleep(2)
# #Main program 
# threading.Thread(target=number(int(input("Enter a number How Many number you Wnat to Generated :"))).gennumber).start()

#^---------------------------------------------------------------------------------------------------
#!Program for accepting Line of Text and display every word and letters in that word
#WordsGenerateOops.py
# import threading ,time 
# class Lineoftext:
#     def __init__(self,line):
#         self.line = line 
#     def dispval(self):
#         for word in self.line.split():
#             print(f"{threading.current_thread().name} ---> {word}")
#             for val in word:
#                 print(f"\t\t\t {val}")
#                 time.sleep(1)
#             print("---------------------")    


# #main  program 
# t1 = threading.Thread(target= Lineoftext(input("Enter a line of text here :")).dispval )
# t1 .start()




        












#^---------------------------------------------------------------------------------------------------
#^---------------------------------------------------------------------------------------------------
#^---------------------------------------------------------------------------------------------------
#^---------------------------------------------------------------------------------------------------
#^---------------------------------------------------------------------------------------------------
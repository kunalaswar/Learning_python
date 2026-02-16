# import threading
# def greet():
#     print(f"Main thread  : {threading.current_thread().name}")
#     # print("I am From greet method ")


# greet()
# t1= threading.Thread(target=greet)
# print(t1)  #todo - <Thread(Thread-1 (greet), initial)>

# print(f"the Execution count thread  = {threading.active_count()}")
# t1.start()
# print(f"the Execution count thread = {threading.active_count()}")

# def square (self,l):
#     for val in lst:
#         print(f"{val} {val*val}")



# #Main program         
# lst = [2,3,4,5,6]
# s= square(lst)

# 

#! Program for Demonstrating the Sequential Execution only with Deafult Thread--MainThread
#todo - TimeCalWithDefaultThreadFlow.py

# import threading,time
# def square(lst):
#     for val in lst:
#         print(f" {threading.current_thread().name} square {val} ---> {val*val}")
#         time.sleep(1)

# def cube(lst):
#     for val in lst:
#         print(f"{threading.current_thread().name} cube {val} ---> {val**3}")
#         time.sleep(1)

# #Main program         
# beginingtime = time.time()
# print(beginingtime)
# print(f"Program Execution  started by {threading.current_thread().name}")
# lst= [2,3,5,6,18,12,8]
# square(lst)
# print("---------------------------")
# cube(lst)

# print(f"Program Execution  Ended by {threading.current_thread().name}")
# endingtime = time.time()
# print(endingtime )


#^------------------------------------------------------------------------------------------------        
#!#Program for Demonstrating the Concurrent Execution only with Sub Threads along MainThread
#todo - TimeCalWithSubThreadsFlow.py

# import threading,time
# def square(lst):
#     for val in lst:
#         print(f"{threading.current_thread().name} square{val} --->{val**2}")
#         time.sleep(1)

# def cube(lst):
#     for val in lst:
#         print(f"{threading.current_thread().name} cube{val} --->{val**3}")        
#         time.sleep(1)

# #main program 
# bigtime = time.time()
# # print(bigtime)
# print(f" the Execution of Stated BY : {threading.current_thread().name}")
# print("-"*50)
# lst= [2,4,6,8]

# #todo -function call Zala aatun
# t1 =threading.Thread(target=square,args=(lst,)) #todo <---
# t2 =threading.Thread(target=square,args=(lst,))
# #Dispatch the sub threads 
# t1.start()
# t2.start()

# print(f"the Execution of End BY : {threading.current_thread().name}")
# endtime = time.time()
# print(endtime)


               
#^------------------------------------------------------------------------------------------------        
# !Program for finding number of threads running in python Program
#todo - ActiveCountEx.py
# import threading
# print("Actived Thread Name =",threading.current_thread().name)
# noat = threading.active_count()
# print("number threaded which are actively Running =",noat)
#^------------------------------------------------------------------------------------------------        

#!Program for demonstrating the default thread
#todo -CurrentThreadEx.py
# import threading
# t = threading.current_thread()
# print(t.name)
# print("----------------- OR -------------------")
# print(threading.current_thread().name)

#^------------------------------------------------------------------------------------------------        


#  #!
# import threading,time
# def square(lst):
#     for val in lst:
#         print("{}---->square({})={}".format(threading.current_thread().name,val,val**2))
#         time.sleep(1)


# def cube(lst):
#     for val in lst:
#         print("{}---->cube({})={}".format(threading.current_thread().name,val,val**3))
#         time.sleep(1)

# # Main program 
# st=time.time()
# print(st)
# print(f"\tprogram Execution stated ",threading.current_thread().name)
# print("-"*50)
# lst = [2,3,4,5,6,7,8]
# print("-"*50)
# square(lst)
# print("-"*50)

# cube(lst)
# print(f"\tprogram Execution Ended ",threading.current_thread().name)
# rt=time.time()
# print(rt)

    
#^------------------------------------------------------------------------------------------------
#!

# import threading, time
# def square(lst):
#     for val in lst:
#         print("{}---->square({})={}".format(threading.current_thread().name,val,val**2))
#         time.sleep(1)

# def cube(lst):
#     for val in lst:
#         print("{}---->cube({})={}".format(threading.current_thread().name,val,val**3))
#         time.sleep(1)
     
# #Main program
# beginingtime = time.time()
# print(beginingtime)
# # print("-"*50)
# print("program Execution Start ",threading.current_thread().name)
# lst = [2,3,4,5,6]
# t1 = threading.Thread(target=square,args=(lst,))
# t2 = threading.Thread(target=cube,args=(lst,))
# #Dispatch the sub threads
# t1.start()
# t2.start()
# print("-"*50)
# print("program Execution Ended ",threading.current_thread().name)
# endtime = time.time()
# print("total execution of time with Sub Threads",beginingtime-endtime)
# t1.join()
# t2.join()

#^------------------------------------------------------------------------------------------------
# import threading
# def greet(val):
#     print(f"{threading.current_thread().name}hii Good morning {val} ")

# #Main program 
# t1 = threading.Thread(target=greet,args=("Rossum",))
# print(threading.active_count())
# print(t1.is_alive())
# t1.start()
# print(t1.is_alive())
# # print(threading.active_count())


#^------------------------------------------------------------------------------------------------
#!Program for Demonstrating Sub thread creation and dispatching the sub thread
#todo - SubThreadStartEx.py

# import threading
# def greet(val):
#     print(f"{threading.current_thread().name} ---> Hii: Good Morning {val}")


# #main program
# t1 = threading.Thread(target=greet,args=("Rossum",))

# print("Number of Threads in program  = ",threading.active_count())
# print("Execution Status of Sub threads t1 = ",t1.is_alive())
# t1.start()
# print("Execution Status of Sub threads t1 = ",t1.is_alive())

#^------------------------------------------------------------------------------------------------
#! Program for Demonstrating Sub thread creation and dispatching the sub thread
#todo -SetGetEx.py

# import threading
# def greet(val):
#     print(f"{threading.current_thread().name}Hii :Good Morning {val}")



# #main program
# t1 = threading.Thread(target=greet,args=([1,2,3]))
# print("Deafult Sub Thread Name before Setting ",t1.name)
# t1.name = "Pdeep"
# print("Set Sub Thread Name After Setting",t1.name)

#^------------------------------------------------------------------------------------------------





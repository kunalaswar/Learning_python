 #! program for showing the internal flow of Deafult 
#todo - Deafultthreadflow.py 
# import threading
# def welcome():
#     print(f"Welcome() - Executed -{threading.current_thread().name}")

# def hello():
#     print(f"Hello() - Execulted -{threading.current_thread().name}")

# def hii():
#     print(f"Hii() - Execulted -{threading.current_thread().name}")

# #main program 
# #todo - program execution started 
# print("LINE 16-------------------------------------------------")
# print(f"program Execution Started by -{threading.current_thread().name}"
# welcome()
# print("-------------------------------------------------")
# hello()
# print("-------------------------------------------------")
# hii()
# print("-------------------------------------------------")
# print(f" program Execution Ended -{threading.current_thread().name}")
#^-----------------------------------------------------------------------------------------------
#todo -  Program for showing the internal flow of sub-thread
# SubThreadsinternal.py
# import threading
# def welcome():
#     print(f"Welcome() - Executed by - {threading.current_thread().name}") #todo- here t1 is called thread object whose name is Thread-1

# def hello():
#     print(f"Hello() -Executed by - {threading.current_thread().name}")  #todo- here t2 is called thread object whose name is Thread-2

# def hii():
#     print(f"Hii - Executed by - {threading.current_thread().name}")  #todo- here t3 is called thread object whose name is Thread-3  

# #main program     
# #todo - Create 3 Sub threads
# t1 = threading.Thread(target=welcome)
# t1.name="Naresh" 
# t2 = threading.Thread(target=hello)
# t3 = threading.Thread(target=hii)
# #todo - Dispatch the sub thread [Dispatch - Send ]
# t1.start()
# t2.start()
# t3.start()

#^-----------------------------------------------------------------------------------------------




# import threading ,time
# def multable(n):
#     if (n<=0):
#         print(f"invalid input {threading.current_thread().name}")
#     else:
#         print(f"multable for {n} --->{threading.current_thread().name}" )    
#         for val in range(1,11):
#             print(f"{threading.current_thread().name} --->{n}x{val} = {n*val}")
#             time.sleep(1)
# #main program             
# t1 = threading.Thread(target=multable,args=(16,))
# t2 = threading.Thread(target = multable,args=( 19,))
# # dispatch the thread
# t1.start()
# t2.start()


#^---------------------------------------------------------------------------------------------------

# import threading,time
# def multable(n):
#     #get the lock
#     l.acquire() 
#     if (n<=0):
#         print(f" invalid input {threading.current_thread().name} {n}")
#     else:
#         print("--------------------------------------")
#         print(f"{threading.current_thread().name} multable for {n}")    
#         for val in range(1,11):
#             print(f"{threading.current_thread().name} --->{n}x{val} --->{n*val}")
#             # time.sleep(0.25)
#             time.sleep(0.25/4)
#         print("--------------------------------------")
#     #Release the lock        
#     l.release()

# #main program
# #todo Creating an object lock class
# l = threading.Lock()

# t1 =threading.Thread(target=multable,args=(16,)) #todo tuple object is this so that we always write into tuple format        
# t2 = threading.Thread(target =multable,args=(19,))
# t3 = threading.Thread(target =multable,args=(6,))
# #Dispatch thread
# t1.start()
# t2.start()
# t3.start()

#^---------------------------------------------------------------------------------------------------
#todo - with oops concept 

# import threading,time
# class kunal:
#     def multable(self,n):
#         l.acquire() #step 2
#         if n<=0:
#             print(f"invalid input{threading.current_thread().name} --->{n}")
#         else:
#             print("--------------------------------------------")
#             print(f"{threading.current_thread().name} --- {n}")    
#             for val in range(1,11):
#                 print(f"{threading.current_thread().name} --->{n} X {val} --->{n*val}")
#             time.sleep(0.25/4)
#         l.release() #step 3    
#         print("--------------------------------------------")
# #Main  program        
# #Creating lock object
# l = threading.Lock()# step 1
# t1 = threading.Thread(target=kunal().multable,args=(19,))
# t2 = threading.Thread(target=kunal().multable,args=(9,))
# # Dispatch the thread
# t1.start()
# t2.start()
#^---------------------------------------------------------------------------------------------------
# 

import threading,time
class multable :
    @classmethod
    def getlock(cls):
        cls.k=threading.Lock() # here k is an object of lock class
        
    def table(self,n):
        self.getlock()
        multable.k.acquire() #step 2
        if n<=0:
            print(f"invalid input{threading.current_thread().name} --->{n}")
        else:
            print("--------------------------------------------")
            print(f"{threading.current_thread().name} --- {n}")    
            for val in range(1,11):
                print(f"{threading.current_thread().name} --->{n} X {val} --->{n*val}")
                time.sleep(0.25/4)
        multable.k.release() #step 3    
        print("--------------------------------------------")
#Main  program        
#Creating lock object
# l = threading.Lock()# step 1
t1 = threading.Thread(target=multable().table,args=(19,))
t2 = threading.Thread(target=multable().table,args=(9,))

# Dispatch the sub threads
t1.start()
t2.start()

#^---------------------------------------------------------------------------------------------------







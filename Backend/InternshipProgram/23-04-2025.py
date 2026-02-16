
# import re
# pattern = 'a*'
# string = 'aaab'
# print(re.findall(pattern,string))

#?===================================================================================================

#! implementing the stack into the python

# class stack:
#     def __init__(self):
#         self.list1 = []
#     def push(self,item):
#         self.list1.append(item)
#         return self.list1
#     def pop(self):
#         if self.isempty():
#             print("List is Empty ")
#         else:
#             self.list1.pop()    
#             return self.list1
        
#     def peek(self):
#         if self.isempty():
#             print("List is Empty")
#         else:
#             return self.list1[-1]     
#     def isempty(self):
#         if len(self.list1) == 0:
#             return True
#         else:
#             return False
        
# # main program
# s = stack()        
# s.push(10)
# s.push(20)
# res1 = s.push(30)
# print(res1)

# res2 = s.pop()
# print(res2)

# res3 = s.peek()
# print(res3)

# s.pop()
# s.pop()
# print(res2)
# s.pop()

# # print(s.pop()) #* None
# print(res2)

# res4 = s.isempty()
# print(res4)

#?===================================================================================================

#! implementing the Queue using list FIFO

# class Queue:
#     def __init__(self):
#         self.queue = []
#     def insert(self,item)    :
#         self.queue.append(item)
#         return self.queue
#     def remove(self):
#         if self.isempty():
#             return "Queue is Empty"
#         else:
                    
#             self.queue.pop(0)
#             return self.queue

#     def front(self):
#         if self.isempty():
#             return "Queue is Empty"
#         else:
#             print(self.queue[0])    

#     def end(self)        :
#         if self.isempty():
#             return "Queue is Empty"
#         else:
#             print(self.queue[-1])    
#     def isempty(self):
#         if len(self.queue)==0:
#             return True
#         return False
    
# s = Queue()    
# s.insert(10)
# res = s.insert(20)
# print(res)  #* remove first element
# s.remove()
# print(res)
# print(s.isempty())
# s.front()
# s.end()

#?===================================================================================================
#! implement the Binary Search Tree using List 

# class BinarySerachTree():
#     def __init__(self):
#         self.list1 = []

        


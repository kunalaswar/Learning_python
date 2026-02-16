    #!
# class C1:
#     def draw(self): #original method
#         print("Draing C1")

# class C2(C1):
#     def draw(self):  #overhidden method
#         print("Drawing C2")        

# class C3(C2):
#     def draw(self):
#         C1.draw(self)
#         super().draw()      
#         print("Drawing C3")  

# c3 = C3()        
# c3.draw()

#^------------------------------------------------------------------------------------------------
#!

# class circle:
#     def draw(self):
#         print("Drawing circle ")

# class square(circle):
#     def draw(self):
#         print("Drawing square ")        

# class rect(square):
#     def draw(self):
#         print("Drawing rect ")        
#         # super().draw()
#         # super().draw()
#         square.draw(self)
#         super().draw()

# r = rect()        
# r.draw()

# class circle:
#     def area(self):pass

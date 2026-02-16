 #! 
#todo  -   1. Method Overriding
#todo  -   2. Constructor Overriding

#  class circle:
#     def draw(self): #original method
#         print(" Drawing circle ")

# class rect(circle):
#     def draw(self): #Overhidden method
#         print(" Drawing Rect ")
#         super().draw() #Calling super() Class original method and from derived class  

# r = rect() 
# r.draw() #todo - single function can call both the instance method 

#^------------------------------------------------------------------------------------------------
#! 1. Method Overriding
# class circle:
#     def draw(self):
#         print("Drawing Circle")
#         # super().draw()   #todo  -circle class is child class of object class but there is not A method draw()

# class rect(circle):
#     def draw(self):
#         print("Drawing rect")        
#         super().draw()
# r= rect() 
# r.draw()


#^------------------------------------------------------------------------------------------------
#!Polymorphism
# todo - polymorphism concept with Multilevel inheritance 
# class circle:
#     def draw(self):
#         print("Drawing circle ")
#         # super().draw() #todo - --AttributeError draw() does not exist in object class.     

# class rect(circle):
#     def draw(self):
#         print("Drawing rect ")        
#         super().draw()     

# class square(rect):
#     def draw(self):
#         print("Drawing square ")   
#         super().draw()     


# s = square()
# s.draw()
# # s.draw()
# # s.draw()

#^------------------------------------------------------------------------------------------------
#!Polymorphism  1. Method Overriding
# todo - polymorphism concept with Multipul inheritance 
# class circle:
#     def draw(self):
#         print("Drawing Circle ")
#         super().draw() #todo --AttributeError draw() does not exist in object class.            

# class rect:
#     def draw(self):
#         print("Drawing rect ")        
#         super().draw()       

# class square(rect,circle):
#     def draw(self):
#         print("Drawing Square ") 
#         super().draw()       

# s = square()        
# s.draw()


#^------------------------------------------------------------------------------------------------
#!polymorphism with multilevel inheritance 
#todo  -   2. class level polymorphism

# class circle(object):
#     def draw(self):
#         print("Drawing circle ")

# class rect(circle):
#     def draw(self):
#         print("Drawing rect ")        
#         # super().draw()
# class square(rect):
#     def draw(self):
#         print("Drawing square ")        
#         rect.draw(self)
#         circle.draw(self)

# s = square()        
# s.draw()

#^------------------------------------------------------------------------------------------------
#todo - class level polymorohism

# class circle:
#     def draw(self):
#         print("Drawing circle")


# class rect(circle):
#     def draw(self):
#         print("Drawing rect")        

# class square(rect):
#     def draw(self):
#         circle.draw(self)
#         rect.draw(self)
#         print("Drawing square ")      
#         # circle.draw(self)
#         # rect.draw(self)  

# s = square()        
# s.draw()

#^------------------------------------------------------------------------------------------------
#!
#todo - calling with BOTH METHOD
# class circle:
#     def draw(self):
#         print(" Drawing Circle ")
        

# class rect:
#     def draw(self):
#         print("Drawing rect ")        


# class square(rect):
#     def draw(self):
#         print("Drawing square ")
#         circle.draw(self)
#         super().draw()

# s = square()        
# s.draw()

#^------------------------------------------------------------------------------------------------
#todo - calling with BOTH METHOD
# class circle:
#     def draw(self):
#         print("Drawing circle ")

# class rect:
#     def draw(self):
#         print("Drawing rect")        

# # class square(circle,rect):
# class square(rect,circle):
#     def draw(self):
#         print("Drawing square ")  
#         rect.draw(self)      
#         circle.draw(self)      

# s = square()
# s.draw()

#^------------------------------------------------------------------------------------------------

#todo - 

# class circle:
#     def draw(self):
#         print("Drawing circle")

# class rect:
#     def draw(self):
#         print("Drawing rect")        

# class square(circle,rect):
#     def draw(self):
#         print("Drawing square")        
#         circle.draw(self)
#         rect.draw(self)


# s= square()
# s.draw()

#^------------------------------------------------------------------------------------------------
#!
# class circle:
#     def draw(self):
#         print("Drawing Circle")

# class rect:
#     def draw(self):
#         print("Drawing rect")        

# class square(rect,circle):
#     def draw(self):
#         print("Drawing square ")        
#         super().draw()
#         rect.draw(self)
#         # circle.draw(self)

# s = square()    
# s.draw()

#* OUTPUT:
#todo-  Drawing square 
#todo-  Drawing rect
#todo-  Drawing rect













#^------------------------------------------------------------------------------------------------






















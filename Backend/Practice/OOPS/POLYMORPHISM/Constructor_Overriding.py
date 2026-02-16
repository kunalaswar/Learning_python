
#! Constructor overriding 
# class C1:
#     def __init__(self):  #Original Constructor 
#         print("C1  - Deafult constructor ")

# class C2(C1):
#     def __init__(self):  #Original Constructor 
#         print("C2  - Deafult constructor  ")
#         super().__init__()

# class C3(C2):
#     def __init__(self):   #Overhidden Constructor 
#         print("C3  - Deafult constructor ")
#         super().__init__()

# c3 = C3()  #todo - Object is Created Constructor call automatically       


#!

# class C1:
#     def area(self):
#         print("C1 - Default constructor")

# class C2(C1):
#     def area(self):
#         print("C2 - Default constructor")        
# class C3(C2):
#     def area(self):
#         print("C3 - Default constructor")        
#         print("------------------------------")
#         super().area()
#         print("------------------------------")
#         C1.area(self)
# #Main program         
# c3 =C3()
# c3.area()

#! constructor

# from math import pi
# class circle:
#     def __init__(self):
#         self.r =int(input("Enter a radius :"))
#         # self.ar =3.14 *r*r
#         self.ar =pi *self.r*self.r
#         print("Area of circle ",self.ar)
# class square(circle):
#     def __init__(self):
#         self.s =int(input("Enter a Side of Square :"))
#         self.sa = self.s*self.s
#         print("Area of square ",self.sa)
# class rect(square):
#     def __init__(self):
#         self.l= int(input("Enter a  length :"))        
#         self .b =int(input("Enter a breadth :"))
#         self.ar = self.l*self.b
#         print("Area of  rect",self.ar)
#         print("-------------------------------")
#         super().__init__()
#         print("-------------------------------")
#         circle.__init__(self)

# r=rect()  #todo -  Object Creation---Makes the PVM to Call Constructor       


#! 
#todo - Dynamic input from User  
#* only call with super() METHOD

# from math import pi
# class circle:
#     def __init__(self,r):
#         self.ar = pi *r*r
#         print("Area of circle",self.ar)

# class square(circle):
#     def __init__(self,s):
#         self.sa = s**2
#         print("Area of Square ",self.sa )
#         super().__init__(int(input("Enter a  radius of circle:")))
# class rect(square):
#     def __init__(self,l,b):
#         self.ar = l * b
#         print("Area of rect",self.ar)
#         super().__init__(int(input("Enter a  side od Square :")))
# # main program         
# #Accept Length and breadth from Keyboard 
# l=int(input("Enter a length :"))
# b= int(input("Enter a breadth :"))
# r = rect(l,b) 


#!
#* only call with CLASS NAME 

# from math import pi
# class circle(object):
#     def __init__(self,r):
#         self.ar = pi*r*r
#         print("Area of Circle ",self.ar)

# class square(circle):
#     def __init__(self,s):
#         self.sa= s*s        
#         print("Area of square ",self.sa)
#         # print("------------------------------------------")
#         # circle.__init__(self,int(input("Enter a radius of circle :")))

# class rect(square):
#     def __init__(self,l,b):
#         self.ar = l*b        
#         print("Area of rect",self.ar)
#         print("------------------------------------------")
#         square.__init__(self,int(input("Enter a side od square :")))
#         print("------------------------------------------")
#         circle.__init__(self,int(input("Enter a radius of circle :")))

# #main program
# l = int(input("Enter a length :"))
# b = int(input("Enter a breadth  :"))
# r = rect(l,b)        

#!
#todo -  PolyExStrong15.py  
#&   Constuctor and instance method are both use in this program

# from math import pi
# class circle:
#     def __init__(self,r):
#         self.ac = pi*r*r
#         print("Area of  the circle ",self.ac)

# class square(circle):
#     def __init__(self,s):
#         self.sa = s*s        
#         print("Area of square ",self.sa)

# class rect(square):
#     def __init__(self,s=0):pass  #^ this is a parameterized 
#     def area(self,l,b):
#         self.ar =l*b        
#         print("Area of Rect",self.ar)
#         print("--------------------------------------------")
#         super().__init__(int(input("Enter a Side of Square :")))
#         print("--------------------------------------------")
#         circle.__init__(self,int(input("Enter a radius :")))


# l= int(input("Enter a Length "))
# b= int(input("Enter a breadth "))
# r = rect()        
# r.area(l,b)

#!
#todo - 
# from math import pi
# class circle:
#     def __init__(self,r):
#         self.ac =pi*r*2
#         print("Area of circle ",self.ac)

# class square(circle):
#     def __init__(self,s):
#         self.sa = s*s
#         print("Area of square",self.sa)

# class rect(square):
#     def __init__(self):
#         print("----------------------------------------------")
#         super().__init__(int(input("Enter a side Square :")))       
#         print("----------------------------------------------")
#         circle.__init__(self,int(input('Enter a radius :')))
#         print("---------------------------------------------")
#     def area(self,l,b):
#         self.ar = l * b
#         print("Area of rect",self.ar)



# r = rect() 
# l = float(input("Enter a length : "))
# b = float(input("Enter a breadth :"))

# r.area(l,b)


#^ DOING FOR PARTICE ONLY NOT A PROGRAM   
# class 
# class circle:
#     def __init__(self,r):
#         self.ac= 3.14*r*r
#         print("Area of the circle : ",self.ac)
# class square(circle):
#     def __init__(self,s):
#         self.sa = s*s      
#         print("Area of the square : ",self.sa)

# class rect(square):
#     def __init__(self):pass
#     def area(self,l,b):
#         self.ar = l*b
#         print("Area of Rect : ",self.ar)
#         super().__init__(int(input("Enter a Square Side :")))
#         circle.__init__(self,int(input("Enter a Circle Area :")))
# l = int(input("Enter a length :"))
# b = int(input("Enter a breadth :"))

# r = rect()        
# r.area(l,b)

#todo -
# class circle:
#     def __init__(self,r):
#         self.ac = 3.14*r*r
#         print("Area of Circle  = > ",self.ac)

# class Square(circle):
#     def __init__(self,s):
#         self.sa = s*s
#         print("Area of square = >",self.sa)
#         # super().__init__(int(input("Enter :  ")))
#         # super().__init__(int(input("Enter :  ")))
        
# class rect(Square):
#     def __init__(self,s=0):pass
#     def area(self,l,b):

#         self.ar= l*b
#         print("Area method ",self.ar)        
#         super().__init__(int(input("Enter SIDE :  ")))
#         circle.__init__(self,int(input("Enter RADIUS:  ")))

# # s=Square(2)
# r = rect()
# r.area(4,5)


































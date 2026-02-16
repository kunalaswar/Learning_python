 #!
#todo  - with the use of mehtod  wwith Dynamic input
# from math import  pi
# class circle:
#     def area(self):
#         self.a = round(float(input("Enter Radius :")))
#         self.ac = pi*self.a
#         print("Area of circle",self.ac)
#         print("---------------------------------")
# class square(circle):
#     def area(self):
#         self.s =float(input("Enter Side Value of  Square :"))
#         self.sa =self.s**2
#         print("Area of the square ",self.sa)
#         print("---------------------------------")
#         super().area()
# class rect(square):
#     def area(self):
#         self.l = int(input("Enter a of length1 :"))        
#         self.b = int(input("Enter a Breadth :"))
#         self.ar = self.l*self.b
#         print("Area of Rect",self.ar)
#         print("---------------------------------")
#         super().area()

# #Main program 
# r=rect()
# r.area()

#!
#todo  - with the use of mehtod  wwith Dynamic input
#todo - multilevel 
# from math import pi
# class circle(object):
#     def area(self):  #Original method
#         self.r = int(input("Enter Radius :"))
#         self.ac = pi *self.r*self.r
#         print("Area of Circle ",self.ac)
#         print("----------------------------")

# class square(circle):
#     def area(self): #Overhidden method
#         self.s = float(input("Enter a side of the Square :"))        
#         self.sa =self.s*self.s
#         print("Areaof square ",self.sa)
#         print("-------------------------------")

# class rect(square):
#     def area(self): #Overhidden method     
#         self.l = int(input("Enter a Length :"))
#         self.b = int(input("Enter a bridth :"))
#         self.ar = self.l*self.b
#         print("Area of rect",self.ar)
#         print("--------------------------------")
#         super().area()
#         circle.area(self)


# r= rect()        
# r.area()

#!
#todo  - multiple inheritance 

# from math import pi
# class circle(object):
#     def area(self):  #Original method
#         self.r = int(input("Enter Radius :"))
#         self.ac = pi *self.r*self.r
#         print("Area of Circle :",self.ac)
#         print("----------------------------")

# class square:
#     def area(self): #Overhidden method
#         self.s = float(input("Enter a side of the Square :"))        
#         self.sa =self.s*self.s
#         print("Area of square :",self.sa)
#         print("-------------------------------")

# class rect(circle,square):  #todo - super() method only call with first class
#     def area(self): #Overhidden method     
#         self.l = int(input("Enter a Length :"))
#         self.b = int(input("Enter a bridth :"))
#         self.ar = self.l*self.b
#         print("Area of rect :",self.ar)
#         print("--------------------------------")
#         super().area()
#         # circle.area(self)
#         square.area(self)



# r= rect()        
# r.area()

#!

# from math import pi
# class circle:
#     def area(self):  #Original method
#         self.r = int(input("Enter a Radius :")) 
#         self.ac = pi * self.r * self.r
#         print("Area of circle",self.ac)

# class square:
#     def area(self):  #Original method
#         self.s = int(input("Enter a side "))        
#         self.sa = self.s * self.s
#         print("Area of rect :",self.sa)

# class rect(square,circle):
#     def area(self):   #Overhidden method
#         self.l = int(input("Enter a Length :"))        
#         self.b = int(input("Enter a breadth :"))
#         self.ar = self.l*self.b
#         print("Area of rect :",self.ar)
#         print("----------------------------------")
#         super().area()
#         print("----------------------------------")
#         circle.area(self)


# r = rect()
# r.area()

#! mutlilevel inheritance
#todo - Taking Dyamnic input for  calling the method
#todo  - taking Dynamic input 
# from math import pi
# class circle:
#     def area(self,r): #Original method
#         self.ac =pi *r*r
#         print("Area of circle",self.ac)
# class square(circle):
#     def area(self,s):  #Original method
#         self.sa = s*s        
#         print("Area of square ",self.sa)
#         super().area(int(input("Enter a Radius :")))

# class rect(square):
#     def area(self, l,b):   #Overhidden  method
#         self.ar = l * b        
#         print("Area of rect ",self.ar)
#         super().area(int(input("Enter  a Side of aquare :")))
# #main program
# l =int(input("Enter a Length :"))
# b =int(input("Enter a Breadth :"))
# r = rect()        
# r.area(l,b)


#!multiple inheritance 
#todo - 
# from math import pi
# class circle:
#     def area(self,r):
#         self.ar =pi* r * r
#         print("Area of Cricle",self.ar)
# class square:
#     def area(self,s):
#         self.sa = s*s
#         print("Area of square ",self.sa)

# # class rect(circle,square):
# class rect(square,circle):
#     def area(self,l,b):
#         self.ar =l*b        
#         print("Area of rectangle ",self.ar)
#         super().area(int(input("Enter a side of circle :")))
#         # super().area(int(input("Enter a Radius of circle :")))
#         circle.area(self,int(input("Enter a radius of circle :")))
# #main program 
# l= int(input("Enter a length :"))
# b=int(input("Enter a breadth :"))
# r= rect()        
# r.area(l,b)

#!
#todo - CALLING WITH THE BOTH CLASS AND MEHTOD 

# from math import pi
# class circle(object):
#     def area(self,r):
#         self.ar = 3.14 *r*r
#         print("Area of circle ",self.ar)

# class square(circle):
#     def area(self,s):
#         self.sa = s*s
#         print("Area of Square ",self.sa)
#         print("------------------------------------------")
#         super().area( int(input("Enter a  radius  of circle :")))

# class rect(square):
#     def area(self,l,b):
#         self.ar =l*b        
#         print("Area of Rectangle ",self.ar)
#         print("------------------------------------------")
#         # square.area(self,int(input("Enter side of Square :")))
#         # print("------------------------------------------")
#         # circle.area(self,int(input("Enter radius of circle :")))
#         super().area( int(input("Enter a  Side of square :")))
#         # super().area()


# l= int(input("Enter a Length :"))
# b= int(input("Enter a Breadth  :"))
# r = rect()        
# r.area(l,b)


#!
#!PolyEx10.py
#todo - 

# from math import pi
# class circle:
#     def area(self,r):
#         self.ar =pi* r*r
#         print("Area of Circle ",self.ar)

# class square:
#     def area(self,s):
#         self.sa = s*s         
#         print("Area of Square ",self.sa )

# class rect(square,circle):
#     def area(self,l ,b):
#         self.ar = l * b        
#         print("Area of rect :",self.ar)
#         print("----------------------------------------")
#         square.area(self,int(input("Enter a side of square :")))
#         print("----------------------------------------")
#         circle.area(self,int(input("Enter a Area of circle :")))
# #main program
# l =int(input("Enter length "))
# b =int(input("Enter Breadth "))

# r = rect()        
# r.area(l,b)


#!
#todo - 

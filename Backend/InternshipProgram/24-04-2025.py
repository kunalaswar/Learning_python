
#We want to model a system where we have a base class for Person that contains basic information (like name and age). Then, we have a Student class that inherits from Person and adds information about the student's roll_number and grades. Finally, we have a GraduateStudent class that inherits from Student and adds additional attributes like the degree they are pursuing.'
#?====================================================================================================
# class person:
#     def f1(self):
#         self.name = "aniket" #input("Enter a Name")
#         self.age =  19       #int(input("Enter a ages "))



# class student(person):
#     def f2(self):
#         self.students_rollno = 101       #int(input("Enter roll number :"))
#         self.grades =  "A"                  #input("Enter  a student grade ")

# class GraduateStudent(student):
#     def f3(self):
#         self.degree = "BCA"

# #main program        
# obj = GraduateStudent()
# obj.f1()
# obj.f2()
# obj.f3()
# print(obj.name)
# print(obj.age)
# print(obj.students_rollno)
# print(obj.grades)
# print(obj.degree)



#?====================================================================================================

# class linear:
#     def getvals(self):
#         lst = [int(val) for val in input("Enter a value :").split()]
#         return lst
    
#     def search(self,lst):
#         lst.sort()
#         print(f"sorted list : {lst}")
#         skey = int(input("Enter search key : "))
#         ski = -1
#         for i in range(len(lst)):
#             if skey == lst[i]:
#                 ski  = i
#                 break
#         if ski == -1:
#             print(f"{skey} value doesn't exist in list ") 
#             print("search is unsuccessful ")
#         else:
#             print(f"the index of value {skey} in list of {ski}")    
#             print("Search is successful ")

# lo = linear()
# lst = lo.getvals()
# if len(lst) ==0:
#     print(f"list is empty : {lst}")
# else:
#     lo.search(lst)    

#?====================================================================================================

# def search(lst):
#     serach_val = int(input("Enter a value of seraching :"))

#     for i in range(len(lst)):
#         if lst[i] == serach_val:
#             return True
#     return -1

# lst = [int(val) for val in input("Enter value : ").split()]        
# s = search(lst)
# print(s)
#?====================================================================================================

# 2.Problem Scenario:
# We are designing a system that models different types of vehicles. The base class, Vehicle, contains common attributes for all vehicles (like brand and model). The Car class inherits from Vehicle and adds attributes specific to cars (like num_doors). Finally, the ElectricCar class inherits from Car and adds features specific to electric cars (like battery_capacity).

# class Vehicle:
#     def f1(self):
#         self.brand = "BMW"
#         self.model = 2020

# class Car(Vehicle) :
#     def f2(self):
#         self.num_doors = "yes"

# class ElectricCar(Car):
#     def f3(self):
#         self.battery_capacity = "50hr"

# e = ElectricCar()        
# e.f1()
# e.f2()
# e.f3()
# print("Brand :",e.brand)
# print("Model :",e.model)
# print("number doors :",e.num_doors)
# print("battery capacity :",e.battery_capacity)

#?====================================================================================================
# Multiple Inheritance
# Problem Scenario:
# We are modeling a Student class that can inherit from two different classes:
# 1.	Academic: This class holds academic-related information like grades and subjects.
# 2.	Extracurricular: This class holds extracurricular-related information like activities and awards.
# The Student class will inherit from both Academic and Extracurricular, thus allowing the student to have both academic and extracurricular information.

# class Academic:
#     def f1(self):
#         self.grades = "A"
#         self.subjects = "maths"
# class Extracurricular:
#     def f2(self):
#         self.Activities = "participate in Hackthons "
#         self.awards = 3
# class Student(Academic,Extracurricular):
#     def f3(self):
#         print("Grades :",self.grades)
#         print("Subject :",self.subjects)
#         print("Activities :",self.Activities)
#         print("Awards :",self.awards)
# s = Student()    
# s.f1()
# s.f2()
# s.f3()

#?====================================================================================================




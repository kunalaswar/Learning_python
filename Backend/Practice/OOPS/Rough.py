# # #!
# class studetns:
#     pass

# s1=studetns
# s2=studetns
# s1.sno=100
# s1.sname="kunal"
# s1.marks=80
# s2.sno=200
# s2.sname="sagar"
# s2.marks=99

# print("studetns Students number ",s1.sno)
# print("students name",s1.sname)
# print("studetns marks ",s1.marks)

# print("studetns Students number ",s2.sno)
# print("students name",s2.sname)
# print("studetns marks ",s2.marks)


#!
# class student :
#     pass

# s1=student
# s2=student
# s1.sno=int(input("Enter a Sno Number :"))
# s1.sname=input("Enter a Name :")
# s1.marks=float(input("Enter a number :"))
# s2.sno=int(input("Enter  a number :"))
# s2.sname=input("Enter a Name :")
# s2.marks=float(input("Enter a number :"))
# print("Studetns  number ",s1.sno)
# print("studetns Sname",s1.sname)
# print("Students marks",s1.marks)
# print("----------------------------------")
# print("students sno",s2.sno)
# print("students name",s2.sname)
# print("students marks",s2.marks)
# print("----------------------------------")



# class student:
#     pass



# s1=student()
# s2=student()
# print("Content of s1",s1.__dict__)
# print("Content os s2",s2.__dict__)
# print("Number os value in s1",len(s1.__dict__))
# print("NUmber of vlaue in s2",len(s1.__dict__  ))


#! Taking the value from Dynamic value and print Dymanically

# class students:
#     pass

# s1=students
# s2=students
# #place instance data member 
# s1.sno=int(input("Enter a strudent number"))
# s1.sname=input("Enter a students name")
# s1.marks=float(input("Enter a students marks"))

# print(s1.sno)
# print(s1.sname)
# print(s1.marks)


#!
# class student:
#     pass

#  s1=student()
# s2=student()
# s1.sno=10
# s1.sname="kunal"
# s1.marks=100
# print("students Content ",s1.__dict__)
# lst=list()
# for k in s1.__dict__.items():
#     print(k)
#     lst.append(k[1])    
# print(lst)    
    

# print("Studetns number",s1.sno)
# print("Studetns Name",s1.sname)
# print("Studetns Marks",s1.marks)

#todo 
# class student:
#     pass

# s1=student()
# s2=student()
# print(s1,type(s1))
# print(s2,type(s2))

#!#! WAY - 1)
# class students:
#     pass

# s1=students()
# s2=students()
# print("Students Contents ",s1.__dict__)
# s1.sno=int(input("Enter a Students number :"))
# s1.sname=input("Enter a students Name :")
# s1.marks=float(input("Enter  a students marks: "))
# # print()
# print(s1.sno)
# print(s1.sname)
# print(s1.marks)


#! WAY - 2)
# class student:
#     pass


# s1=student()
# s2=student()
# s1.sno=int(input("Enter a student number :"))
# s1.sname=input("Enter a students Name")
# s1.marks=float(input("Enter a students Marks"))
# print("Student Content ",s1.__dict__)
# for k,v in s1.__dict__.items():
#     print(f"{k} ---> {v}")

#todo - Class level data Member
#!
# class student:
#     crs="python"
#     city="HYD"


# s1=student()
# s1=student()
# print("Students Content Access with Class name",s1.__dict__)
# print(student.crs)
# print(student.city)
# print("Students Content Access with Object name",s1.__dict__)

# print(s1.crs)
# print(s1.city)

#!
# class student:
#     def readstud(self):
#         self.sno=int(input("Enter  a number: "))
#         self.sname=input("Enter a student name : ")
#         self.marks=float(input("Enter a student marks : "))

# s1=student()
# s2=student()
# s1.readstud()
# s2.readstud()
# for key,val in s1.__dict__.items():
#     print(f"{key}--->{val}")
# print("----------------------------------")
# for val in s2.__dict__.keys():
#     print(val, s2.__dict__.get(val))

#!

# class student:
#     def readstud(self):
#         self.sno=int(input("Enter a number :"))
#         self.sname=input("Enter a student name :")
#         self.marks=float(input("Enter a marks :"))


#     def disstud(self):
#         print(self.sno)    
#         print(self.sname)
#         print(self.marks)
# s1=student()
# s2=student()
        
# s1.readstud()        
# s2.readstud()
# s1.disstud()
# s2.disstud()


#todo -second way to see or access 
#!
# class student:
#     def readstud(self):
#         self.sno=int(input("Enter  a number :"))
#         self.sname=input("Enter a  students  name :")
#         self.marks=float(input("Enter a students marks :"))
#     def dispstud(self):

#         print(self.sno)
#         print(self.sname)
#         print(self.marks)


# s1=student()        
# s2=student()
# s1.readstud()
# s2.readstud()
# s1.dispstud()
# s2.dispstud()

#!

# class student:
#     def readstud(self):
#         self.sno=int(input("Enter studets number :"))
#         self.sname= input("Enter   a students name :")
#         self.marks=float(input("Enter  a students  marks :"))


# s1=student()        
# s2=student()
# s1.readstud()
# s2.readstud()
# for k,v in s1.__dict__.items():
#     print(f"{k}---> {v}")
# print("----------------------------")
# for k,v in s2.__dict__.items():
#       print(f"{k}---> {v}")


#!

# class students:
#     def read(self):
#         self.sno=int(input("Enter a number :"))
#         self.sname=input("Enter a Name ")
#         self.marks=float(input("Enter a studens marks :"))


# s1=students()        
# s2=students()
# s1.read()
# s1.read()
# # for val in s1.__dict__.items():
# #     print(f"{val}--->{s1.__dict__.get(val)}")

# for k,v in s1.__dict__.items():
#     print(f"{k}--->{v}")

# for v,k in s2.__dict__.items():
#     print(f"{k}--->{v}")


#^--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!
# class student:
#     def readstud(self):
#         self.sno=int(input("Enter a students number :"))
#         self.sname=input("Enter a students name :")
#         self.marks=float(input("Enter a students marks:"))
#     def dispstud(self):
#         # for k,v in self.__dict__.items():
#         #     print(k,v)
#         for k in s1.__dict__.keys():
#             print(k,s1.__dict__.get(k))
# s1=student()
# s1.readstud()
# s1.dispstud()


#^--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!

# 
#^-----------------------------------------------------------
# class student:
#     pass
    

# s1=student()    
# s2=student()
# print(id(s1),type(s1))
# print(id(s2),type(s2))

# #^----------------------------------------------------------------------------------------------------
#! 
# How to define or created instance variables?
# 1. Outside the class
# 2. Inside the class
# These variables are bind with object name
# Outside the class
# 1. Instance variables can be created outside the class after creating
# object.

# class student:pass

# s1=student()
# s2=student()
# print("ID of s1",id(s1))
# print("ID of s2",id(s2))
# s1.sno=100
# s1.name="harsh"
# s1.marks=90

# s2.sno=200
# s2.name="ankit"
# s2.marks=80
# print("----------------------------------------------------------")
# print("content of s1 students")
# print("students number ",s1.sno)
# print("students name",s1.name)
# print("studetns marks",s1.marks)
# print("----------------------------------------------------------")

# print("----------------------------------------------------------")
# print("content of s2 studetns")
# print("students number ",s2.sno)
# print("students name",s2.name)
# print("studetns marks",s2.marks)
# print("----------------------------------------------------------")

# #^---------------------------------------------------------------------------------------------------
#! Program for Storing Sno,name and marks by using Classes and Objects
#InstanceDataMembersEx2.py
# class student:
#     pass

# s1=student()    
# s2=student()
# print(id(s1))
# print(id(s2))
# print("Content of s1",s1.__dict__)
# print("content of s2",s2.__dict__)
# print("Number of value is s1",len(s1.__dict__))
# print("Number of value is s2",len(s2.__dict__))
# print("------------------------------------------")
# s1.sno=100
# s1.name="pratik"
# s1.marks=70

# s2.sno=200
# s2.name="paa"
# s2.marks=80
# print("content of s1",s1.__dict__)
# print("content of s1",s2.__dict__)
# print("NUmber of value is s1",len(s1.__dict__))
# print("NUmber of value is s2",len(s2.__dict__))

# print("------------------------------------------")


# print("-------------------------")
# #Display the Object Data of S1
# print("Content of s1 Object")
# for dmn,dmv in s1.__dict__.items():
#     print("\t{}---->{}".format(dmn,dmv))
# print("-------------------------")
# print("-------------------------")
# print("Content of s1 object")
# for key ,value in s1.__dict__.items():
#     print(f"{key}--->{value}")
# print("-------------------------")
# print("Content of s2 object ")
# for key in s2.__dict__.keys():
#     print(f"{key}--->{s2.__dict__.get(key)}")


# #^---------------------------------------------------------------------------------------------------
# #^---------------------------------------------------------------------------------------------------
#!

# class students:
#     pass

# s1=students()    
# s2=students()
# print(id (s1))
# print(id (s2))


# s1.__dict__={'sno':10,'sname':"aniket",'marks':50}
# s2.__dict__={'sno':20,'sname':"paa",'marks':80}
# print("Content of s1 ")
# print("studetns of number",s1.sno )
# print("studetns of NAME",s1.sname )
# print("studetns of MARKS",s1.marks )
# print("content of s2 ",s2)
# print("studetns of number",s2.sno )
# print("studetns of NAME",s2.sname )
# print("studetns of MARKS",s2.marks )
# #^---------------------------------------------------------------------------------------------------
# !


















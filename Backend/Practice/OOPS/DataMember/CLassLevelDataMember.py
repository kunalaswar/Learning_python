#
# class students:
#     pass

# s1=students()
# s2=students()
# print("content of the Students s1",s1.__dict__)
# print("content of students s2",s2.__dict__)
# print("length of the size ",len(s1.__dict__))
# print("length of the size",len(s2.__dict__))

# s1.sno=100
# s1.sname="kunal"
# s1.marks=90
# s2.sno=200
# s2.sname="paa"
# s2.marks=99
# print("content of the Students s1",s1.__dict__)
# print("content of students s2",s2.__dict__)
# print("length of the size ",len(s1.__dict__))
# print("length of the size",len(s2.__dict__))
# print(s1.sno)
# print(s1.sname)
# print(s1.marks)
# print("------------------------")
# print(s2.sno)
# print(s2.sname)
# print(s2.marks)
# print("------------------------")

#^-----------------------------------------------------------------------------------------------------
# #! 1) First way
# class student:
#     crs="python"
#     city="HYD"

# s1=student()    
# s2=student()
# print(s1)
# print(s2)

# print("student content ",s1.__dict__)
# print("Students content",s2.__dict__)
# print("studennts course",s1.crs)
# print("student city",s1.city)

# #^ OR with the help of the class name OR object name
# print("students course",student.crs)
# print("students city",student.city)


#^-----------------------------------------------------------------------------------------------------
#^ with in the main Program to create the class level data member


#! 2)second way
# class students:pass

    

# #main program     
# # ~Defining the data member in side the main program
# students.crs="python"
# students.city="HYD"
# s1=students()
# print("students content ",s1.__dict__)
# print("Students course",students.crs)
# print("Students city",students.city)

#^-----------------------------------------------------------------------------------------------------
#! program for Demonstrating the class level Data member  

# class student:
#     crs="python"
#     city="HYD"


# *Main program

# s1=student()
# s1.sno=100
# s1.sname="kunal"
# s1.marks=80
# print("Students number",s1.__dict__)

# s2=student()
# s2.sno=200
# s2.sname="harsh"

# s2.marks=100
# print("Content s1 Students")

# print("students sno",s1.sno)
# print("students name",s1.sname)
# print("students marks",s1.marks)
# print("STUDENTS COURSE =",s1.crs)
# print("STUDENTS CITY",s1.city)

# print("content of Students = > ",len(s1.__dict__))
# print("-------------------------------------")
# print("Content s2 Students")
# print("students sno",s2.sno)
# print("students name ",s2.sname)
# print("students marks",s2.marks)
# print("STUDENTS COURSE",s2.crs)
# print("STUDENTS CITY",s2.city)
# print("length of the students s2",len(s2.__dict__))
# print("------------------------------------")
#^-----------------------------------------------------------------------------------------------------
#! program for Developing the class level DATA MEMBER DYMANIC

# class students:
#     pass


# #*main program
# # students.crs="python"
# # students.city=""
# s1=students()
# s2=students()
# s1.sno=int(input("Enter Students a number :"))
# s1.sname=input("Enter a Students name :")
# s1.marks =float(input("Enter a Students Marsk :"))
# print("------------------------------------")

# s2.sno=int(input("Enter a students number"))
# s2.sname=input("Ente a students Name ")
# s2.marks=float(input("Enter students marks"))

# print("------------------------------------")
# print("Students NUmber",s1.sno)
# print("Students name" ,s1.sname)
# print("Students marks",s1.marks)
# print("------------------------------------")
# print("Students NUmber",s2.sno)
# print("Students name" ,s2.sname)
# print("Students marks",s2.marks)
#^-----------------------------------------------------------------------------------------------------

#!#Program for Demonstrating the Need of Class Level Data Members

# class students:
#     pass

# #*main program 
# #Defining the class level data member inside the MAIN PROGRAM
# students.crs="python"
# students.city="HYD"
# s1=students()
# print("Students Content",s1.__dict__)
# print("students course = ",s1.crs)
# print("Students city",s1.city)

# # print("Students Content",s1.__dict__)
# print("THIS DATA MEMBER ARE ACCESS WITH OBJECT NAME ")
# print("-------------OR---------------------")
# print("Students course",s1.crs)
# print("Studenets city",s1.city)
#^-----------------------------------------------------------------------------------------------------
#! Program for Storing Sno,name and marks by using Classes and Objects
# class students :
#     pass

# #* main program
# s1=students()
# s2=students()

# print("length of the students conternt",len(s1.__dict__))
# print("length of the students content",len(s2.__dict__))
# s1.sno=int(input("Enter a student snumber :"))
# s1.sname=input("Enter  a Students name")
# s1.marks=float(input("Enter a  students marks"))
# print("students number",s1.sno)
# print("students name",s1.sname)
# print("students marks",s1.marks)

#^-----------------------------------------------------------------------------------------------------
#!#Program for Storing Sno,name and marks by using Classes and Objects
#InstanceDataMembersEx3.py
# class students:
#     pass

# s1=students()
# s2=students()
# print("students content",s1.__dict__)
# s1.sno=100
# s1.sname="ankit"
# s1.marks=89
# print("Students content",s1.__dict__)
# for k,v in s1.__dict__.items():
#     print(f"{k} ---> {v}")
# print("------------------------------------")
# print("Content Students",s2.__dict__)
# s2.sno=200
# s2.sname="abhi"
# s2.marks=90
# print("Content Students",s2.__dict__)
# for k,v in s2.__dict__.items():
#     print(f"{k} ---> {v}")

# print("-------------------------------------")
#^-----------------------------------------------------------------------------------------------------
#!













#^-----------------------------------------------------------------------------------------------------













#^-----------------------------------------------------------------------------------------------------






#^-----------------------------------------------------------------------------------------------------






#^-----------------------------------------------------------------------------------------------------












#^-----------------------------------------------------------------------------------------------------





















#^----------------------------------------------------------------------------------------
#!Static Method Example -1 
# class Emp:
#  def getempvals(self):
#      self.eno = int(input("Enter Employee Number : "))
#      self.name = input("Enter Employee Name : ")
#      self.sal =  float(input("Enter Employee Salary : "))


# class student : 
#      def getstudvals(self):
#           self.sno = int(input("Enter Student Number :  "))
#           self.name = input("Enter Student Marks : ")

# class teacher :
#     def getteachervals(self):
#         self.tno = int(input("Enter Teacher Number : "))
#         self.name = input("Enter Teacher Name : ")
#         self.exp = int(input("Enter Teacher Experiance : "))
#         self.sub = input("Enter Teacher Subject : ")

# class Res:
#   @staticmethod
#   def displayvals(obj,objinfo):
#       print(f"{objinfo} Object Information")
#       print("-"*20)
#       for dmn,dmv in obj._dict_.items():
#           print(dmn,"-->",dmv)
#       print("-"*20)

# eo = Emp()
# so = student()
# to = teacher()
# eo.getempvals()
# print("-"*20)
# so.getstudvals()
# print("-"*20)
# to.getteachervals()
# print("-"*20)

# Res.displayvals(eo,"Employee")
# Res.displayvals(so,"Student")
# Res.displayvals(to,"Teacher")


# class Emp:
#  def getempvals(self,objinfo):
#      print(f"Enter Values for : {objinfo}")
#      print("-"*20)
#      self.eno = int(input("Enter Employee Number : "))
#      self.name = input("Enter Employee Name : ")
#      self.sal =  float(input("Enter Employee Salary : "))


# # class student : 
# #      def getstudvals(self,objinfo):
# #           print(f"Enter Values for : {objinfo}")
# #           print("-"*20)
# #           self.sno = int(input("Enter Student Number :  "))
# #           self.name = input("Enter Student Marks : ")

# # class teacher :
# #     def getteachervals(self,objinfo):
# #         print(f"Enter Values for : {objinfo}")
# #         print("-"*20)
# #         self.tno = int(input("Enter Teacher Number : "))
# #         self.name = input("Enter Teacher Name : ")
# #         self.exp = int(input("Enter Teacher Experiance : "))
# #         self.sub = input("Enter Teacher Subject : ")

# # class Res:
# #   @staticmethod
# #   def displayvals(obj,objinfo):
# #       print(f"{objinfo} Object Information")
# #       print("-"*20)
# #       for dmn,dmv in obj._dict_.items():
# #           print(dmn,"-->",dmv)
# #       print("-"*20)

# # eo = Emp()
# # so = student()
# # to = teacher()
# # eo.getempvals("Employee")
# # print("-"*20)
# # so.getstudvals("Student")
# # print("-"*20)
# # to.getteachervals("Teacher")
# # print("-"*20)

# # Res.displayvals(eo,"Employee")
# # Res.displayvals(so,"Student")
# # Res.displayvals(to,"Teacher")

#^----------------------------------------------------------------------------------------

#!Static Method Example -2
# class Emp:
#  def getempvals(self,objinfo):
#      print(f"Enter Values for : {objinfo}")
#      print("-"*20)
#      self.eno = int(input("Enter Employee Number : "))
#      self.name = input("Enter Employee Name : ")
#      self.sal =  float(input("Enter Employee Salary : "))


# class student : 
#      def getstudvals(self,objinfo):
#           print(f"Enter Values for : {objinfo}")
#           print("-"*20)
#           self.sno = int(input("Enter Student Number :  "))
#           self.name = input("Enter Student Marks : ")

# class teacher :
#     def getteachervals(self,objinfo):
#         print(f"Enter Values for : {objinfo}")
#         print("-"*20)
#         self.tno = int(input("Enter Teacher Number : "))
#         self.name = input("Enter Teacher Name : ")
#         self.exp = int(input("Enter Teacher Experiance : "))
#         self.sub = input("Enter Teacher Subject : ")

# class Res :
#     @staticmethod
#     def Displayobjinfo(obj,objinfno):
#         print(f"Display {objinfno} Object Information")
#         print("-"*20) 
#         for k,v in obj._dict_.items():
#             print(k,"->",v)
#         print("-"*20)


# e = Emp()
# s = student()
# t = teacher()
# e.getempvals("Employee")
# print("-"*20)
# s.getstudvals("Student")
# print("-"*20)
# t.getteachervals("Teacher")
# print("-"*20)

# r1 = Res()
# r1.Displayobjinfo(e,"Employee")
# r1.Displayobjinfo(s,"Student")
# r1.Displayobjinfo(t,"Teacher")
#^----------------------------------------------------------------------------------------
#!Static Method Example -3
# class Emp:
#  def getempvals(self,objinfo):
#      print(f"Enter Values for : {objinfo}")
#      print("-"*20)
#      self.eno = int(input("Enter Employee Number : "))
#      self.name = input("Enter Employee Name : ")
#      self.sal =  float(input("Enter Employee Salary : "))

#      print("-"*20)
#      Res.Displayobjinfo(self,"Employee")



# class student : 
#      def getstudvals(self,objinfo):
#           print(f"Enter Values for : {objinfo}")
#           print("-"*20)
#           self.sno = int(input("Enter Student Number :  "))
#           self.name = input("Enter Student Marks : ")
          
#           Res.Displayobjinfo(self,"Student")


# class teacher :
#     def getteachervals(self,objinfo):
#         print(f"Enter Values for : {objinfo}")
#         print("-"*20)
#         self.tno = int(input("Enter Teacher Number : "))
#         self.name = input("Enter Teacher Name : ")
#         self.exp = int(input("Enter Teacher Experiance : "))
#         self.sub = input("Enter Teacher Subject : ")

#         print("-"*20)
#         Res.Displayobjinfo(self,"Teacher")

# class Res :
#     @staticmethod
#     def Displayobjinfo(obj,objinfno):
#         print(f"Display {objinfno} Object Information")
#         print("-"*20) 
#         for k,v in obj._dict_.items():
#             print(k,"->",v)
#         print("-"*20)


# e = Emp()
# s = student()
# t = teacher()
# e.getempvals("Employee")
# s.getstudvals("Student")
# t.getteachervals("Teacher")

#^----------------------------------------------------------------------------------------
#!ArithmeticCalOops.py
# class Calculator:
#      def getvals(self):
#           self.a = int(input("Enter First Values : "))
#           self.b = int(input("Enter Second Values : "))
#           self.op = input("Enter Arithmetic Operator : ")

# class Result:
#      @staticmethod
#      def dispvals(obj):
#         match(obj.op):
#              case "+":
#                   print(f"sum = ({obj.a},{obj.b}) = {obj.a+obj.b}")
#              case "-":
#                   print(f"sub = ({obj.a},{obj.b}) = {obj.a-obj.b}")
#              case "*":
#                   print(f"mul = ({obj.a},{obj.b}) = {obj.a*obj.b}")
#              case "/":
#                   print(f"div = ({obj.a},{obj.b}) = {obj.a/obj.b}")
#              case "//":
#                   print(f"div = ({obj.a},{obj.b}) = {obj.a//obj.b}")
#              case "%":
#                   print(f"Modulodiv = ({obj.a},{obj.b}) = {obj.a%obj.b}")
#              case "":
#                   print(f"Pow = ({obj.a},{obj.b}) = {obj.a**obj.b}")
#              case _:
#                   print(f"{obj.op} is not a Arithmethic Operator")


# co = Calculator()
# while True:
#  try:
#   co.getvals()
#   Result.dispvals(co)
#  except ValueError:
#         print("Don't enter alnums,strs and symbols--try again")
#  else:
#       ch = input("do you want to do another operation-(yes,no) :").lower()
#       if ch == "no":
#        break
#^-----------------------------------------------------------------------------------------
#!ArithmeticCalOops2.py
# class Calculator:
#      def getvals(self):
#           self.a = int(input("Enter First Values : "))
#           self.b = int(input("Enter Second Values : "))
#           self.op = input("Enter Arithmetic Operator : ")

# class Result:
#      @staticmethod
#      def dispvals(obj):
#         match(obj._dict_['op']):
#              case "+":
#                   print(f"sum = ({obj._dict['a']},{obj.dict['b']}) = {obj.dict['a']+obj.dict_['b']}")
#              case "-":
#                   print(f"sub = ({obj._dict['a']},{obj.dict['b']}) = {obj.dict['a']-obj.dict_['b']}")
#              case "*":
#                   print(f"mul = ({obj._dict['a']},{obj.dict['b']}) = {obj.dict['a']*obj.dict_['b']}")
#              case "/":
#                   print(f"div = (({obj._dict['a']},{obj.dict['b']}) = {obj.dict['a']/obj.dict_['b']}")
#              case "//":
#                   print(f"div = ({obj._dict.get('a')},{obj.dict.get('b')}) = {obj.dict.get('a')//obj.dict_.get('b')}")
#              case "%":
#                   print(f"Modulodiv = ({obj._dict.get('a')},{obj.dict.get('b')}) = {obj.dict.get('a')%obj.dict_.get('b')}")
#              case "":
#                   print(f"Pow = ({obj._dict.get('a')},{obj.dict.get('b')}) = {obj.dict.get('a')**obj.dict_.get('b')}")
#              case _:
#                   print(f"{obj.op} is not a Arithmethic Operator")


# co = Calculator()
# while True:
#  try:
#   co.getvals()
#   Result.dispvals(co)
#  except ValueError:
#         print("Don't enter alnums,strs and symbols--try again")
#  else:
#       ch = input("do you want to do another operation-(yes,no) :").lower()
#       if ch == "no":
#        break

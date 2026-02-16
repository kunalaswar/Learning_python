

#*Matrix operation OR Arithmetic operation on ndarray object
#*Addition 
#*syntax -1
import numpy as np
# a = np.array([1,2,3,4]).reshape(2,2)
# b = np.array([10,20,30,40]).reshape(2,2)
# print("Matrix -A")
# print(a,type(a))
# print("Matrix -B")
# print(b,type(b))
# print("------------------------")
# c = np.add(a,b)
# print(c,type(c))
#^-----------------------------------------------------------------------------------------------
#*syntax -2
# import numpy as np 
# a = np.array([1,2,3,4]).reshape(2,2)
# b = np.array([10,20,30,40]).reshape(2,2)
# print("Matrix -A")
# print(a,type(a))
# print("Matrix -b")
# print(b,type(b))
# print("-----------------------------------------")
# c = a+b
# print(c,type(c))
#^-----------------------------------------------------------------------------------------------
#*substract()
#*syntax -1
# a = np.array([1,2,3,4]).reshape(2,2)
# b = np.array([10,20,30,40]).reshape(2,2)
# print("Matrix -a")
# print(a,type(a))
# print("Matrix -b")
# print(b,type(b))
# print("----------------------------")
# # c = np.subtract(a,b)
# print(c,type(c))

#*syntax -2
# a = np.array([1,2,3,4])
# a.shape = (2,2)
# b = np.array([10,20,30,40]).reshape(2,2)
# print("matrix -a")
# print(a,type(a))
# print("matrix -b")
# print(b,type(b))
# print("----------------------------------")
# c = np.subtract(b,a)
# print(c,type(c))

#^-----------------------------------------------------------------------------------------------
#*syntax -3
# a = np.array([1,2,3,4]).reshape(2,2)
# b = np.array([10,20,30,40]).reshape(2,2)
# print("Matrix -a")
# print(a,type(a))
# print("Matrix -b")
# print(b,type(b))
# print("----------------------------")
# # c = np.subtract(a,b)# another way 
# # c =a-b #another way
# c = b-a
# print(c,type(c))

#^-----------------------------------------------------------------------------------------------
#*multiply()
#* syntax -1
# a = np.array([1,2,3,4])
# a.shape = (2,2)
# b = np.array([10,20,30,40]).reshape(2,2)
# print("matrix -a")
# print(a,type(a))
# print("matrix -b")
# print(b,type(b))
# print("----------------------------------")
# c =np.multiply(a,b)
# print("Matrix c(Multiply operation )")
# print(c,type(c))

#^-----------------------------------------------------------------------------------------------
#* syntax -2
# a = np.array([1,2,3,4]).reshape(2,2)
# print("matrix -A")
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print("matrix -B")
# print(b,type(b))
# print("-----------------------------")
# c = np.multiply(b,a)
# print(c,type(c))
#^-----------------------------------------------------------------------------------------------
#* syntax -3
# a = np.array([1,2,3,4]).reshape(2,2)
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print(b,type(b))
# print("-------------------------------")
# c = a*b
# print("c -Matrix (Multiplication c)")
# print(c,type(c))
#^-----------------------------------------------------------------------------------------------
#*this work on the ROW and COLUMN into the Matrix --- >using np.dot(a,b)
# a = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix -A")
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print("Matrix -B")
# print(b,type(b))
# print("----------------------------")
# c = np.dot(a,b)
# print("ACTUAL MULTIPLICATION NOT ELEMENT WISE MULTIPLICATION :")
# print(c,type(c))

#^-----------------------------------------------------------------------------------------------
#*this work on the ROW and COLUMN into the Matrix --- >using np.matmul(a,b)
# a = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix -a")
# print(a)
# b = np.array([10,20,30,40]).reshape(2,2)
# print("Matrix -b")
# print(b)
# print("----------------------")
# # c = np.matmul(a,b)
# c = np.matmul(b,a)
# print("ACTUAL MULTIPLICATION NOT ELEMENT WISE MULTIPLICATION :")
# print(c)
#^-----------------------------------------------------------------------------------------------
#*divide()
#* syntax -1 ----by using --- 
# a = np.array([1,2,3,4]).reshape(2,2)
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print(b,type(b))
# print("----------------------------------")
# c = np.divide(a,b)
# print("Divide of c ")
# print(c,type(c))
#^-----------------------------------------------------------------------------------------------
#* syntax -2----by using --- 
# a = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix -A")
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print("matrix -B")
# print(b,type(b))
# print("--------------------------------")
# c = np.divide(b,a)
# print(c,type(c))
#^-----------------------------------------------------------------------------------------------
#* syntax -3----by using --- /
# a = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix -A")
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print("matrix -B")
# print(b,type(b))
# print("--------------------------------")
# c = a/b
# print(c,type(c))

#^-----------------------------------------------------------------------------------------------
#* syntax -4----by using --- /
# a = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix a")
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print("Matrix -b")
# print(b,type(b))
# print("-----------------------------")
# c = b/a
# print("Division (Actual Elementwise divide)")

#^-----------------------------------------------------------------------------------------------
#* floor_divide()
#* provide only interger value not float
#*syntax -1
# a = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix a")
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print("Matrix -b")
# print(b,type(b))
# print("-----------------------------")
# c = np.floor_divide(a,b)
# print("Floor Division (Actual Elementwise floor_divide)")
# print(c,type(c))

#^-----------------------------------------------------------------------------------------------
#*syntax -2 
#* provide only interger value not float
# a = np.array([1,2,3,4]).reshape(2,2)
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print(b,type(b))
# print("--------------------------------------")
# c = np.floor_divide(b,a)
# print("floor_division ")
# print(c)
#^--------------------------------------------------------------------------------------------------
# #* provide only interger value not float
# #*syntax -3 using -----//
# a = np.array([1,2,3,4]).reshape(2,2)
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print(b,type(b))
# c = a//b
# print("Floor division ")
# print(c,type(c))
# #^--------------------------------------------------------------------------------------------------
# #* provide only interger value not float
# #*syntax -4 ---//
# a = np.array([1,2,3,4]).reshape(2,2)
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print(b,type(b))
# c = b//a
# print("Floor division ")
# print(c,type(c))
# #^--------------------------------------------------------------------------------------------------
#* mod ()
# #*syntax -1
# a = np.array([1,2,3,4]).reshape(2,2)
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print(b,type(b))
# c = np.mod(a,b)
# print("Matrix Module division Reminder")
# print(c,type(c))
# #^--------------------------------------------------------------------------------------------------


# #*syntax -2
# a = np.array([1,2,3,4]).reshape(2,2)
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print(b,type(b))
# c = np.mod(b,a)
# print("Matrix Module division Reminder")
# print(c,type(c))

# #^--------------------------------------------------------------------------------------------------
# #*syntax -3
#* Using module operator -------%
# a = np.array([1,2,3,4]).reshape(2,2)
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print(b,type(b))
# c = a%b
# print("Matrix Module division Reminder")
# print(c,type(c))

# #^--------------------------------------------------------------------------------------------------
# #*syntax -4
#* Using module operator -------%
# a = np.array([1,2,3,4]).reshape(2,2)
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print(b,type(b))
# c = b%a
# print("Matrix Module division Reminder")
# print(c,type(c))

#^--------------------------------------------------------------------------------------------------
#*mod()
#* using mod() function  to find reminder
# a = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix -A")
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print("Matrix -B")
# print(b,type(b))
# c = np.power(a,b)
# print("#Find Elementwise Exponentiation--Power-off Operator")
# print(c,type(c))
# #^--------------------------------------------------------------------------------------------------
#*mod()
#* using mod() function  to find reminder
# a = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix -A")
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print("Matrix -B")
# print(b,type(b))
# c = np.power(b,a)
# print("#Find Elementwise Exponentiation--Power-off Operator")
# print(c,type(c))
# #^--------------------------------------------------------------------------------------------------
#*mod()
#* using Arithmetic operator --- **

# a = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix -A")
# print(a,type(a))
# b = np.array([10,20,30,40]).reshape(2,2)
# print("Matrix -B")
# print(b,type(b))
# c = a**b
# # c= b**a
# print("#Find Elementwise Exponentiation--Power-off Operator")
# print(c,type(c))
#^--------------------------------------------------------------------------------------------------


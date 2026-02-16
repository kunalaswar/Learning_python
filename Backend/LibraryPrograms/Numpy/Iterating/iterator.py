    #todo - Iterate the Data from ndarray object by using Loops
# import numpy as np
# a = np.random.randint(20,50,size= 6)
# print("content of a ")
# print(a)
# print("Dim of a =",a.ndim)
# print("------------------------")

# for val in a:
#     print(val)


#todo - Iterate the Data from ndarray object by using Loops 2D matrix
# import numpy as np
# # a = np.random.randint(20,50,size= 6)
# # a.shape = (2,3)
# #* OR
# a = np.random.randint(20,50,size= (3,3))
# print("content of a ")
# print(a)
# print("Dim of a =",a.ndim)
# print("------------------------")

# for row in a:
#     # print(val)
#     for col in row:
#         print(col,end=" ")
#     print()    


#todo - Iterate the Data from ndarray object by using Loops 2D matrix
# import numpy as np
# a = np.random.randint(20,50,size=(3,3,3))
# print(a)
# print("Dim of a =",a.ndim)
# print("-----------------------------")
# for row in a:
#     for col in row:
#         for val in col:
#             print(val,end=" ")
#         print()    

import numpy as np
# a = np.random.randint(20,50,size=(2,3,3))
# print(a)
# print("Dim of a = ",a.ndim)
# print("--------------------------")
# for matrix in a:
#     for row in matrix:
#         for col in row:
#             print(f"{col}",end=" ")
#         print()    

# How to create the 3-D matrix 
a = np.array([10,20,30,40,50,60,70,80,90])
# b = a.reshape(3,3) #* or
# print(b)
# print(a.reshape(3,3)) #* or
# 
# a.shape = (3,3) #* or
# print(a)

# lst = [[10,20],[30,40],[50,60],[70,80]]
# # print(lst)
# a = np.array(lst)
# print(a)
# print("dim of a =",a.ndim)


# lst = [[[10,20],[30,40]],[[50,60],[70,80]]]
# a = np.array(lst)
# print(a)
# print("Dim of a =",a.ndim)
# print("-------------------------")
# for row in a:
#     for col in row:
#         for val in col:
#             print(val,end=" ")
#         print()    

# lst = [10,20,30,40,50,60,70,80,90,15,25,35,45,55,65]
# a = np.array([10,20,30,40,50,60,70,80,90,15,25,35,45,55,65,75]).reshape(2,2,2,2)
# print(a)
# print("-------------------")
# for cluster in a:
#     for matrix in cluster:
#         for rows in matrix:
#             for cols in rows:
#                 print("\t",cols,end=" ")
#             print()    

#^  Iterate the data USING Numpy Function 
#todo - Iterate the Data from ndarray object by using nditer()

# a  =np.array([10,20,30,40,50,60,70,80])
# print(a)
# print("Dim of a =",a.ndim)
# print("-----------------------------")
# for val in np.nditer(a):
#     print(val)
    

#todo - Iterate the Data from ndarray object by using nditer() ---2D Martix

# a  =np.array([10,20,30,40,50,60,70,80,90]).reshape(3,3)
# print(a)
# print("Dim of a =",a.ndim)
# print("-----------------------------")

# for val in np.nditer(a):
#     print(val,end=" ")
    
#todo - Iterate the Data from ndarray object by using nditer() ---3D Martix
# a = np.arange(12).reshape(2,3,2)
# print(a)
# print("Dim of a =",a.ndim)
# print("--------------------------------")
# for val in np.nditer(a):
#     print(val,end=" ")

#todo - Iterate the Data from ndarray object by using nditer() ---3D Martix
# a = np.arange(3*3*3).reshape(3,3,3)
# print(a,type(a))
# print("Dim of a =",a.ndim)
# print("size of a=",a.size)
# print("---------------------------")
# for val in np.nditer(a):
#     print(val,end=" ")

#todo - Iterate the Data from ndarray object by using nditer() ---4D Martix
# a = np.arange(2*2*2*2).reshape(2,2,2,2)
# print(a)
# print("Dim of a = ",a.ndim)
# print("size of a = ",a.size)
# # print("------------------------")
# # # for val in np.nditer(a):
# # #     print(val,end=" ")

# a.shape = (16,)
# print(a)
# print("Dim of a = ",a.ndim)


#^-----------------------------------------------------------------------------------------------
# s = "RADAR"
# print(s.index("R"))
# print(s.index("A"))

# for val in enumerate(s):
#     print(val,type(val))
#     # print(val[0],"---> ",val[1])
    
# for index,value in enumerate(s):
#     print(f"{index} --->{value}")

# for index,value in enumerate(s):
#     if value=="R":
#         print(index," --->",value)

#todo -1D matrix or flated 
# a = np.array([10,20,30,40,50,60,70,80,90])
# print(a)
# print("Dim of a =",a.ndim)
# print("size of a =",a.size)
# print("---------------------------")


# for val in np.ndenumerate(a):
    # print(val,type(val)) # ((0,), np.int64(10)) <class 'tuple'>

# for index,value in np.ndenumerate(a):
#     print(index[0],value)

#todo -2D matrix 
# a = np.array([10,20,30,40,50,60,70,80,90]).reshape(3,3)
# print(a)
# print("Dim of a =",a.ndim)
# print("size of a =",a.size)
# print("---------------------------")
# for indval in np.ndenumerate(a):  
#     print(indval)  #((0, 0), np.int64(10))

# for indval in np.ndenumerate(a):
#     print(indval[0],"--->",indval[1])

    
# for indval in np.ndenumerate(a):
#     print(f"{indval[0][0]}--->{indval[0][1]}--->{indval[1]}")

# find the  Row Indices and Col indices of 2D -Matrix

# for indval in np.ndenumerate(a):
#     if indval[1]==10:
#         print(f"{indval[0][0]}--->{indval[0][1]}--->{indval[1]}")

a = np.random.randint(10,20,size=(3,2,2))
print(a)
print("Dim of a = ",a.ndim)
print("------------------------")

# for indval in np.ndenumerate(a):
    # print(indval,type(indval))

for indval in np.ndenumerate(a):
    print(f"{indval[0][0]}--->{indval[0][1]}--->{indval[0][2]} --->{indval[1]}")    
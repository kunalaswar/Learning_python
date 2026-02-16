 #Basic indexing in 1-D
# syntax :ndarrayobj[Index] 
# import numpy as np
# a = np.array([10,20,30,40,50,60,15,25,35])
# print("Content of a ")
# print(a)
# print("Dimension of a =",a.ndim)
# print("Data type of a ",a.dtype)
# print("shape of a =",a.shape)
# print("size of a =",a.size)

# #Get the value 10 from ndarray object
# print(a[0])
# print(a[1])
# print(a[-1])
# print(a[8])

# print(a[len(a)-1])

#todo -Basic indexing on 2-D matrix ----- collection of rows ans column

import numpy as np
# a = np.array([10,20,30,40,50,60,15,25,35])
# print(a,type(a))
# print("Dimension of a=",a.ndim)
# print("Data type of a= ",a.dtype)
# print("shape of a =",a.shape)
# print("size of a =",a.size)

# # print(a.reshape(3,3))
# # print("-----OR------")
# a.shape = (3,3)
# print(a)
# print(a[0,0]) #10
# print(a[-3,-3]) #10
# print(a[-3,0]) #10
# print(a[-3,0]) #10
# print("-------------------")
# print(a[0][1])
# print(a[-3][-2])
# print(a[-3,1])
# print(a[0,-2])
# print("------------------")


import numpy as np
# a = np.array([10,20,30,40,50,60,70,80,90,15,25,35])
# # print(a,type(a))
# # print("Dimension of a =",a.ndim)
# a.shape = (3,4)
# print(a)
# # print("Dimension of a= ",a.ndim)
# print("---------------------------")

# Get the complete rows By using indexing
# print(a[0])
# print(a[-3])

# Get the complete rows By using indexing
# print(a[1])
# print(a[-2])

#todo - Get the complete rows By using indexing
# print(a[2])
# print(a[-1])

# a = np.array([10,20,30,40,50,60,70,80,90,15,25,35]) #.reshape(2,3,2)
# print(a.reshape(2,3,2))
# a.shape = (2,3,2)
# print(a.ndim)
# a = np.array([10,20,30,40,50,60,70,80,90,15,25,35]).reshape(2,3,2)
# print(a)
# print("--------------------------------------")
# print("Dimension of a =",a.ndim)
# print("shape of a =",a.shape)
# print("Data type of a =",a.dtype)
# print("size of a =",a.size)

#todo - total 12 ways to find it 
# print(a[0,1,1]) #40
# print(a[0,1,-1]) #40
# print(a[-2,1,1]) #40
# print(a[-2,-2,-1]) #40
# print(a[-2,-2,1]) #40

# print(a[1,2,1])
# print(a[-1,-1,-1])
# print(a[1,2,-1])
# print(a[-1,2,-1])

#todo - Get complete First matrix with indexing
# print(a[0])
# print("--------")
# print(a[1])
# print("--------")
# print(a[-2])
# print("------------")
# print(a[-1])


#^----------------------------------------------------------------------------------------
#*Basic Indexing in 1-D---Obtains Single Element
#*Syntax: ndarrayobj[Index]
 
# import numpy as np
# a = np.array([10,20,30,40,50,60,70,80,90])
# print(a)

# print(a[0])
# print(a[1])
# print(a[-1])
# print(a[len(a)-1])
# print(a[-2])
# print(a[-len(a)])

#* Basic indexing in 2D(Matrix) ---Obtains Single Element
#*syntax -2: ndarrayobj [RowIndex] [ColIndex]
#* Here rowIndex and Colindex can be Either +ve or -ve
#^-------------------------------------------------------------------------------------------------
# import numpy as np
# a = np.array([10,20,30,40,50,60,70,80,90,47,67,43])
# a.shape=(3,4)
# print(a)

#*get the element 20

# print(a[0,1])
# print(a[-3,-3])
# print(a[0,-3])
# print(a[-3,1])
# print(a[0][1])
# print(a[-3][-3])
# print(a[0][-3])
# print(a[-3][1])

# print(a[0])
# print(a[-1])
# print(a[2])

#^-------------------------------------------------------------------------------------------------
#*Basic indexing in n-D (MatrixNumber,Rows,Clos) ---Obtains single Element
#*syntax-3:ndarrayobj [MatrixIndex,Rowsindex][Colindex]
#* Here matrix index ,RowIndex,ColsIndex can be either +ve or -ve

import numpy as np
a = np.array([10,20,30,40,50,60,70,80,90,47,67,43]).reshape(2,3,2)
print(a)

#* Get the Element 40
# print(a[0,1,1])
# print(a[0,1,-1])
# print(a[-2,-2,-1])
# print(a[0,-2,-1])
# print(a[0,1,-1])
# print(a[-2,1,-1])

#* sagar way
# print(a[0,1,1])
# print(a[-2,-2,-1])
# print(a[0,-2,-1])
# print(a[-2,1,1])
# print(a[0][1][1])
# print(a[-2][-2][-1])
# print(a[0][-2][-1])
# print(a[-2][1][1])
# print(a[0,1][1]) 
# print(a[-2][-2,-1])
# print(a[0,-2][-1])
# print(a[-2][1,1])


#*Get Complete First Matrix with Indexing
# print(a[0])
# print(a[-2])

#* Get Complete Second  Matrix with Indexing
# print(a[1])
# print(a[-1])

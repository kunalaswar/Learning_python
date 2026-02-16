
# import numpy as np
# a = np.array([10,20,30,40,50,60,70,80,90,15,25,35,55,65,75,12]).reshape(4,4)
# print(a)
# print("dim of a =",a.ndim)
# print("--------------------------")
# print(a[2:,::])
# print(a[2:,:])
# print(a[2::,::1])
#last two column
# print(a[::,2:])
# print(a[::1,2::])
# print(a[0::3,::3]) 
# print(a[0:4:3,0:4:3])
#

# print(a[::3,1:2:3]) # me
# print(a[::3,1:2]) #sir
# print(a[:4:3,1:2])

#todo -  3-D matrix slicing

# import numpy as np
# a = np.array([10,20,30,40,50,60,70,80,90,15,25,35,55,65,75,12]).reshape(2,4,2)
# print(a)
# print("dim of a =",a.ndim)
# print("--------------------------")

# print(a[0:1,1:3,::])
# print(a[0:1,1:3:,::1])
# print(a[:1,1:3:1,:])

# print(a[0:1,0:4:3,0:1])
# print(a[0:1,::3,0:1])

# print(a[0:2,0:1,::])
# print(a[::,0:1:1,0:2:1])
# print(a[:2,:1,:2])

# print(a[0:,1:3,0:2])
# print(a[::1,1:3,::1])



#todo -  4-D matrix slicing

# import numpy as np
# a = np.array([10,20,30,40,50,60,70,80,90,15,25,35,55,65,75,12]).reshape(2,2,2,2)
# print(a)
# print("dim of a =",a.ndim)
# print("--------------------------")

# print(a[0::3,0:2,::,::])
# print(a[0:2,0:1,:,:])
# print(a[0:2,:1,0:2,0:2])
# print(a[::,:1,::,::])
# print(a[0:2,0:2,0:1,::])
# print(a[:,:,0:1,:])
# print(a[::,::,:1,::])


#todo - Advance indexing and slicing 

import numpy as np
# a = np.array([10,20,30,40,50,60,70])
# print("content of a ")
# print(a)

# we want to 10 40 50 only by using indexing
#* step-1 -Identify the Indecies of taken them in Traditional object of python or ndarray of numpy
#* step-2 -pass the Traditional object OR Ndarray object with indices of Element of Element to the Ndarray object

# lst = [0,3,4] #tpl =(0,3,4)
# print(a[lst])

# OR 
# #step -1: Identify the Indices 0f 10 40 50
# b = np.array([0,3,4])
# #step-2: pass ndarray object b to ndarray object---a
# print(a[b])


#OR
# a[[0,3,4]]
# print(a[[0,3,4]])

# a[[-1,-2,1,0]]
# print(a[[-1,-2,1,0]])


# a = np.arange(0,25)
# print(a)
# print(a[[0,9,4,3,8]])

# a = np.random.randint(10,100,size=25)
# print(a)
# # print(a[[2,9,5,2,7,6]])
# #*I want to get --- --- ---
# # for index ,value in enumerate(a):
#     # print(f"{index} --->{value}")

# print(a[[5,23,5]])     

#todo - 2-D matrix
# a = np.random.randint(1,100,size = (5,5))
# print(a)
#* step for advance indexing and slicing with 2-D
#* step-1 :Identify the Row Indices of Elements place them in Traditional python object OR Ndarray object
#* step-2 :Identify the column Indices of Elements place them in Traditional python object OR Ndarray object
#* step-3:pass row indices and column Indices to ndarray object

# step-1
# rowind = [0,4] #OR  rowind =(0,4)
# # step-2
# colind = [0,4] #OR  colind =(0,4)
# step -3 pass the Rowind and colind to ndarray object
# a[rowind,colind]
# print(a[rowind,colind])

# print(a[(0,4),(0,4)])

# a = np.array([0,4]),np.array((2,4))
# print(a[np.array([0,4]),np.array((2,4))]) #*error is there

#* Get the principle digonal element ---
# print(a[[0,1,2,3,4],[0,1,2,3,4]]) #* internally processed as (0,0),(1,1),(2,2),(3,3),(4,4)
# print(a[np.array([4,3,2,1,0]),np.array((0,1,2,3,4))])

#get the Elements 
# print(a[[-5,-4,-1],[-5,-2,-4]])
# print(a[[0,1,4],[0,3,2]])


# a =np.random.randint(1,100,size=(3,3,3))
# print(a)
# # print(a[[0,1,2],[0,1,0],[0,1,1]])
# print(a[np.array([0,0,2,2]),np.array([0,2,0,2]),np.array([0,2,2,0])])

# ^--------------------------------------------------------------------------------------
#! Steps for Advanced Indexing on 1-D
# *Step-1: Identify the Indices of Elements and taken them in Traditional object of Python or ndarray obj
# *Step-2: Pass the Traditional Object OR Ndarray Object with Idices of Elements to the NDArray Object

import numpy as np
a = np.array( [10,20,30,40,50,60,70])
print(a)
print("-----------------------------------")

# # Step-1 Indentity the Indices of 10,40,50
# lst = [0,3,4] #tpl =(0,3,4)
# # Step- pass [0,3,4] to ndarry object  ---a
# print(a[lst])

#* OR
# Step-1 :Identify the Indices of 10 40 50
# b = np.array([0,3,4])
# print(b,type(b))
# print(a[b])

# #*OR
# # print(a[[0,3,4]])

# #* get 70 60 20 10
# print(a[[-1,-2,-6,0]])

# print(a[np.array([-1,-2,1,2])])

#& -------------------------------------------------------------------------------------------------

# import numpy as np
# a = np.arange(25,50)
# print(a)

# #0,10,13,15,24-----------Indices are 0 ,10,13,15,24
# print(a[[0,10,13,15,24]])

# import numpy as np
# a = np.random.randint(1,100,size=25)
# print(a)
# print(type(a))

# for val in enumerate(a):
#     print(val[0],"------>",val[1])

#& -------------------------------------------------------------------------------------------------
#step for Advance Indexing with 2D
# step -1 Identify the Row Indices of Element and Places them in Traditional Python object/ndarray object
# step -2 Identify the Row Indices of Element and Places them in Traditional Python object/ndarray object
# step -3 Pass Row Indices and Column Indecis to ndarray object


# import numpy as np
# a = np.array([
#     [57, 61, 98, 52, 94],
#     [90, 27, 28, 17, 37],
#     [69, 31, 27, 16, 64],
#     [98, 71, 85, 86, 60],
#     [49, 45, 33, 84, 31]
# ])
# print(a)

#* Get the Element 98 and 31
# rowindex = [0,4]
# colindex = [2,4]
# rowindex = [0]
# colindex = [2]
# print(a[rowindex,colindex])


# *Get the Principle Diagnol Elements---57,27,27,86 and 31
# print(a[[0,1,2,3,4],[0,1,2,3,4]])

# * Get the Elements 49,71,27,17 and 94
# print(a[np.array([4,3,2,1,0]),np.array([0,1,2,3,4])])

#* get the Element 57,17,45
# print(a[[-5,-4,-1],[-5,-2,-4]])
# print(a[[0,1,4],[0,3,1]])


# import numpy as np
# a = np.array(
#     [
#         [[47, 98, 63], [78, 42, 41], [97, 98, 74]],
#         [[20, 20, 18], [3, 27, 86], [11, 60, 99]],
#         [[67, 97, 83], [4, 75, 6], [14, 36, 87]],
#     ]
# )
# print(a)

#* get 47 3,14
# print(a[[0,1,2],[0,1,2],[0,0,0]])

#*Get 47 , 74 , 83 and 14
# print(a[[0,0,2,2],[0,2,0,2],[0,-1,-1,0]])



#*=================================================================================================
# find second maxinum in list
# lst = [4,5,2,8,9,13,15,15]
# max_1 = lst[0]
# for val in lst:
#     # print(val)
#     if max_1 < val :
#         max_1 =val
# print(max_1)    
    
# a = int(input("Enter :"))
# if a<0:
#     print("Ne")
# else:
#     print("po")    

#*=================================================================================================



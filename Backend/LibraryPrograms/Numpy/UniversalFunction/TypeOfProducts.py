  
#!product()
#*syntax = np.prod(arrobj)
#^=================================================================================================
#* 1D
#& product of Hole Array
import numpy as np
# arr = np.array([1,2,3,4])
# print(arr)
# #* product of the Hole data
# x = np.prod(arr)
# print(x) #----24 


#*syntax = np.prod([arrobj1,arrobj2])
#^=================================================================================================
#* 2D
#& product of Both array 1 aand array2
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([5,6,7,8])
# x = np.prod([arr1,arr2])
# print("Product of the Both array")
# print(x)  #* 1*2*3*4*5*6*7*8 = 40320

#^=================================================================================================
#* product of the two number
# *1x2x3x4x1x2x3x4 = 576 
#* syntax = np.prod([arr1,arr2])


# arr1 = np.array([1,2,3,4]).reshape(2,2)
# print(arr1)
# arr2 = np.array([1,2,3,4]).reshape(2,2)
# print(arr2)
# x = np.prod([arr1,arr2])
# print(x) # ----576

#^=================================================================================================
#* syntax = np.prod(arr,axis = 0)
#* Here axis=0 Represents Column Product
#* 2D 

# import numpy as np
# a= np.array([[1,2,3],[3,4,5]]) #* OR a = np.array([1,2,3,3,4,5]).reshape(2,2)
# # print(a)
# arr  = np.prod(a,axis=0) #* here axis = 0 column wise product
# print(arr)

#^=================================================================================================
#* Product Over an Axis
#* Here axis=1 Represents Row Product
#*2D
# import numpy as np
# arr =np.array([[1,2,3,],[3,4,5]]) #*OR arr = np.array([1,2,3,,3,4,5]).reshape(2,2)
# print("Given array ")
# print(arr)
# print("-----------------")
# x = np.prod(arr,axis=1) #* axis = 1 row - wise product
# print(x)

#^=================================================================================================

#*Perform Product in the following array over 1st axis:
#todo - Not a 2D data Only take 2 array and preform operation 

# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([5,6,7,8])
# newarr = np.prod([arr1,arr2],axis=1)  #* axis = 1 row - wise product
# * Here axis=1 Represents Row Product
# print(newarr) #* Returns: [24   1680]

#^=================================================================================================
#* perform Product in the following array over the 1st axis
#todo - Not a 2D data Only take 2 array and preform operation 
# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([5,6,7,8])
# newarr = np.prod([arr1,arr2],axis=0)  #* axis = 0 column - wise product
#* Here axis=0 Represents Column Product
# print(newarr) #* Returns: [ 5 12 21 32]


#^=================================================================================================

#* performing product in the following array over 1st lst
#todo - perform on the 2 array at a time 
#& Here axis = 1 represent row wise 

# import numpy as np
# arr1 = np.array([1,2,3,4]).reshape(2,2)
# arr2  = np.array([5,6,7,8]).reshape(2,2)
# print("---------------------------------")
# print("Array -1")
# print(arr1)
# print("---------------------------------")
# print("Array -2")
# print(arr2)
# print("----------------------------")
# newarr = np.prod([arr1,arr2],axis=1) #* Here axis=1 Represents Row Product
# print(newarr)

#^=================================================================================================

#*Perform Product in the following array over 1st axis:
#* performing product in the following array over 1st lst
#todo - perform on the 2 array at a time 
#& Here axis = 0 represent column wise 

# import numpy as np
# arr1 = np.array([1,2,3,4]).reshape(2,2)
# arr2  = np.array([5,6,7,8]).reshape(2,2)
# print("---------------------------------")
# print("Array -1")
# print(arr1)
# print("---------------------------------")
# print("Array -2")
# print(arr2)
# print("----------------------------")
# newarr = np.prod([arr1,arr2],axis=0) #* Here axis=0 Represents column Product
# print(newarr)

#!cumprod() 
#* syntax : varname = np.cumprod(arrobj)
#^=================================================================================================
#* take commulative product of all element for following array 
# import numpy as np
# arr  = np.array([5,6,7,8])
# print("content of a =")
# print(arr)
# newarr = np.cumprod(arr)
# print(newarr)


#^=================================================================================================
#* syntax : varname = np.cumprod(arrobj1,axis= 1) #* for Row 
#* 3D
#* Here axis = 1 represent cumulative Row product
# import numpy as np
# arr = np.array([[1,2,3],[3,4,5],[2,3,5]]) #*OR arr = np.array([1,2,3,3,4,5,2,3,5]).reshape(3,3)
# print("Content of a ")
# print(arr)
# print("-----------------------------------------")
# newarr = np.cumprod(arr,axis=1) #* Here axis=1 Represents Cumulative Row Product
# print(newarr) 

#& O/P :
# [[ 1  2  6]
#  [ 3 12 60]
#  [ 2  6 30]]
#^=================================================================================================
#* syntax : varname = np.cumprod(arrobj1,axis= 0) #* for Cols 

#* 3D
#* Here axis = 0 represent cumulative Column product

arr = np.array([[1,2,3],[3,4,5],[2,3,5]]) #*OR arr = np.array([1,2,3,3,4,5,2,3,5]).reshape(3,3)
print("Contnet  of arr  ")
print(arr)
print("----------------------------------")
x = np.cumprod(arr,axis=0) #* Here axis=0 Represents Cumulative Col Product
print(x)



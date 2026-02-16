
#!sort() function
#* sort function is in numpy module
#^=====================================================================================================
#* data stored itself

# import numpy as np
# a = np.array([10,2,13,14,25,16,-1,0,23])
# print("Given Ndarray data :")
# print(a)
# print("-----------------------")
# print("Data after sorting ")
# print(np.sort(a))

#^---------------------------------------------------------------------------------------------------
#* data Stored into NEW array 
# import numpy as np
# a = np.array([10,2,13,14,25,16,-1,0,23])
# print("Content of Given data :")
# print(a)
# print("----------------------------")
# b = np.sort(a)
# print("Sorted after sorting")
# print(b)
#^---------------------------------------------------------------------------------------------------
#* Data stored into itself
# import numpy as np
# a = np.array([10,2,13,14,25,16,-1,0,23])
# print("Given Ndarray object :")
# print(a)
# print("--------------------------")
# print(np.sort(a)[::-1])
# #* sorted Ndarray into DECREASING order 
## 
##
#^---------------------------------------------------------------------------------------------------
#* data Stored into NEW array 
# import numpy as np
# a = np.array([10,2,13,14,25,16,-1,0,23])
# print("Given Ndarray object :")
# print(a)
# print("-----------------------------------")
# print("Sorted Ndarray data :")
# c = np.sort(a)
# print(c)

#^---------------------------------------------------------------------------------------------------
#todo - rahala
# import numpy as np
# a = np.array([10,2,13,14,25,16,-1,0,23])
# print("Given Ndarray data ")
# print(a)
# print('----------------------------')
# b = np.sort(a)
# print("Sorted Data ")
# print(b)

#* Data stored into itself
#^---------------------------------------------------------------------------------------------------

#* find max and second max
import numpy as np
# a = np.array([10,2,13,14,25,16,-1,0,23])
# print("Given Ndarray data ")
# print(a)
# print('----------------------------')
# b = np.sort(a)[::-1]
# print("Sorted Data ")
# print(b)
# print("Max Element =",b[0])
# print("Second Max = ",b[1])
# print("Min Element =",b[-1])
# print("Second min = ",b[-2])

#^---------------------------------------------------------------------------------------------------
#* apply to 2D array   
#* default sort the 2d array data on the basic on the row (axis = 1)
import numpy as np #todo - Default = axis = 1  row - wise 
# a=np.array([10,2,13,14,25,16,-1,0,23]).reshape(3,3)
# print("Given ndarray data ")
# print(a) 
# print("Sorted ndarray data to the row - wise ")
# b = np.sort(a) #* default sort the 2d array data on the basic on the row (axis = 1)
# print(b)

#^---------------------------------------------------------------------------------------------------
#* sorting  2D data 
#* sort the 2d array data on the basic on the row (axis = 1)

# a=np.array([10,2,13,14,25,16,-1,0,23]).reshape(3,3)
# print("Given ndarray data ")
# print(a)
# print("Sorted ndarray data to the row - wise ")
# b = np.sort(a,axis=1) #* sort the 2d array data on the basic on the row (axis = 1)
# print(b)

#^---------------------------------------------------------------------------------------------------
#*sorting 2D data 
#*sort the 2D array data on the basic on the column

# a=np.array([10,2,13,14,25,16,-1,0,23]).reshape(3,3)
# print("Given Ndarray data ")
# print(a)
# print("------------------------")
# b = np.sort(a,axis=0)#*  sort the 2D array data on the basic on the column
# print("Data after sorting Column wise ")
# print(b)

#^---------------------------------------------------------------------------------------------------
#* sort the complete 2D Array data 
#* Hole  data  is sorted 
# a=np.array([10,2,13,14,25,16,-1,0,23]).reshape(3,3)
# print("Given Ndarray data ")
# print(a)
# print('------------------------------')
# #* first convert the 3D into 1D array 
# # Flatten the data 
# a = a.flatten() #todo - convert the 2D array into the Flatten array 
# a = np.sort(a)# todo - to sort the array 
# a.shape = (3,3)
# print("Sorted Ndarray data ")
# print(a)
# print("-----------------------------")

#^---------------------------------------------------------------------------------------------------

# a=np.array([10,2,14,6]).reshape(2,2)
# print("Given Ndarray data ")
# print(a)
# print("------------------------------------")
# print("Sorted the hole Matrix ") #
# #* first convert the 2D data into the 1D 
# #* with the use of the Flatten() function
# a = a.flatten()
# # print(a)
# a= np.sort(a)
# a.shape = (2,2)
# print(a)


#
#^---------------------------------------------------------------------------------------------------

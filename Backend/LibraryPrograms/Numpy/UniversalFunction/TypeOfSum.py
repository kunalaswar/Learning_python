

#todo  - types of sum 
#* add the two matrix

import numpy as np
# arr1 = np.array([1,2,3])
# arr2 = np.array([1,2,3])
# newarr =  np.add(arr1,arr2)
# print(newarr)
#^---------------------------------------------------------------------------------------------------
#* Add the 2D array matrix 

# arr1 = np.array([1,2,3,4]).reshape(2,2)
# arr2 = np.array([1,2,3,4]).reshape(2,2)
# newarr = np.add(arr1,arr2) #* using add() function 
# print("-----------------------------")
# print(newarr)

#^---------------------------------------------------------------------------------------------------
#* Add the 3D array matrix 
#* it provide only one value becauisee sum os only ONE

# import numpy as np
# a = np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# # print(a)
# b = np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# # print(b)
# newarr = np.add(a,b) #*using add function 
# print(newarr)

#^---------------------------------------------------------------------------------------------------
#todo - sum() function with 1D array 
#* sum the both value in arr1 and arr2
# arr1 =np.array([1,2,3]) 
# arr2 =np.array([1,2,3]) 
# # print("Sum of all the vlaue ")
# c = np.sum([arr1,arr2]) #* put he Value into the list[ ] format
# print("Sum of all both the matrix")
# print(c)
#^---------------------------------------------------------------------------------------------------
#todo - sum() function with 2D array 
#* sum both the value in arr1 and arr2
#& sum provide always one value 
# arr1  = np.array([1,2,3,4]).reshape(2,2)
# arr2  = np.array([1,2,3,4]).reshape(2,2)
# print("SUM of the both matrix ")
# newarr = np.sum([arr1,arr2])
# print(newarr)

#^---------------------------------------------------------------------------------------------------

#todo - sum() function with 2D array 
#& sum provide always one value 
#* sum both the value in arr1 and arr2
#* syntax = np.sum([arrobj1,arrobj2])

# arr1  = np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# arr2  = np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# print("SUM of the both matrix ")
# newarr = np.sum([arr1,arr2])
# print(newarr)
#^---------------------------------------------------------------------------------------------------
#!colun wise on 1D
#!colun wise on 2D
#!colun wise on 2D
#* column - column wise sum so axis = 1 
#todo -  # Col-Col Elements Considers
#* syntax = np.sum([arrobj1,arrobj2],axis = 1)
# arr1 = np.array([1,2,3,4]).reshape(2,2)
# arr2 = np.array([1,2,3,4]).reshape(2,2)
# #we want to column- wise we use  axis = 1
# print(arr1)
# print(arr2)
# newarr = np.sum([arr1,arr2],axis=1)
# print("---------------------------")
# print("Column - wise sum ")
# print(newarr)

#^---------------------------------------------------------------------------------------------------
#!row wise on 1D
#!row wise on 2D
#!row wise on 2D
#*row - row wise  Element so axis = 0
#todo - Row - Row Element considers
#* syntax = np.sum([arrobj1,arrobj2],axis = 0)
# arr1 = np.array([1,2,3,4]).reshape(2,2)
# arr2  = np.array([1,2,3,4]).reshape(2,2)
# #we want  row wise so that we use axis = 0
# print("ROW - ROW wise sum ")
# print(arr1)
# print(arr2)
# print("-------------------------------------------")
# newarr = np.sum([arr1,arr2],axis=0)
# print(newarr)

#! Cummulative Sum
#! cumsum()
#^==================================================================================================
#* syntax = np.cumsum(arrayobj)
#* [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
#* 1D
#& perform partical sum with cumsum() function 
# import numpy as np
# a = np.array([1,2,3,4])
# arr = np.cumsum(a)
# print(arr)

#^---------------------------------------------------------------------------------------------------
#* 2D
#todo - cumsum on the 2D array object
# a = np.array([1,2,3,4]).reshape(2,2)
# print(a)
# arr  = np.cumsum(a)
# print(arr)








# lst = [1,2,3,4,5,6]
# m  = 0
# secondmax = 0
# for val in lst:
#     if val>m:
#         m = val
#         secondmax = secondmax = val
#     elif secondmax < val<m:
#         secondmax = val     
# print(m)        
# print(secondmax)


# lst = [1,2,3,4,5,6]
# m = 0
# for val in lst:
#     if val>m:
#         m = val      
# print(m)
# sm  = 0
# for val in lst:
#     if val ==m:pass
#     # elif val 


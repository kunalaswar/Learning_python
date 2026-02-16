
#!   split()
#* syntax:varname = np.split(array,size of an array to split)
#todo - first axis=0 means ROW
#^=======================================================================================================
# import numpy as np
# # Creating an Array 
# array = np.arange(6)
# # print(array)
# #* Splitting the array into 2 Equal parts along the first axis(axis= 0)
# x = np.split(array,2)
# print("\tresult after numpy.split()")
# print(x)

#^=======================================================================================================
#*print the array with the help of for loop
#todo - printing the data 
# import numpy as np
# # creating an example array 
# array = np.arange(6)
# #* splitting the array into 2 Equal parts along with first axis(axis =0)
# x = np.split(array,2)
# print("\tresult after numpy.split()")
# print(x)
# print("-------------------")
# for arr in x:
#     print(arr,end=" ")

#^=======================================================================================================
#* this array can not split the odd array Element 
#todo - split() function can cot split the unequal array 
# import numpy as np
# #* creating an example array 
# array = np.arange(7)
# #* Splitting the array into 2 Equal part along with first axis (axis = 0)
# x = np.split(array,2)
# print("\tresult after numpy.split()")
# print(x,type(x))  #&ValueError: array split does not result in an equal division
# print("------------------------------------")

#^=======================================================================================================
#* Splitting the array into 4 unequal parts along the first axis (axis=0) 
#todo - spliting array into UnEqual part 
# import numpy as np
# # Creating an array 
# array  = np.arange(7)
# #* spliting the array into 4 unequal parts along the first axis (axis =0)
# # print(len(array))
# print("Array ")
# print(array)
# x = np.array_split(array ,2)
# print("\n Result after numpy.array_split()")
# print(x)

#^=======================================================================================================

# import numpy as np
# arr = np.arange(13)
# print("Array :")
# print(arr)
# #* spliiting the array into 4 unequal part along with first axis(axis = 0)
# x = np.array_split(arr,4)
# print("\tResult after numpy.array_split()")
# print(x)
# print("------------------------------------")
# for val in x:
#     print(val,end= " ")

#^=======================================================================================================
#todo - 
# import numpy as np
# #* Creating an Array
# arr = np.arange(12)
#* Splitting the array into unequal part along the first axis (axis = 0)
# print("Array ")
# print(arr)
# print("----------------------")
# result = np.array_split(arr,4) #todo - 
# print("\tResult after numpy.array_split()")
# print(result)
# print("-----------------------")
# for val in result:
#     print(val,end =" ")

#^=======================================================================================================
#* second axis (axis =1) means column
#* 

# import numpy as np
# # Creating a 2D array     
# array = np.array([[3,2,1],[8,9,7],[4,6,5]])
#todo - Splitting the array into 3 equal parts along the second axis(axis = 1)
# result = np.split(array, 3 ,axis=1)
# print("2D Array :")
# print(array)

# print("\tResult after numpy .split() along axis = 1")
# print(result)

#^=======================================================================================================

# import numpy as np
#* Creating the array object
# arr = np.array([[3, 2, 1], [8, 9, 7], [4, 6, 5]])
# #* Spliting the array into 3 Equal part along the second axis (axis =1)
# result = np.split(arr,3,axis=1)
# print("array 2")
# print(arr)
# print("\t Result after numpy.split() along axis =1")
# print(result)

#^=======================================================================================================
# import numpy as np

# # Creating a 2D array
# array = np.array([[3, 2, 1], [8, 9, 7], [4, 6, 5]])
# #* Splitting the array into 3 equal parts along the first axis (axis =0)
# result = np.split(array,3,axis=0)
# print(" 2D Array :")
# print(array)
# print("After numpy.split() along axis=0")
# print(result)

#^=======================================================================================================
# #todo - printing the 2D array with for loop
# import numpy as np
# arr = np.array([[3, 2, 1], [8, 9, 7], [4, 6, 5]])
# print("2D Array ")
# print(arr)
# #* Splitting the array into 3 equal parts along the first axis (axis =0)
# result = np.split(arr,3,axis=1)
# print("\t Result numpy.split() along axis=0")
# print(result)
# print("-----------------------")
# for val in result:
#     print(val,end =" ")

#^=======================================================================================================
#todo - Creating an ndarray Matrix
# import numpy as np
# martix  = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# #* Vertically Splitting into 2 subarrays along axis = 0
# print("matrix :")
# print(martix)
# result = np.vsplit(martix,2)
# print("\t Result after numpy.vsplit()")
# print(result)

#^=======================================================================================================

#todo - Creating an Ndarray 
# import numpy as np
# matrix  = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# #* Vertically Splitting into 2 subarrays along axis = 0
# print("Array - 2D")
# print(matrix)
# result = np.split(matrix,2,axis =0)
# print("\n Result after numpy.split()")
# print(result)

#^=======================================================================================================
#*
# import numpy as np
# #* Creating the 2D array 
# array = np.array([[3,2,1],[8,9,7],[4,6,5]])

# print("2D Array ")
# print(array)
# print("--------------------------------------------------")
# #* Splitting the array into 3 equal  parts along with the First axis (axis =0)
# result = np.split(array,3,axis=0) #todo - Here axis=0Represents Rows
# print("2D Array ")
# print(array)
# print("\n Result after numpy.split() along axis =0")
# print(result)
# print("------------------------")
# for rows in result:
#     # print(val)
#     for cols in rows:
#         print(cols)
#     # print()

#^=======================================================================================================
#!   vsplit()
#* syntax: varname = np.vsplit(matrix , 2)
#*   Creating the  Matrix 
# # Creating an example matrix
# import numpy as np
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print("Array -2D")
# print(matrix)
# #* Vertical splitting into 2 subarray along axis =0

# result = np.vsplit(matrix,2)
# print("Matrix  :")
# print(result)


#^=======================================================================================================
#todo   OR 
#* Creating the Matrix 
# import numpy as np
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print("Array -2D")
# print(matrix)
# #* Vertical splitting into 2 subarray along axis =0
# result = np.split(matrix,2,axis= 0 ) #todo - OR with out the vsplit() function 
# print("\nResult after numpy vsplit()")

# print(result)

#^=======================================================================================================
#* creating  an example matrix
#* Vertical splitting into 2 subarrays along axis=0

# import numpy as np
# # Creating an example matrix
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# print("Matrix :")
# print(matrix)
# result   = np.vsplit(matrix,2)
# print("Result after numpy.split ")
# print(result)

#^=======================================================================================================
# import numpy as np
# # Creating the 2D array 
# array = np.array([[3, 2, 1], [8, 9, 7], [4, 6, 5]])
# print(array)
# print()
# print("'Contnet woth defines")
# result = np.split(array,axis=0)

#^=======================================================================================================
# Creating an example matrix
# import numpy as np
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print("Array -2D")
# print(matrix)
# print("---------------------------------")
# x = np.split(matrix,2,axis=0 )
# print("\n Result after numpy.split()")
# print(x)

#^=======================================================================================================
#*
# import numpy as np
# array  = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print("Matrix ")
# print(array)
# print("-------------------------------------")
# result = np.hsplit(array ,2)
# print(result)
# print("--------------------------------")
# print("\nResult after numpy.split()")
# print(result)


#^=======================================================================================================
# import numpy as np
# array = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print("Matrix ")
# print(array)
# print("\n result after numpy.hsplit()")
# x = np.hsplit(array ,2)
# print(x)

#^=======================================================================================================



















#^=======================================================================================================














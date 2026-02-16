
#!diff()
#*syntax: varname = np.diff(Ndarrobj)
#^===================================================================================================
#* compute discrete difference of the   following array
# import numpy as np #[2-1, 3-2, 4-3] = [1, 1, 1]
# arr = np.array([10, 15, 25, 5])
# print("Given Array :",arr)
# newarr = np.diff(arr)
# print("Discrete difference array :",newarr)

#^===================================================================================================
#todo - find the array double Discrete difference 
#* n = 2 that meaning is that to find Double Discrete Difference of the array 

#*syntax: varname = np.diff(Ndarrobj,n = 2)
#todo -syntax: varname = np.diff(Ndarrobj,n = How many time you want to find Discrete difference)
# import numpy as np
# arr = np.array([10,15,25,5])
# print("Given Array :",arr)
# newarr  = np.diff(arr,n = 2) #todo  n = 2
# print("Discrete differece array = ",newarr)

#^===================================================================================================
#todo - find the array Third time Discrete difference 
#* n = 2 that meaning is that to find Double Discrete Difference of the array 

#*syntax: varname = np.diff(Ndarrobj,n = 3)
#todo -syntax: varname = np.diff(Ndarrobj,n = How many time you want to find Discrete difference)

# import numpy as np
# arr = np.array([10,15,25,5])
# print("Given array = ",arr)
# newarr = np.diff(arr  ,n=3) #* n = 3
# print("Discrete difference Array :",newarr)

#^===================================================================================================

#* Compute discrete difference of the following 2D array    
# Here axis=0 Represents  Column Discrete Difference

# import numpy as np
# arr = np.array([[1,2,3],[3,4,5],[2,3,5]])
# print("Content of arr :")
# print(arr)
# print("----------------------------")
# x = np.diff(arr,axis=0) #* Here axis=0 Represents  Column - wise Discrete Diff
# print("Discrete difference Array :")
# print(x) 
#O/P:-
# [[ 2  2  2]
#  [-1 -1  0]]

#^=====================================================================================================
#* compute 
#* compute Discrete difference of the following 2D array 
# import numpy as np
# arr = np.array([[1,2,3],[3,4,5],[2,3,5]])
# print("COntent of array ")
# print(arr)
# print("----------------------")
# x = np.diff(arr,axis = 1) # Here axis = 1 represents Rows Discrete Diff
# print("Discrete difference array :")
# print(x)

#^=====================================================================================================

#*compute the Discrete difference of the following 2D Array
 #* Here  axis =1 Represents Rows-wise Discrete Difference
# import numpy as np
# arr = np.array([[1,2,3],[3,4,5],[2,3,5]])
# print("Content of Arr")    
# print(arr)
# print("----------------------")
# x = np.diff(arr,n =2,axis=1) #* Here  axis =1 Represents Rows-wise Discrete Difference
# print(x)

#^=====================================================================================================

#* compute discrete difference  of the following 2D Array
# import numpy as np
# arr = np.array([[1,2,3],[3,4,5],[2,3,5]])
# print("Content of arr :")
# print(arr)
# print("---------------------------")
# x = np.diff(arr,n=2,axis=0) #* Here  axis =0 Represents column-wise Discrete Difference
# print("Discrete difference Array with Column")
# print(x)

#^=====================================================================================================










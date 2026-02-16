
#! unique()
#^==================================================================================================
#* remove dubplicate from ndarray in the from of set 
#* 

# import numpy as np
# arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
# print(arr)
# x = np.unique(arr)
# print(x)

#^==================================================================================================
#*ndarray object pass to the unique() function
#* 2D
# import numpy as np
# arr = np.array([10, 10, 10, 20, 30, 20, 30, 10, 40,30]).reshape(2,5)
# print("Array ")
# print(arr)
# print("---------------------------")
# x = np.unique(arr) #* get all unique Element to in ndarray
# print("Unique Elements (set conpect in numpy)")
# print(x,type(x))


#^==================================================================================================
#* 3D

# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8,9,1,2,3]).reshape(2,2,3)
# print("Array ")
# print(arr)
# print("------------------------------")
# x = np.unique(arr)
# print("Unique Elements of 3D array (set conpect in numpy)")
# print(x)  #![1 2 3 4 5 6 7 8 9]

#^==================================================================================================

#! union1d()
#* find union of the follwing two set arrays:
#* to combine to the element

# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])
# print("Array -1")
# print(arr1)
# print("Array -2")
# print(arr2)

# newarr = np.union1d(arr1,arr2) #* Remove dublicate data from both array 
# print("Union Array :")
# print(newarr)
#^==================================================================================================
# #* direct passing the array
# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])
# print("Array -1")
# print(arr1)
# print("Array -2")
# print(arr2)
# print("------------------")
# print(np.union1d(arr1,arr2))

# #* OR
# print(np.union1d(arr2,arr1))

#^==================================================================================================
#!intersect1d()
# #*Find Intersection of the following two set arrays:
# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])
# print("Array -1")
# print(arr1)
# print("Array -2")
# print(arr2)
# newarr = np.intersect1d(arr1,arr2)
# print("intersection of both array")
# print(newarr)
#^==================================================================================================
#*
# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])
# print("Array -1")
# print(arr1)
# print("Array-2")
# print(arr2)
# print("-------------")
# print(np.intersect1d(arr1,arr2))

# #* OR
# print(np.intersect1d(arr2,arr1))

#^==================================================================================================
#!assume_unique=True 
#* Using  3 parameter ()
# import numpy as np
# arr1= np.array([1,2,3,4])
# arr2= np.array([3,4,5,6])
# print("Array -1")
# print(arr1)
# print("Array -2")
# print(arr2)
# print("---------------")
# newarr = np.intersect1d(arr1,arr2,assume_unique=True)
# print(newarr)

#^==================================================================================================
#only increase the performance
# import numpy as np
# arr1= np.array([1,2,3,4])
# arr2= np.array([3,4,5,6])
# print("Array -1")
# print(arr1)
# print("Array -2")
# print(arr2)
# print("---------------")
# newarr = np.intersect1d(arr1,arr2,assume_unique=False)
# print(newarr)

#^==================================================================================================
#! setdiff1d()
#*Find the difference of the set1 from set2:
#* syntax 1 - varname = np.setdiff1d(arrobj1,arrobj2)
#todo - to get the data from arr1 object
# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])
# print("Array -1")
# print(arr1)
# print("Array -2")
# print(arr2)
# print("-------------------")
# x = np.setdiff1d(arr1,arr2) #
# print("Set Diff Array")
# print(x) #& [1,2]


#* syntax 2 - varname = np.setdiff1d(arrobj2,arrobj1)
#todo - to get the data from arr2 object
# import numpy as np
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])
# print("Array -1")
# print(arr1)
# print("Array -2")
# print(arr2)
# print("---------------------")
# newarr = np.setdiff1d(arr2,arr1)
# print(newarr) #& [5 6]

#^==================================================================================================
#*Find the difference of the set1 from set2:
# import numpy as np
# set1 = np.array([1,2,3,4])
# set2 = np.array([3,4,5,6])
# print("Array -1")
# print(set1)
# print("Array -2")
# print(set2)
# print("-------------------")
# newarr = set1 -set2 #* 
#* print("Set difference Array -Substraction")
# print(newarr)

#^==================================================================================================
#! setxor1d()
#* find the symmetric difference of the set1 and set2
# import numpy as np
# set1 = np.array([1, 2, 3, 4])
# set2 = np.array([3, 4, 5, 6])
# print("Array-1")
# print(set1)
# print("Array-2")
# print(set2)
# print("Set Symmentric Diff array ")
# newarr = np.setxor1d(set1,set2) #* symmentric difference
# print(newarr)

# import numpy as np
# set1 = np.array([1, 2, 3, 4])
# set2 = np.array([3, 4, 5, 6])
# print("Array-1")
# print(set1)
# print("Array-2")
# print(set2)
# print("Set Symmentric Diff array ")
# newarr = np.setxor1d(set2,set1)
# print(newarr)

#^==================================================================================================
#!without the USE of Symmentric difference  find Symmentric difference
#* find the symmentric difference of the set1 form set2
#* FORMULA : np.setxor1d(set1,set2 ),np.intersect1d (set1,set2)
#* np.setdeff1d(np.union1d(set1,set2)) ,np.intersect1d(set1,set2)

# import numpy as np
# set1  = np.array([1,2,3,4])
# set2 = np.array([3,4,5,6])
# print("Array -1")
# print(set1)
# print("Array -2")
# print(set2)
# print("---------------")
# newarr = np.setdiff1d(np.union1d(set1,set2),np.intersect1d(set1,set2))
# print(newarr)


#^==================================================================================================
#!without the USE of Symmentric difference  find Symmentric difference
#* Find the symmetric difference of the set1 from set2:
#* Formula1: np.setxor1d(set1, set2)-->for this use Bellow Statement
#* newarr = np.union1d(np.setdiff1d(set1,set2),np.setdiff1d(set2,set1))

# import numpy as np
# set1 = np.array([1,2,3,4])
# set2 = np.array([3,4,5,6])
# print("Array -1")
# print(set1)
# print("Array -2")
# print(set2)
# print("-------------------")
# print("Set Symmentric diffenrce array :")
# a = np.setdiff1d(set1,set2)
# b = np.setdiff1d(set2,set1)
# c = np.union1d(a,b)
# print(c)
# #*OR
# #* sir
# newarr = np.union1d(np.setdiff1d(set1,set2),np.setdiff1d(set2,set1))
# print(newarr)











 #todo - varname =numpy.hstack ((ndarray1,ndarray2))

import numpy as np
# a = np.array([[10,20,30],[40,50,60]])
# print("Array1")
# print(a)

# b= np.array([[1,2],[3,4]])
# print("Array2")
# print(b)

# # merge  Array1 and Array2  into Array3
# c= np.hstack((a,b))
# print("Merge Array1 and Array2")
# print(c)

# #merge array1 and array2 into array3
# d= np.hstack((b,a))
# print("Merge Array1 and Array2")
# print(d)


a = np.arange(9).reshape(3,3)
# print(a,type(a))
b =np.array([10,20,30,40,50,60,70,80,90]).reshape(3,3)
print("Array1")
print(a)
print("array2")
print(b)

#merge the both Array1 and Array2 into Array3
c = np.hstack((a,b))
print("Array3")
print(c)

# Merge the both Array1 and aarry2 into Array3
d = np.hstack((b,a))
print("Array4")
print(d)

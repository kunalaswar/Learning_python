 #todo 
import numpy as np
a = np.array([[10,20,30],[40,50,60]])
print("Array1")
print(a)
print("----------------------------")
b = np.array([[1,2,3],[4,5,6,],[7,8,9]])
print("Array2")
print(b)
print("------------------------------")

# merge both Array1 and Array2 into Array3
c =np.vstack((a,b))
print("Array3")
print(c)

#merge both Array1 and Array2 into Array4
d = np.vstack((b,a))
print("Array4")
print(d)



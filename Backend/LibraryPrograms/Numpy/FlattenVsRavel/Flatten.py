
#^----------------------------------------------------------------------------------------------------
import numpy as np
# a = np.random.randint(10,20,size=(2,3,3))
# print(a)
# print("Dim of a = ",a.ndim)
# print("shape of a = ",a.shape)
# # convert the 3D into 1D array 
# a.shape = (18,)
# print("content of a \n",a)
# print("Dim of a=",a.ndim)
# print("shape of a =",a.shape)
#^----------------------------------------------------------------------------------------------------

a = np.random.randint(10,20,size=(2,3,3))
print(a)
print("Dim of a = ",a.ndim)
print("shape of a =",a.shape)

#flatten the 3darray into 1darray object
#varname = ndarraayobj.flatten()    
b = a.flatten()
print("content of b = \n",b)
print("Dim of b = ",b.ndim)
print("shape of b = ",b.shape)

print("base of object =",a.base)
print("base of flatten object =",b.base)



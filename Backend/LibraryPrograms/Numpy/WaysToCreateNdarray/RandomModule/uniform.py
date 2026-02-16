 #todo - 
from numpy import random as r
#todo - syntax-1 varname =
# uv = r.uniform()
# print(uv,type(uv))

#todo - syntax-2 varname =
#uniform(low,high)
# uv = r.uniform(10,11)
# print(uv,type(uv))


# #todo - syntax-3 varname =
# #uniform(low,high,size = value)
# uv = r.uniform(10,11,size=4) #todo - 1D form value 
# print(uv,type(uv))
  
# uv = r.uniform(10,11,size=(8))
# print(uv,type(uv))
# print("Dimension of uv = ",uv.ndim)
# print("Data type of uv=",uv.dtype)
# print("shape of uv = ",uv.shape)
# print("size of uv = ",uv.size)

# uv = r.uniform(10,11,size=(2,3))
# print(uv,type(uv))
# print("dimension of uv = ",uv.ndim)
# print("Data type of uv=",uv.dtype)
# print("shape of uv = ",uv.shape)
# print("size of uv = ",uv.size)


# uv = r.uniform(99.1,99.5,size=(3,3,3))
# print(uv,type(uv))
# print("dimension of uv = ",uv.ndim)
# print("Data type of uv=",uv.dtype)
# print("shape of uv = ",uv.shape)
# print("size of uv = ",uv.size)


uv = r.uniform(99.1,99.5,size=(2,2,3,3))
print(uv,type(uv))
print("dimension of uv = ",uv.ndim)
print("Data type of uv=",uv.dtype)
print("shape of uv = ",uv.shape)
print("size of uv = ",uv.size)

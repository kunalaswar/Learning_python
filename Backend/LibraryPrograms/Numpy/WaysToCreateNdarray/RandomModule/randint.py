 #todo 
# import numpy as np
# import numpy.random as r
# x = r.randint(10)
# print(x,type(x))

#todo - Another way is to import the random module 
from numpy import random as r
# a = r.randint(100 )
# print(a,type(a))

#x= r.randint(1000,10000)
# print(x)

# x = r.randint(10000,100000)
# print("G-"+str(x))

# x = r.randint(10000,100000)
# print(x)

# from numpy import random as r
# x = r.randint(10,20,size=5)
# print(x,type(x))

# x = r.randint(10,20,size=(5))
# print(x,type(x))

# x = r.randint(10,20,size=(12))
# print(x,type(x))
# print("dim of x=",x.ndim)
# print("shape of x =",x.shape)
# print("Data type of x = ",x.dtype)
# print("six=ze of x = ",x.size)

# x = r.randint(10,20,size = (3,3))
# print(x,type(x))
# print("dimension of x =",x.ndim)
# print("shape of x=",x.shape)
# print("data type of x=",x.dtype)
# print("size of x= ",x.size)

# x = r.randint(10,20,size=(3,6))
# x.dtype = (float)
# print(x,type(x))
# print("Dimension of x=",x.ndim)
# print("Data type of x=",x.dtype)
# print("shape of x =",x.shape)
# print("size of x = ",x.size)   

# x = r.randint(1)
# print(x)

# x = r.randint(10,20,size=(2,3,3))
# print(x,type(x))
# print("Dimension of x=",x.ndim)
# print("shape of x= ",x.shape)
# print("data type of x =",x.dtype)
# print("size of x =",x.size)

# x = r.randint(1,101,size=2*3*3) # size=18
# print(x,type(x))
# print("dimension of x = ",x.ndim)
# print("Data type of x = ",x.dtype)
# print("shape of x= ",x.shape)
# print("size of x =",x.size)

# x = r.randint(1,10,size=2*3*3).reshape(2,3,3)
# print(x,type(x))
# print("Dimension of x =",x.ndim)
# print("Data type of x =",x.dtype)
# print("shape of x = ",x.shape)
# print("size of x=",x.size)


x = r.randint(1000,1021,size=(2,2,2))
print(x,type(x))
print("dimension of x=",x.ndim)
print("shape of x=",x.shape)
print("data type of x=",x.dtype)
print("size of x=",x.size)


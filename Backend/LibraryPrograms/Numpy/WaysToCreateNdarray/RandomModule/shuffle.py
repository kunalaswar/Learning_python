 #todo -
import numpy as np 
from numpy import random as r

# a = np.arange(10)
# print("Original content of ndarray ")
# print(a,type(a),id(a))  # id will be same
# print("-----------------------------")
# r.shuffle(a)
# print("shuffle content of ndarray")
# print(a,id(a))

# s = "mississippi"
# print(s,type(s))
# st = set(s)
# print(st)

# a = np.arange(10)
# print(a)
# r.shuffle(a)
# print(a)

# uv = list()
# for val in a:
#     print(val)
#     uv.append(val)
# print(uv)        

# s ="MISSISSIPPI"
# # st = set(s)
# # print(st)cls

# a = np.array(list(s))
# print("Original Array")
# print(a)

# r.shuffle(a)
# print("shuffle value")
# print(a)


# for i in range(1,len(a)):
#     r.shuffle(a)
#     print("conbination ",i,"---> ","".join(a))

#shuffling 2-Data ---shuffles Row 
# a = r.randint(1,101,size=(6,5))
# print("original Matrix ")
# print(a)
# print("------------------------------")
# print("shuffle Matrix ")
# r.shuffle(a)
# print(a)

#shuffling n-D Data ---shuffles ---matrix Numbers
a = np.arange(48).reshape(4,3,4)
print("Original Matrix ")
print(a)
r.shuffle(a)
print("shuffle Matrix ")
print(a)









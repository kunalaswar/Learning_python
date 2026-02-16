 #
import numpy as np 
from numpy import random as r 
# a = np.array([10,20,30,40,50,60,70,80,90])
# print(a,type(a))

# b = r.permutation(a)
# print(b,type(b))

# import itertools
# lst =[1,2,3]
# perm = itertools.permutations(lst)
# # print(tuple(perm))

# import itertools as kvr
# lst= [1,2,3]
# perlist=[]
# for i in range(1,len(lst)+1):
#     onepr=list(kvr.permutations(lst,i))
#     perlist.extend(onepr)
# else:
#     print("-------------------------------")    
#     print("permutation of ",lst)
#     print("-------------------------------")
#     for comb in perlist:
#         print(comb)

import itertools as kvr
a = np.array([10,20,30])
print("Original array before permutation ")
print(a)
print("------------------------")
prlst = []
for i in range(1,len(a)+1):
    l1=list(kvr.permutations(a))
    prlst.append(l1)

print(prlst)
# for val in prlst:
    # print(int(val))


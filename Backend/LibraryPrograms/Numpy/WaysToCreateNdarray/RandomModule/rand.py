 #todo -  varname = numpy.random.rand()--->single Raandom value Between 0.0 to 1.0 
from numpy import random as r 
# rv = r.rand()
# print("Random float value= ",rv)

# rv =r.rand()
# print("Random float value =%0.2f" %rv)

# rv = r.rand()
# print("Random float value =",round(rv,3))

#todo - varname = numpy.random.rand(value)
#todo -Random vlaue of value (value times) Between 0.0 to 1.0
from numpy import random as r
# rv = r.rand(5)
# print(rv, type(rv))
# print("Dimension of rv=",rv.ndim)
# print("Data type of rv=",rv.dtype)
# print("shape of rv=",rv.shape)
# print("size of rv = ",rv.size)

# rv = r.rand(12)
# print(rv,type(rv))
# # rv.shape = (1)
# print("Dimension of rv=",rv.ndim)
# print("Data type of rv=",rv.dtype)
# print("shape of rv=",rv.shape)
# print("size of rv=",rv.size)

#todo - varname = numpy.random.rand(Rows,cols)
# rv = r.rand(3,3)
# print(rv,type(rv))
# print("Dimension of  rv=",rv.ndim)
# print("Data type of rv=",rv.dtype)
# print("shape of rv = ",rv.shape)
# print("size of rv= ",rv.size)

# rv = r.rand( 2,3,3)
# print(rv,type(rv))
# print("Dimension of rv",rv.ndim)
# print("Data type of rv=",rv.dtype)
# print("shape of rv=",rv.shape)
# print("size of rv =",rv.size)

# a = r.rand(3,4)
# print(a,type(a))
# for val in a:
    # print(round(val,2))

#todo - for my understanding
# for i in range(len(a)):
#     print(a[i,i])

# for i in range(len(a)):
#     print(a[0])

# for ri in range(len(a)):
#     print(ri)
#     print("-----------")
#     for ci in range(len(a[0])):
#         print(ci)
#     print("-----------")

# for ri in range(len(a)):
#     for ci in range(len(a[1])):
#         print(round(a[ri,ci],3),end=" ")
        # print()  


a = r.rand(2,3,3)
print(a,type(a))
for mn in range(len(a)):
    # print(mn)
    for rn in range(len(a[0])):
        for cn in range(len(a[0])):
            print(a[mn,rn,cn],end="\t")
        print()    
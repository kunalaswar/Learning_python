
# import pandas as pd
# print(pd.__version__)
#^====================================================================================================
# import numpy as np
# import pandas as pd
# lst = [10,20,30,40,50]
# print(lst,type(lst))
    

import numpy as np
# a = np.array([[10,20],[30,40]])
# b = np.array([[1,2],[3,4]])
# print(a,type(a))
# print(b,type(b)) 
# c = np.dot(a,b)  #* Row x Column
# print(c)

# a = np.array([1,2])
# b = np.array([3,4])
# c = np.dot(a,b)
# print(c)

# a = np.array([1,2])
# b = np.array([3,4])
# c = np.inner(a,b)
# print(c)
# d = np.inner(b,a)
# print(d)

# a = np.array([[1,3],[5,7]])
# b = np.array([[2,4],[6,8]])
# c = np.inner(a,b)
# print(c)

# a  = np.array([1,3,5,2]).reshape(2,2)
# b = np.array([4,2,5,6]).reshape(2,2)
# print(a)
# print(b)
# c = np.outer(a,b)
# print(c)

# a = np.array([1,2,3,4]).reshape(2,2)
# print(a)
# b = np.linalg.det(a)
# print(b)

# a = np.array([4,2,1,3]).reshape(2,2)
# print(a)
# b = np.linalg.det(a)
# print(np.round(b))
# print(round(b,5))

a = np.array([[2,3],[6,1]])
b = np.array([4,2])
sol = np.linalg.solve(a,b)
print(sol)
print(round(sol[0],3))
print(round(sol[1],3))

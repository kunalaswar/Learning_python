
#!dot()
#* varname = numpy .dot(obj1,obj2)
#^====================================================================================================

#* 2d- matrix
# import numpy as np
# a = np.array([[10,20],[30,40]])
# b = np.array([[1,2],[3,4]])
# print("Matrix -A")
# print(a)
# print("matrix -B")
# print(b)
# c = np.dot(a,b)
# print("Matric -C (dot product to 2D matirx)")
# print(c)

#^-----------------------------------------------------------------------------------------------
#* for 1D only
# import numpy as np
# a = np.array([1,2])
# b = np.array([3,4])
# print("content of a")
# print(a)
# print("Content of b")
# print(b)
# c = np.dot(a,b)
# print("Content of c (Dot product on 1D)")
# print(c)

#^-----------------------------------------------------------------------------------------------
#* 1D array
# import numpy as np
# a = np.array([10,20,30])
# b = np.array([4,5,6])
# # print(a.ndim)
# print("content of a ")
# print(a)
# print("Content of b")
# print(b)
# c = np.dot(a,b)
# print("Content of c")
# print(c)

#^-----------------------------------------------------------------------------------------------
#!Inner product
#* 2D -array
#* row to row 

# import numpy as np
# a =np.array([[1,2],[5,7]])
# b = np.array([[2,4],[6,8]])
# print("Matrix-A")
# print(a)
# print("Matrix -B")
# print(b)
# c = np.inner(a,b)
# print("Matrix of c")
# print(c)

#^-----------------------------------------------------------------------------------------------
#* for 1D array
# import numpy as np
# a = np.array([1,2])
# b = np.array([3,4])
# print("Content of a ")
# print(a)
# print("Content of b")
# print(b)
# c = np.inner(a,b)
# print("Content of c")
# print(c)

#^-----------------------------------------------------------------------------------------------
#!outer product
# #* 1D array 
# import numpy as np
# a = np.array([1,3,5])
# b = np.array([2,4,6])
# # print(a.ndim)
# print("contnet of a")
# print(a)
# print("content of b")
# print(b)
# c = np.outer(a,b)
# print("Content of c")
# print(c)
#^--------------------------------------------------------------------------------------------------
#* finding outer of 3D matrix


#^-----------------------------------------------------------------------------------------------
#* 2D array
# import numpy as np
# a = np.array([1,3,5,2]).reshape(2,2)
# b = np.array([4,2,5,6]).reshape(2,2)
# print("Matrix -A")
# print(a)
# print("Matrix -B")
# print(b)
# c = np.outer(a,b)
# print("Matrix -C (outer product - 2D)")
# print(c)

#^-----------------------------------------------------------------------------------------------
#!   Determinent 
import numpy as np
# a = np.array([1,2,3,4]).reshape(2,2)
# print("Matrix -A")
# print(a)
# print("----------------------------")
# da = np.linalg.det(a)
# print("Det. of Matrix ",da)
# print("Det. of Matrix ",round(da,2))
# print("Det. of Matrix %2f "%da)
#^-----------------------------------------------------------------------------------------------

import numpy as np
# a = np.array([10,20,30,40]).reshape(2,2)
# print("Matrix -1")
# print(a)
# print("---------------------------")
# da = np.linalg.det(a)
# print("Det. of c =",da)

#^-----------------------------------------------------------------------------------------------
# a = np.array([10,20,30,40,50,60,70,80,90]).reshape(3,3)
# print(a)
# c = np.linalg.det(a)
# print("Det of c =")
# print(c)

#^-----------------------------------------------------------------------------------------------
#* finding Determinent of 2D
# a = np.array([1,2,4,3]).reshape(2,2)
# print(a)
# c = np.linalg.det(a)
# print("Det of c")
# print(c)

#^-----------------------------------------------------------------------------------------------
# a = np.identity(3,dtype=int)
# print(a)
# c = np.linalg.det(a)
# print("Det of c")
# print(c)


#^-----------------------------------------------------------------------------------------------
# a= np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# print(a)
# c = np.linalg.det(a)
# print("Det of c =")
# print(c)

#^-----------------------------------------------------------------------------------------------
#*Finding Determinent 3-D
# a= np.identity(3,dtype=int)
# print("Matrix -A")
# print(a)
# det3d = np.linalg.det(a)
# print(det3d)

#^-----------------------------------------------------------------------------------------------
#*Finding Determinent 3-D in reverse
# a = np.array([1,2,3,4,5,6,7,8,9])[::-1].reshape(3,3)
# print("matrix -A")
# print(a)
# det2d = np.linalg.det(a)
# print("Determinent of martix in reverse order ",det2d)

#^-----------------------------------------------------------------------------------------------
#* finding Determinent of 3D   
# a=np.array([2,-3,1,2,0,-1,1,4,5]).reshape(3,3)
# print("matrix -A")
# print(a)
# da = np.linalg.det(a)
# print("Determinent of da ")
# print(da)
#^-----------------------------------------------------------------------------------------------
#










#^-----------------------------------------------------------------------------------------------
 #todo - 
#todo - with out the use of the identity() function 
import numpy as np
# lst = [1,0,0,1]
# a = np.array(lst)
# print(a,type(a))
# a.shape = (2,2)
# print("unit matrix",a)

#todo  - with out the use of shape attribute
# import numpy as np
# lst = [[1,0],[0,1]]
# a = np.array(lst)
# # a.shape = (2,2)
# print("unit matrix =\n",a)

# import numpy as np
# lst = [[1,0,0],[0,1,0],[0,0,1]]
# a = np.array(lst)
# print("unit matrix :\n",a)
# print("Dimension of a=",a.ndim)
# print("shape of a=",a.shape)


#todo  - varname = numpy.identity(N,dtype)

#create ndarray object with 2 x 2 identity matrix OR unit matrix
# import numpy as np
# a= np.identity(2)
# print(a)
# print("Dimension of a= ",a.ndim)
# print("shape of a= ",a.shape)


# a= np.identity(2,dtype=int)
# print(a)
# print("Dimension of a= ",a.ndim)
# print("shape of a= ",a.shape)


# a= np.identity(3,dtype=int)
# print(a)
# print("Dimension of a= ",a.ndim)
# print("shape of a= ",a.shape)

# # for val in range(len(a)):
# #     print(val,a[val])

# p =1 
# for i in range(len(a)):
#     p = p*a[i,i]
# print("product of principle digonal element =",p)


# a = np.identity(3,dtype=int)
# print(a)

# p =1 
# for i in range(len(a)):
#     print(a[i,i])


# a = np.identity(3,dtype=int)
# print(a,type(a))
# print("Dimension of a=",a.ndim)
# print("shape of a = ",a.shape)

# a.shape = (9,)
# print("Unit matrix\n",a)
# print("Dim of a= ",a.ndim)
# print("shape of a= ",a.shape)



#! <7>.identity()
#* Syntax:    varname=numpy.identity(N,dtype)
#*dtype default float aste
#^----------------------------------------------------------------------------------------
#*Create 2x2 Identity OR Unit Matrix
# lst = [1,0,0,1]
# a = np.array(lst).reshape(2,2)
# print(a,type(a))

# lst = [[1,0],[0,1]]
# a = np.array(lst)
# print(a,type(a))

#* Create ndarray object with 2 x 2 identity OR Unit Matrix
# a = np.identity(4,dtype=int)
# print(a,type(a))

# a = np.identity(4)
# print(a,type(a))

# a = np.identity(2,str)
# print(a,type(a))

# a = np.identity (2,dtype=int)
# print(a)
# print(a.ndim)
# print(a.dtype)
# print(a.size)
# print(a.shape)

#* Create ndarray object with 3 x 3 identity OR Unit Matrix
# a = np.identity(3,dtype=int)
# print("Unit Matrix ")
# print(a)
# print("Dim of a =",a.ndim)
# print("shape of a =",a.shape)

#*create ndarray object with 6 x 6 indentity OR  Unit matrix

# a = np.identity(6,dtype=int)
# print(a,type(a))
# print("Dim of a  = ",a.ndim)
# print("shape of a =",a.shape)

#*create ndarray object with 10 x 10 indentity OR  Unit matrix
#*
# a = np.identity(0,dtype=int)
# # print(a,type(a))
# print("Unit matrix ")
# print(a)
# print("Dim of a =",a.ndim)
# print("shape of a =",a.shape)
# print("size of a =",a.size)


# a = np.identity(10,dtype=int)
# # print(a,type(a))
# print("Unit matrix ")
# print(a)
# print("Dim of a =",a.ndim)
# print("shape of a =",a.shape)
# print("size of a =",a.size)

# p =1
# for i in range(len(a)):
#     p = p*a[i,i]
# print(f"product of principle digonal element = {p}")    

# a.shape = (100,)
# print(a)
# print("Dimension of a =",a.ndim)
# print("shape of a =",a.shape)
# print("size of a = ",a.size)

# import numpy as np
# p = 1
# lst = [[1,0,0],[0,1,0],[0,0,1]]
# a = np.array(lst)
# print(a,type(a))
# for i in range(len(a)):
#     p = p*a[i,i]
# print("product of =",p)



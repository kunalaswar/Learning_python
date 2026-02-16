# import numpy as np
# # print(numpy._version_)

import sys
import numpy as np
lst = [10,20,30,40,50,60,70,70,80,90,12,3,34,54,56,67,87,9,80,13,14,15,61,71,3,43,24,26,27,4,3,36,37,38,30,40,50,60,70,70,80,90,12,3,34,54,56,67,87,9,80,13,14,15,61,71,3,43,24,26,27,4,3,36,37,38,30,40,50,60,70,70,80,90,12,3,34,54,56,67,87,9,80,13,14,15,61,71,3,43,24,26,27,4,3,36,37,38]
print(lst,type(lst))
# print("Content of list =",lst)
print("Memory space of the list object =",sys.getsizeof(lst))
print("*"*90)

a =np.array(lst)
print(a,type(a))
print("Memory space of the list object =",sys.getsizeof(a))

#todo - here ndarry objects ---takes less memory space for storing sampling of the data


#todo - on list we can perform  vector operation Based operation 
#todo - programtically we can perform Vector Based operation 
# import numpy as np 

# lst = [10,20,30]
# for i in range(len(lst)):
#     lst[i]=lst[i]+1
# print("After increment of the value by 1 ")
# print(lst,type(lst)) 

#todo - on ndarray object can perform vector operation Based operation 

# lst1 = [40,50,60]
# a = np.array(lst1)  
# a = a+1
# print(a,type(a ))

# import numpy as np
# #todo - Data Retrival point  OR  Extraction from Traditional python objects 
# lst = [10,20,30,40,50,60,70,80,90,32,34,54]
# print("-------------------------------------")
# print("Content of list ")
# print(lst,type(lst))
# print("Address of Element of list ")
# for val in lst:
#     print(f"val: {val}  Address : {id(val)}------>{id(lst)}")
# print("---------------------------------------")

# a = np.array(lst)
# print("content in ndarray ")
# print(a )
# print("Address of Element of array ")
# for val in a :
#     print(f"val :{val}  Address :{id(val)} ------->{id(a)}")



import numpy as np 
# lst = [10,20,30,40,50,60]
# print("Content of list ")
# print(lst,type(lst))
# print("----------------------------------------")
# #*Convert list object into ndarray object 
# a = np.array(lst )
# print("Content of ndarray ")
# print(a)
# #* get the dimension of ndarray
# print("Dimension of ndarray =>",a.ndim) #todo- ndim is the pre-defined attribute of the ndarray 
# print(a.reshape(2,3))
# a.reshape(3,2) 
# a.reshape(2,3)


# lst = [10,20,30,40,50,60,80,90,21,22,45,56]
# print("content of list ")
# print(lst,type(lst ))
# #* Convert the list into ndarray object 
# a = np.array(lst )
# print("content of ndarray ")
# print(a ,type(a))
# print("Dimension of ndarray =>",a.ndim)
# print(a.reshape(2,3,2))
# # print(a.reshape(3,4))
# print(a.reshape(2,3,2)).ndim
# print(a.reshape(2,3,2)).shape


#!              DATE - 09-01-2025
# a = [[10,20 ],[30,40]]
# b = [[1,2],[3,4]]
# for i in a:
#     print(i)
# for i in b:
#     print(i)
# print("-----------------------")    
# c = a+b    
# for j in c:
#     print(j)

# import numpy as np
# m1 = np.array(a)
# m2 = np.array(b)
# print(m1,type(m1))
# print(m2,type(m2))
# print("----------------------")
# #To add both the m1,m2 into the m3
# m3 = m1+m2
# print(m3,type(m3))
# #todo- OR add() operator 
# m4 = np.add(m1,m2)
# print("add the both the matrics with use of the add() function ",m4)



#list of the value with different type 
# lst = [10,"RS",23.37,2+3j,True]
# for val in lst:
#     print(val,"--->",type(val))

# import numpy as np
# lst = [10,"RS",23.37,2+3j,True]
# a = np.array(lst)
# print(a,type(a)) #all the value are store into single cotes ---> ''
# for val in a:
#     print(val,"--->",type(val))
    
# a = np.array(lst,dtype=object)
# print(a,type(a))
# for val in a:
#     print(val,"--->",type(val))


#!           DATE - 10-01-2025

# lst = [10,"RS",23.37,2+3j,True]
# print(lst,type(lst))
# for val in lst:
#     print(val,"---> ",type(val))

# import numpy as np
# a = 10
# print("val of a =",a)
# print("type of val",type(a))
# print("------------------------------------")
# # convert int type data into the ndarray
# b =np.array(a) 
# print("content of b = ",b)
# print("type of b=",type(b))
# print("Data type of b=",b.dtype)
# print("Dimension of b",b.ndim)
# print("Shape of b = ",b.shape)
# print("Size of b = ",b.size) #number of element 

# import numpy as np
# a = 12.5
# print("val of a =",a)
# print("type of val",type(a))
# print("------------------------------------")
# # convert int type data into the ndarray
# b =np.array(a) 
# print("content of b = ",b)
# print("type of b=",type(b))
# print("Data type of b=",b.dtype)
# print("Dimension of b",b.ndim)
# print("Shape of b = ",b.shape)
# print("Size of b = ",b.size) #number of element 

# import numpy as np
# a = 12.5
# print("val of a =",a)
# print("type of a =",type(a))
# print("---------------------")
# #convert int type data into ndarry
# b = np.array(a)
# print("value of b =",b)
# print("Type of b=",type(b))
# print("Dimension = ",b.ndim)
# print("type of array = ",b.dtype)
# print("size of the b = ",b.size)
# print("shape of the b = ",b.shape) # number of Element
# import numpy as np
# a = "python"
# print(a ,type(a))
# #convert the str into the  ndarry
# b = np.array(a)

# print(b,type(b))
# print("type of b=",b.dtype)
# print("size of b=",b.size)
# print("shape of b=",b.shape)

# import numpy as np
# a = range(12)
# print(a,type(a))
# print("----------------------------")
# # convert the range data type into ndarry 
# #todo - this is an int type of data into the list
# b = np.array(a)
# print(b,type(b))  #todo -[ 0  1  2  3  4  5  6  7  8  9 10 11] <class 'numpy.ndarray'>
# print("data type of b=",b.dtype)
# print("shape of b =",b.shape)
# print('size of b=',b.size)

# import numpy as np
# a = range(12)
# print(a,type(a))
# print("----------------------------")
# # convert the range data type into ndarry 
# #todo - this is an float type of data into the list
# b = np.array(a,float) #todo - float type of the data type 
# print(b,type(b))  #todo -[ 0  1  2  3  4  5  6  7  8  9 10 11] <class 'numpy.ndarray'>
# print("data type of b=",b.dtype)
# print("shape of b =",b.shape)
# print('size of b=',b.size)

#?=================================================================================================
#?=================================================================================================
# import numpy as np
# import sys
# #Reshape of 6 Element of ndarry by using reshape()
# # as 2*3 or 3*2 OR 1*6 or 6*1    
# r= [10,12,14,16,18,20]
# print(r,type(r),sys.getsizeof(r)) #104 
# a = np.array(r)
# print(a,type(a),sys.getsizeof(a)) #todo- 160 size of the ndarry is small so that size of the ndarry is large
# a = a.reshape(1,6)
# print(a)
# # print(b.reshape(1,6))
# # print(b.reshape(2,3))

# print("--------------------------------------")
# a.reshape(1,6)
# print("Content of a =",a)
# print("type of a",type (a))
# print(" Data type of a",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a=",a.shape)
# print("Size of a=",a.size)

# #todo - convert the 2D array into 1D array ,reshape can not be used
# #todo - to do this we use shape attribute
# print("-------------------------------------")
# a.shape=(6,) #convert 
# print("content of a = ",a)
# print("type of a =",type(a))
# print("Data type of a = ",a.dtype)
# print("Dimension of a=",a.ndim)
# print("shape of a=",a.shape)
# print("size of a =",a.size)



# #todo- convert 1D to 2D by using Shape attribute 
# print("---------------------------")
# a.shape = (3,2) # 
# print(a,type(a))
# print("Dimension of a = ",a.ndim)
# print(a.reshape(3,2))

#?=================================================================================================
#?=================================================================================================
# import numpy as np
# a = np.array(range(16))
# print(a,type(a))
# print("Data type of a =",a.dtype)
# print("Dimension of a =",a.ndim)
# print("Shape of a =",a.shape)
# print("size of a =",a.size)
# print("--------------------------------")


#convert the Above 1D data into 2D 
# a.shape = (4,4)
# print(a,type(a))
# print("Data type of a=",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a =",a.shape )
# # #a.shape = (2,8)
# # #a.shape = (8,2)
# print("shape of a =",a.shape )
# print("size of a =",a.size)

#^-----------------------------------------------------------------------------------------------
#^ chatgpt
# # To convert a 2D NumPy array into a 3D array, you can use the numpy.reshape() function.
# import numpy as np

# # Create a 2D array
# array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# # Convert 2D to 3D
# array_3d = np.reshape(array_2d, (2, 3, 1))

# print("2D Array:")
# print(array_2d)
# print("\n3D Array:")
# print(array_3d)
#^-----------------------------------------------------------------------------------------------
#& TO See this line number 259
# # #convert the above 2D data into 3D
# a.shape = (2,4,2)
# print(a,type(a))
# print("Dimension of a =",a.ndim)
# print("shape of a =",a.shape)
# print("size of a =",a.size)
# print("--------------------------------------------------")

# #todo - convert the above 3D into 4D ------(2,2,2,2)
# a.shape = (2,2,2,2) #* cluster ,no of matrics,no of rows, no of column
# print(a,type(a))
# print("Data type of a =",a.dtype)
# print("dimension of a = ",a.ndim)
# print("shape of a = ",a.shape)
# print("size of a =",a.size)

#Convert list object into ndarray object 
# import numpy as np
# lst = [10,20,30,40,50,60,70,80,90]
# print("Content of list",lst)
# print("type of lst",type(lst))
# print("-----------------------")
# a = np.array(lst,float)
# a.shape = (3,3)
# print("content of a=",a)
# print("type of a",type(a))
# print("Data type of a =",a.dtype)
# print("dimension of a = ",a.ndim)
# print("shape of a = ",a.shape)
# print("size of a =",a.size)

# 

# lst=[10,"RS",34.56,True,2+3j]
# print("content of lst=",lst)
# print("Type of lst=",type(lst))
# print("---------------------------------")
#^----------------------------------------
# import numpy as np
# lst=[10,"RS",34.56,True,2+3j,"Python"]
# a = np.array(lst,dtype=object)
# print(a,type(a))
# print("Data type of a=",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a = ",a.shape)
# print("size of a =",a.size)

# print("-----------------------------------------")
# print(a.reshape(3,2)) #* VS code madhe aasa lihayacha jagya var print() karayacha
# print(a)  

#!          SAME FOR TUPLE() DATA TYPE






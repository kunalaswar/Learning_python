 #todo -range()
# range(value) 
# range(start,stop)
# range(start,stop,step)

#todo - arange()
# import numpy as np
# np.arange(value)
# np.arange(start,stop)
# np.arange(start,stop,step)

# import numpy as np
# lst = [10,20,30,40,50,60,70,80,90] 
# a = np.array(lst)
# print(a)  #-------------1D

# import numpy as np
# lst = [10,20,30,40,50,60,70,80,90]
# a = np.array(lst)
# a.shape = (3,3)
# print(a)  #-------------2D


# import numpy as np
# lst=[[10,20,30],[40,50,60],[70,80,90]]
# a = np.array(lst)
# print(a)   #-------------3D

#todo -syntax 1) numpy.arange(value)
#todo - generate range of the value form 0 to 10
import numpy as np
# a = np.arange(11)
# print("-----------------------------")
# print("content of a=",a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)   
# print("shape of a =",a.shape)
# print("size of a =",a.size)

# a = np.arange(6)
# a.shape =(3,2)
# print("-----------------------------")
# print("content of a=\n",a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)   
# print("shape of a =",a.shape)
# print("size of a =",a.size)


#todo -syntax 2) numpy.arange(start,stop)
#generate the values from 10 to 20
# import numpy as np
# a = np.arange(10,21)
# print("-------------------------------------")
# print("content of a=\n",a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)   
# print("shape of a =",a.shape)
# print("size of a =",a.size)

# import numpy as np
# a = np.arange(100,107)
# print("-------------------------------------")
# print("content of a=\n",a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)   
# print("shape of a =",a.shape)
# print("size of a =",a.size)


#todo -syntax 3) numpy.arange(start,stop,step)
#generated the values from 100 to 105
# a = np.arange(100,106).reshape(3,2)
# print("-------------------------------------")
# print("content of a=\n",a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)   
# print("shape of a =",a.shape)
# print("size of a =",a.size)


#Generate the range of values as 10,12,14,16,18,20,22,24,26
# a = np.arange(10,27,2)
# print("-------------------------------------")
# print("content of a=\n",a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)   
# print("shape of a =",a.shape)
# print("size of a =",a.size)
# a.shape=(3,3)
# print(a)
# print(a.reshape(3,3))

# # a =np.arange(10,27,0.5)
# a  =np.arange(10,27,0.5,dtype=float)
# print(a,type(a))


# a =np.arange(10,15,0.25)
# # print(a,type(a))
# print("-------------------------------------")
# print("content of a=\n",a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)   
# print("shape of a =",a.shape)
# print("size of a =",a.size)

# # print(a.reshape(5,4))
# print(a.reshape(4,5))

#todo - ==================== OR ==============================

# a =np.arange(10,15,0.25).reshape(5,4)
# # print(a,type(a))
# print("-------------------------------------")
# print("content of a=\n",a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)   
# print("shape of a =",a.shape)
# print("size of a =",a.size)

# # print(a.reshape(5,4))
# # print(a.reshape(4,5))

#Generated the range of values 10 to 15 in interval 0.25 with 3-D matrix format
# a = np.arange(10,15,0.25,float).reshape(2,5,2)
# print("-------------------------------------")
# print("content of a=\n",a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)   
# print("shape of a =",a.shape)
# print("size of a =",a.size)
 
#! <1>.arange()
#*numpy.arange(Value)----------------> 0 to Value-1 with Default Step     +1
#*numpy.arange(Start,Stop)---------->Start to Stop-1 with Default Step  +1
#*numpy.arange(Start,stop,Step)----> Start to Stop-1 with Programmer Choice Step
#^----------------------------------------------------------------------------------------
#* numpy.arange(Value)----------------> 0 to Value-1 with Default Step     +1
#* genarte range of values from 0 to 10

# import numpy as np
# a = np.arange(9)
# a.shape = (3,3)
# print("content of a=\n",a)
# print("type of a =",type(a))
# print("values type of a =",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a =",a.shape)
# print("size of a =",a.size)

# a = np.arange(10,dtype=float)
# print(a,type(a))
# print("Values types of = ",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a =",a.shape)
# print("size of a =",a.size)

#^----------------------------------------------------------------------------------------
#* numpy.arange(Value)----------------> 0 to Value-1 with Default Step     +1
#* genarte range of values from 0 to 6
# import numpy as np
# a = np.arange(0,6,dtype=float)
# print(a,type(a))
# a.shape =(3,2) #todo -(2,3)
# print("content of a =\n",a)
# print("type of a=",type(a))
# print("Values type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)

#^----------------------------------------------------------------------------------------
#* numpy.arange(Start,Stop)---------->Start to Stop-1 with Default Step  +1
#*generate the values from 10 to 20
# a = np.arange(10,21,dtype=float)
# print("content of a=",a)
# print("type of a=",type(a))
# print("Values type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)

#^---------------------------------------------------------------------------------------------------
#* numpy.arange(Start,stop,Step)----> Start to Stop-1 with Programmer Choice Step
#* Generate the range of values as 10 12 14 16 18 20 22 24 26
# a = np.arange(10,27,2)
# print(a,type(a))
# print("type of a=",type(a))
# print("Values type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)

#^----------------------------------------------------------------------------------------
#*Generate the range of values as 10 12 14 16 18 20 22 24 26 with Matrix Format
# # a = np.arange(10,27,2).reshape(3,3)
# a = np.arange(10,27,2)
# a.shape = (3,3)
# print("content of a =\n",a)
# print("Type of a =",type(a))
# print("Value type of a =",a.dtype)
# print("Dimension of a=",a.ndim)
# print("shape of a =",a.shape)
# print("size of a =",a.size)

#^----------------------------------------------------------------------------------------
#*Generate the range of values as 10 to 15 with Interval value 0.25 with Matrix Format
# a = np.arange(10,15,0.25)
# print("content of a =",a)
# print("type of a =",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a =",a.shape)
# print("size of a =",a.size)

# a = np.arange(10,15,0.25,dtype = float)
# print("content of a =",a)
# print("type of a =",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a =",a.shape)
# print("size of a =",a.size)

#^----------------------------------------------------------------------------------------
#* Generate the range of values as 10 to 15 with Interval value 0.25 with Matrix Format
# a = np.arange(10,15,0.25).reshape(5,4)
# print("content of a =\n",a)
# print("type of a =",type(a))
# print("values type of a =",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a =",a.shape)
# print("size of a =",a.size)

#^----------------------------------------------------------------------------------------
#*Generate the range of values as 10 to 15 with Interval value 0.25 with 3-D Matrix Format
import numpy as np
a = np.arange(10,15,0.25).reshape(5,2,2)
print(a)
print("type of a =",type(a))
print("values type of a =",a.dtype)
print("Dimension of a =",a.ndim)
print("shape of a =",a.shape)
print("size of a =",a.size)

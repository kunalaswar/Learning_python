 #todo 
# import sys 
# lst = [10,20,30,40,50,60,708,80,90]
# print(sys.getsizeof(lst))

# import numpy as np 
# a = np.array(lst)
# print(a,type(a),sys.getsizeof(a))

# import sys
# lst= [10,20,30,40,56,78,9,45,678,999,234]
# print(lst,sys.getsizeof(lst))

# import numpy as np
# a = np.array(lst)
# print(a,sys.getsizeof(a))

# import sys
# import numpy as np
# lst= [10,20,30,40,56,78,9,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,10,20,30,40,56,78,9,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,10,20,30,40,56,78,9,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,10,20,30,40,56,78,9,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,10,20,30,40,56,78,9,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,10,20,30,40,56,78,9,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,10,20,30,40,56,78,9,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999,23,12,1,314,15,16,17,18,19,10,111,222,333,444,555,666,777,888,999]

# print(lst,sys.getsizeof(lst))

# a = np.array(lst)
# print(a,sys.getsizeof(a)) #304 #sir #208

# import sys
# import numpy as np
# lst= [10,20,30 ]
# # lst = lst+1   #error
# # print(lst)
# # for val in lst:
# for i in range(len(lst)):
#     # print(i)
#     lst[i]=lst[i]+1
# print(lst)

# lst = [10,20,30]
# a = np.array(lst)
# print("content of ndarry")
# print(a,type(a))
 
# a= a+1  #a = a*2 #vector based operations
# print("content of ndarray after vector based operation  ")
# print(a,type(a))



# import numpy as np
# print(np.__version__)

#
# import sys
# import numpy as np
# lst =[10,20,30,40]
# print("content of list=",lst)
# print("memory space of list ",sys.getsizeof(lst))

# #
# a = np.array(lst)
# print(a)
# print("memory space of a= ",sys.getsizeof(a))


# import sys
# import numpy as np
# lst = [10,20,30,40,56,56,78,99,12,34,78,99,]
# print("content of list=",lst)
# print("memory space of list ",sys.getsizeof(lst))

# #
# a = np.array(lst)
# print(a)
# print("memory space of a= ",sys.getsizeof(a))


# import sys
# import numpy as np
# lst = [10,20,30,40,56,56,78,99,12,34,78,99,10,20,30,40,56,56,78,99,12,34,78,99]
# print("content of list=",lst)
# print("memory space of list ",sys.getsizeof(lst))

# #
# a = np.array(lst)
# print(a)
# print("memory space of a= ",sys.getsizeof(a))


#data retrival or Extraction 
# lst = [10,20,30,40,50,60,70,80,90,15,25,35]
# print(lst)
# for val in lst:
#     print(f"{val} ---{id(val)}   {id(lst)}")
    
# import numpy as np    
# lst = [10,20,30,40,50,60,70,80,90,15,25,35]
# print(lst)
# a = np.array(lst)
# for val in a:
#     print(f"{val} ---{id(val)}   {id(a)}")
    

# lst = [10,20,30,40,50,60]
# print(lst) #it is not possible Reshape the list data

# import numpy as np
# lst = [10,20,30,40,50,60]
# # print(lst) #it is  possible Reshape the in ndarry object
# a = np.array(lst)
# print(a,type(a))

#get the dimension of ndarray 
# print("Dimension of an Ndarray = ", a.ndim)


#convert the 1-D array into 2D array with 3 Rows and 2 columns
# b =a.reshape(3,2)
# b =a.reshape(2,3)
# print(b)

# import numpy as np
# lst = [10,20,30,40,50,60,70,80,90,25,35,45]
# a = np.array(lst)

# print("Dimension of ndarray = ",a.ndim)

# a = a.reshape(3,4)
# a = a.reshape(4,3)
# print(a)

# a = a.reshape(6,2)
# a = a.reshape(2,6)
# print(a)

# # 3-D
# # a =a.reshape(2,3,2).ndim
# a =a.reshape(2,3,2).shape
# print(a)


#      todo----------------------DAY-4
# a = [[10,20],[30,40]]
# b = [[1,2],[3,4]]
# print(a)
# print(b)

# for val in a:
#     print(val)

# for val in b:
#     print(b)

#todo - ndarray 
# a = [[10,20],[30,40]]
# b = [[1,2],[3,4]]
# import numpy as np
# m1 = np.array(a)
# m2 = np.array(b)
# m3 = m1+m2
# print("using +operator = ",m3,type(m3))

# m4  =np.add(m1,m2)
# print("using add function = ",m4)

# lst = [10,"RS",34.56,2+3j,True]
# for val in lst:
#     print(val,"--->",type(val))

# import numpy as np
# a = np.array(lst)
# print(a,type(a))
# # for val in a:
#     # print(val,"--->",type(val))

# a = np.array(lst,dtype=object)
# for val in a:
#     print(val,"--->",type(val))

# print(a[0]+10) #we can perform adding operation on the ndarray



# lst = [10,"RS",34.56,2+3j,True]
# print(lst,type(lst),id(lst)) 
# lst[0]=100 #index based modification
# print(lst,type(lst),id(lst))

#slice based modification 
# lst[0:2]=[1,2,3]
# print(lst,type(lst),id(lst))

# import numpy as np
# a= np.array(lst)
# print(a,type(a))
# print(a[0])


# l1 = list()
# print(l1,type(l1))
# l2 = [10,20,30,40,"RS"]
# print(l2,type(l2))

# s= "MISSISSIPPI"
# l3 = list(s)
# print(l3,type(l3))

# import numpy as np
# # a = np.identity(3)
# # print(a,type(a))

# # a = np.identity(3,int)
# # print(a,type(a))

# a = np.identity(6,int)
# print(a,type(a))




#  todo  DAY -5
#todo - array()
# a = 10
# print(a,type(a))
# #convert the type of data into ndarray object

# import numpy as np
# # varname = np.array() #syntax
# b= np.array(a)
# print(b,type(b))

# import numpy as np

# a = 10 #10.3
# print(a,type(a))

# #convert int datatype into ndarray object
# b = np.array(a)
# print("content of b = ",b)
# print("type of b= ",type(b))
# print("Data typ of b=",b.dtype)
# print("Dimension of b =",b.ndim)
# print("shape of b =",b.shape)
# print("size of b= ",b.size)

# import numpy as np
# a = 10.3
# print(a,type(a))
# #convert float datatype  into the ndarray object
# b = np.array(a)
# print(b,type(b))
# print("content of b =",b) 
# print("type of b =",type(b))
# print("Data type of b =",b.dtype)
# print("Dimension of b =",b.ndim)
# print("shape of b =",b.shape)
# print("size of b =",b.size)
# print("-------------------------------------")

# import numpy as np
# a = "python"
# print(a,type(a))
# #convert str  datatype  into the ndarray object
# b = np.array(a)
# print(b,type(b))
# print("content of b =",b) 
# print("type of b =",type(b))
# print("Data type of b =",b.dtype)
# print("Dimension of b =",b.ndim)
# print("shape of b =",b.shape)
# print("size of b =",b.size)
# print("-------------------------------------")

# import numpy as np
# r  =range(12)
# print(r,type(r))
# # for val in r:
# #     print(val)
# #convert str  datatype  into the ndarray object
# b = np.array(r,float) #(r,dtype=float)
# print(b,type(b))
# print("content of b =",b) 
# print("type of b =",type(b))
# print("Data type of b =",b.dtype)
# print("Dimension of b =",b.ndim)
# print("shape of b =",b.shape)
# print("size of b =",b.size)
# print("-------------------------------------")

import numpy as np
# r  =range(12)
# print(r,type(r))
# # for val in r:
# #     print(val)
# #convert str  datatype  into the ndarray object
# b = np.array(r,dtype=float) 
# print(b,type(b))
# print("content of b =",b) 
# print("type of b =",type(b))
# print("Data type of b =",b.dtype)
# print("Dimension of b =",b.ndim)
# print("shape of b =",b.shape)
# print("size of b =",b.size)
# print("-------------------------------------")


#Reshape  the ndarray Elements
#1 .By using reshape() of ndarray object
#2 .By us ing shape attributes


#reshape the 6 Element of ndarray as 3x2 or 2x3 or 1x6 or 6x1 using reshape()

# r = range(10,21,2)
# a = np.array(r)
# print(a,type(a))
# # print(a.reshape(3,2)) #todo - both the 2 way is to reshape the array 
# a = a.reshape(3,2)  #todo - both the 2 way is to reshape the array
# print(a)
# print("content of a = ",a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)
# print("shape of a= ",a.shape)
# print("size of a = ",a.size)


#reshape the 6 elements of ndarray as 3x2 or 2x3
# a = a.reshape(6,1)
# print("content of a = ",a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)
# print("shape of a= ",a.shape)
# print("size of a = ",a.size)

# a = a.reshape(1,6) 
# print("content of a = ",a) #content of a =  [[10 12 14 16 18 20]]
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)
# print("shape of a= ",a.shape)
# print("size of a = ",a.size)

#todo  convert the 2D to 1D by using shape attribute
# a.shape = (6,)
# print("content of a = ",a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)
# print("shape of a= ",a.shape)
# print("size of a = ",a.size)

#todo  convert the 1D to 2D by using shape attribute
# a.shape = (3,2)
# print("content of a = ",a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)
# print("shape of a= ",a.shape)
# print("size of a = ",a.size)
 
a =np.array(range(16))
# print("content of a = ",a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)
# print("shape of a= ",a.shape)
# print("size of a = ",a.size)

# #todo - convert the 1D into 2D 
# a.shape = (4,4)
# print("content of a = ",a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)
# print("shape of a= ",a.shape)
# print("size of a = ",a.size)

#todo - convert the 2D into 3D 
# a.shape = (2,4,2)
# print(a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)
# print("shape of a= ",a.shape)
# print("size of a = ",a.size)


#todo - convert the 2D into 3D 
# a.shape = (4,2,2)
# print(a)
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)
# print("shape of a= ",a.shape)
# print("size of a = ",a.size)

#todo - convert the 3D into 4D 
# a.shape = (2,2,2,2)
# print(a,type(a))
# print("type of a =",type(a))
# print("Data type of a= ",a.dtype)
# print("Dimension of a= ",a.ndim)
# print("shape of a= ",a.shape)
# print("size of a = ",a.size)

#todo - convert list object into ndarray object
# # lst =[10,20,30,40,50,60,70,80,90]
# #print("content of lst = ",lst)
# #print("type of lst",type(lst))
# #print("----------------------------------")
# a = np.array(lst,float)
# print(a)
# print("type of a =",type(a))
# print("Data type a=",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a = ",a.shape)
# print("size of a =",a.size)

# a.shape = (3,3)
# print(a)
# print("type of a =",type(a))
# print("Data type a=",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a = ",a.shape)
# print("size of a =",a.size)

# lst =[10,"RS",34.56,True,2+3j,"python"]
# print("COntent os lst =",lst)
# print("Type of lst=",type(lst))
# print("---------------------------")

# a = np.array(lst)
# print("content os a ",a)
# print("type of a",type(a))
# print("Data type a=",a.dtype)

# a = np.array(lst,object) # dtype = object 
# print("content os a ",a)
# print("type of a",type(a))
# print("Data type a=",a.dtype)


# print(a.reshape(3,2))
# print(a) #normal element aahe 


# a = a.reshape(3,2)
# print("type of a =",type(a))
# print("Data type a=",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a = ",a.shape)
# print("size of a =",a.size)





#todo - convert tuple object into ndarray object
# lst =(10,20,30,40,50,60,70,80,90)
# print("content of lst = ",lst)
# print("type of lst",type(lst))
# print("----------------------------------")
# a = np.array(lst,float)
# print(a)
# print("type of a =",type(a))
# print("Data type a=",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a = ",a.shape)
# print("size of a =",a.size)


#todo - convert set object into ndarray object
# s = {10,20,30,40,50}
# print("content of set=",s)
# print("type of set=",type(s))
# print("----------------------------")
# a = np.array(s)
# print(a)
# print("type of a =",type(a))
# print("Data type a=",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a = ",a.shape)
# print("size of a =",a.size)

# d = {   10:1.2,20:2.2,30:3.3,40:4.4}
# print("content of set=",d)
# print("type of set=",type(d))
# print("----------------------------")
# a = np.array(d)
# print(a)
# print("type of a =",type(a))
# print("Data type a=",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a = ",a.shape)
# print("size of a =",a.size)

#! <1>.array()
#^----------------------------------------------------------------------------------------
#* int
#*syntax-1
import numpy as np
# a = 10
# print("content of a =",a)
# print("type of a = ",type(a))
# b =np.array(a)
# print("content of b = ",b)
# print("type of b = ",type(b))
# print("Data type of b =",b.dtype)
# print("Dimension of b = ",b.ndim)
# print("shape of a = ",b.shape)
# print("size of b =",b.size)

#*syntax 2
# a = 10
# print("content of a =",a)
# print("type of a = ",type(a))
# b = np.array(a,dtype= str) #*
# print("content of b=",b)
# print("type of b=",type(b))
# print("data type of b =",b.dtype)
# print("dimension of b=",b.ndim)
# print("shape of b=",b.shape)
# print("size of b=",b.size)

#*syntax 3
# import numpy as np
# a =20
# print("content of a =",a)
# print("type of a =",type(a))
# # print()
# b = np.array(a,float)
# print("content of b =",b)
# print("type of b=",type(b))
# print("data type of b=",b.dtype)
# print("dimension of b=",b.ndim)
# print("shape of b =",b.shape)
# print("size of b =",b.size)

#^---------------------------------------------------------------------------------------------------
#*float
#*syntax 1
# import numpy as np
# a = 20.2
# print("content of a =",a)
# print("type of a =",type(a))
# b = np.array(a)
# print("content of b =",b)
# print("type of b =",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b =",b.shape)
# print("size of b=",b.size)

#*syntax 2
# import numpy as np
# a = 20.2
# print("content of a=",a)
# print(type(a))
# b = np.array(a,dtype=int)
# print("content of b =",b)
# print("type of b =",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b =",b.shape)
# print("size of b=",b.size)

#*syntax 3
# import numpy as np
# a = 20.2
# print("content of a=",a)
# print(type(a))
# b = np.array(a,str)
# print("content of b =",b)
# print("type of b =",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b =",b.shape)
# print("size of b=",b.size)

#^---------------------------------------------------------------------------------------------------
#*str
# import numpy as np
# a = "python"
# print("content of a =",a)
# print(type(a))
# b = np.array(a)
# print("content of b =",b)
# print("type of b =",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b =",b.shape)
# print("size of b=",b.size)

#^---------------------------------------------------------------------------------------------------

#*range 
#* syntax 1
# import numpy as np
# r = range(12)
# print("content of r =",r)
# print("type of r= ",type(r))
# b = np.array(r)
# print("content of b =",b)
# print("type of b =",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b =",b.shape)
# print("size of b=",b.size)

#*syntax 2
# import numpy as np
# r = range(12)
# print("content of r =",r)
# print("type of r= ",type(r))
# b = np.array(r,dtype=str)
# print("content of b =",b)
# print("type of b =",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b =",b.shape)
# print("size of b=",b.size)

#*syntax 3
# import numpy as np
# r = range(12)
# print("content of r =",r)
# print("type of r= ",type(r))
# b = np.array(r,str)
# print("content of b =",b)
# print("type of b =",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b =",b.shape)
# print("size of b=",b.size)


# import numpy as np
# r = range(10,21,2)
# print("content of r =",r)
# print("type of r= ",type(r))
# b = np.array(r)
# print("content of b =",b)
# print("type of b =",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b =",b.shape)
# print("size of b=",b.size)


# import numpy as np
# r = range(10,21,2)
# print("content of a =",r)
# print("type of a =",type(r))
# b = np.array(r,float)
# print("content of b =",b)
# print("type of b=",type(b))
# print("data type of b = ",b.dtype)
# print("dimension of b = ",b.ndim)
# print("shape of b =",b.shape)
# print("size of b=",b.size)

#^---------------------------------------------------------------------------------------------------
#* 1. By using reshape() of ndarray object
#* 2. By using shape attribute
# import numpy as np
# a = [10,20,30,40,50,60]
# b =np.array(a)
# print(b.reshape(3,2))
# print(b)

# #^---------------------------------------------------------------------------------------------------
# #* b la pan update karalagat asel asel tar b la pan update kara lagate
# b = b.reshape(3,2)
# print("Content of b=\n",b)
# print("type of b =",type(b))
# print("data type of b=",b.dtype)
# print("Dimension of b=",b.ndim)
# print("shape of b =",b.shape)

# import numpy as np
# a = [10,20,30,40,50,60]
# b = np.array(a)
# b.shape = (3,2)
# # print(b,type(b))
# b = b.reshape(6,)
# print("content of b =",b)
# b.shape = (6,)
# print(b)

#* i want to convert 2Darray into 1D array ,reshape() can't be used
#* to do this we use shape attribute

# b.shape = (6,)
# print("content of b =",b)
# print("type of b = ",type(b))
# print("data type of b =",b.dtype)
# print("dimension of b =",b.ndim)
# print("shape of b = ",b.shape)

# import numpy as np
# a = np.array(range(16))
# print("content of b=\n",a)
# print("type of b=",type(a))
# print("data type of a =",a.dtype)
# print("dimension of a =",a.ndim)
# print("shape of a = ",a.shape)
# print("size of a =",a.size)

# # #*convert 1D data into 2D
# a.shape = (4,4)
# print("content of a =\n",a)
# print("type of a =",type(a))
# print("data type of a",a.dtype)
# print("Dimension  of a =",a.ndim)
# print("shape of a =",a.shape)
# print("size of a =",a.size)

# #*Convert the above 2D data into 3D---(2,4,2)
# a.shape =(2,4,2)
# print(a,type(a))
# print("data type of a =",a.dtype)
# print("Dimension of a=",a.ndim)
# print("shape of a =",a.shape)
# print("size of a =",a.size)

# #* Convert the above 3D data into 4D---(2,2,2,2)
# a.shape =(2,2,2,2)
# print("content of a =\n",a)
# print("Type of a=",type(a))
# print("Data Type of a=",a.dtype)
# print("Dimension of a=",a.ndim)
# print("Shape of a=",a.shape)
# print("Size of a=",a.size)

# a.shape =(4,2,2,1)
# print(a)

#* convert list object into ndarray object
# lst = [10,20,30,40,50,60,70,80,90]
# a = np.array(lst)
# print("content of a =",a)
# print("type of a =",type(a))
# print("Data type of a =",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a =",a.shape)
# print("size of a =",a.size)


# lst = [10,20,30,40,50,60,70,80,90]
# a = np.array(lst,float)
# print("content of a =",a)
# print("type of a =",type(a))
# print("Data type of a =",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a =",a.shape)
# print("size of a =",a.size)

# a.shape = (3,3)
# print("content of a =\n",a)
# print("type of a =",type(a))
# print("Data type of a =",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a =",a.shape)
# print("size of a =",a.size)

# import numpy as np
# lst = [10,"RS",34.56,True,2+3j]
# a = np.array(lst)
# print("content of a =\n",a)
# print("type of a =",type(a))  # ['10' 'RS' '34.56' 'True' '(2+3j)'] 

# print("Data type of a =",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a =",a.shape)
# print("size of a =",a.size)

# import numpy as np
# lst = [10,"RS",34.56,True,2+3j]
# a = np.array(lst,dtype=object)  # [10 'RS' 34.56 True (2+3j)]
# print("content of a =\n",a)
# print("type of a =",type(a))
# print("Data type of a =",a.dtype)
# print("Dimension of a =",a.ndim)
# print("shape of a =",a.shape)
# print("size of a =",a.size)

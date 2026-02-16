# import numpy as np
# a= np.array([10,15,25,30,35,40,45,34,56,67,19,18])
# print("Content of a ")
# print(a)

# #get all even values
# ba= a%2 ==0
# print(ba,type(ba))
# #convert the boolean arraay into the Ndarray 

# print(a[ba])

#^--------------------------------------------------------------------------------------------------
#Get all odd values boolean array
# ba = a%2!=0
# print(ba)
# print(a[ba])


#^--------------------------------------------------------------------------------------------------
# import numpy as np
# a=np.array([10,-15,0,25,-30,35,0,-40,45,-34,56,67,-19,18])
# print("content of a ")
# print(a)


# ba = a>0
# print(ba,type(ba))

# #convert the boolean array into Ndarray
# print(a[ba])

# boolarray = a<0     # here ba is called Boolean Array
# print(boolarray,type(boolarray))
#                 #Pass Boolean Array to ndarray object

# print(a[boolarray])                

#^--------------------------------------------------------------------------------------------------



#
#*Get all the negative values 
# ba = a<0       # here ba is called Boolean Array
# print(a[ba])   #Pass Boolean Array to ndarray object  

#*or 
# print(a[a<0])
#^--------------------------------------------------------------------------------------------------

# import numpy as np
# a=np.array([10,15,25,30,35,40,45,34,56,67,19,18])
# print("Content of a")
# print(a)

# #Get multiple of 3
# ba = a%3 ==0
# print(ba,type(ba))
# # pass the bool array into Ndarray
# print(a[ba])  #Get multiple of 3

# #* OR

# print(a[a%3==0])
#^--------------------------------------------------------------------------------------------------
#! Filtering with where()
#! 1D
# import numpy as np
# a=np.array([10,15,25,30,35,40,45,34,56,67,19,18])
# print("content of a ")
# print(a)

#* Get Multiple 4 by using numpy.where()
# index = np.where(a%4==0)
# print(index)
# print(a[index]) 
# #
# for val in index[0]:
#     # print(val)
#     print(a[val],end=" ")

#^--------------------------------------------------------------------------------------------------
import numpy as np
a=np.array([10,-15,0,25,-30,35,0,-40,45,-34,56,67,-19,18])
print("Content of a ")
print(a)

#* Get +Ve Elements by using numpy.where()
# indx = np.where(a>0)
# print(indx ,type(indx))

# print("Positive Element Indeices")
# # print(indx[0])

# print("Positive Element ")
# for i in indx[0]:
#     print(a[i],end=" ")

#*OR 
# print(a[indx])
#^--------------------------------------------------------------------------------------------------

#* Get -Ve Elements by using numpy.where()
# indx = np.where(a<0)
# print(indx,type(indx))

# print("Negative Element indices ")
# print(indx[0])

# print( "Negative Element ")
# for i in indx[0]:
#     print(a[i])

# #*OR
# print(a[indx])
#^--------------------------------------------------------------------------------------------------







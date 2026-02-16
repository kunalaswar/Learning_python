    #! extract()
    #* by using this function we can get the boolean array object
    #*
import numpy as np
lst = [10,15,20,25,34,36,21]
# lst =lst+1 #*Error
# for val in lst:
#     if val%2==0:
#         print(val)

# print(lst+1)
# lst1=[]
# for val in lst:
#     lst1.append(val+1)
# print(lst1)    
# positivelist = list(filter(lambda x:x%2==0,lst))
# print(positivelist)
    

# import numpy as np
# a = np.array(lst)
# print(a,type(a))
# a = a+1
# print(a)



# a = np.array([10,15,25,30,35,40,45,34,56,67,19,18])
# print("content of a ")
# print(a)

#*Get all Even element into ndarray 
# ba = a%2==0
# print(ba,type(ba))

# print("list of Even values")
# print(a[ba])


#*Get all Odd element into ndarray 
# booleanarray=a%2!=0
# print(booleanarray,type(booleanarray))
# print("list of Odd values")
# print(a[booleanarray])


# a = np.array([10,-15,0,25,-30,35,0,-40,45,-34,56,67,-19,18])
# print("content of a ")
# print(a)
# print("Positive values")
# ba = a>0
# #pass Boolean Array to ndarray object
# print(a[ba])

#* OR
# Get all +ve values
# print(a[a>0])

#Negative values
# ba = a<0 #todo - ba is called Boolean array
# print(a[ba])

#* OR
# print(a[a<0])

#* get multiples of 3
# print(a[a%3==0])

#get multiple of 3 and 5
# ba = (a%3==0 and (a%5==0)) # we can not use the and operator in numpy 
# ba = (a%3==0 & (a%5==0)) # we use bitwise &
# print(a[ba])

#*
# a = np.array([10,15,25,30,35,40,45,34,56,67,19,18])
# print(a)
# ind = np.where(a%4==0)
# # print(ind,type(ind))
# print(ind)
# for i in ind[0]:
#     print(a[i])

#*
# a = np.array([10,-15,0,25,-30,35,0,-40,45,-34,56,67,-19,18])
# print("content of a ")
# print(a)
# # get +VE Element by using numpy.where()
# ind = np.where(a>0)
# print(ind)
# for i in ind:
#     print(a[i])

#*

# a = np.array([10,-15,0,25,-30,35,0,-40,45,-34,56,67,-19,18])
# print("content of a ")
# print(a)
# # get -VE Element by using numpy.where()
# ind = np.where(a<0)
# print(ind)
# for i in ind:
#     print(a[i])

#todo - 2D 
# a = np.random.randint(10,25,size=(3,3))
# print(a,type(a))
# print(a.ndim)
#get the element More than 15 with filtering
# print(a[a>15])

#get the element Less than or equal to 15 with filtering
# print(a[a<=15])


#todo - get the Element More the 15 with numpy.where()
# ind = np.where(a>15)
# a.shape = (9,)
# for i in ind[0]:
#     print(i)

#*
# a = np.random.randint(10,25,size=(3,3))
# print(a,type(a))
# # print(a.ndim)
# ind = np.where(a>15)
# a.shape = (9,)
# print(a)
# print("-------------------")
# for i in ind[0]:
#     print(a[i])


#todo - 

# working  with Missing Data ---which is Represented with np.NaN OR None
import numpy as np
# #value is replace with 0 
# data  = np.array([1,2,None,3,4])
# #replace Missing with 0
# print("---------------------------------------")
# data = np.where(data==None, 0, data)
# print(data)
#* OR 

# print(np.where(data==None, 0, data))

import numpy as np
a =np.random.randint(2,40,size=14)
print(a,type(a))
#* #Get the values which are more than 20
# morethan_20= np.extract(a>20,a)
# print("Value is more than 20 :",morethan_20) # with use of where function 

# #* Get the Values which is less than 20
# lessthan_20 = np.extract(a<=20,a)
# print("Value less than 20 =",lessthan_20)

# a = np.random.randint(2,40,size=14)
# print(a,type(a))
# more = np.extract(a>30,a)
# print(more)

#^-----------------------------------------------
# a =19
# def more20(n):
#     res = True if n>20 else False    
#     return res

# morethan20 = np.extract(more20 ,a)
# print("More than 20 =",morethan20)

#^-----------------------------------------------







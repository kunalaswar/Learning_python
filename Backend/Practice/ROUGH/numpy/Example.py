# import numpy as np
# import sys 
# lst =[1,2,3,4,56,7,8,9,1,2,3,4,5,6,7,8,9]

# print("Size of lst",sys.getsizeof(lst))

# arr = np.array(lst)
# print("Size of arr ",sys.getsizeof(arr))

# import sys
# import numpy as np
# lst = [10,20,30,40,56]
# print("lst = ",sys.getsizeof(lst))

# a = np.array(lst)
# print("ndarry = ",sys.getsizeof(a))



# a = np.array(lst)
# print(a,type(a))
# print("Memory space of the list object =",sys.getsizeof(a))


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



#import numpy as np 
# lst = [10,20,30,40,50,60]
# print("Content of list ")
# print(lst,type(lst))
# print("----------------------------------------")
# #*Convert list object into ndarray object 
# a = np.array(lst )
# print("Content of ndarray ")
# print(a)
# #* get the dimension of ndarray
# print("Dimension of ndarray =>",a.ndim)
# print(a.reshape(2,3))


# lst = [10,20,30,40,50,60,80,90,21,22,45,56]
# print("content of list ")
# print(lst,type(lst ))
# #* Convert the list into ndarray object 
# a = np.array(lst )
# print("content of ndarray ")
# print(a ,type(a))
# print("Dimension of ndarray =>",a.ndim)
# print(a.reshape(2,3,2))



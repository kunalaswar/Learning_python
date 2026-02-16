
import numpy as np
# a= np.array([10,20,30,40,50,60,70,80,90])
# print(a,type(a))

# import sys 
# lst = [1,2,3,4,5,6,7,8,9,12,23,4,5,65,67,78,89,90]
# print(lst,type(lst),sys.getsizeof(lst))
# a = np.array(lst)
# print(a,type(a),sys.getsizeof(a))

# # vector based operation
# lst = [10,20,30,40]
# # lst2 = lst+1 #*Error
# # print(lst2)
# lst3 = []
# for val in lst:
#     # print(val+1) 
#     lst3.append(val+1)
# print(lst3)    
    
# a = np.array(lst)    
# print(a+1)


# lst = [10,20,30,40]
# for i in range(len(lst)):
#     lst[i]=lst[i]+1
# print(lst)    

# lst= [10,20,30,40]
# print(lst)
# a = np.array(lst).reshape(2,2)
# a = np.array(lst,dtype=object)
# a.shape = (2,2)
# print(a,type(a))
# print(a.dtype)   
# print(a.ndim)
# print(a.shape)
# print(a.size)

# a = np.arange(5)
# print(a)
# a = np.arange(0,5)
# print(a)
# a = np.arange(0,5,1)
# print(a)


# a = np.zeros(6).reshape(2,3)
# print(a,type(a))
# a = np.zeros(6,dtype=int)
# print(a)
# a = [1,2,3,4,5]

#^========================================================================================

# a = [12,45,65,99,90,90,99]
# a.sort()
# m = a[-1]
# c = a.count(m)
# sm = a[-(c+1)]
# cs = a.count(sm)
# tm = a[-(cs+c+1)]
# print("First Max :",m,"Second Max :",sm,"Third Max :",tm,sep='\n')

#^========================================================================================

# a = [12,45,35]
# m = 0
# sm = 0
# for val in a:
#     if val>m:
#         sm = m
#         m = val
#     elif sm<val<m:
#         sm = val
# print("Max :",m)
# print("Second Max :",sm)

#^========================================================================================

# a = [12,45,65,99,90,90,99]
# m=0
# for i in a:
#     if i>m:
#         m=i 
# sm=0
# for i in a:
#     if i==m:pass
#     elif i>sm:
#         sm=i 
# print(m,sm)


# a = np.array([1,2,3,4])
# # print(a)
# print(np.where(a>2 ,a,100))
# # print()

# a  =np.array([1,2,3,4])
# x = np.array([10,20,30,40])
# y = np.array([100,200,300,400])
# print(np.where(a>2 ,x,y))

# a = "python"
# for val in a:
#     print(val)

# import sys
# lst = [1,2,3,4,5,6]
# print(lst,sys.getsizeof(lst))
# a = np.array(lst)
# print(a,type(a),sys.getsizeof(a))

# a = np.arange(10)
# print(a,type(a))

# a = np.zeros()
# a = np.zeros(6,dtype=int).reshape(3,2)
# print(a,type(a))
# print(a.ndim)

# a = np.ones(6,dtype=int).reshape(3,2)
# print(a,type(a))

# a = np.full(6,fill_value=9,dtype=int).reshape(3,2)
# print(a,type(a))


# a = np.identity(2,dtype=int)
# print(a,type(a))

# a = np.eye(10,k = -1)
# print(a)

# a,rv = np.linspace(1,2,num=4,retstep=True)
# # print(round(a,2))
# # print(np.round(a,2))
# print(a)
# print(rv)

# a  = np.array([1,2,3,4,5,6]).reshape(2,3)
# print(a)
# b  = np.array([10,20,30,40,50,60]).reshape(2,3)
# print(b)

# c = np.hstack((a,b))
# print(c)
# d = np.vstack((a,b))
# print(d)

 
# import numpy as np
# a = np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# print(a,type(a))

# a.shape = (3,3)
# print(a,type(a))

# lst = [21,3,2,4,15,6,7,]
# a = np.array((lst))
# a = np.where(a<=15)
# print(a)

from numpy import random as r
# a  = r.randint(10)
# print(a)

# a = r.randint(1,5)
# print(a)

# a = r.randint(1,2,size=9).reshape(3,3)
# print(a)

# a = r.rand(3)
# print(a)

# a = r.rand(size =3) #*  Error 

# a = r.rand(2,2)
# print(a)

# a = r.uniform() #It Gives values in uniform manner like a same 
# print(a)

# a = r.uniform(2,3)
# print(a)

# a = r.uniform(0,11)
# print(a)

# a = r.uniform(10,15,size=5)
# print(a,type(a))

# a = r.randn()
# print(a)

# a = r.randn(1,4).reshape(2,2)
# print(a)


# a = r.normal()
# print(a,type(a))

# a = r.normal(loc=2,scale=3,size=4).reshape(2,2)
# print(a)

# lst = [1,2,3,4,5,6,7,8,9]
# a =np.array(lst)
# a2 = r.choice(a)
# print(a2)

# a = r.randint(10,size=(3,3))
# print(a)
# print(r.choice(a))

# a = r.randint(9)
# ch  = r.choice(a,size=(2,2))
# print(ch)

# a = np.arange(10)
# print(a)
# # print(r.shuffle(a)) #* None
# print(a)

# a = np.arange(9).reshape(3,3)
# print("After shuffle :")
# print(a,type(a))
# print("Before shuffle :")
# r.shuffle(a)
# print(a)

# a = r.randint(1,100,size=(4,3,3))
# print("After shuffle the matrix:")
# print(a,type(a))

# print("Before shuffle the matrix:")
# r.shuffle(a)
# print(a)

# a = r.randint(1,100,size=(4,3,3))
# # print(a)
# s1 = r.permutation(a)
# print(a)
# print("-------------------")
# print(s1)

# import itertools as i
# lst = [1,2,3]
# # a = tuple(i.permutations(lst))
# a = list(i.permutations(lst))
# print(a)


# import itertools as i
# lst = [1,2,3]
# a = list(i.permutations(lst,2))
# print(a)


# Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3]
# Output: 5
# Explanation: Union set of both the arrays will be 1, 2, 3, 4 and 5. So count is 5.

# class Solution:    
#     #Function to return the count of number of elements in union of two arrays.
#     def findUnion(self, a, b):
#         # code here
#         count =0
#         union_list=[]
#         for val in a:
#             if val not in union_list:
#                 union_list.append(val)
#         for val in b:
#             if val not in union_list:
#                 union_list.append(val)    

#         return len(union_list)

        

        
# s = Solution()        
# c=s.findUnion(a=[1,2,3,4,5],b=[1,2,3])
# print(c)

# class Solution:    
#     #Function to return the count of number of elements in union of two arrays.
#     def findUnion(self, a, b):
#         # code here
#         count =0
#         lst3=[]
#         for val in a:
#             lst3.append(val)
#         for val1 in b:
#                 lst3.append(val1)  
#         print(lst3) 
#         for val in lst3:
#                 if val  in b:
#                       continue
#                 else:         
#                     count=count+1
#         return count
        
# s = Solution()        
# c=s.findUnion(a=[1,2,3,4,5],b=[1,2,3])
# print(c)


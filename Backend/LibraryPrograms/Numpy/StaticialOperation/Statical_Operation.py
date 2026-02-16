 #todo - Statistical function 
import numpy as np
# a = np.random.randint(10,30,size=15)
# print(a,type(a))

# print("----------------------------------------------------")

#^-----------------------------------------------------------------------------------------------------
# Find Min and Max into the 1D array
# a = np.random.randint(10,30,size=15)
# print("content of a ")
# print(a,type(a))

#* Find the min and max form ndarray object
# maxv = np.amax(a)
# minv = np.amin(a)
# print("Max value = ",maxv)
# print("Min value =",minv)

#^-----------------------------------------------------------------------------------------------------
# Find Min and Max into the 2D array

# a = np.random.randint(10,30,size=(4,4))
# print(a)
# print("Type of a =",type(a))
# maxv = np.amax(a)
# minv = np.amin(a)
# print("Mix vlaue =",maxv)
# print("Min value =",minv)
# print("-------------------------------------")

#^-----------------------------------------------------------------------------------------------------
# Find Min and Max into the 3D array
# a = np.random.randint(10,30,size=(2,3,3))
# print(a)
# print(type(a))
# print("----------------------------------------")
# maxv = np.amax(a)
# minv = np.amin(a)
# print("Min value = ",maxv)
# print("Min value =",minv)
#^-----------------------------------------------------------------------------------------------------

#todo -Now my req :To find Column wise and Row wise Max and min value
#todo - To Do this above Me must use axis concept
#todo - if axis = 0 then its refers COLUMNS
#todo - if axis = 1 then its refers ROWS
# a = np.random.randint(10,30,size=(4,4)) 
# print(a)
# maxv = np.amax(a)
# minv = np.amin(a)
# colmax = np.amax(a,axis =0)
# rowmax = np.amin(a,axis=1)
# print("------------------------------------------------")
# colmax = np.amax(a,axis=0)
# rowmax = np.amax(a,axis=1)
# rowmin = np.amin(a,axis=0)
# colmin = np.amin(a,axis=1)

# print(maxv)
# print(minv)
# print("column Max = ",colmax)
# print("Row Max =",rowmax)
# print("Column min =",rowmin)
# print("Row max = ",colmin)
# print("---------------------------------------------")


#^-----------------------------------------------------------------------------------------------------
#find the mean of the ndarray  by using mean() --1 D dim
#todo - To find Average 
# a = np.array([3,1,2,4])
# m = np.mean(a)
# print(f"Mean of {a} = {m}")

# #Our own code for finding the sum and mean 
# s  =0
# for val in a:
#     s = s+val
# print("Sum of it =",s)    
# print("Mean of the =",s/len(a))

#^-----------------------------------------------------------------------------------------------------
#* find the Mean of the ndarray by using Mean() ---2  dim
# a = np.array([3,1,2,4]).reshape(2,2)
# print("Matrix A")
# print(a)
# m = np.mean(a)
# cm = np.mean(a,axis=0)
# rm = np.mean(a,axis=1)
# print(m)
# print("Column value mean ",cm)
# print("Row value mean = ",rm)

#^-----------------------------------------------------------------------------------------------------
#find the mean on the ndarray by using mean()
# Find mean for row and cols 
# a = np.random.randint(1,50,size=(5,5))
# print("------------------------------")
# print("MAtris _A")
# print(a)
# m = np.mean(a)
# cm = np.mean(a,axis=0)
# rm = np.mean(a,axis=1)
# print("Mean " ,m)
# print("Column mean",cm)
# print("Row mean",rm)

#^-----------------------------------------------------------------------------------------------------
#find the median of ndarray --Dim with ODD Number of Element
# a = np.array([10,2,14,3,18,20,5])
# print("------------------------")
# print("Content of a ")
# print(a)
# m = np.median(a)
# print(f"Median {a} = {m}")
# print("--------------------------------------")

#^-----------------------------------------------------------------------------------------------------
#Find the median of ndarray--1-Dim with Even Number of Elements
# a=np.array([10,2,14,3,18,20,5,6])
# print("----------------------------------")
# print("Content of a")
# print(a)    
# m = np.median(a)
# print(f"Median {a} = {m}")

#^-----------------------------------------------------------------------------------------------------
#find  the median of ndarray --2D with Even  number of element
# a=np.array([10,2,14,3,18,20,5,6,12,22,13,25,19,4,1,9]).reshape(4,4)
# print("COntent of a ")
# print(a)
# print("---------------------------")
# m=np.median(a)
# print(f"Median of {a} = {m}")
# # to get this col -wise and Row -Wise Median
# cm = np.median(a,axis=0)
# rm = np.median(a,axis=1)
# print(f"Col Median\n {a} = {cm}   ")
# print(f"row median\n {a} = {rm}")
#^-----------------------------------------------------------------------------------------------------
#find Varience by using var()
# a = np.array([3,1,2,4])
# print("Content of a =")
# print(a)
# v = np.var(a)
# print("Varience of a =",v)

#^-----------------------------------------------------------------------------------------------------
#find Col; and Row -wise Varience
# a = np.array([3,1,2,4]).reshape(2,2)
# print("Content of a ")
# print(a)
# v = np.var(a)
# print(v)
# cv = np.var(a,axis=0)
# rv = np.var(a,axis=1)
# print("Column var =",cv)
# print("Row var =",rv)

#^-----------------------------------------------------------------------------------------------------
#find col and Row-wise Varience 
# a = np.arange(4*3).reshape(4,3)
# print("Content of a")
# print(a)
# v = np.var(a)
# print("Varience =",v)
# cv = np.var(a,axis=0)
# rv = np.var(a,axis=1)
# print("Column Wise varience = ",cv)
# print("ROw wise  varience = ",rv)
#^-----------------------------------------------------------------------------------------------------

# #find col and Row-wise Varience 
# a = np.arange(4*3).reshape(4,3)
# print("---------------------------")
# print("Content of a ")
# print(a)
# v = np.var(a)
# print("varience =%0.2f" %v)
# cv = np.var(a,axis=0)
# rv = np.var(a,axis=1)
# print("Column wise varience =",cv)
# print("Row eise varience =",rv)
# for val in cv:
#     print(round(v,2),end=" ")
# print()

# for val in rv:
#     print(round(val,2),end=" ")
#^-----------------------------------------------------------------------------------------------------
#We Know that standard Deviation= sqrt(Var)
#Find Col and Row-wise variance
# a = np.array([3,1,2,4]).reshape(2,2)
# print("-----------------------")
# print("content of a ")
# print(a)
# s = np.std(a)
# print("Standard deviation  = ",s)
# csd = np.std(a,axis=0)
# rsd = np.std(a,axis=1)
# print("Col std = ",csd)
# print("Row std = ",rsd)
#^-----------------------------------------------------------------------------------------------------
#find the mode of ndarray
# a = np.array([3,1,2,4,3,3])
# print("Content of a ")
# print(a)
# m = np.mode(a) AttributeError: module 'numpy' has no attribute 'mode'. Did you mean: 'mod'?


#^-----------------------------------------------------------------------------------------------------
#find the Mode of ndarray by using a pre-defined Module statistics of python
# import statistics as s
# a = np.array([3,1,2,4,3,3])
# print("Content of a ")
# print(a)
# print("-----------------------")
# m = s.mode(a)
# print("Mode =",m)

#^-----------------------------------------------------------------------------------------------------


##find the mode of ndarray by using a predefined module Statistics of python
# import statistics as s
# a=np.array([3,1,2,4,3,3,1,1]) #^ give proverity to the First Given Element 
# print("----------------------------------")
# print("Content of a")
# print(a)
# m = s.mode(a)
# print("mode = ",m) # *mode =  3

#^-----------------------------------------------------------------------------------------------------
##find the mode of ndarray by using a predefined module Statistics of python
import statistics as s
# a=np.array([1,3,2,4,3,3,1,1]) #^ give proverity to the First Given Element  
# print("----------------------------------")
# print("Content of a")
# print(a)
# m = s.mode(a)
# print("mode = ",m) #* mode =  1

#^-----------------------------------------------------------------------------------------------------
#* find the mode of ndarray by using a predefined module Statistics of python
# import statistics as s
# a = np.array([1,3,2,4,3,3,1,1,2,2])
# print("Content of a ")
# print(a)
# print("---------------")
# m = s.multimode(a)
# print("Using Multimode = ",m)

#^-----------------------------------------------------------------------------------------------------
#* find the mode of ndarray by using a predefined module Statistics of python
# import statistics as s
# a = np.array([1,3,2,4,3,3,1,1,2,2,3])
# print("Content of a ")
# print(a)

# m = s.multimode(a)
# print("Using Multimode =",m)

#^-----------------------------------------------------------------------------------------------------

#find second maximun into array/list
lst = [10,12,14,15,16]
l = lst[0]
count = 0
for val in lst:
    if val>l:
        l=val
        count = count+1

print(l)










#^-----------------------------------------------------------------------------------------------------










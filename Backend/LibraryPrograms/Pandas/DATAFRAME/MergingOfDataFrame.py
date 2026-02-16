

#* Syntax =  pandas.concat(DataFrameobj1,DataFrameobj2,.....DataFramobj-n,axis = 0)  #row-wise concat

#* Syntax =  pandas.concat(DataFrameobj1,DataFrameobj2,.....DataFramobj-n,axis = 1)  #column-wise concat

import numpy as np,pandas as pd
# List of tuple
data1= [('Jack', 34, 'Sydney', 5) ,
        ('Riti', 31, 'Delhi' , 7) ,
        ('Aadi', 46, 'New York', 11)]
# List of Tuples
data2= [('Mohit', 34, 'Tokyo', 11) ,
        ('Veena', 31, 'London' , 10) ,
        ('Shaun', 36, 'Las Vegas', 12)]
# List of Tuples
data3= [('Mark', 47, 'Mumbai',   13) ,
        ('Jose', 43, 'Yokohama', 14) ,
        ('Ramu', 49, 'Paris',    15)]

#Convert data1 , data2 and data3 into DataFrame
df1 = pd.DataFrame(data1,index = ["a","b","c"],columns=["Name","Age","City","Exp"])
df2 = pd.DataFrame(data1,index = ["e","f","g"],columns=["Name","Age","City","Exp"])
df3 = pd.DataFrame(data1,index = ["h","i","j"],columns=["Name","Age","City","Exp"])
print("----------------------------------------")
print("DataFrame -1")
print(df1)
print("----------------------------------------")
print("DataFrame-2")
print(df2)
print("----------------------------------------")
print("DataFrame-3")
print(df3)
print("----------------------------------------")

#! Concatenating DataFrames
#* By default row wise data dete
# fdf = pd.concat([df1,df2,df3])
# print(fdf)


#! Concatenating DataFrames

# xfdf = pd.concat([df1,df2,df3],axis=0)
# print(xfdf)

#!Concatenating DataFrames
#* Concatenating with axis =1 column -wise
# yfdf = pd.concat([df1,df2,df3],axis= 1)
# print(yfdf)



import numpy as np ,pandas as pd
df = pd.read_csv("D:\\PYTHON FULL STACK\\LibraryPrograms\\Pandas\\DATAFRAME\\studentmarks.csv")
print(df)
print("*"*80)

#^======================================================================================================
#& get 7th Record by using loc[]
# print(df.loc[7])

# print(df.loc[10])

#slicing
# print(df.loc[6:7])

#^======================================================================================================
#& Get 14th Record Name
# print(df.loc[14]["name"])    #* sonu

#?======================================================================================================
#& Get 14th Record Name
#todo - get single record name from into table
# print(df.loc[14,["name"]])  
#?======================================================================================================

#& Get 10th Record Name and Maths
#todo - get Multiple record  from into table
# print(df.loc[10,["name","maths"]])
#?======================================================================================================

#& Get 10th Record Name Maths, social Marks
# print(df.loc[10,["name","maths","social"]])
#?======================================================================================================


#& Get 10th Record Name Maths, social Marks and htno
# print(df.loc[10,["htno","name","maths","social"]])

# print(df.loc[10,["name","htno","social","maths"]]) #* Order Not matter  

#^======================================================================================================

#! Applying the slicing Operation by using loc[]

#^======================================================================================================

#& Get the Records from 3 to 6
#* syntax = dataframeobj.loc[start :stop:step]

# print(df.loc[3:6]) # Both are included
#?======================================================================================================

#&  Records from 10 to Last
# print(df.loc[10:])

#?======================================================================================================


#& Get the Records from 10 to Last with Name and Maths Marks
# print(df.loc[10:1,["name","maths"]])   #* KeyError: ('name', 'maths')
# print(df.loc[10:][["name","maths"]])   #* put it into double list into list from
#todo - OR
# print(df.loc[10:,["name","maths"]])


#?======================================================================================================
#& Get the Records from 10 to Last with Name and Maths Marks
# print(df.loc[10:][["name","maths"]])


#?======================================================================================================
#& By using loc[] , Display all Names of Rows

# print(df.loc[::1,["name"]])

#?======================================================================================================

#& get size of the table  by using count() function

# print(df.loc[::1,["name"]].count()) 

#o/p:-
#* name    17
#* dtype: int64
#& get size of the table by using size attribute
# print(df.loc[::-1,["name"]].size)
#o/p:-
#* 17
#?======================================================================================================

#! get the Random records from DataFrame
#todo - it give all data to the number
# print(df.loc[[1,6,9]])

#?======================================================================================================

#& get the Random records from DataFrame with Name, Science and Maths
#todo - it give only Name, Science and Maths
# print(df.loc[[1,6,9]][["name","science","maths"]])


#*   OR
#& get the Random records from DataFrame with Name, Science and Maths
# print(df.loc[[1,6,9],["name","science","maths"]])

#?======================================================================================================
#todo - give complete table 
# print(df.loc[::])
#?======================================================================================================

#& get all the Records from dataFrame with Name, to Maths

#todo - it take more time with it
# df.loc[::,['name','telugu','hindi','english','maths']]


#* OR 

#& get all the Records from dataFrame with Name, to Maths with Column Slicing
#todo -  get  Name, to Maths with Column Slicing
# print(df.loc[::,"name":"maths"])

#?======================================================================================================

#& get only even the Records from dataFrame with Name, to Maths with Column Slicing
# print(df.loc[::2,"name":"maths"])


#& get all the Records from dataFrame with Name, to Maths with Column Slicing
# print(df.loc[::2,"name":"maths":2])

#?======================================================================================================

























   
















#^=====================================================================================================
#!   iloc[]

#todo - It Take size -1 like a python slicing  
#todo - any slicing is done with indexing so that it take size-1  
#todo -it is not like as a label in the loc
#^=====================================================================================================
import numpy as np ,pandas as pd
df = pd.read_csv("D:\\PYTHON FULL STACK\\LibraryPrograms\\Pandas\\DATAFRAME\\studentmarks.csv")
print(df)
print("*"*80)

#?======================================================================================================
#& get 13 Record by using iloc[]
# print(df.iloc[13])

#?======================================================================================================
#& get 10Record by using iloc[]
# print(df.iloc[10])


#?======================================================================================================
#& Get 3 8 14 Records random record
#todo - Alternative record  
#* it give Complete record 
# print(df.iloc[[3,8,14]])

#?======================================================================================================
#& Get 3 Record name
#* it give  record 
# print(df.iloc[3][0])  #* 103

# print(df.iloc[3,[0]]) 

#?======================================================================================================
#& Get 3 Record name and maths and science
# print(df.iloc[3,[1,5,6]])

#?======================================================================================================
#^======================================================================================================

#! Applying the slicing Operation by using iloc[]

#^======================================================================================================

#& Get 3rd record to 6th  Record
# print(df.iloc[3:7])

#?======================================================================================================
#& Get 3rd record to 6th  Record and Need Name and Social
# print(df.iloc[3:7,[1,7]]) #* row column

#?======================================================================================================

#& Get 3rd record to 6th  Record and Need Name and Social
# print(df.iloc[3:7:2,[1,7]])
# print(df.iloc[3:6:2,[1,7]])

#?======================================================================================================
#& Get all  Record and Need Name and Social
# print(df.iloc[::,[1,7]])

#?======================================================================================================

#& Get all  Record and Need  with column slicing
# print(df.iloc[::,1:7])  #* No need to write into brackets

#?======================================================================================================

#& Get all record with alternate column and Need name english and maths
# print(df.iloc[::,1:7:2]) #* No need to write into brackets

#?======================================================================================================

#! get the Random records from DataFrame
#todo - it give all data to the number
# print(df.iloc[[1,5,6]])

#?======================================================================================================
#& get the Random records from DataFrame with Name, Science and Maths
#todo - it give only Name, Science and Maths
# print(df.iloc[[1,5,6]][[1,6,7]]) #* this Syntax is not in it

#*   OR
#& get the Random records from DataFrame with Name, Science and Maths
# print(df.iloc[[1,5,6],[1,6,7]])

#?======================================================================================================
#todo - give complete table 
# print(df.iloc[::])

# print(df.iloc[::-1])

#?======================================================================================================
#& get all the Records from dataFrame with Name, to Maths
# print(df.iloc[::,[1,2,3,4,5,6,7]])

#?======================================================================================================
#& get all the Records from dataFrame with Name, to Maths with Column Slicing
#todo -  get  Name, to Maths with Column Slicing
# print(df.iloc[::,::])

# print(df.iloc[::,1:7])

#?======================================================================================================
#& get only even the Records from dataFrame with Name, to Maths with Column Slicing
# print(df.iloc[::2,1:7])



#& get all the Records from dataFrame with Name, to Maths with Column Slicing
# print(df.iloc[1::2,1:7])
#?======================================================================================================






















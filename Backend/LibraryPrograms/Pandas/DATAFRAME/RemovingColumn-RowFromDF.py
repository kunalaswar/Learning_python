
import numpy as np,pandas as pd
df = pd.read_csv("D:\\PYTHON FULL STACK\\LibraryPrograms\\Pandas\\DATAFRAME\\studentmarks.csv")
# print(df)
print("*"*80)


#! adding the total column to the DataFrame
df["total"] = df["telugu"]+df["english"]+df["hindi"]+df["maths"]+df["science"]+df["social"]
# print(df)

#! adding the percent column to the DataFrame
df["percent"] = round((df["total"]/600)*100,2)
print(df)
print("*"*100)

#^==================================================================================================

#?===============================================================================================
#& -    Removing the Columns to DataFrame  with Column NAME

#* Syntax = DataFrameobj.drop(columns="ColumnName")
#* Syntax = DataFrameobj.drop(columns=["ColumnName1","ColumnName2","ColumnName-n"])
#* Syntax = DataFrameobj.drop(columns="ColumnName",inplace ="True")
#* Syntax = DataFrameobj.drop(columns=["ColumnName1","ColumnName2","ColumnName-n"],inplace ="True")

#& -    Removing the Columns to DataFrame  with Column NUMBER
#* Syntax = DataFrameobj.drop


#?===============================================================================================

#! remove the Percent Column from DataFrame
# df.drop(columns="percent")
# print(df)

#* put into df inself
# df = df.drop(columns="percent")
# print(df)

#todo - OR
#!remove the Percent Column from DataFrame

# df.drop(columns="percent",inplace=True)
# print(df)


#& Add and Cal percentage of Marks to remove it again
df["percent"] = round((df["total"]/600)*100,2)
print(df)
print("*"*100)




#!remove Multiple Columns from datafarme object
# df.drop(columns=["total","percent"]) #* changes is not done
# print(df)


#* put into df inself

# df = df.drop(columns=["total","percent"])
# print(df)

# df.drop(columns=["total","percent"],inplace=True)
# print(df)





#! adding the total column to the DataFrame
df["total"] = df["telugu"]+df["english"]+df["hindi"]+df["maths"]+df["science"]+df["social"]
# print(df)

#! adding the percent column to the DataFrame
df["percent"] = round((df["total"]/600)*100,2)
print(df)
print("*"*100)


#! Remove the column 'percent' based on Column Number
#todo - Column Number
print(df.columns[9])  #* ----Percent 
print(df.columns[8])  #* ----total 

# df = df.drop(columns=df.columns[9])
# print(df)

#todo - OR
#! Remove the column 'percent' based on Column Numbe
# df.drop(columns=df.columns[9],inplace=True)
# print(df)


#! Remove the multiple column names 'social' and 'total' based on Column Number
# df = df.drop(columns=df.columns[[7,8]])
# print(df)

#todo - OR
# df.drop(columns=df.columns[[7,8]],inplace=True)
# print(df)


#?====================================================================================================
#&  Removing Rows from  DataFrame

#* Syntax = DataFrameObj = drop(labels=index Value , axis=0)
#* Syntax = DataFrameObj = drop(labels=[indexValue1, indexValue2, indexValue3...] axis=0)
#* Syntax = DataFrameObj = drop(labels=index Value , axis=0,inplace=True)
#* Syntax = DataFrameObj = drop(labels=[indexValue1, indexValue2, indexValue3...] axis=0,inplace=True)


#?===================================================================================================

#! remove the Row 10 from dataframe object
# df = df.drop(labels=10,axis=0)  #* 10 number row is removed
# print(df)

#todo - OR
df.drop(labels=[10],axis=0,inplace=True)
print(df)



#!#remove the Row 2 5 and 7 from dataframe object 

# df.drop(labels=[2,5,7],axis=0,inplace=True)
# print(df)


# print("Number of Records=",df.shape[0])

#remove the Rows from 12 to 16from dataframe object
# df.drop(labels=[12,13,14,15,16],axis=0,inplace=True)
# print(df)



#! finding the Dublicate in DataFrame 
#?===============================================================================================
#* DataFrameobj.duplicated() --------gives us boolean array

#?===============================================================================================


import numpy as np,pandas as pd
df = pd.read_csv("D:\\PYTHON FULL STACK\\LibraryPrograms\\Pandas\\DATAFRAME\\studentmarks.csv")
# print(df)
print("*"*80)



#^==================================================================================================

#!#Find Duplicate Entry
# print(df.duplicated()) #--------gives us boolean array

# print(df[df.duplicated()])


#?===============================================================================================
#* Removing the Duplicates Values form DataFrame

#?===============================================================================================
#* syntax = DataFrameobj.drop_duplicates()


#!remove the Duplicated Entry
#todo - but it is not reflected to the df 
# print(df.drop_duplicates())
# print(df)

#! remove the Duplicated Entry and place data without duplicates in same DataFarme
# df = df.drop_duplicates()
# print(df)

#todo - OR
df.drop_duplicates(inplace=True)
print(df)

#! number of record who to find
# print("Number of Record =",df.shape)  #contain row and column
# print("Number of Record =",df.shape[0])
# print("Number of Record =",df.shape[1])



#?===============================================================================================
#* Adding the row/Record the DataFrame

#?===============================================================================================
#* syntax = dataframeobj.loc[len(DataFrameobj)+1] = [val1,val2,.........valn]


df.loc[len(df)+1] = [125,"Mehraj",55,90,95,92,89,78]  #* put the proper column other we get an error 

print(df)

print("Number of Record /Rows =",df.shape[0])



#?===============================================================================================
#* Sorting the Data of DataFrame

#?===============================================================================================
#* syntax = dataframeobj.sort_values(["colname"])
#* syntax = dataframeobj.sort_values(["colname"],ascending = False)
#* syntax = dataframeobj.sort_values(["colname"]ascending = True)
#* syntax = dataframeobj.sort_values(["colname"],inplace =True)
#* syntax = dataframeobj.sort_values(["colname"]ascending = True,inplace =True)

# print(df.sort_values(["maths"]))

# print(df.sort_values(["name"]))


#!reverse Order / Decending order
# print(df.sort_values(["name"])[::-1])

#todo - 
print(df.sort_values(["name"],ascending=False))

df.sort_values(["name"],ascending=False,inplace=True)
print(df)






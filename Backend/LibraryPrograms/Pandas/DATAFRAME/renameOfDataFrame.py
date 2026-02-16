
# import pandas as pd
# #Creating the DataFrame
# df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6],"C": [7,8,9]})
# print("-------The DataFrame is-------")
# print(df)
# print("----------------------------------")

#^=====================================================================================================
#! Change / Rename the Column name  with a,b,c
# print(df.rename(columns={"A":"a","B":"b","C":"c"}))

#todo -OR

# print(df.rename(columns={"A":"Col-1","B":"Col-2","C":"Col-3"}))
#^=====================================================================================================
# import pandas as pd
# #Creating the DataFrame 
# df = pd.DataFrame({"A":[1,2,3],"B":[4,5,6],"C":[7,8,9]})
# print("-------The DataFrame is-------")
# print(df)
# print("----------------------------------")


#! Changing OR Renaming Indices (Row Indexes)
# print(df.rename(index={0:"index_1",1:"index_2",2:"index_3"}))




import pandas as pd
#Creating the DataFrame 
df = pd.DataFrame({"A":[1,2,3],"B":[4,5,6],"C":[7,8,9]})
print("-------The DataFrame is-------")
print(df)
print("----------------------------------")

#! both the Column Name and index name rename
print(df.rename(index={0:"index_1",1:"index_2",2:"index_3"},
          columns={"A":"Col-1","B":"Col-2","C":"Col-3"}))
        


#! to access the 1 from DataFrame

print(df.values[0][0:1][0])

import numpy as np,pandas as pd
df = pd.read_csv("D:\\PYTHON FULL STACK\\LibraryPrograms\\Pandas\\DATAFRAME\\studentmarks.csv")
print(df)
print("*"*80)

#?=======================================================================================================
#&  Adding the New column(s) to the DataFrame
#?=======================================================================================================

# df["total"]=0 
# print(df)


#! add the new column total
# dobj= df["total"] = 0
# print(dobj)

#! add the new column total
#* Syntax = DataFrameObj["NewColname"] = Default Value
# dobj= df["total"] = 0
# dobj= df["total"] = None


#^=======================================================================================================
#* Syntax = DataFrameObj["NewColname"] = Expression Here 

#! add the all students dataFrame record 
#* dataFrame object are vector based operation

df["total"]=df["telugu"]+df["english"]+df["hindi"]+df["maths"]+df["science"]+df["social"]
print(df)

#^=======================================================================================================

#! Add and Column percentage of Marks with out round()
# df["percent"] = (df["total"]/600)*100
# print(df)

#^=======================================================================================================
#! Add and Column percentage of Marks 
#* round the percentage with python round()
df["percent"] = round((df["total"]/600)*100,2)
print(df)

#! Find maximun  percentage
# print("Maximun percentage = ",df["percent"].max())



#^=======================================================================================================











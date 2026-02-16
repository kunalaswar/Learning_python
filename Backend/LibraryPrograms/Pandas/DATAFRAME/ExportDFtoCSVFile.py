
#?=================================================================================================

#& Exporting the DataFrame Data CSV file
#?=================================================================================================
#* Syntax DataFrame.to_csv("ABS Path")

import numpy as np,pandas as pd
df = pd.read_csv("D:\\PYTHON FULL STACK\\LibraryPrograms\\Pandas\\DATAFRAME\\studentmarks.csv")
print(df)
print("*"*80)

#!Add and total of Marks
df["total"]=df["telugu"]+df["english"]+df["hindi"]+df["maths"]+df["science"]+df["social"]
print(df)

#!Add and Cal percentage of Marks
df["percent"]=round(df["total"]/600*100,2)
print(df)


#Give the Grade to Students with Following Conditions
#Distinction Grade----->Percentage >=74
#First Grade----------> 74>Percentage>=65
#Second Grade--------->65>percentage>=60
#Third Grade--------->60>percentage

#!Add Grade Column to data frame
df["grade"]=None
print(df)


df.loc[(df["percent"]>74),["grade"]]="DISTINCTION"
# print(df)

df.loc[((df["percent"]>=65)&(df["percent"]<74)),["grade"]]="FIRST"
# print(df)

df.loc[((df["percent"]>=60)&(df["percent"]<65)),["grade"]]="SECOND"
print(df)


df.loc[(df["percent"]<60),["grade"]] = "THIRD"
print(df)


#! Export DataFrame Object to the CSF File on the Name of StudentFinalResult.csv
df.to_csv("D:\\PYTHON FULL STACK\\LibraryPrograms\\Pandas\\DATAFRAME\\EXPORT.csv")
print("DataFrame Data exported to CSV File-verify")


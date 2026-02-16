

import numpy as np,pandas as pd
df = pd.read_csv("D:\\PYTHON FULL STACK\\LibraryPrograms\\Pandas\\DATAFRAME\\studentmarks.csv")
# print(df)
print("*"*80)

#?====================================================================================================
#&  Filtering  to the DataFrame by using Condition
#todo -   OR
#& Quering the Data to the DataFrame by using Condition
#?====================================================================================================

#*------------------------------------------------------------------
#todo- Data Filtering from DataFrame by using Conditions  
#todo -  OR  
#todo- Querying the Data from DataFrame by using Conditions  
#*------------------------------------------------------------------

#* Syntax1: DataFrameObj.loc[Simple Test Cond]  
#* Syntax2: DataFrameObj.loc[Compund Test Cond]  
#* Syntax3: DataFrameObj.loc[Simple Test Cond, ["Colname1","colname2"...]]  
#* Syntax4: DataFrameObj.loc[Compund Test Cond, ["Colname1","colname2"...]] 
#  
#* Syntax5: DataFrameObj[ DataFrameObj[SingleTest Cond] ] ["ColName1"]  
#* Syntax6: DataFrameObj[ DataFrameObj[SingleTest Cond] ] [["ColName1","ColName-2"...]]  
#* Syntax7: DataFrameObj[ DataFrameObj[Compound Test Cond] ] ["ColName1"]  
#* Syntax8: DataFrameObj[ DataFrameObj[Compund Test Cond] ] [["ColName1","ColName-2"...]]  

 



#! adding the total column to the DataFrame
df["total"] = df["telugu"]+df["english"]+df["hindi"]+df["maths"]+df["science"]+df["social"]
# print(df)

#! adding the percent column to the DataFrame
df["percent"] = round((df["total"]/600)*100,2)
print(df)
print("*"*100)

#^==================================================================================================

#* syntax = DataFrameObj.loc[Simple Test condition]
#* syntax = DataFrameObj.loc[Compound Test condition]


#! get name of the students whose maths marks is >=90
# print(df["maths"]>=90) #* this gives boolean array

# print(df[df["maths"]>=90]) #*gives all the row and Column in the df

#* pass the boolean array to the df
# print(df[df["maths"]>=90]["name"])

#todo -  OR one more way
# print(df.loc[["maths"]]>=90)

# print(df.loc[::1,["maths"]]>=90)

#* syntax = DataFrameObj.loc[Simple Test condition ],["colname1","colname2",....]]

# print(df[df["maths"]>=90] [["name","maths"]])
# #todo - OR
# print(df.loc[df["maths"]>=90,["name","maths"]])


# x = df.loc[((df["maths"]>=80) & (df["maths"]<=90)),["name","maths"] ]
# print(x)


#^=======================================================================================================

#* syntax = DataFrameObj.loc[Simple Test condition,["colname1","colname2",....]]
#* syntax = DataFrameObj.loc[Compound Test condition][["colname1","colname2",....]]

#! get name of the students whose maths marks is >=90 we want name and maths marks

# print(df["maths"]>=90,["name","maths"]) #* this Gives Boolean array pass the Boolean array to the df



# print(df.loc[df["maths"]>=90,["name","maths"]])



#^=======================================================================================================

#* syntax = DataFrameObj.loc[Compound Test condition]

#! Get Name of the students Whose maths Marks is more than 80 and 90

#todo - we Never used the and or not operator
# print(((df["maths"]>=80) and (df["maths"]<=90)) ,["name","maths"])

#todo - we always use Bitwise & | ~ 
# print(((df["maths"]>=80) & (df["maths"]<=90)) ,["name","maths"])  #* Pass the boolean array to the df 

# print(df[((df["maths"]>=80) & (df["maths"]<=90))])

# print(df[((df["maths"]>=80) & (df["maths"]<=90))] ["name"])

# print(df[((df["maths"]>=80) & (df["maths"]<=90)) ,["name","maths"]])  #! Not like this it give an error


#^=======================================================================================================

#* syntax = DataFrameObj.loc[Compound Test condition,[["colname1","colname2"]]]
print("------------------------------------------------")
#todo - Without  loc doing
# print(df[((df["maths"]>=80) & (df["maths"]<=90))] [["name","maths"]])

#todo - With loc doing
# print(df.loc[((df["maths"]>=80) & (df["maths"]<=90)),["name","maths"]])


#! Get the Names and Total Marks whose Total marks ranges bewteen 410 to 430

# print(((df["total"]>=410) & (df["total"]<=430)),[["name","total"]])

# print(df[((df["total"]>=410) & (df["total"]<=430))]) #* It will give you complete information 

#* we want only the Name and marks

# print(df[((df["total"]>=410) & (df["total"]<=430))] [["name","total"]])

#?=========================================================================
# print(df[((df["total"]>=410) & (df["total"]<=430))])
# print()
# print("SIZE =",df[((df["total"]>=410) & (df["total"]<=430))].size)
#?=========================================================================

# print(df[((df["total"]>=410 )& (df["total"]<=430))][["name","total"]].size)


# print(df[((df["total"]>=410 )& (df["total"]<=430))][["name","total"]].shape[0])


#todo - Do this with the loc[] 

# print(df.loc[((df["total"]>=410) & (df["total"]<=430),["name","total"])])























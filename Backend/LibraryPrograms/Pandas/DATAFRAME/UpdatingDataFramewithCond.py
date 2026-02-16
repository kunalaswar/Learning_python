
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

#?====================================================================================================
#&   Conditional Updations in DataFrame
#todo -   OR

#?===================================================================================================

#* Give the Grade to Students with Following Conditions
#* Distinction Grade----->Percentage >=74   ------single condition
#* First Grade----------> 74>Percentage>=65 ------compound condition
#* Second Grade--------->65>percentage>=60  ------compound condition
#* Third Grade--------->60>percentage       ------Single condition

#! Add Grade Column to data frame
df["grade"] = None
# print(df)

# print(df[df["percent"]>74])
#todo - OR

# print(df.loc[df["percent"]>=74])


#* Distinction Grade----->Percentage >=74   ------single condition

# df.loc[df["percent"]>=74,["grade"]]="DISTINCTION"
# print(df)



#* First Grade----------> 74>Percentage>=65 ------compound condition

#todo - firstly access the element and then assign the Value
# print(df.loc[((df["percent"]>=65) & (df["percent"]<74))])


# df.loc[((df["percent"]>=65) & (df["percent"]<74)),["grade"]]="FIRST"
# print(df)


#^----------------------------------------------------------------------
# print("apple" and "mango")

# print("apple" & "mango")  #* TypeError: unsupported operand type(s) for &: 'str' and 'str'

# print(1.2 and 2.3)

# print(1.2 & 2.3)

#& Bitwise operator are used only on the integer

# print(2 and 3)

# print(2 & 3)

#^----------------------------------------------------------------------

#* Second Grade--------->65>percentage>=60  ------compound condition

# print(((df["percent"]>=60) & (df["percent"]<65)))


# print(df[((df["percent"]>=60) & (df["percent"]<65))])

#todo -  OR

# print(df.loc[((df["percent"]>=60) & (df["percent"]<65))])

# df.loc[((df["percent"]>=60) & (df["percent"]<65)),["grade"]]="SECOND"
# print(df)


#* Third Grade ---------> 60>percentage    ------Single condition

# df.loc[(df["percent"]<60),["grade"]]="THIRD"
# print(df)


#^==================================================================================================
#! count number of students who got Distinction
# df[df["grade"]=="Distinction".upper()].shape[0]
# print(df)


#^==================================================================================================
#find the name of the students  who got Higgest percentage
# print(df["percent"].max())

# print(df["percent"].max())

# print(df["percent"].max(),["name"])

#^==================================================================================================


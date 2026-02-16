
#?====================================================================================================
#&   Working with Missing Value 

#?===================================================================================================

# #todo ----------------Finding with Missing Value 
# import numpy as np
# import pandas as pd
# d={'First Score':[100,90,np.nan,95],
#    "Second Score":[30,45,56,np.nan],
#    "Third Score":[np.nan,40,80,90]}

# # print(d,type(d))

# #convert the dict data into dataFrame
# df = pd.DataFrame(d)
# print("------------------------------------------------")
# print(df)
# print("------------------------------------------------")

#?===================================================================================================

#!#To find Missing Values we use  isna(), isnull()
# print(df.isna())

# print(df.isna().sum())

#!#To find Missing Values we use  isna(), isnull()
# print(df.isnull())

# print(df.isnull().sum())

#?===================================================================================================
#todo - We can apply with  a single column
# print(df["First Score"].isna())

# print(df["First Score"].isna().sum())

#?===================================================================================================
#todo - We can apply with a single Row

# print(df.loc[0].isna())
# print(df.loc[1].isna())    

# print(  df.loc[1].isna().sum())  #* 0


# print(df.iloc[1].isna().sum())  #* 0

# print(df.iloc[1].isnull().sum()) #* 0


#?===================================================================================================
#! Find Non-Missing Values by using notna() and notnull()
# print(df.notna()) #* it is Oposite to the isna() and isnull()

# print(df.notna().sum())  #todo - it By Defalut came column-wise 
#   O/P:
# First Score     3
# Second Score    3
# Third Score     3

#& in first row how many notna is there 
# print(df.loc[0].notna())  #todo - We can done with the row-wise

# print(df.notnull())
# print(df.notnull().sum())


# todo --------------------------Replaceing with Missing Value ----------------------------

#! Fill 0 value for NaN in entire DataFrame Object
# print(df.fillna(0))


#! Fill 0 value for NaN in entire DataFrame Object
# df = df.fillna(0)
# print(df)
#*OR
# df.fillna(0,inplace=True)
# print(df)


#?===================================================================================================
# import numpy as np
# import pandas as pd
# d={'First Score':[100,90,np.nan,95],
#    "Second Score":[30,45,56,np.nan],
#    "Third Score":[np.nan,40,80,90]}
# #convert the dict data into dataFrame
# df = pd.DataFrame(d)
# print("------------------------------------------------")
# print(df)
# print("------------------------------------------------")

#?===================================================================================================

#! Fill 0 value for NaN in entire DataFrame Object
# df = df.replace(to_replace=np.nan,value=0)
# print(df)

#* OR
# print(df.replace(to_replace=np.nan,value=0))

# df.replace(to_replace=np.nan,value=0,inplace=True)
#?===================================================================================================
#& Replace the fill data with another fill data
# df.replace(to_replace=0.0 ,value=11.11,inplace=True)
# print(df)
#?===================================================================================================

#?===================================================================================================
import numpy as np
import pandas as pd
d={'First Score':[100,90,np.nan,95],
   "Second Score":[30,45,56,np.nan],
   "Third Score":[np.nan,40,80,90]}
#convert the dict data into dataFrame
df = pd.DataFrame(d)
print("------------------------------------------------")
print(df)
print("------------------------------------------------")

#?===================================================================================================

#! replace NAN Value of 'First Score'   
#todo - filling the column with data
# print(df["First Score"].fillna(0.0))

#* OR
# df["First Score"].fillna(0.0,inplace=True)
# print(df)


#! replace Nan Values of 'Second Score'
# df["Second Score"].replace(to_replace=np.nan,value=0.1,inplace=True)
# print(df)


#replace Nan Values of 'Third Score'
# df["Third Score"].replace(to_replace=np.nan,value=1.1,inplace=True)


# #?===================================================================================================
# import numpy as np
# import pandas as pd
# d={'First Score':[100,90,np.nan,95],
#    "Second Score":[30,45,56,np.nan],
#    "Third Score":[np.nan,40,80,90]}
# #convert the dict data into dataFrame
# df = pd.DataFrame(d)
# print("------------------------------------------------")
# print(df)
# print("------------------------------------------------")
# #?===================================================================================================

#!replace Nan Values of Second Score and Third Score
#todo - replacing with multiple data 
# print(df[["Second Score", "Third Score"]].fillna(11.11))


#! replace Nan Values of Second Score and Third Score
# df[["Second Score", "Third Score"]].fillna(11.11,inplace=True)  #*FetureWarning
# print(df)

#*   OR
# df[["Second Score","Third Score"]] = df[["Second Score","Third Score"]].fillna(11.11)
# print(df)


#?===================================================================================================
import numpy as np
import pandas as pd
d={'First Score':[100,90,np.nan,95],
   "Second Score":[30,45,56,np.nan],
   "Third Score":[np.nan,40,80,90]}
#convert the dict data into dataFrame
df = pd.DataFrame(d)
print("------------------------------------------------")
print(df)
print("------------------------------------------------")
#?===================================================================================================

#! Filling Row based Missing Values
#todo -   Row wise filling
# print(df.loc[0].fillna(0))

#! Filling Row based Missing Values
# df.loc[0] = df.loc[0].fillna(0)

#?===================================================================================================
#! Accessing the multiple value and Next
#todo  --- Retrive the Row
# df.loc[[2,3]].fillna(11.11,inplace=True)
# print(df)

# df.loc[[2,3]]=df.loc[[2,3]].fillna(11.11)
# print(df)

#?===================================================================================================

# #df.iloc[0:3] = df.iloc[0:3].replace(to_replace=np.nan,value=11.11)     
# df.iloc[0:4] = df.iloc[0:4].replace(to_replace=np.nan,value=11.11)     
# print(df)

#?===================================================================================================
#TODO -     -------------------EXERCISE-------------------------------

#Consider the Following Problem
# d={"Courses":["SPARK","JAVA","SCALA","PYTHON"],
#               "Fees":[20000,np.nan,26000,28000],
#                "Duration":["30days","40days",pd.NA,"40days"],
#                "Discount":[1000,np.nan,2500,None]}
# df=pd.DataFrame(d)
# print("--------------------------------------------------------")
# print(df)
# print("--------------------------------------------------------")
             
#! Provide OR Give Discount Rs:500 for Python Course
#todo -ROW kind of filling the value
# df.loc[3] = df.loc[3].fillna(500)
# print(df)


#?===================================================================================================
#todo -Column kind of filling the value
# print(df["Duration"])
# df["Duration"]=df["Duration"].replace(to_replace=np.nan,value=50)
# print(df)

print(type(np.nan),type(pd.NA))
#*  <class 'float'> <class 'pandas._libs.missing.NAType'>

#?===================================================================================================
#Consider the Following Problem
d={"Courses":["SPARK","JAVA","SCALA","PYTHON"],
              "Fees":[20000,np.nan,26000,28000],
               "Duration":["30days","40days",pd.NA,"40days"],
               "Discount":[1000,np.nan,2500,None]}
df=pd.DataFrame(d)
print("--------------------------------------------------------")
print(df)
print("--------------------------------------------------------")
#?===================================================================================================

#! ROW -wise updation

# df.loc[1,"Fees"]=15000
# # print(df)


# #!
# df.loc[1,"Discount"]=1000
# # print(df)

#?===================================================================================================
# #! Column -Wise
# df["Duration"] = df["Duration"].fillna(35)
# print(df)

# df["Discount"]=df["Discount"].fillna(500)
# print(df)
#?===================================================================================================

#Consider the Following Problem
d={"Courses":["SPARK","JAVA","SCALA","PYTHON"],
              "Fees":[20000,np.nan,26000,28000],
               "Duration":["30days","40days",pd.NA,"40days"],
               "Discount":[1000,np.nan,2500,None]}
df=pd.DataFrame(d)
print("--------------------------------------------------------")
print(df)
print("--------------------------------------------------------")

#*         ERROR in this 
# df.loc[["Fees","Discount"]]=[15000,1000]
# print(df)





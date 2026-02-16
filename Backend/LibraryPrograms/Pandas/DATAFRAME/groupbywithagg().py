
#?====================================================================================================


#?====================================================================================================
import numpy as np 
import pandas as pd
df = pd.read_csv("D:\\PYTHON FULL STACK\\LibraryPrograms\\Pandas\\DATAFRAME\\population.csv")
print(df)
# print("type of df ",type(df))

#^====================================================================================================
# ppgb = df.groupby("City")
# print("type of ppgb =",type(ppgb))

# for grpname,grpdata in ppgb:
#     print("Group Name:",grpname)
#     print(grpdata)
#     print("-----------------------------")

#^====================================================================================================

# for grpname,grpdata in df.groupby("City"):
#     print("Group Name :",grpname)
#     print(grpdata)
#     print('-------------------------')

#^====================================================================================================

# print(df.groupby("City").size())

#! how to find the numbeer of group
# print(df.groupby("City").ngroups)  # 3
#^====================================================================================================

# print(df.groupby("City").get_group("Mumbai").groupby("Age"))
# for grpname,grpdata in df.groupby("City").get_group("Mumbai").groupby("Age"):
#     print("Group Name :",grpname)
#     print(grpdata)
#     print("------------------------")

#^====================================================================================================

k = len(df.groupby("City").get_group("Delhi"))
print(k)   # 4

#todo - Here Experience is not meaning in this place 
# values = df.groupby("City").agg({"Age":"mean","Experience":"sum"})
# print(values)

# values = df.groupby("City").agg({"Age":"mean","Experience":"mean"})
# print(values)

values =df.groupby("City")["Age"].agg(['size','sum','mean'])
print(values)






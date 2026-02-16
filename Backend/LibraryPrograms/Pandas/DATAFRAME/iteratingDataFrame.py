
#?===================================================================================================
#! WithOut giving the Name indices
# import numpy as  np 
# import pandas as pd
# lst = [[10,20,30,40,50],["RS","TR","SS","DR","JH"],[1.2,2.3,4.5,5.6,6.7]]
# df = pd.DataFrame(lst)
# print(df)
#?===================================================================================================


#todo - type of the row is tuple NOT a series 
#* type of the column is series 
# for val in df.iterrows():
#     print("\n",val)

#^===================================================================================================
#!1. Iterating the DataFrame Object Data by using Row Indices
#* it provide the two things row index and row values

# for rec in df.iterrows():
#     print("Row Index ",rec[0])
#    # print("\tRecord value ",type(rec[1]))
#     print("\tRecord value ",rec[1])

#^===================================================================================================
#!1. Iterating the DataFrame Object Data by using Row Indices
# for rec in df.iterrows():
#     print("Row Index",rec[0])
#     print("\tRecord value ",rec[1].values)

#^===================================================================================================

#*  iterrows return 2 values

# for rind,rvals in df.iterrows():
#     print("Row Index ",rind)
#     print("\t Record value",rvals.values)

#^===================================================================================================
#!1. Iterating the DataFrame Object Data by using Row Indices
#& with the help of iloc[] 
#*syntax = DataFrameobj .iloc[row index]
# for i in range(df.shape[0]):
#     print("Row Index Value =",i)
#     print("\t Row values =",df.iloc[i].values)

#^===================================================================================================
#!1. Iterating the DataFrame Object Data by using Row Indices
#& with the help of loc[]
#*syntax = DataFrameobj .loc[row index]
# for i in range(df.shape[0]):
#     print("Row Index Value =",i)
#     print("\t Row values =",df.loc[i].values)
#^===================================================================================================

#?===================================================================================================
#! With giving the Name indices
# import numpy as np
# import pandas as pd
# lst=[[10,20,30,40,50],["RS","TR","SS","DR","JH"],[1.2,2.3,4.5,5.6,6.7]]
# df=pd.DataFrame(lst,index=["ID","NAME","CGPA"])
# print(df)
# print("*"*60)

#?===================================================================================================
# print(df.shape)
# print(df.shape[0])
 
# #! 2.Iterating the DataFrame Object Data by using Row Names
# for i in range(df.shape[0]):
#     print(df[i],df[i].values)
#     print(type(df[i]))

#^===================================================================================================

# for rec in df.iterrows():
#     print("Row name",rec[0])
#     print("\t Record Value",rec[1].values)

#^===================================================================================================
#*  iterrows return 2 values
# for rowname,rowvals in df.iterrows():
#     print("Row Index name ",rowname)
#     print("\tRow values",rowvals.values)

#^===================================================================================================
#?===================================================================================================
# import numpy as np
# import pandas as pd
# lst=[[10,20,30,40,50],["RS","TR","SS","DR","JH"],[1.2,2.3,4.5,5.6,6.7]]
# df=pd.DataFrame(lst,columns=["Rec1","Rec2","Rec3","Rec4","Rec5"])
# print(df)
#?===================================================================================================
#^===================================================================================================
#! 3.Iterating the DataFrame Object Data by using  Col Names

#* column attribute gives us values
# for colname in df.columns:
#     print("column name : ",colname)
#     print("\t\tColumn values:",df[colname].values )
#     # print("\t\tColumn values:",type(df[colname].values ))


#?===================================================================================================
import numpy as np,pandas as pd
lst=[[10,20,30,40,50],["RS","TR","SS","DR","JH"],[1.2,2.3,4.5,5.6,6.7]]
df=pd.DataFrame(lst)
print(df)
print("*"* 60)
#?===================================================================================================
#^===================================================================================================
#! 4.Iterating the DataFrame Object Data by using Column  Indices

# for colindex in range(df.shape[1]):
#     print(colindex)

# for colindex in range(df.shape[1]):
#     print("column Index :",colindex)
#     # print("\tcolumn Data ",df.iloc[:,[colindex]].values)
#     print("\tcolumn Data ",df.iloc[:,colindex].values)


# print(df.shape[1])


#?==================================================================================================
import numpy as np
import pandas as pd
df = pd.read_csv("D:\\PYTHON FULL STACK\\LibraryPrograms\\Pandas\\DATAFRAME\\peoples.csv")
print("---------------------------------")
print(df)
print("---------------------------------")

#?==================================================================================================
#^==================================================================================================

#!Get State-wise Data from DataFrame--apply groupby()
# sg = df.groupby("STATE")
# print(sg)   #*<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000019998046C60>
# print(type(sg))  #*<class 'pandas.core.groupby.generic.DataFrameGroupBy'>


#!Get State-wise Data from DataFrame--- apply groupby()
# sg = df.groupby("STATE")
# # print(sg)
# print("------------------------")
# for groupname,groupdata in sg:
#     print("Group Name",groupname)
#     print(groupdata)
#     print("----------------------------")

#^==================================================================================================

# print("Number of groups =",sg.ngroups)    #* Number of groups = 3

# print("Number of Groups=",len(sg))        #* Number of groups = 3

#^==================================================================================================

#! Get State-wise Data from DataFrame--apply groupby()
# sg = df.groupby("STATE")
# print("-------------------------")
# for groupname ,groupdata in df.groupby("STATE"):
#     print("Group Name",groupname)
#     print(groupdata)
#     print("------------------------------------")
#^==================================================================================================


#! Get State-wise Data from DataFrame--apply groupby()
#sg=df.groupby("STATE")
# print("-------------------------------------")
# for groupname ,groupdata in df.groupby("DSG"):
#     print("Group Name",groupname)
#     print(groupdata)
#     print("--------------------------------")

#^==================================================================================================

#! Get State-wise Data from DataFrame--apply groupby()
sg = df.groupby("STATE")
print("----------------------------------------")
for groupname,groupdata in sg:
    print("Group Name",groupname)
    print(groupdata )
    print("---------------------------------")

#^==================================================================================================

#! Find Number of People in each group
# print(sg.count())

#! Find Number of People in each group
# print(sg.size)


#^==================================================================================================
#! Get the First Record in Each Group---first()
# print(sg.first())


#! Get the last Record in Each Group---last()
# print(sg.last())

#! Get the 3rd Record in Each Group---nth(3)
# print(sg.nth(3))

# print(sg.nth([1,2,3]))

#^==================================================================================================
#! groupby "AP"
# sg.get_group("AP")

#! groupby "BANG"
# sg.get_group("BANG")

#! groupby "TS"
# sg.get_group("TS")

#^==================================================================================================
# apg=sg.get_group("AP")
# print(type(apg))    #* <class 'pandas.core.frame.DataFrame'>

#^==================================================================================================
#! in AP STATE there also get a group with DSG
# apsbg=sg.get_group("AP").groupby("DSG")
# # print(apsbg)    #*<pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001A761B221B0>

# print("----------------------------------")
# for groupname,groupdata in apsbg:
#     print(" Group Name ",groupname)
#     print(groupdata)
#     print("--------------------------")
#^==================================================================================================

# for groupname,groupdata in df.groupby("STATE").get_group("AP").groupby("DSG"):
#     print("Group Name",groupname)
#     print(groupdata)
#     print("------------------------------------")

#^==================================================================================================

# for groupname,groupdata in df.groupby("STATE").get_group("TS").groupby("DSG"):
#     print("Group Name :",groupname)
#     print(groupdata)
#     print("-------------------------------------")

#^==================================================================================================
















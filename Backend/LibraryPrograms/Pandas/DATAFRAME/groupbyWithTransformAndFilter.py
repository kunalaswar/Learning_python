
#?=====================================================================================================




#?=====================================================================================================
#^=====================================================================================================
# import numpy as np
# import pandas as pd
# # Create DataFrame
# df = pd.DataFrame({'team':['A','A','A','A','B','B','B','B'],
#                    "points":[30,22,19,14,14,11,20,28]})
# # View DataFrame
# print(df)
#^=====================================================================================================

# tgp = df.groupby("team")
# for grpname,grpdata in tgp:
#     print("Group Name :",grpname)
#     print(grpdata)
#     print("-----------------------------")
#^=====================================================================================================
#todo - Method -1
#* using groupby() and transform() with built-in function 
#* Syntax = df["new"] = df.groupby("group_var")["value_var"].transform('mean')

#! Calculate the Mean Points of each Time
#todo - transform give a single value to group wise data
# df["Mean-Points"]=df.groupby("team")["points"].transform("mean")
# print(df)

# df["sum-Points"]=df.groupby("team")["points"].transform("sum")
# print(df)

#^=====================================================================================================

#todo - Method -2
#* Syntax = df["new"] = df.groupby("group_var")["value_var"].transform(lambda x:some function)

#! create new column called percent_of_points
# df["percent_of_points"]=df.groupby("team")["points"].transform(lambda x:x/x.sum())
# print(df)


#!create new column called percent_of_points
#todo - percent form it will come
# df["percent_of_points"]=df.groupby("team")["points"].transform(lambda x:(x/x.sum())*100)
# print(df)

#^=====================================================================================================

#* suppose we dont no DataFrame what will do 
# print(df.groupby("team")["points"].agg(["sum"]))

#! appling two function
# print(df.groupby("team")["points"].agg(["sum","mean"]))

#^=====================================================================================================


#* But what if you want to group by more than one column ?
#* That's where multiple column grouping comes in
# import pandas as pd

# df = pd.DataFrame({'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot'], 
#                    'Max Speed': [380., 370., 24., 26.], 
# 				'Type': ['Bird', 'Bird', 'Bird', 'Bird']})
# print(df)
#! get group more than one column
# print(df.groupby(['Animal', 'Type']).mean())

#^=====================================================================================================

#! Apply multiple Pre-defined function
# import pandas as pd
# df = pd.DataFrame({"Animal":["Falcon","Falcon","parrot","Parrot"],
#                    "Max Speed":[380.,370.,24.,26. ],
#                    "Type":["Bird","Bird","Bird","Bird"]})
# print(df)                   

# print(df.groupby(["Animal","Type"]).agg(["mean","max","min"]))
#^=====================================================================================================
#* Syntax-1 = DataFrameObj.groupby("CommonColValue").filter(lambda function)
#* Syntax-2 = DataFrameObj.groupby(["CommonColValue-1",CommonColvalue-2]).filter(lambda function)
#!Filtering  Group
import pandas as pd
df = pd.DataFrame({"Animal":["Falcon","Falcon","parrot","Parrot"],
                   "Max Speed":[380.,370.,24.,26. ],
                   "Type":["Bird","Bird","Bird","Bird"]})
# print(df)                   
print(df.groupby(["Animal"]).filter(lambda x:x["Max Speed"].mean()>100))

#^=====================================================================================================

#!Filtering  Group
import pandas as pd
df = pd.DataFrame({"Animal":["Falcon","Falcon","parrot","Parrot"],
                   "Max Speed":[380.,370.,24.,26. ],
                   "Type":["Bird","Bird","Bird","Bird"]})
# print(df)
print(df.groupby(["Animal"]).filter(lambda x:x["Max Speed"].mean()<100))









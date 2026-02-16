
#! Attributes of DataFrame
#^====================================================================================================
# import pandas as pd
# d = {"students":["Arvind","Aryan","Rossum","Travis"],
#      "Marks":[85,92,78,83],
#       "sport":["Cricket","Vollyboll","Hockey","Shuttle"]}
# df = pd.DataFrame(d)      
# print("------------------------------------------")
# print(df)
# print("------------------------------------------")

#^====================================================================================================

#! Attribute Name :dataframeobj.index 
# import pandas as pd
# d = {"students":["Arvind","Aryan","Rossum","Travis"],
#      "Marks":[85,92,78,83],
#       "sport":["Cricket","Vollyboll","Hockey","Shuttle"]}

# df = pd.DataFrame(d)
# print(df)
# print(df.index)  #*RangeIndex(start=0, stop=4, step=1)

# #* We have to use for loop to Access the value
# for val in df.index:
#     print(val)

#^====================================================================================================
#! Attribute Name : dataframeobj :columns

# import pandas as pd
# d = {"students":["Arvind","Aryan","Rossum","Travis"],
#      "Marks":[85,92,78,83],
#       "sport":["Cricket","Vollyboll","Hockey","Shuttle"]}

# df = pd.DataFrame(d)
# print("------------------")
# print(df)
# print("------------------")
# #todo - Attribute Name :  dataframeobj.columns
# print(df.columns)  #* Index(['students', 'Marks', 'sport'], dtype='object')
# for val in df.columns:
#     print(val)

#^====================================================================================================
#! Attribute Name :  dataframeobj.dtypes
#* it Gives datatype of the each Column /Series 
# import pandas as pd
# d = {"students":["Arvind","Aryan","Rossum","Travis"],
#      "Marks":[85,92,78,83],
#       "sport":["Cricket","Vollyboll","Hockey","Shuttle"]}

# df = pd.DataFrame(d)
# print(df)
# print(type(df))

# #todo -#Attribute Name :  dataframeobj.dtypes
# print(df.dtypes)

#^====================================================================================================
#! Attribute Name :  dataframeobj.axes
# import pandas as pd
# d = {"students":["Arvind","Aryan","Rossum","Travis"],
#      "Marks":[85,92,78,83],
#       "sport":["Cricket","Vollyboll","Hockey","Shuttle"]}

# df = pd.DataFrame(d) 
# print(df )
# print(df.axes)  #*[RangeIndex(start=0, stop=4, step=1), Index(['students', 'Marks', 'sport'], dtype='object')] It Gives Value in the form of list 
# for val in df.axes:
#     print(val)

# print("----------------------------------")
# #todo - it contain always row 
# for i in df.axes[0]:
#     print(i)

# #todo - it contain always column
# for j in df.axes[1]:
#     print(j)

#^====================================================================================================
#! Attribute Name :  dataframeobj.size
# import pandas as pd
# d = {"students":["Arvind","Aryan","Rossum","Travis"],
#      "Marks":[85,92,78,83],
#       "sport":["Cricket","Vollyboll","Hockey","Shuttle"]}
# df = pd.DataFrame(d)
# print(df)

#todo - Attribute Name :  dataframeobj.size
# print(df.size)

#^====================================================================================================
#! Attribute Name :  dataframeobj.shape
# print("shape of DataFrame =",df.shape)
# print("Number of rows",df.shape[0])
# print("Number of Column",df.shape[1])

#^====================================================================================================
#! Attribute Name :  dataframeobj.ndim
# print("Dimension of DataFrame =",df.ndim)

#^====================================================================================================
#* Create a empty DataFrame
# import pandas as pd
# df1 = pd.DataFrame()
# print(df1)

# #! Attribute Name :  dataframeobj.empty
# # print("Is df is empty =",df.empty)
# print("Is df1 is empty =",df1.empty)


#^====================================================================================================
#! Attribute Name :  dataframeobj.values
# import pandas as pd
# d = {"students":["Arvind","Aryan","Rossum","Travis"],
#      "Marks":[85,92,78,83],
#       "sport":["Cricket","Vollyboll","Hockey","Shuttle"]}
# df = pd.DataFrame(d)
# print(df)

#todo - Attribute Name :  dataframeobj.values
# print(df.values) 
# print(type(df.values))   #*<class 'numpy.ndarray'>

# for record in df.values:
#     print(record)

# for record in df.values:
#     for value in record:
#         print(f"\t{value}",end="\t")
#     print()    

#^====================================================================================================
#! Attribute Name :  dataframeobj.T
# import pandas as pd
# d = {"students":["Arvind","Aryan","Rossum","Travis"],
#      "Marks":[85,92,78,83],
#       "sport":["Cricket","Vollyboll","Hockey","Shuttle"]}
# df = pd.DataFrame(d)
# print(df)
# print("--------------------------------------------------------------")
# print(df.transpose()) #* row index is goto the column and column index goto row
# # print(df.T)  #* row index is goto the column and column index goto row









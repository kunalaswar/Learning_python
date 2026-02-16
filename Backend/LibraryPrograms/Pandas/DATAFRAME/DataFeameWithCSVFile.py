
#! Create an object of DataFrame by using CSV File
#^======================================================================================================
# import pandas as pd

# df = pd.read_csv("D:\\PYTHON FULL STACK\\LibraryPrograms\\Pandas\\DATAFRAME\\students.csv")
# print("---------------------")
# print(df)
# print("---------------------")

#^======================================================================================================
#! Create an object of DataFrame by using CSV File
# import pandas as pd
# df = pd.read_csv("D:\\PYTHON FULL STACK\\LibraryPrograms\\Pandas\\DATAFRAME\\student_data.csv")
# print(df)

#^======================================================================================================

# import pandas as pd
# df = pd.read_csv("D:\\PYTHON FULL STACK\\LibraryPrograms\\Pandas\\DATAFRAME\\studentmarks.csv")
# print(df)
# print(type(df))
#^======================================================================================================

# import numpy as np ,pandas as pd
# df = pd.read_csv("D:\\PYTHON FULL STACK\\LibraryPrograms\\Pandas\\DATAFRAME\\studentmarks.csv")
# print(df)
# print("*"*80)

# print(df.shape)
#^=======================================================================================================

#todo===================================================================================================

#* 19-02 -2025
#todo===================================================================================================
#* varchar = dataframeobj.head() OR varchar = dataframeobj.head(n)

#& Get 5 Records from DataFrame
# recs = df.head()
# print(recs)
# print(type(recs))


#& Get 3 Records from DataFrame
# recs = df.head(3)
# print(recs)
# print(type(recs))


#& Get 6 Records from DataFrame
# recs = df.head(6)
# print(recs)
# print(type(recs))

#^=======================================================================================================
#& get Last 5  Records by using tail()
#* varchar = dataframeobj.tail() OR varchar = dataframeobj.tail(n)

# recs =df.tail()
# print(recs)
# print(type(recs))

#& get Last 2  Records by using tail()
# recs = df.tail(2)
# print(recs)
# print(type(recs))

#& get Last 6  Records by using tail()
# recs = df.tail(6)
# print(recs)
# print(type(recs))


#^=======================================================================================================
#! Obtain the Stastistical Information abount studentmarks1.csv file
#! which is available in the form of DataFrame
# print(df.describe())

# print(df.describe(include="all"))


# print(df["name"].describe())

#^=======================================================================================================

# import numpy as np ,pandas as pd
# df = pd.read_csv("D:\\PYTHON FULL STACK\\LibraryPrograms\\Pandas\\DATAFRAME\\studentmarks.csv")
# print(df)
# print("*"*80)



#& Get Record by Record by using iterrows()
# for rec in df.iterrows():
#     print(rec,end=" ")
# print()    


#& Get the Records from 4th to 9th from DataFrame Object
# print(df[4:10])


#& Get the Records all Even  Indexed Records from DataFrame Object
# print(df[::2])


#& Get the Records all Odd  Indexed Records from DataFrame Object
# print(df[1::2])

# print(df[4:9:2])

#* it Give only Column name because it the Slicing is wrong
#todo - slicing is wrong so that is Create an space
# print(df[4:10:-1])

#& get all record in reverse order 
# print(df[::-1])



#& Get the Name of all students    
#todo - get single Series of record into table
# print(df["name"])

# print(df["htno"])

#todo - get the both 
#todo - get more Series of record into table
# print(df["name","htno"])    #* KeyError: ('name', 'htno')
# print(df[["htno","name"]])

#& Get Name and Their Maths Marks
# print(df[["name","maths"]])

#^=======================================================================================================
#& Get Name and Their Maths Marks from 4th to 8th
# print(df[["name","maths"]][4:9])


#^=======================================================================================================
# #*   OR
#& Get Name and Their Maths Marks from 4th to 8th
#todo - OR 
# print(df[4:9][["name","maths"]])


#& Get Name and Their Maths Marks from 4th to 8th
# print(df[["name","maths"]][4:9:2])

#^=======================================================================================================


























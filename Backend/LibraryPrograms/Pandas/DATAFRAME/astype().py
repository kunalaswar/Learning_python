
#?===================================================================================================
#! create DataFrame from  Dictionary
import numpy as np
import pandas as pd
technologies = {'Fee':["20000","25000","26000"],"Discount":["1000","23000","1500"]}
df = pd.DataFrame(technologies)
# print(df)
#?===================================================================================================
#* object
# print(df.dtypes)

#^===================================================================================================
#! Cast all Column to int 
# df = df.astype(np.int64)

# print(df)
# print(df.dtypes)

#^===================================================================================================

#! Cast all column to string
# df =df.astype("string")
# print(df)
# print(df.dtypes)

#^===================================================================================================
#! Cast all columns to string
# df = df.astype("str")
# print(df)
# print(df.dtypes)
#^===================================================================================================


#! Cast all columns to float
# df = df.astype("float")
# print(df)
# print(df.dtypes)

#^===================================================================================================
#! convert a perticular column
# df["Fee"]=df["Fee"].astype("int")
# print(df) #*--->  int64
# print(df.dtypes)
#* OR
# df.Fee = df.Fee.astype("int")
# print(df)
# print(df.dtypes)


#?===================================================================================================
technologies = {'Courses':["Spark","PySpark","Hadoop"],
    'Fee' :["20000","25000","26000"],
    'Duration':['30day','40days','35days'],
    'Discount':["1000","2300","1500"]
               }
df = pd.DataFrame(technologies)
print("------------------------------------------")
print(df)
print("------------------------------------------")
print(df.dtypes)
#?===================================================================================================

#! Apply cast type for multiple columns
# df2 = df.astype({"Courses":"string","Fee":"int","Discount":"float"})
# print("---------------------------")
# print(df2)
# print("---------------------------")
# print(df2.dtypes)

#^===================================================================================================

#! Raise error when unable to cast
# df["Courses"]=df["Courses"].astype("int")
# print(df["Courses"])  #*ValueError: invalid literal for int() with base 10: 'Spark'


#* Syntax -1 DataFrame.astype("Datatype Values of Numpy OR python") --- for all the column of DataFrame
#* Syntax -2 DataFrame["colname "].astype("Datatype Values of Numpy OR python")--- for single column of DataFrame
#* Syntax -3 DataFrame["colname "].astype("Datatype Values of Numpy OR python",errors = "ignore")--- for single column of DataFrame-unable to Cast and keep original; type As it is without Raising ValueError


#* Syntax -4 DataFrame.colname.astype("Datatype Values of Numpy OR python",errors = "ignore")--- for single column of DataFrame-unable to Cast and keep original; type As it is without Raising ValueError



#! Ignore error when unable to cast
# df.Courses = df.Courses.astype("int",errors="ignore")
# print("-----------------------")
# print(df)
# print("--------------------------")
# print(df.dtypes)


#! Ignore error when unable to cast   
# df.Courses = df.Courses.astype("int",errors='ignore')
# print("----------------------------------")
# print(df)
# print("----------------------------------")
# print(df.dtypes)
# print("----------------------------------")







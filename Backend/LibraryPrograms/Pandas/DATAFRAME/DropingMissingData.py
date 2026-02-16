

#^===================================================================================================
#!   Dropna()

#^===================================================================================================
# import numpy as np
# import pandas as pd
# dict = {'First Score':[100, 90, np.nan, 95],
#         'Second Score': [30, np.nan, 45, 56],
#         'Third Score':[52, 40, 80, 98],
#         'Fourth Score':[np.nan, np.nan, np.nan, 65]}
# #Creating DataFrame object with dict 
# df=pd.DataFrame(dict)
# print("---------------------------------------------------------")
# print(df)
# print("---------------------------------------------------------")

#?===================================================================================================

#! Checking for missing values using isna(),isnull() ,notna() and notnull() :
# print(df.isna())
# print(df.isnull())


#! to drop the missing Values using dropna() function 
                #* DataFrame.dropna( axis=0, how='any')


# df.dropna() #* By Default is 0
# print(df)
#?===================================================================================================

#! place it itself
# df = df.dropna()
# print(df)

#todo - OR
# df.dropna(inplace=True)
# print(df)
#?===================================================================================================

# import numpy as np
# import pandas as pd
# dict = {'First Score':[100, 90, np.nan, 95],
#         'Second Score': [30, np.nan, 45, 56],
#         'Third Score':[52, 40, 80, 98],
#         'Fourth Score':[np.nan, np.nan, np.nan, 65]}
# df=pd.DataFrame(dict)
# print("---------------------------------------------------------")
# print(df)
# print("---------------------------------------------------------")

#?===================================================================================================
#* axis = 0 represent  for row
# df = df.dropna(axis=0)
# print(df)

#* axis = 1 represent for column
# df = df.dropna(axis=1)
# print(df)

#?===================================================================================================
#todo - OR
# df.dropna(axis=1,inplace=True)
# print(df)
#?===================================================================================================

#^===================================================================================================
#* how = "all"   
#* how = "any"
#todo  default Value of 'how' argument is 'any' and default axis is 0 (row)

#^===================================================================================================
#! HERE it not contain complete nan Value at the end Fourth Score 
# import numpy as np
# import pandas as pd
# dict = {'First Score':[100, 90, np.nan, 95],
#         'Second Score': [30, np.nan, 45, 56],
#         'Third Score':[52, 40, 80, 98],
#         'Fourth Score':[np.nan, np.nan, np.nan, 65]}
# df=pd.DataFrame(dict)
# print("---------------------------------------------------------")
# print(df)
# print("---------------------------------------------------------")
#?===================================================================================================

#todo - it take Only the with out nan value and default axis  = 0   row
# df = df.dropna(how="any") #* default Value of 'how' argument is 'any' and default axis is 0 (row)
# print(df)

# df.dropna(how="any",inplace=True) #* default Value of 'how' argument is 'any' and default axis is 0 (row)
# print(df)

#?===================================================================================================
#! HERE it WE contain complete nan Value at the end Fourth Score 
import numpy as np
import pandas as pd
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score':[52, 40, 80, 98],
        'Fourth Score':[np.nan, np.nan, np.nan, None]}
df=pd.DataFrame(dict)
print("---------------------------------------------------------")
print(df)
print("---------------------------------------------------------")

#todo - it take all the value with include nan value also
#todo - By default it axis =0 represent row
# df = df.dropna(how = "all")    #todo - By default it axis =0 represent row
# print(df)

# #* OR 
# df.dropna(how="all",inplace=True)
# print(df)

#?===================================================================================================
# df = df.dropna(how="all")
# print(df)

# #todo - By we mension it axis = 1 represent column
# #* Not affecting
# df.dropna(axis=1 ,how="all")
# print(df)

# #
# df.dropna(axis=1 ,how="all",inplace= True)
# print(df)









#! #Adding the Series of Values
#todo - Here the Index is same to add the data
#^=====================================================================================================
# import numpy as np
# import pandas as pd
# a = pd.Series([100,200,300,400,500],index=["a","b","c","d","e"])
# b = pd.Series([10,20,30,40,50],index=["a","b","c","d","e"])
# print("------------------------")
# print("Series-1")
# print(a)
# print("-------------------------------")
# print("Series-2")
# print(b)

# #* Add the Series of the values ---we use 
# #todo -    setobj3=serobj1.add(serobj2)
# c = a.add(b)
# print("Series -3")
# print(c)

#^=====================================================================================================
#! Adding the Series of Values 
#todo - the Label is not match is give NaN 
# import pandas as pd
# a = pd.Series([100,200,300,400,500],index=["a","b","h","d","e"])
# b = pd.Series([10,20,30,40,50],index=["a","b","f","c","e"])
# print("Series -1")
# print(a)
# print("Series -2")
# print(b)

# #todo - add the series of Different Values----we use   setobj3=serobj1.add(serobj2)
# c = a.add(b)
# print("Series -3")
# print(c)  #todo -it give both the series of data with the Label is not match is give NaN 

#^=====================================================================================================
#! Adding the Series of Values when Series object contains Different Label Names
#* Syntax : setobj3=serobj1.add(serobj2,fill_value=0)

# import pandas as pd
# a = pd.Series([100,200,300,400,500],index=["a","b","h","d","e"])
# b = pd.Series([10,20,30,40,50],index=["a","b","f","c","e"])
# print("------------------------------")
# print("Series -1")
# print(a)
# print("------------------------")
# print("Series-2")
# print(b)
# print("-------------------")
# #* add the series of Values----we use   setobj3=serobj1.add(serobj2,fill_value=0)
# c = a.add(b,fill_value=0)
# print('Series -3')
# print(c)
# print("----------------")

#^=====================================================================================================
#! Adding the Series of Values when Series object contains Different Label Names
#todo - it Gives complete NaN
# import pandas as pd
# a = pd.Series([100,200,300],index=["a","b","c"])
# b = pd.Series([10,20,30],index=["x","y","z"])
# print("----------------------------------")
# print("Series -1")
# print(a)
# print("---------------------")
# print("series-2")
# print(b)
# print("----------------------")
# c = a.add(b)
# print(c)

#^=====================================================================================================
#! Adding the Series of Values when Series object contains Different Label Names
#* syntax : setobj3=serobj1.add(serobj2,fill_value=0)
# import pandas as pd
# a = pd.Series([100,200,300],index=["a","b","c"])
# b = pd.Series([10,20,30],index=["x","y","z"])
# print("Series -1")
# print(a)
# print("Series -2")
# print(b)
# #* add the series of Values----we use   setobj3=serobj1.add(serobj2,fill_value=1)

# c = a.add(b,fill_value=1)
# print("Series -3")
# print(c)
#^=====================================================================================================

# import pandas as pd

# s1 = pd.Series([1, 2, 3])
# s2 = pd.Series([4, 5, 6])

# result = s1.attrs(s2, fill_value=0)
# print(result)





#! sub()
#^=====================================================================================================

#! Subtracting the Series of Values
# #* syntax :setobj3=serobj1.sub(serobj2)
# import pandas as pd
# a = pd.Series([100,200,300,400,500],index=["a","b","c","d","e"])
# b = pd.Series([10,20,30,40,50],index=["a","b","c","d","e"] )
# print("Series - 1")
# print(a)
# print("Series - 2")
# print(b)
# #* subtract the series of Values----we use   setobj3=serobj1.sub(serobj2)

# c = a.sub(b)
# print("Series - 3")
# print(c)

#^=====================================================================================================

#! Subtracting the Series of Values when Series object contains Different Label Names
#todo - output gives the values to the NaN when index Missmatch

# import pandas as pd
# a = pd.Series([100,200,300,400,500],index=["a","b","h","d","e"])
# b = pd.Series([10,20,30,40,50],index=["a","b","f","c","e"])
# print("---------------------------")
# print("Series - 1")
# print(a)
# print("Series -2")
# print(b)
# #* add the series of Values----we use   setobj3=serobj1.sub(serobj2,fill_value=0)
# c = a.sub(b)
# print("Series -3")
# print(c)
#^=====================================================================================================

#! Subtracting the Series of Values when Series object contains Different Label Names
# import pandas as pd
# a = pd.Series([100,200,300,400,500],index=["a","b","h","d","e"])
# b = pd.Series([10,20,30,40,50],index=["a","b","f","c","e"])
# print("---------------------------")
# print("Series - 1")
# print(a)
# print("Series - 2")
# print(b)
# # #* add the series of Values----we use   setobj3=serobj1.sub(serobj2,fill_value=0)
# c = a.sub(b,fill_value=0)
# print("Series - 3")
# print(c)

#^=====================================================================================================

# import pandas as pd
# a = pd.Series([100,200,300,400,500],index = ["a","b","h","d","e"])
# b = pd.Series([10,20,30,40,50],index=["a","b","f","c","e"])
# print("Series -1")
# print(a)
# print("Series -2")
# print(b)
# c = a-b
# print(c)



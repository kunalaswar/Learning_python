
#! drop()
#^======================================================================================================
#! Droping the Series of Values


# import numpy as np
# import pandas as pd
# a = pd.Series([100,200,300,400,500],index=["a","b","c","d","e"])
# print("---------------------------")
# print("Series -1")
# print(a)
# print("---------------------------")
#^======================================================================================================
#! To drop the values from series, we use  seriesobj.drop(['Label']) OR seriesobj.drop([index])
#* syntax = seriesobj.drop(['label']) or seriesobj.drop([index])
# import pandas as pd
# a = pd.Series([100,200,300,400,500],index=["a","b","c","d","e"])
# print("---------------")
# print("Series -1")
# print(a)
# print("---------------")
# #! Drop the C label Values
# print("Series of Values after drop")
# print(a.drop(['c']))

#^======================================================================================================
#! To drop the values from series, we use  seriesobj.drop(['Label']) OR seriesobj.drop([index])
# import pandas as pd
# a = pd.Series([100,200,300,400,500],index=["a","b","c","d","e"])
# print('Series -1')
# print(a)
# print("----------------------")

# #* Drop the C label Values
# print("Series of Value after drop")
#* Store into a repeate

# a = a.drop(['c'])
# print(a)
#^======================================================================================================
#! To drop the values from series, we use  seriesobj.drop(['Label']) OR seriesobj.drop([index])
# import pandas as pd
# a = pd.Series([100,200,300,400,500],index=["a","b","c","d","e"])
# print("Series -1")
# print(a)
# print("--------------------")
# #* Drop the c label values
# print("Series of values after drop")
# a.drop(['c'],inplace=True)
# print(a)

#^======================================================================================================
#! To drop the values from series, we use  seriesobj.drop(['Label']) OR seriesobj.drop([index])
# import pandas as pd
# a = pd.Series([100,200,300,400,500],index=["a","b","c","d","e"])
# print("Series -1")
# print(a)
# #* Drop the C label Values
# #todo -  print Multipul vlaues
# print("Series of Values after drop")
# a.drop(['b','d'],inplace=True)
# print(a)

#^======================================================================================================
#! To drop the values from series, we use  seriesobj.drop(['Label']) OR seriesobj.drop([index])
# import pandas as pd
# a=pd.Series([100,200,300,400,500])
# print("----------------------------------")   
# print("Series -1")
# print(a)
# #* Drop the value with index
# #todo - seriesobj.drop([index])
# a.drop([3],inplace=True)
# print(a)

#^=====================================================================================================
#* Drop the multiple value with index
#todo -Drop the Multiple values
# a.drop([1,4],inplace=True)
# print(a)

#^=====================================================================================================









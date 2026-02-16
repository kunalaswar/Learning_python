
# import numpy as np, pandas as pd
# a = pd.Series([100,200,np.nan,400,None],index=["a","b","c","d","e"])
# print("-----------------------")
# print("Series -1")
# print(a)
# print("-------------------------")

#^====================================================================================================
#todo -  isna()
#^====================================================================================================
#! To Find the Nan Value, we have a Function Call seriesobj.isna()
# import numpy as np ,pandas as pd
# a = pd.Series([100,200,np.nan,400,None],index=["a","b","c","d","e"])
# print("----------------------------")
# print( "Series -1")
# print(a)
# print("----------------------")
# print(a.isna())  #* Gives boolean array

#^====================================================================================================
#! To Find the Nan Value, we have a Function Call seriesobj.isna()

# import numpy as np ,pandas as pd
# a = pd.Series([100,200,np.nan,400,None],index=["a","b","c","d","e"])
# print("----------------------------")
# print( "Series -1")
# print(a)
# print("----------------------")
# print(a.isna())#* Gives boolean array

# print("Number of Missing vlaues",a.isna().sum()) #* Gives Number of Missing Values (NaN Values)

#^====================================================================================================
#todo -  isnull()
#^====================================================================================================
#! To Find the Nan Value, we have a Function Call seriesobj.isnull()
# import pandas as pd, numpy as np
# a = pd.Series([100,200,np.nan,400,None],index=["a","b","c","d","e"])
# print("-------------------------")
# print("Series -1")
# print(a)
# print("--------------------------")
# print(a.isnull()) #* Gives Boolean array

#^====================================================================================================
#! To Find the Nan Value, we have a Function Call seriesobj.isnull()
# import numpy as np,pandas as pd
# a = pd.Series([100,200,np.nan,400,None],index=["a","b","c","d","e"])
# print("-------------------")
# print("Series -1")
# print(a)
# print("------------------")
# #* store in into itself
# a = a.isnull()
# print(a) #* Gives Boolean array

#^====================================================================================================
#! To Find the Nan Value, we have a Function Call seriesobj.isnull()
# import numpy as np,pandas as pd
# a = pd.Series([100,200,np.nan,400,None],index=["a","b","c","d","e"])
# print("----------------")
# print("Series -1")
# print(a)
# print("--------------------")
# print("Number of  Missing values = ",a.isnull().sum()) #*Gives Number of Missing Values (NaN Values)

#^====================================================================================================

# print("Number of Missing values = ",a.size-a.count())


#^====================================================================================================









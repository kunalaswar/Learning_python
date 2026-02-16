
#* max()
#*  syntax : seriesobj.max()
#^======================================================================================================
#! Find Max Element by using seriesobj.max()
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("--------------------------")
# print("Series -1")
# print(a)
# print("-----------------------------")
# maxv = a.max()
# print("max values = ",maxv)

#^======================================================================================================
#! Find Max Element by using seriesobj.max()
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("-----------------")
# print("Original Series -1")
# print("--------------")
# a.sort_values(inplace=True)
# print(a)
# #todo - a.values gives ndarray 
# print("max Element =",a.values[-1])

#^======================================================================================================
#! Find Max Element by using seriesobj.max()
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("-------------------")
# print("Original Series -1")
# print(a)
# print("------------------------")
# #* in descending order and after getting max
# a.sort_values(ascending=False,inplace=True)
# print(a)

# #todo - a.values gives ndarray 
# print("max values = ",a.values[0])
#^======================================================================================================

#! syntax  = seriesobj=a.nlargest(Size how many Element )
#^======================================================================================================
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("-------------")
# print("Original Series -1")
# print(a)
# print("-------------------")
# maxv = a.nlargest(1)
# print(maxv)  #* Max Index Sobat yete

#^======================================================================================================
#! 
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("--------------")
# print("Original Series -1")
# print(a)
# print("-----------------")
# maxv = a.nlargest()  #* bydefault 5 values dete
# print("Max Element \n",maxv)  

#^======================================================================================================
#! Find Max Element by using seriesobj.nlargest(n)
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("--------------")
# print("Original Series -1")
# print(a)
# print("-----------------")
# maxv = a.nlargest(1)  #* bydefault 5 values dete
# print("Max Element \n",maxv.values[0])  

#^======================================================================================================
#!  Find Max Element by using seriesobj.nlargest(n)
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("-----------")
# print("Original Series -1")
# print(a)
# maxv = a.nlargest(2) #* N  values we can pass
# print("Max Element \n",maxv.values)  #* Max Element [23 14] Gives the values in the from of list

#^======================================================================================================
#! Find Max Element by using seriesobj.nlargest(n)
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("-----------------")
# print("Orignal Series -1")
# print(a)
# print("-------------------")
# maxv = a.nlargest(3)
# print("Max Element \n",maxv.values)  # [23 14 12]

#^======================================================================================================
#! Find Max Element by using seriesobj.nlargest(n)
# import pandas as pd
# a=pd.Series([10,2,-3,23,5,0,12,14,34,12,11,7,16,7,1,5,3])
# print("-----------------------")
# print("Original Series ")
# print(a)
# print("--------------------")
# maxv = a.nlargest()  #* By default It Gives 5 Largest Elements
# print(f"Max Element = ",maxv.size,maxv.values)

#^======================================================================================================
#! Find Min Element by using seriesobj.min()

# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("----------------")
# print("Series -1")
# print(a)
# print("------------------")
# a.sort_values(inplace=True)
# print("Min Element ",a.values[0])

#^======================================================================================================

# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("---------------------")
# print("Series 1")
# # print(a)
# print("------------------------------")
# minv = a.sort_values()
# print("Min Element = ",minv.values[0])
# print("Second Min Element = ",minv.values[1])

#^======================================================================================================

#! Find Min Element by using seriesobj.min()
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("------------------------")
# print("Series -1")
# print(a)

# a.sort_values(inplace=True)
# print("Min Element=",a.values[0])

#^======================================================================================================
#! Find Min Element by using seriesobj.min()
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14])
# print("---------------")
# print("Series -1")
# print(a)
# print("---------------")
# a.sort_values(ascending=False,inplace=True)
# print("Min Element= ",a.values[a.size - 1])
# print("Min Element= ",a.values[a.size - 2])

#^======================================================================================================










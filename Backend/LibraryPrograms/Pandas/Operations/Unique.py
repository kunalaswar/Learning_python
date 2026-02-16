
#! unique()
#^=====================================================================================================
# import numpy as np
# import pandas as pd
# s = pd.Series([10,20,10,20,30,10,30,20,10,15,25])
# print("Series of values ")
# print(s)
# print(s.unique())
#^=====================================================================================================

#* stored into another varible 
# import pandas as pd
# s = pd.Series([10,20,10,20,30,10,30,20,10,15,25])
# print("Series of values")
# print(s)
# s = s.unique()
# print(s)

#^=====================================================================================================
#! Our Code for Finding Unique Values from series object
# import pandas as pd
# import numpy as np
# s = pd.Series([10,20,10,20,30,10,30,20,10,15,25])
# lst = []
# for val in s:
#     if val not in lst:
#         lst.append(val)
# a = np.array(lst)        
# print("unique Element ")
# print(a)

#^=====================================================================================================
#& value_counts() to count the occurance of the values
# import pandas as pd
# s = pd.Series([10,20,10,20,30,10,30,20,10,15,25])
# print("Series values")
# print(s)
# #! Finding Number of Occuences of Series of Elements
# x = s.value_counts()
# print(x,type(x))

#^=====================================================================================================
# import pandas as pd
# s = pd.Series([10,20,10,20,30,10,30,20,10,15,25])
# print("Series of values :")
# print(s)

# #& Our Own Code for Finding Number of Occurences of Series of Elements
# dictobj = {}
# for val in s:
#     if val not in dictobj:
#         dictobj[val] = 1
#     else:
#         dictobj[val]=dictobj.get(val)+1
#         # dictobj[val]=dictobj[val]+1
# print("------------------------------------------------")            

# for key,val in dictobj.items():
#     print(f"{key}   {val}")

#^=====================================================================================================
# #* convert into the again the series 
# s1 = pd.Series(dictobj)
# print(s1,type(s1))


#^=====================================================================================================
#& To Find Number of Unique Values of Series Object---we use nunique()

# import pandas as pd
# s = pd.Series([10,20,10,20,30,10,30,20,10,15,25])
# print("Series of Values ")
# print(s)

# #* To find the number of unique values
# nou  = s.nunique()
# print("Number of Unique values ",nou)
#^=====================================================================================================
#& To Find Number of Unique Values of Series Object---we use nunique()
#*OR 
# import pandas as pd
# s = pd.Series([10,20,10,20,30,10,30,20,10,15,25])
# print("Series of values")
# print(s)

# print("Number of Unique vlaues = \n",s.value_counts())
# print("Number of Unique values = ",s.value_counts().size)
# #^=====================================================================================================
# #*OR
# print("Number of unique values = ",s.value_counts().count())

# #^=====================================================================================================

# #& Our Own Code for Finding Number of Occurences of Series of Elements
# dictobj = {}
# for val in s:
#     if val not in dictobj:
#         dictobj[val] = 1
#     else:
#         dictobj[val]=dictobj.get(val)+1
#         # dictobj[val]=dictobj[val]+1
# print("------------------------------------------------")            

# for key,val in dictobj.items():
#     print(f"{key}   {val}")
#^=====================================================================================================

# import pandas as pd
# import numpy as np
# s = pd.Series([10,20,10,20,30,10,30,20,10,15,25])
# lst = []
# for val in s:
#     if val not in lst:
#         lst.append(val)
# a = np.array(lst)        
# print("unique Element ")
# print(a)


#^=====================================================================================================








#!
#^======================================================================================================
# import numpy as np
# import pandas as pd
# lst = ["Rossum","Travis","Ritche","Dennis","Hunter"]
# s = pd.Series(lst)
# print("Series object data :")
# print(s)  #*  dtype: object

#^======================================================================================================
#! using name attribute  -------------5 attribute 
#*
# import pandas as pd
# lst = ["Rossum","Traavis","Ritche","Dennis","Hunter"]
# s = pd.Series(lst,name= "Emp")
# print("Series object data")
# print(s)    #* Name: Emp, dtype: object

#^======================================================================================================
#! give index and name 
#* Give our own index 
#* syntax: varname = pandas.Series(object,index = ,name = )
# import pandas as pd
# lst = ["Rossum","Traavis","Ritche","Dennis","Hunter"]
# s = pd.Series(lst,index=[100,101,102,103,104],name="Emp")
# print("Series object data ")
# print(s)

#! - Get the Series Name ---- Attribute name is name
# import pandas as pd
# lst = ["Rossum","Travis","Ritche","Dennis","Hunter"]
# s = pd.Series(lst,index=[100,101,102,103,104],name="Emp")
# print("Series object data ")
# print(s)
# #get the Series Name-----Attribute name is name
# print("---------------------------------")
# print("Series Name:  ",s.name)

#! rename the Name of the object ---- Attribute name is name
# s.name = "Scientists"
# print(s)

#!get all the values Series by using 'values'  -------Attribute values is name
# print(s.values,type(s.values))

# for names in s.values:
#     print(names)

#! Get Number of Values in series object--'size'--------- Attribute size is name
# print("Number of Element : ",s.size)

#! Get the data type of value in the Series Using dtype Attribute 
# print("Values type in s=",s.dtype)

#^======================================================================================================
#! provide some NaN value to the Series object 
#* datatypes is changes float
# import pandas as pd
# import numpy as np
# s1 = pd.Series([10,20,30,np.nan,40,50 ,np.nan])
# print(s1,type(s1))

# #! Give the all value in the Series object NaN also
# print("Number of Element in s1 USNIG size Attribute  = ",s1.size)

# #! Give only only value in the Series object  Not a NaN Value
# print("Number of Element is s1 USING count() = ",s1.count())

# #! Check the value type in Series object 
# print("Values type is s1 = ",s1.dtype)

#^======================================================================================================
#! Create an empty Series object
# import pandas as pd
# s2 =pd.Series()
# print("Content of s1 :")
# print(s2,type(s2))
# print("Is s2 Empty =",s2.empty) #* True

#^-------------------------------------------------------
#todo - Note--Series Attributes are
#todo - 1. name
#todo - 2. values
#todo - 3. size
#todo - 4. empty
#todo - 5 dtype

#^-------------------------------------------------------













#^======================================================================================================
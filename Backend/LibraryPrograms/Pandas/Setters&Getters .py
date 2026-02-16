
#^=========================================================================================

# import numpy as np
# import pandas as pd
# lst=["Rossum","Travis","Ritche","Dennis","Hunter","James","Jhon"]
# s = pd.Series(lst)
# print("Content of s")
# print(s)


# #! Accessing the Elements of Series by using indices
# print(s[0])  #*Rossum
# print(s[6])  #*Jhon

#^=========================================================================================
#!  Series object never Takes -Ve Indices.
#todo - Negative indexing is not in Series object
# print(s[-1])  #* keyError -1
# print(s[-2])  #* keyError -2

#^=========================================================================================
#! Accessing the Multiple Elements of Series by using Indices
# print(s[0::2]) #* even index
# print(s[1::2]) #* odd index


#^=========================================================================================

# import numpy as np
# import pandas as pd
# lst=["Rossum","Travis","Ritche","Dennis","Hunter","James","Jhon"]
# s = pd.Series(lst)
# print("Content of s")
# print(s)

#! Accessing the  Random Element of Series by using Random Indices /Slicing
# print(s[[2,5,6]]) #* ALL this provide random indices
# print(s[[0,5,2]]) 
# print(s[[0,2,6]])
#^=========================================================================================
#! changing Single Element by using Index
# s[0] = "GUIDO VAN ROSSUM"
# print(s,type(s))

#! changing Multiple Elements by using Indices
# s[0:3] = ["bhim","sandeep","kvr"]
# print(s,type(s))

#! changing Random Multiple Elements by using Random Indices
# s[[0,5,6]] = ["CHANGE0","CHANGE5","CHANGE6"]
# print(s,type(s))

#^=========================================================================================


#^=========================================================================================
#! Create the Series object with Label 
# import numpy as np
# import pandas as pd
# lst=["Rossum","Travis","Ritche","Dennis","Hunter","James","Jhon"]
# s1 = pd.Series(lst,index=["name1","name2","name3","name4","name5","name6","name7"],)
# print("Series Object Data")
# print(s1)

#! Accessing the Multiple Elements of Series by using Indices or slicing 
# print("---------------")
# print(s1[0:5])
#^=========================================================================================


#! Accessing the Multiple Elements of Series by using Indices
# print(s1[0::2])

#^=========================================================================================

#! Accessing the  Element of Series by using Label names
# print(s1[0])   #* Answer is come with future Warning
# print(s1["name1"]) #* Direct give the answer when passing the index
# print(s1["name2"])
# print(s1["NAME1"]) #*  keyError NAME1
# ^=========================================================================================

#! Accessing the  Element of Series by using Label names
#todo - It not take Size-1  like slicing or Indexing 
# print(s1["name2":"name5"])  #* it Provide all value to it
# print(s1["name1":])
# print(s1["name1"::2]) #odd indices
# print(s1["name2"::2]) #Even indices

# print(s1["name1":"name4"])
# print(s1["name1":"name4"][::-1])  #reverse of indices


#^=========================================================================================
#! Create the Series object with Label 
# import numpy as np
# import pandas as pd
# lst=["Rossum","Travis","Ritche","Dennis","Hunter","James","Jhon"]
# s1 = pd.Series(lst,index=["name1","name2","name3","name4","name5","name6","name7"],)
# print("Series Object Data")
# print(s1)

#^=========================================================================================
#!  Accessing the  Random Element of Series by using Random Label Name
# print(s1["name5"])

#^=========================================================================================
#& it come  with index and values
# print(s1[["name5","name2","name7"]])
#^=========================================================================================
#! changing Single Element by using Labels
# s1["name1"] = "ANKIT"
# print(s1,type(s1))

#!changing Multiple Elements by using Labels
# s1[["name1","name2"]] = ["SAGAR","OLI"]
# print(s1,type(s1))

# #! changing Random Multiple Elements by using Random Labels
# s1[["name2","name7"]]  = ["RISI","RAJ"]
# print(s1,type(s1))

























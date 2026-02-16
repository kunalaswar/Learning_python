
#!Number of approaches to Create an object of Series
#^=====================================================================================================
#todo - int
# import pandas as pd
# a = 10
# # print(a,type(a)) #*10 <class 'int'>
# s = pd.Series(a)
# print(s,type(s))

#^=====================================================================================================
#todo - float
# import pandas as pd
# a = 10.45 #* here a is an object of float
# print(a,type(a))
# s  = pd.Series (a)
# print(s,type(s))
# print(s.dtype)

#^=====================================================================================================
#todo - Bool
# import pandas as pd
# a = True #* here a is an object of Bool
# print(a,type(a))
# s = pd.Series(a)
# print(s,type(s))
# print(s.dtype)

#^=====================================================================================================
#todo - complex
# import pandas as pd
# a = 2+3j #* Here a is an object of complex
# print(a,type(a))
# s = pd.Series(a)
# print(s,type(s))
# print(s.dtype)

#^=====================================================================================================
# #todo - str
# import pandas as pd
# a = "python" #* Here a is an object of str
# print(a,type(a))
# s = pd.Series(a)
# print(s,type(s))
# print(s.dtype)  #* dtype = object

#^=====================================================================================================
#& It takes index automatically by default start from 0 
#todo -  range(start,stop,step)
# import pandas as pd
# a = range(10,21,2)
# print(a,type(a))  #* <class 'range'>
# s = pd.Series(a)
# print(s,type(s))
# print(s.dtype)

#^=====================================================================================================
#todo - bytes
# import pandas as pd
# b = bytes([1,2,3,4,5])
# print(b,type(b))
# s = pd.Series(b)
# print(s,type(s))

#^=====================================================================================================
# #todo -list
# import pandas as pd
# lst = [100,200,300,400]
# print(lst,type(lst))
# s = pd.Series(lst)
# print(s,type(s))


# lst = [100,200,300,400]
# s = pd.Series(lst,dtype=float)
# print(s,type(s))
# print(s.dtype)
#^=====================================================================================================
#! taaking all different Data to the list
# import pandas as pd
# lst= [100,"Rossum",45.67,"python",True]
# s = pd.Series(lst)
# print(s,type(s))
# print(s.dtype)
#^=====================================================================================================
#! Creating Series object with index name
# import pandas as pd
# lst= [100,"Rossum",45.67,"python",True]
# s = pd.Series(lst,index=["EID","NAME","SAL","LANG","STATUS"])
# print(s,type(s))

# print(s["EID"])
# print(s["NAME"])
#^-------------------------------------------------------------
# print(s[0]) #*FutureWarning:
#^-------------------------------------------------------------
# print(s["name"])  #* KeyError: 'name'

#^=====================================================================================================

#! Creating Series object with Index Names
# import pandas as pd
# lst =[100,"Rossum",45.67,"Python",True]
# s = pd.Series(lst,index=[1,2,3,4,5])
# print(s,type(s))

# #^-------------------------------------------------------------
# print(s[1])

#^-------------------------------------------------------------

# print(s[0]) #* KeyError: 0
#^=====================================================================================================

#! Creating the object with Index Names
# import pandas as pd
# lst=[100,"Rossum",45.67,"Python",True]    
# s = pd.Series(lst,index=[111,222,333,444,555])
# print(s,type(s))

# print(s[444])

# # print(s[4]) #* KeyError: 4

#^=====================================================================================================
# import pandas as pd
# lst = [[10,"RS"],[20,"TR"],[30,"DR"]]
# s = pd.Series(lst)
# print(s)
# print(type(s))


# print(s[0])

#^=====================================================================================================
#! Creating an object with index
# import pandas as pd
# lst = [[10,"RS"],[20,"TR"],[30,"DR"]]
# s = pd.Series(lst,index = ["Rec1","Rec2","Rec3"])
# print(s,type(s))

# print(s["Rec1"])

#^-------------------------------------------------
#todo - answer is come with the futureWarining
# print(s[0])   #* FutureWarning:

#^-------------------------------------------------
# print(s[::-1])
#^=====================================================================================================

#todo - tuple
# import pandas as pd
# tpl=([10,"RS"],[20,"TR"],[30,"DR"])
# s = pd.Series(tpl,index=[1,2,3])
# print(s,type(s))

#^=====================================================================================================
#! Creating an object of Series with set
# import pandas as pd
# st = {10,20,30,40,50}
# s = pd.Series(st)
# print(s,type(s))  #*TypeError: 'set' type is unordered

#^=====================================================================================================

#! Creating an object of series with frozenset
# import pandas as pd
# fst = frozenset({10,20,30,40,50})
# s = pd.Series(fst)
# print(s,type(s)) #* TypeError: 'frozenset' type is unordered
#^=====================================================================================================
#todo -Dict
#& Here key go to index Automatically

# import pandas as pd
# d = {10:1.2,20:2.3,30:4.5,40:5.6}
# s = pd.Series(d)
# print(s,type(s))

# print(s[10])

#^=====================================================================================================
#! converting Ndarray object into Series

# import numpy as np
# import pandas as pd
# a = np.array([10,20,30,40,50,60])
# print("Content of a")
# print(a,type(a))
# print("-------------------")
# s = pd.Series(a)
# print(s,type(s))

#^=====================================================================================================
#! Converting ndarray object into Series
# import numpy as np
# import pandas as pd
# a = np.array([10,20,30,40,50,60])
# print("COntent of a")
# print(a)
# print("----------------------")
# s = pd.Series(a,index=["ID1","ID2","ID3","ID4","ID5","ID6"])
# print(s)

#^=====================================================================================================




























#^======================================================================================================
#! a.nsmallest()
#! #Find Max Element by using seriesobj.nsmallest(n)
#^======================================================================================================
# import pandas as pd
# a=pd.Series([10,2,-3,23,5,0,12,14,34,12,11,7,16,7,1,5,3])
# print("-----------")
# print("Series -1")
# print(a)
# minv  = a.nsmallest(1)
# print("Min Element ",minv.values[0])

#^======================================================================================================
#* syntax :seriesobj = a.nsmallest(number)
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14,34,12,11,7,16,7,1,5,3])
# print("Series -1")
# print(a)
# a = a.nsmallest()  #* By defalut it's gives 5 values
# print(a)
#^======================================================================================================
#* syntax :seriesobj = a.nsmallest(number)

# import pandas as pd
# a  = pd.Series([10,2,-3,23,5,0,12,14,34,12,11,7,16,7,1,5,3])
# print("Series -1")
# print(a)
# minv = a.nsmallest(3) 
# print("Min Element :",minv.values[0],minv.values[1],minv.values[2])

#^======================================================================================================
#! Find Min Element by using seriesobj.nsmallest()
# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14,2,7,8,-1,-2,0])
# print("----------------")
# print("Original Series -1")
# print(a)
# minv = a.nsmallest(3)
# print("Min Element \n",minv.values)

#^======================================================================================================
#! Find Min Element by using seriesobj.nsmallest()

# import pandas as pd
# a = pd.Series([10,2,-3,23,5,0,12,14,2,7,8,-1,-2,0])
# print("Series -1")
# print(a)
# print("-----------------")
# minv = a.nsmallest()
# print("Min Elemnt : ",minv.values)

#^======================================================================================================





#& Statistical Operations on Series Object
#							Syntax:     seriesobj.sum()
#										seriesobj.count()
#										seriesobj.max()
#										seriesobj.min()
#										seriesobj.mean()
#										seriesobj.median()
#										seriesobj.var()
#										seriesobj.std()
#^====================================================================================================
#* syntax : seriesobj.sum()
#* syntax : seriesobj.count()
#* syntax : seriesobj.max()
#* syntax : seriesobj.min()

# import pandas as pd
# s = pd.Series([10,2,5,13,5,8])
# print("Series of values ")
# print(s)

# print("Sum of Series of Element = ",s.sum())
# print("Max of Series of Element = ",s.max())
# print("Min of Series of Element = ",s.min())
# print(" Number Element in Series = ",s.count())


#^====================================================================================================
# #& 
# Today Topic: Operations on Series
# ----------------------------------------------------
# 				1. Adding the Series of Values
# 						Syntax:     SeriesObj3=SeriesObj1.add(SeriesObj2)
# 								   SeriesObj3=SeriesObj1.add(SeriesObj2,fill_value=0)
	
# 				2. Substracting the Values of Series
# 						Syntax:     SeriesObj3=SeriesObj1.sub(SeriesObj2)
# 								SeriesObj3 = SeriesObj1.sub(SeriesObj2,fill_value=0)

# 				3. Droping the Values of Series
# 						Syntax:	SeriesObj.drop([Index])
# 								SeriesObj.drop([Label])
# 								SeriesObj.drop([Index1,index2,.....,Index-n])
# 								SeriesObj.drop([Label1,Label2,.....Label-n])
# 								SeriesObj.drop([Index1,index2,.....,Index-n],inplace=True)
# 								SeriesObj.drop([Label1,Label2,.....Label-n],Inplace=True)

# 				4. Finding Number of Missing values(NaN,None,NA)
# 							Syntax:   SeriesObj.isna()
# 									SeriesObj.isna().sum()
# 									SeriesObj.isnull()
# 									SeriesObj.isnull().sum()

# 				5. Sorting the Values of Series
# 							Syntax:   seriesobj.sort_values(ascending,inplace)
# 									seriesobj.sort_values()
# 									seriesobj.sort_values(inplace)
# 									seriesobj.sort_values(ascending)

# 				6. Finding Max / Highest Element from Series and Number Approaches
# 							Syntax:   SeriesObj.max()
# 									SeriesObj.nlargest(n)
# 				6. Finding Min / smallest Element from Series and Number Approaches
# 							Syntax:   SeriesObj.min()
# 									SeriesObj.nsmallest(n)
				
# 				8. Finding Unique Values from Series 
# 							Syntax:    serobj.unique()
# 				9 Finding Number of Unique Values from Series 
# 							Syntax:  serobj.nunique()
# 				10. Display Unique Values from Series Object.
# 							Syntax:   serobj.value_counts()
# 				11. Statistical Operations on Series Object
# 							Syntax:           seriesobj.sum()
# 										seriesobj.count()
# 										seriesobj.max()
# 										seriesobj.min()
# 										seriesobj.mean()
# 										seriesobj.median()
# 										seriesobj.var()
# 										seriesobj.std()
# 										seriesobj.mode()	
# 										seriesobj.describe()
# 										print(seriesobj.agg(["max","min","mean".........]))
# 										seriesobj.product()
# 										seriesobj.cumprod()

#^====================================================================================================
#& TO find the mean of the Series 
import pandas as pd
s = pd.Series([10,2,5,13,5,8])
print("Series of Values ")
print(s)
print("Mean  of Series = ",s.mean())
print("Mean of Series =",round(s.mean(),2))

#^====================================================================================================
#* To find the Median of Series first is to Sort the values
# print(s.sort_values())
# print("Median of Series  = ",s.median())

#^====================================================================================================
# #& To find the varience 
# print("Varience of Series = ",s.var())

# #& To find the Standard Deviation 
# print("Standard Deviation of Series = ",s.std())
#^====================================================================================================

#todo - In numpy there is not a mode function so that pandas have the mode function in it
#& To find the mode 
# print("Mode of Series = ",s.mode())


#^====================================================================================================

#&
# import pandas as pd
# s = pd.Series([2,5,3,4])
# print("Series of Values ")
# print(s)

# print("Product of series of Element = ",s.prod())  #*OR 
# #* prod() and product() are both Work same like
# print("Product of Series of Element = ",s.product())

#^====================================================================================================
#& To find cumprod of series  

# import pandas as pd
# s = pd.Series([2,5,3,4])
# print("values of Series ")
# print(s)
# print("cumulative product of Series of Values = ",s.cumprod())

#^====================================================================================================
#& Give all Summary of the Element
#& Describe()
#todo -this well apply only on the int values in series
# import pandas as pd
# s = pd.Series([2,5,3,4])
# print("Value of Series ")
# print(s)

# print("Summary of series of Element  = ")
# print(s.describe())

#^====================================================================================================
#& Give all Summary of the Element
#& Describe()
#todo -this well apply only on the str values in series

# import pandas as pd
# s = pd.Series(["RS","TR","DR","RS","SS"])
# print("Series of values")
# print(s)

# print("Summary of Series of Element In str ")
# print(s.describe())


# print("Summary of Series of Element ")
# print(s.describe(include=all))

#^====================================================================================================
# #todo -this well apply BOth int and str values in series
# import pandas as pd
# s = pd.Series([10,20,"RS",30,"TR","DR",10,"RS","SS",30])
# print("values of Seires")
# print(s)

# #& Give all Summary of the Element
# #*todo - describe(include = 'all') is not Work into in Series it work on Dataframe
# print("Summwry of Series of Element ")
# print(s.describe(include='all'))



#^====================================================================================================

# # & Finding the Aggregate Result of Statistical Operations--we use agg()
# import pandas as pd
# s = pd.Series([10,2,5,13,5,8])
# print("Series of values")
# print(s)
# print("----------------------------------")
# print("Aggregate Result of statistical Operations")
# print(s.agg(['max','min','sum','mean','median','var','std']))
# print("--------------------------------------------------------")

#^====================================================================================================


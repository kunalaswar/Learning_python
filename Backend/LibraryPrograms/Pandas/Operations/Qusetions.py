
#& 

#^=====================================================================================================
#& Convert the Series of values into  the lowercase

# import numpy as np
# import pandas as pd
# s = pd.Series(['Amit','Bob','Kate','A','b', np.nan, 'Car', 'dog', 'cat'])
# print("Series of Element ")
# print(s)

# for val in s:
#     print(val.lower()) #* It give an error ho convert the float value is not convert into the str

#^=====================================================================================================
#!   Q  1)
# import numpy as np
# import pandas as pd
# s = pd.Series(['Amit','Bob','Kate','A','b', np.nan, 'Car', 'dog', 'cat'])
# print("Series of values")
# print(s)

# for val in s:
#     print(str(val).lower())  #* type casting  the nan value into the str

#^=====================================================================================================
#!   Q  2)

# import numpy as np
# import pandas as pd
# s = pd.Series(['Amit','Bob','Kate','A','b', np.nan, 'Car', 'dog', 'cat'])
# print("Series of values")
# print(s)

# #todo - Doing with list comprasion 
# s1 = [str(val).lower() for val in s ]
# print(s1)

#todo - print the values with the nan into the list
#^=====================================================================================================
# import numpy as np
# import pandas as pd
# s = pd.Series(['Amit','Bob','Kate','A','b', np.nan, 'Car', 'dog', 'cat'])
# print("Series of values")
# print(s)

# s1 = [str(val).lower() for val in s if str(val)=="nan"]
# print(s1)

# s1 = [str(val).lower() for val in s if str(val)!="nan"]
# print(s1)

#^=====================================================================================================
#!   Q  3)
# import numpy as np
# import pandas as pd
# s = pd.Series(['Amit','Bob','Kate','A','b', np.nan, 'Car', 'dog', 'cat'])
# print("Series of values")
# print(s)
# s1 = [str(val).upper() for val in s  if str(val)!='nan']
# print(s1)

#^=====================================================================================================
#todo - Do this with the dict compresion
#& Give the value with How many letter of word is this
# import pandas as pd
# import numpy as np
# s = pd.Series(['Amit','Bob','Kate','A','b', np.nan, 'Car', 'dog', 'cat'])
# print("Series of values ")
# print(s)
# #todo -Dict compresion
# s1 = {str(val):len(val) for val in s if str(val)!='nan'}
# print(s1)
# for key,val in s1.items():
#     print(f"{key}---{val}")

#^=====================================================================================================
#& 6.2: From the raw data below create a Pandas Series ' Atul', 'John ', ' jack ', 'Sam'
# a) Print all elements after stripping spaces from the left and right
# b) Print all the elements after removing spaces from the left only
# c) Print all the elements after removing spaces from the right only
# import numpy as np
# import pandas as pd
# s= pd.Series([' Atul', 'John ', ' jack ', 'Sam'])
# print(s)


# #& a) Print all elements after stripping spaces from the left and right
# series_stripped = [str(ele).strip() for ele in s]
# print(series_stripped)

# #& b) Print all the elements after removing spaces from the left only
# series_lstripped = [str(val).lstrip() for val in s]
# print(series_lstripped)

#& c) Print all the elements after removing spaces from the right only
# series_rstripped = [str(val).rstrip() for val in s]
# print(series_rstripped)

#^=====================================================================================================
#& 6.3: 
# import numpy as np
# import pandas as pd
# s = pd.Series(  ['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])
# print(s)


#& a) split the individual strings wherever ‘_’ comes and create a list out of it.
# list_splited = [str(val).split()  for val in s]

# list_splited = [str(val).split("_")  for val in s]
# print(list_splited)

# complist = []
# for listwords in list_splited:
#     for words in listwords:
#         complist.append(words)
#     # print(words)
#         print(words)
#^=====================================================================================================

#& c) Expand the elements so that all individual elements get splitted by ‘_’ andinsted of list returns individual elements        
# print("complete list of word")
# print(complist)

# print("Complete list of word in single line ")
# print("".join(comlist))
#^=====================================================================================================
#& get the list of word with nan 
# import numpy as np
# import pandas as pd
# s= pd.Series(['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])
# print(s)
# list_splitted= [str(val).split("_") for val in s ]
# print(list_splitted)

# complist =[]
# for listwords in list_splitted:
#     for word in listwords:
#         if (word!="nan"):
#             complist.append(word)
#             print(word)

# print("Complete List of words")
# print(complist)

# print("Complete List of words in Single Line")
# print(" ".join(complist))
#^====================================================================================================

#& Create a series object from CSV File
# import pandas as pd
# # x = pd.read_csv("D:\\PYTHON FULL STACK\\LibraryPrograms\\Pandas\\Operations\\teacher2.csv")
# x = pd.read_csv("D:\\PYTHON FULL STACK\\Practice\\Files\\CSVFILE\\DynamicDict.csv")['TNAME']
# print(x,type(x))


# s = x['TNAME']
# print(s)












# #^RegExpr1.py
# import re 
# gd  = "python is an oop lang.python is also fun prog lang "
# sp  = "python"
# res = re.search(sp,gd)  #Here res is an object of re.Match OR None type 
# if (res!=None):
#     print("Search is successful")
#     print(f"start index : {res.start()}")
#     print(f"End index :{res.end()}")
#     print(f"Group Value : {res.group()}")


# else:    
#     print("Search is Unsuccessful")


# #^RegExpr2.py    
# import re 
# gd  = "python is an oop lang.python is also fun prog lang "
# sp  = "raj"
# res = re.search(sp,gd)  #Here res is an object of re.Match OR None type 
# if (res!=None):
#     print("Search is successful")
#     print(f"start index : {res.start()}")
#     print(f"End index :{res.end()}")
#     print(f"Group Value : {res.group()}")


# else:    
#     print("Search is Unsuccessful")

#*also in used
# lst =["python","python "]
# print(len(lst))


#^RegExpr3.py

# import re 
# gd  = "python is an oop lang.python is also fun prog lang "
# sp  = "python"
# res = re.findall(sp,gd) #res of type list Beacuse of the this holding Multiple value 
# print(res,type(res))
# print(f"{sp} found {len(res)} Time ")

# import re 
# gd  = "python is an oop lang.python is also fun prog lang "
# sp  = "an"
# res = re.findall(sp,gd) #res of type list Beacuse of the this holding Multiple value 
# print(res,type(res))
# print(f"{sp} found {len(res)} Time ")


#* we want both index and occurance
#^RegExpr4.py
# import re
# gd= "python is an oop lang.python is also fun prog lang"
# sp = "python"
# mattab= re.finditer(sp,gd)# <callable_iterator object at 0x000001E443B96FE0> <class 'callable_iterator'>
# print(mattab,type(mattab)) #Here mattab is object of  <class 'callable_iterator'>
# for mat in mattab:  #Here mat is object of<class 'class,re.Match'>
#     # print(mat)
#     print(f"start index : {mat.start()} , End index : {mat.end()} , value Group : {mat.group()}")
    
#?============================================================================================
#* Programmer Defined Character Classes in Regular Expressions 
#?============================================================================================
#todo - [abc] --->Searches for either 'a' or 'b' or 'c' only
#!program for searching Either 'a' or 'b' or 'c' only
#^RegExpr5.py
# import re 
# mattab = re.finditer("[abc]","cAK@2aLp4#Gq8HbQw")
# # print(mattab,type(mattab)) #<class 'callable_iterator'>
# for mat in mattab:
#     print(f"start index :{mat.start()}, End index :{mat.end()}, Value Group: {mat.group()} ")
# print("----------------------------------")    

#todo - [^abc] --->Searches for all Execpt 'a' or 'b' or 'c'
# #^RegExpr6.py
# import re  #todo - all the result came Except the abc 
# gd = "cAK@2aLp4#Gq8HbQw"
# sp = "[^abc]"
# mattab = re.finditer(sp,gd)
# # print(mattab,type(mattab))
# for mat in mattab:
#     print(f"start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("---------------------------------")


#*ANOTHER WAY ONLY  NOT STORING VARIABLE DIRECT USE  
# import re  #todo - all the result came Except the abc 
# mattab = re.finditer("[^abc]","cAK@2aLp4#Gq8HbQw")
# # print(mattab,type(mattab))
# for mat in mattab:
#     print(f"start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("---------------------------------")


#todo - [A-Z] program for Searching all the Upper Case Alphabets
#^RegExpr7.py
# import re
# mattab = re.finditer("[A-Z]" ,"cAK@2aLp4#Gq8HbQw")
# # print(mattab,type(mattab))
# for mat in mattab:
#     print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    

#todo - [^A-Z] program for Searching all Except  Upper Case Alphabets
#^RegExpr8.py
# import re
# mattab = re.finditer("[^A-Z]" ,"cAK@2aLp4#Gq8HbQw")
# # print(mattab,type(mattab))
# for mat in mattab:
#     print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    


#todo - [a-z] program for Searching all the Lower Case Alphabets
# #^RegExpr9.py
# import re
# mattab = re.finditer("[a-z]" ,"cAK@2aLp4#Gq8HbQw")
# # print(mattab,type(mattab))
# for mat in mattab:
#     print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    


#todo - [^a-z] program for Searching all Except Lower Case Alphabets
# #^RegExpr10.py
# import re
# mattab = re.finditer("[^a-z]" ,"cAK@2aLp4#Gq8HbQw")
# # print(mattab,type(mattab))
# for mat in mattab:
#     print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    


#todo - [0-9] program for Searching all Digits
#^RegExpr11.py
# import re
# mattab = re.finditer("[0-9]" ,"cAK@2aLp4#Gq8HbQw")
# # print(mattab,type(mattab))
# for mat in mattab:
#     print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    

#todo - [^0-9] program for Searching for all Except Digits
# #^RegExpr12.py
# import re
# mattab = re.finditer("[^0-9]" ,"cAK@2aLp4#Gq8HbQw")
# # print(mattab,type(mattab))
# for mat in mattab:
#     print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    

#todo - [A-Za-z0-9] program for Searching all Alphabets and Digits
#^RegExpr13.py
# import re
# mattab = re.finditer("[A-Za-z0-9]" ,"cAK@2aLp4#Gq8HbQw")
# # print(mattab,type(mattab))
# for mat in mattab:
#     print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    

#todo - [^A-Za-z0-9] program for Searching all Special symbol
#^RegExpr14.py
# import re
# mattab = re.finditer("[^A-Za-z0-9]" ,"cAK@2aLp4#Gq8HbQw")
# # print(mattab,type(mattab))
# for mat in mattab:
#     print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    


#todo - [A-Za-z] program for Searching all Alphabets
# #^RegExpr15.py
# import re
# mattab = re.finditer("[A-Za-z]" ,"cAK@2aLp4#Gq8HbQw")
# # print(mattab,type(mattab))
# for mat in mattab:
#     print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    

#todo - [^A-Za-z] program for Searching all Except Alphabets
# #^RegExpr15.py
# import re
# mattab = re.finditer("[^A-Za-z]" ,"cAK@2aLp4#Gq8HbQw")
# # print(mattab,type(mattab))
# for mat in mattab:
#     print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    

#?============================================================================================
#todo - [A-Z0-9] = Searches for uppercase Alphabets and all Digits
#todo - [^A-Z0-9] = Searches for Lowercase Alphabets and Special Symbols
#todo - [a-z0-9] = Searches for Lowercase Alphabets and all Digits
#todo - [^a-z0-9] = Searches for uppercase Alphabets and all Special symbols

#?============================================================================================



#todo - [A-Z0-9] = Searches for uppercase Alphabets and all Digits only
# #^RegExpr16.py
# import re 
# mattab = re.finditer("[A-Z0-9]","cAK@2aLp4#Gq8HbQw")
# # print(mattab,type(mattab))
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    


#todo - [^A-Z0-9] = Searches for Lowercase Alphabets and Special Symbols
# #^RegExpr17.py
# import re 
# mattab = re.finditer("[^A-Z0-9]","cAK@2aLp4#Gq8HbQw")
# # print(mattab,type(mattab))
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    



# #todo - [a-z0-9] = Searches for Lowercase Alphabets and all Digits
# # #^RegExpr18.py
# import re 
# mattab = re.finditer("[a-z0-9]","cAK@2aLp4#Gq8HbQw")
# # print(mattab,type(mattab))
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    


# #todo - [^a-z0-9] = Searches for uppercase Alphabets and all Special symbols
# # #^RegExpr19.py
# import re 
# mattab = re.finditer("[^a-z0-9]","cAK@2aLp4#Gq8HbQw")
# # print(mattab,type(mattab))
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    

#?============================================================================================
#* - pre- defined charaacter classes in Regular Expressions
#todo - 1) \s = seraches for spaces Character only
#todo - 2) \S = searches for all except spaces Character only
#todo - 3) \w = searches for word Character (Alphabets + Digits = Alpha-Numeric)only OR[A-Za-z0-9]
#todo - 4) \W = searches for Special Symbols  OR [^A-Za-z0-9]
#todo - 5) \d = seraching for digit OR [0-9]
#todo - 6) \D = searching for all Except Digits OR [^0-9] 

#?============================================================================================


# #todo -1) \s is pre-defined charecter class in regular Expression 
# #^RegExpr20.py
# import re 
# mattab = re.finditer("[\s]","cA K@2aL p4#Gq8 HbQw")
# # # print(mattab,type(mattab))
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    


#todo - 2)\S = searches for all except spaces Character only
# #^RegExpr21.py
# import re 
# mattab = re.finditer("[\S]","cA K@2aL p4#Gq8 HbQw")
# # # print(mattab,type(mattab))
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    


#todo - 3) \w = searches for word Character (Alphabets + Digits = Alpha-Numeric)only OR[A-Za-z0-9]
# #^RegExpr22.py
# import re 
# mattab = re.finditer("[\w]","cA K@2aL p4#Gq8 HbQw")
# # # print(mattab,type(mattab))
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    


#todo - 4) \W = searches for Special Symbols  OR [^A-Za-z0-9]
# #^RegExpr23.py
# import re 
# mattab = re.finditer("[\W]","cA K@2aL p4#Gq8 HbQw")
# # # print(mattab,type(mattab))
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    


#todo - 5) \d = seraching for digit OR [0-9]
# #^RegExpr24.py
# import re 
# mattab = re.finditer("[\d]","cA K@2aL p4#Gq8 HbQw")
# # # print(mattab,type(mattab))
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    


#todo - 6) \D = searching for all Except Digits OR [^0-9] 
# #^RegExpr25.py
# import re 
# mattab = re.finditer("[\D]","cA K@2aL p4#Gq8 HbQw")
# # # print(mattab,type(mattab))
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    

#?=========================================================================================
#todo - Quatiflers in Reg Expr
#todo - 1) k = searches for exactely one k
#todo - 2) k+ = searches for one k or More k
#todo - 3) k* = searches Zero k OR one k OR more k
#todo - 4) k? = searches for Zero k OR One k
#todo - 5) k = searches for exactely one k
#todo - 6) k = searches for exactely one k
#?=========================================================================================

#todo - 1) k = searches for exactely one k
# #^RegExpr26.py
# import re 
# mattab = re.finditer("k" ,"kvkkvkkvkvk")
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    


#todo - 2) k+ = searches for one k or More k
# # #^RegExpr27.py
# import re 
# mattab = re.finditer("k+" ,"kvkkvkkkvk")
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    

#todo - 3) k* = searches Zero k OR one k OR more k
# #^RegExpr28.py
# import re 
# mattab = re.finditer("k*" ,"kvkkvkkkvk")
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    


#todo - 4) k? = searches for Zero k OR One k
# #^RegExpr29.py
# import re 
# # mattab = re.finditer("." ,"kvkkvkkkvk")
# mattab = re.finditer("k?" ,"kvkkvkkkvk")
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    


#? Special Points
#?==============================================================================================================

# #^RegExpr30.py
# import re 
# # mattab = re.finditer("\d{2}" ,"cA K@23aL p4#Gq8 HbQw")
# mattab = re.finditer("\d{1,3}" ,"cA K@23aL p4#Gq8 HbQw890Jk%8765")
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    

# #^RegExpr31.py
# import re 
# # mattab = re.finditer("\d{2}" ,"cA K@23aL p4#Gq8 HbQw")
# mattab = re.finditer("[A-Za-z]+" ,"cA K@23aL p4#Gq8 HbQw890Jk%8765")
# # mattab = re.finditer("[A-Za-z]{3,6}" ,"cA K@23aL p4#Gq8 HbQw890Jk%8765")
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    


# #^RegExpr32.py
# import re 
# # mattab = re.finditer("\d{2}" ,"cA K@23aL p4#Gq8 HbQw")
# # mattab = re.finditer("\w" ,"cA K@23aL p4#Gq8 HbQw890Jk%8765")
# mattab = re.finditer("\W" ,"cA K@23aL p4#Gq8 HbQw890Jk%8765")

# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    

# #^RegExpr33.py
# import re 
# mattab = re.finditer("\dd.\dd" ,"cA K@23aL p4#Gq8 HbQw890Jk%8765 21.22")
# for mat in mattab:
#      print(f"Start index :{mat.start()}, End index :{mat.end()}, Value Group :{mat.group()}")
# print("--------------------------------------------")    







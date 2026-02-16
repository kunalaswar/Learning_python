  #* Applied only on str data

#!findall()
#^=======================================================================================================

# import re 
# gd = "python is an oop lang.python is also fun lang"
# sp = "python"
# kvr = re.findall(sp,gd)
# print(kvr,type(kvr))      #*['python', 'python'] <class 'list'>


# import re 
# 
# gd = "python is an oop lang.python is also fun lang"
# sp = "kvr"
# kvr = re.findall(sp,gd)
# print(kvr,type(kvr))  #*[] <class 'list'>
# print(len(kvr))

#^=======================================================================================================
#!search()
#& give the first ocurence
# import re
# gd = "python is an oop lang.python is also fun lang"
# search_pattern = "python"
# # print(re.search(search_pattern,gd))
# #* OR

# match_obj = re.search(search_pattern,gd)  #*endindex +1
# print(match_obj,type(match_obj))  #* <re.Match object; span=(0, 6), matdet='Python'>
# print(type(match_obj))         #*<class 're.Match'>


# import re
# gd = "python is an oop lang.python is fun lang"
# sp = "kvr"
# mat = re.search(sp,gd)
# print(mat)              #* None
# print(type(mat))        #*class 'NoneType'>


# import re 
# gd = "python is oop langauge.python is fun lang"
# sp = "python"
# # sp = "PYTHON"
# mat = re.search(sp,gd)
# if mat != None:
#     print("Search is Successfull")  #* Here mat is an object of class <re.match>
#     print("Start value :",mat.start())   #* 0
#     print("End value :",mat.end())       #* 6
#     print("Group value :",mat.group())   #* python
# else:
#     print("search is Unsuccessfull")    

#^=======================================================================================================
#! finditer()
#& gives the all occurence
# #* iter means search iteraterally
# import re
# gd = "Python is an oop lang.Python is also fun lang"
# sp = "Python"
# x  = re.finditer(sp,gd)

# print(x) #*<callable_iterator object at 0x00000250036FC250>
# print(type(x)) #*<class 'callable_iterator'>

# for val in x:
#     # print(val,type(val)) #* type of val <class 're.Match'> 

#     print(f"Start index: {val.start()} End index :{val.end()} \t Group value :{val.group()}")

#! if no then no output
# import re
# gd = "Python is an oop lang.Python is also fun lang"
# sp = "kvr"
# x = re.finditer(sp,gd)
# print(x) #* <callable_iterator object at 0x000001C9D724C3A0>
# for k in x: #* Here k is match class object   
#     print(f"Start index: {k.start()} End index :{k.end()} \t Group value :{k.group()}")
    
#^=======================================================================================================
import re
gd = "Python is an oop lang.Python is also fun lang"
sp = "an"
x = re.finditer(sp,gd)
print(x)
print(type(x))
for k in x:
    print(f"Start index: {k.start()} End index :{k.end()} \t Group value :{k.group()}")






#^=======================================================================================================









#&Programmer defined character classes
#!Program for Searching A or B or C only
#^========================================================================================================
#todo -without using th re module how to find the 'A' 'B' 'C' in gd
# gd = "Ak5#GnRp@7W&BYPQs6!CMx"
# for ch in gd:
#     if ch =="A"or "B" or"C":
#         print([ch] )

#^========================================================================================================
#!RegExpr4.py
# import re
# # gd = "Ak5#GnRp@7W&BYPQs6!CMx"
# gd = "aAk5#GnRp@7W&BYPQs6!CMx"
# sp = "[ABC]"
# print("---------------------")
# matdet = re.finditer(sp,gd) 
# for val in matdet:
#     print(f"Start index:{val.start()} \tEnd index:{val.end()}\t group value {val.group()} ")
    
#^========================================================================================================

#!Program for Searching A or B or C only
#!RegExpr5.py 
#* searching for Either 'A' or 'B' or 'C' Only
# import re
# metdet = re.finditer("[ABC]","aAk5#GnRp@7W&BYPQs6!CMx")
# for mat in metdet:
#     print(f"start value:{mat.start()}\t End value: {mat.end()}\t Group value: {mat.group()}")
#^========================================================================================================
#! Program for Searching for all  except A or B or C only
#! RegExpr6.py
#* searching for all Except "a" or "b" or "c"
# import re
# matdet = re.finditer("[^ABC]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#     print( f"start value {mat.start()}\t End Value {mat.end()}\t Group value {mat.group()}")

#^========================================================================================================
#!Program for Searching for all Upper Case Alphabets
#!RegExpr7.py
# import re
# matdet = re.finditer("[A-Z]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#     print(f"Start Index:{mat.start()} \t End Index : {mat.end()} \t  Value:{mat.group()}")

#^========================================================================================================
#! Program for Searching for all  except Upper Case Alphabets
#! RegExpr8.py
# import re
# matdet = re.finditer("[^A-Z]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#     print(f"start Index:{mat.start()}\t End Index:{mat.end()} \tGroup Value{mat.group()}")

#^==============================================================================================
#! Program for Searching for all  except Upper Case Alphabets
#! RegExpr8.py
# import re
# matdet = re.finditer("[^A-Z]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#      print(f"Start Index:{mat.start()} \t End Index:{mat.end()} \t  Value:{mat.group()}")


#^==============================================================================================
#! Program for Searching for all Lower Case Alphabets
#! RegExpr9.py
# import re
# matdet = re.finditer("[a-z]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#     print(f"Start Index:{mat.start()} \t End Index:{mat.end()} \t  Value:{mat.group()}")

#^==============================================================================================
#! Program for Searching for all   except Lower Case Alphabets
#! RegExpr10.py
#* R = row meaning is there
# import re 
# matdet = re.finditer(r"[^a-z]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#     print(f"Start Index:{mat.start()} \t End Index:{mat.end()} \t  Value:{mat.group()}")
    
#^==============================================================================================

#! Program for Searching for Upper  and Lower Case Alphabets only
#! RegExpr11.py
# import re
# matdet = re.finditer("[A-Za-z]","Ak5#GnRp@7W&BYPQs6!CMx")
# print("Ak5#GnRp@7W&BYPQs6!CMx")

# for mat in matdet:
#     print(f"Start Index:{mat.start()} \t End Index:{mat.end()} \t  Value:{mat.group()}")

#^==============================================================================================
#! Program for Searching for all except Upper  and Lower Case Alphabets
#! RegExpr12.py
# import re
# matdet = re.finditer("[^A-Za-z]","Ak5#GnRp@7W&BYPQs6!CMx")
# print(matdet)
# for mat in matdet:
#     print(f"Start Index:{mat.start()}\t End Index :{mat.end()} \t Group Value :{mat.group()}")
#^==============================================================================================
#!Program for Searching only Digits
#!RegExpr13.py
# import re
# matdet = re.finditer("[0-9]","Ak5#GnRp@7W&BYPQs6!CMx")
# print(matdet)
# for mat in matdet:
#     print(f"Start Index:{mat.start()}\t End Index :{mat.end()} \t Group Value :{mat.group()}")

#* search only for Specific Data 
# import re 
# matdet = re.finditer("[56]","Ak5#GnRp@7W&BYPQs6!CMx")
# print(matdet)
# for mat in matdet:
#     print(f"Start Index:{mat.start()}\t End Index :{mat.end()} \t Group Value :{mat.group()}")


#^==============================================================================================
#!Program for Searching for all except  Digits
#!RegExpr14.py
# import re
# matdet = re.finditer("[^0-9]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#     print(f"Start Index:{mat.start()}\t End Index :{mat.end()} \t Group Value :{mat.group()}")

#^==============================================================================================
#!Program for Searching for all Alpha-numerics only
#!RegExpr15.py
# import re
# matdet = re.finditer("[A-Za-z0-9]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
    # print(f"Start Index:{mat.start()}\t End Index :{mat.end()} \t Group Value :{mat.group()}")
#^==============================================================================================
# #!Program for Searching for all Special Symbols only
# #!RegExpr16.py
# import re
# nof_symbols = 0
# matdet = re.finditer("[^A-Za-z0-9]","Ak5#GnRp@7W&BYPQs6!CMx")
# for mat in matdet:
#     nof_symbols = nof_symbols+1
#     print(f"Start Index:{mat.start()}\t End Index:{mat.end()} \t Group value :{mat.group()}")
    
# print(f"TOtal Number of Special Symbols : {nof_symbols}")

#^==============================================================================================
#!Program for Searching for Upper case Alphabets and Digits only
#!RegExpr17.py
# import re
# matdet = re.finditer("[A-Z0-9]","Ak5#GnRp@7W&BYPQs6!CMx")
# print(matdet)
# for mat in matdet:
#     print(f"Start Index:{mat.start()}\t End Index:{mat.end()} \t Group value :{mat.group()}")

#^==============================================================================================
#!Program for Searching for all except  Upper case Alphabets and Digits only
#!RegExpr18.py
# import re
# matdet = re.finditer("[^A-Z0-9]","Ak5#GnRp@7W&BYPQs6!CMx")
# print(matdet)
# for mat in matdet:
#     print(f"Start Index:{mat.start()}\t End Index:{mat.end()} \t Group value :{mat.group()}")


#^==============================================================================================
#!Program for Searching for all Lower case Alphabets and Digits only
#!RegExpr19.py
# import re
# matdet = re.finditer("[a-z0-9]","Ak5#GnRp@7W&BYPQs6!CMx")
# print(matdet)
# for mat in matdet:
#     print(f"Start Index:{mat.start()}\t End Index:{mat.end()} \t Group value :{mat.group()}")

#^==============================================================================================
#!Program for Searching for all  except Lower case Alphabets and Digits 
#!RegExpr20.py    
# import re
# matdet = re.finditer("[^a-z0-9]","Ak5#GnRp@7W&BYPQs6!CMx")
# print(matdet)
# for mat in matdet:
#     print(f"Start Index:{mat.start()}\t End Index:{mat.end()} \t Group value :{mat.group()}")







#^==============================================================================================

    
    



    


    
    

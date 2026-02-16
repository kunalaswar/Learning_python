

#& Predefined Character Class
#^==============================================================================================
#todo - When you write r = row then SyntaxWarning is not comming
#todo - Treated as it is the data what we are written

#! program for Searching space 
# import re 
# matdet = re.finditer(r"\s","abKp5Dw&8cLq@6PxzU6!amS")
# for mat in matdet:
#     print(f"start Index:{mat.start()}\t End Index:{mat.end()} Group value :{mat.group()}")

#* Give some Space in it
#todo - \s --- for Space only
# import re 
# matdet = re.finditer(r"\s","ab Kp5Dw&8cLq@6PxzU6!amS")
# for mat in matdet:
#     print(f"start Index:{mat.start()}\t End Index:{mat.end()} Group value :{mat.group()}")
#^==============================================================================================
#! program for Searching all Except Space char(s)

#todo - \S --- for NOt Space only
# import re
# matdet = re.finditer(r"\S","ab Kp5Dw&8c Lq@6PxzU6!amS")
# for mat in matdet:
#     print(f"start Index:{mat.start()}\t End Index:{mat.end()} Group value :{mat.group()}")

#^==============================================================================================
#!Program for Searching the digits  
#! RegExpr21.py
#* "[0-9]"
# import re
# matdet = re.finditer(r"\d","Ak5Y#55GnR55.55p@7W&5555bP)s6!CMx")
# for mat in matdet:
#     print(f"start Index:{mat.start()}\t End Index:{mat.end()} Group value :{mat.group()}")

#^==============================================================================================
#! Program for Searching  for all  except the digits
#! RegExpr22.py
#!Program for Searching for all Except digits  
#*"[^0-9]"
# import re
# matdet = re.finditer(r"\D","Ak5Y#55GnR55.55p@7W&5555bP)s6!CMx")
# for mat in matdet:
#     print(f"start Index:{mat.start()}\t End Index:{mat.end()} Group value :{mat.group()}")
#^==============================================================================================
#!Program for Searching  for  Word Characters ( Alphabets+Digits) Only
#!RegExpr23.py
#* "[A-Za-z0-9]"
# import re
# matdet = re.finditer(r"\w","Ak5Y#GnRp@7W&bP)s6!CMx")
# print(matdet)
# for mat in  matdet:
#     print(f"start Index:{mat.start()}\t End Index:{mat.end()} Group value :{mat.group()}")

#^==============================================================================================
#!Program for Searching  for all special Symbols
#!RegExpr24.py    
#* "[^A-Za-z0-9]"

# import re
# matdet = re.finditer(r"\W","Ak5Y#GnRp@7W&bP)s6!CMx") #todo -   # start form 4 End From 5 so size-1
# for mat in matdet:
#     print(f"start Index:{mat.start()}\t End Index:{mat.end()} Group value :{mat.group()}")
#^==============================================================================================
#! Program for Searching  Space Characetr Only
#! RegExpr25.py
#* Here r means raw
# import re
# matdet = re.finditer(r"\s","A k5Y#GnRp @7W&bP)s6!CMx")
# for mat in matdet:
#     print(f"start Index:{mat.start()}\t End Index:{mat.end()} Group value :{mat.group()}")

#^==============================================================================================
#!Program for Searching  Except Space Characeter Only
#!RegExpr26.py
# import re
# matdet = re.finditer(r"\S","A k5Y#GnRp @7W&bP)s6!CMx")
# for mat in matdet:
#     print(f"start Index:{mat.start()}\t End Index:{mat.end()} Group value :{mat.group()}")


#^==============================================================================================
#& Quantifiers in Regular  Expression 

#^==============================================================================================
#!Program for Searching  One Char exactly 'K'
#!RegExpr27.py    
import re
# # matdet = re.finditer("K","KVKKVKKKVKV") #*OR
# matdet = re.finditer("[K]","KVKKVKKKVKV")
# for mat in matdet:
#     print(f"start Index:{mat.start()}\t End Index:{mat.end()} Group value :{mat.group()}")

#^==============================================================================================
#!Program for Searching  One K OR More K's
#!RegExpr28.py
# import re
# matdet = re.finditer("K+","KVKKVKKKVKV")
# for mat in matdet:
#     print(f"start Index:{mat.start()}\t End Index:{mat.end()} Group value :{mat.group()}")

#^==============================================================================================
#! Program for Seraching for Zero K One k OR More K's
#! RegExpr29.py
#* Place var K Nasel tar Space dete 
# import re
# matdet = re.finditer("K*","KVKKVKKKVKV") 
# for mat in matdet:
#      print(f"Start Index:{mat.start()} \t End Index : {mat.end()} \t Value:{mat.group()} ")

#^==============================================================================================
#!Program for Searching  Zero K or One K  
#!RegExpr30.py
#todo - ? meaning yek tar answar aahe ya nahi yes or no aasa
#* one k asl tr nasla tr space 
# import re
# matdet = re.finditer("K?","KVKKVKKKVKV") 
# for mat in matdet:
#      print(f"Start Index:{mat.start()} \t End Index : {mat.end()} \t Value:{mat.group()} ")


#^==============================================================================================
#!Program for Searching  Each and Every Character ALL Char
#!RegExpr31.py
# import re
# matdet = re.finditer(".","KVKKVKKKVKV") 
# for mat in matdet:
#      print(f"Start Index:{mat.start()} \t End Index : {mat.end()} \t Value:{mat.group()} ")
     


#& Predefined Character Class
#^==============================================================================================
#!Program for Searching the digits  
#! RegExpr21.py
#* "[0-9]"
# import re
# metdet = re.finditer(r"\d","Ak5Y#55GnR55.55p@7W&5555bP)s6!CMx")
# for mat in metdet:
#      print(f"Start Index : {mat.start()}\t End Index : {mat.end()} \t Value: {mat.group()}")

#* d+ one or more than one 
#* \dd two digits
#* \ddd {3}
#* \d{4}
#* \d{2,4} minimum 2 and maximum 4 
#* "[A-za-z]{3}"
#* \dd.\dd decimal number

# import re
# metdet = re.finditer("[A-Za-z0-9]{5}","Ak5Y#55GnR55.55p@7W&5555bP)s6!CMx")
# for mat in metdet:
#      print(f"Start Index : {mat.start()}\t End Index : {mat.end()} \t Value: {mat.group()}")

# ! Program for Searches for Floating Point values contains An interger part with 2 Digits and Decimal Part  with 2 Dogits

import re
metdet = re.finditer(r"\d\d.\d\d","Ak5Y#55GnR55.55p@7W&5555bP)s6!CMx")
for mat in metdet:
     print(f"Start Index : {mat.start()}\t End Index : {mat.end()} \t Value: {mat.group()}")


#^==============================================================================================

    


    







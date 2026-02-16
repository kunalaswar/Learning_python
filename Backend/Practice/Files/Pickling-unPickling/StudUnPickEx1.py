#StudUnpick.py
# import pickle
# try:
        
#     with open("stud.pick","rb") as fp:
#         obj=pickle.load(fp)
#         print(obj)
#         obj=pickle.load(fp)
#         print(obj)
#         obj=pickle.load(fp)
#         print(obj)
# except FileNotFoundError:
#     print("File not found ")        
# except EOFError:
#     print("EOFError handle by Except block")
    

#! With the While loop
    
#StudUnpick.py

import pickle
with open("stud.pick","rb") as fp:
    while(True):
        try:
            obj=pickle.load(fp)
            # print(obj)
            for val in obj:
                print(val,end="\t")
            print()    
            
        except EOFError:
            break    

#!write a python program which will copy an image  


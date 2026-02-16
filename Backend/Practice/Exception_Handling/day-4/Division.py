# from NumberDivisionError import NumberDivisionError #*class name 
# def divop(a,b):
#     if b==0:
#         raise NumberDivisionError  #todo -here raise is used for Hitting the exception 
#     else:
#         return (a/b)
        

import NumberDivisionError        
def multi(a,b):
    if b==0:
        raise NumberDivisionError
    else:
        return a/b    
        
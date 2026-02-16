from NameExcept import InvalidNameError,SpaceNameError
from NameExcept import ZerolengthError
# def validation(name:str):
    # # words=name.split()
    # # print(words)

    # if(len(name)==0):
    #     raise ZerolengthError
    # elif(name.isspace()):
    #     raise SpaceNameError    
    # else: 
    #     if( name.startswith("Dr.")):

    #         words=name[3:].split()   
    #         res=True
    #         for word in words:
    #             if not(word.isalpha()):
    #                 res=False
    #                 break

    #         if(res):
    #             return res
    #         else:
    #             raise InvalidNameError
    #     else:

    #         words=name.split()   
    #         res=True
    #         for word in words:
    #             if not(word.isalpha()):
    #                 res=False
    #                 break

    #         if(res):
    #             return res
    #         else:
    #             raise InvalidNameError


    
# print(validation("Dr.Sagar"))

def validation(name):
    if(len(name)==0):
        raise ZeroLengthError
    elif(name.isspace()):
        raise SpaceNameError
    else:
            words = name.split()
            res = True
            for word in words:
                if (not word.isalpha()):
                    res = False
                    break
            if (res):
               return name
            else:
               raise InvalidNameError
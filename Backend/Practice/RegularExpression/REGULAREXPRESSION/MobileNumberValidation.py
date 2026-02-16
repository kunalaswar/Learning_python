
#^===============================================================================================
#! Program for Validation of Mobile Number
#! MobileNumberValidEx1.py
# while (True):
#     mno = input("Enter a mobile number :")
#     if(len(mno)==10):
#         print("Valid mobile Number ")
#     else:
#         print("Invalid Mobile number :")    
#         break

#^===============================================================================================

#! Program for Validation of Mobile Number
#! MobileNumberValidEx1.py
# import re
# while(True):
#     mno = input("Enter a mobile number :")
#     if (len(mno)==10):
#         res = re.search(r"\d{10}",mno)
#         if res!=None:
#             print(f"{res.group()} is Valid mobile Number ")
#             break
#         else:
#            print(f"{res} is invalid mobile number its length - it must contain integer values - try again")   
#     else:
#         print(f"{res}Invlaid Mobile Number Due to Its Length ---Try again   ")

#^===============================================================================================
#!Program for validating Mobile Number Validation with country code
#! MobileNumberValidationEx2.py

# import re
# while True:
#     mno  = input("Enter a Mobile munber with COuntry code ")
#     if len(mno) ==13:
#         res = re.search(r"\+91\d{10}",mno)
#         if res!=None:
#             print(f"{res.group()} is Valid mobile Number ")
#         else:
#             print(f"{res} ia not Mobile Number Try---again ")    
#     else:
#         print(f"{mno} is invalid mobile number length")        

#^===============================================================================================
#! Program for validating Mobile Number Validation with country code
#! MobileNumberValidationEx3.py
# import re
# while(True):
#     mno = input("Enter your Mobile number with youe Country Code ")
#     if len(mno)==13:
#         res = re.search(r"\+9198\d{8}",mno)
#         if res!=None:
#             print(f"{res.group()} Is Valid Mobile Number ")
#             break
#         else:
#             print(f"{res} Is Not mobile number")    
#     else:
#         print(f"{mno} is Invalid number Length ---Try again")        

#^===============================================================================================
#! Program for validating Mobile Number Validation with country code
#! MobileNumberValidationEx4.py
import re
while True:
    mno = input("Enter Your Mobile number with Country Code ")
    if len(mno)==13:
        res = re.search(r"\+91[98]\d{8}",mno)
        if res!=None:
            print(f"{res.group()} Is valid Number ")
        else:
            print(f"{res} is invalid number")
    else:
        print(f"{mno} is invalid length number")

# +91898123456 Is valid Number
## +91989812345 Is valid Number         

#^===============================================================================================





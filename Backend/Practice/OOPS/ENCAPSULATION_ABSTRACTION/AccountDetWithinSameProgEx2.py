class Account:
    def __init__(self):
        self.__acno = 100
        self.name = "RS"
        self.__bal = 5.5
        self.__pin = 1234
        self.bank ="SBI"
    def __dispvals(self):
        print("Account number ",self.__acno)    
        print("Account name",self.name)    
        print("Account Balance ",self.__bal)    
        print("Account pin ",self.__pin)    
        print("Account Bank  ",self.bank)   
    def viewaccount(self):
        self.__dispvals()
ac=Account()
# ac.dispvals()
ac.viewaccount()


# todo - KVR SIR program
# #AccountDetWithinSameProgEx1.py
# class Account:
#     def __init__(self):
#         self.__acno=100
#         self.cname="Rossum"
#         self.__bal=5.5
#         self.__pin=1234
#         self.bname="SBI"
#     def __dispaccdet(self):
#         print("-----------------------------")
#         print("Account Number:",self.__acno)
#         print("Account Holder Number:", self.cname)
#         print("Account Balance:",self.__bal)
#         print("Account Pin:",self.__pin)
#         print("Account Branch Name:", ac.bname)
#         print("-----------------------------")
#     def viewaccount(self):
#         self.__dispaccdet()


# #Main Program
# ac=Account() # Object Creation
# #print("Account Number=",ac.__acno)Not Possible
# #It is Nt Possible to access encspsulated
# # Data Members of Account class as part of Main Program
# #ac.dispaccdet()---Not Possible to Access bcoz dispaccdet() is encapsulated
# ac.viewaccount()

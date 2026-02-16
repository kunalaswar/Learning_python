#AccountDetWithinSameProgEx1.py
class Account:
    def __init__(self):
        self.__acno = 100
        self.name = "RS"
        self.__bal = 5.5
        self.__pin = 1234
        self.bank ="SBI"

    def dispvals(self):
        print("--------------------------------------")
        print("Account number",ac.__acno) #todo - Data Abstraction   
        print("Account name",self.name)
        print("Account Balance",self.__bal)  #todo - Data Abstraction
        print("Account pin",ac.__pin)      #todo - Data Abstraction
        print("Account Branch name",self.bank)
#main program
#todo-It is Nt Possible to access encspsulated
#todo-Data Members of Account class as part of Main Program

ac = Account()        
ac.dispvals()


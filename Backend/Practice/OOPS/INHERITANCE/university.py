#university.py<---File Name and Module Name
class university:
    def getval1(self):
        self.uname= input("Enter a university name :")
        self.uloc= input("Enter a university location ")

    def disp1(self):
        print("-"*50)
        print("\t\tUniversity details ")
        print("-"*50)

        print("university name",self.uname)    
        print("university location",self.uloc)

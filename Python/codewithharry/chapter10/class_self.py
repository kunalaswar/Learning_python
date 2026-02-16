class Employee:
    language= "python"
    salary=12000

    def getInfo(self):
        print("this is an getInfo method")
        print(f"the language is {self.language} and salary is {self.salary}")


    def greet(self):
        print("Good Morning")    

E1 = Employee()
E1.getInfo()
E1.greet()
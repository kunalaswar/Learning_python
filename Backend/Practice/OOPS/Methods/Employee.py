# employee #<--- file name or module name 
class emp:
    def getvals(self,eno,ename,sal):
        self.eno = eno 
        self.name = ename
        self.sal = sal
        
    def displayvals(self):
        print(f"\t{self.eno} \t{self.name} \t{self.sal}")
            
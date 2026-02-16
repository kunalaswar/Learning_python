from university import university

class Collage(university):
    def getval2(  self):
        self.cname= input("Enter a collage name :")
        self.cloc =input("Enter  a collage location :")

    def disp2(self):
        print("-"*50)
        print("\t\t Collage Details ")     
        print("-"*50)
        print("Collage name ",self.cname)
        print("Colage location",self.cloc)

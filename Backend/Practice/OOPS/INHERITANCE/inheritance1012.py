 
#! InhProg3.py additon of two class data member

# class C1:
#     def getval1(self): #instance method
#         self.a = float(input("Enter a value for a :"))  #instance data member

# class C2(C1):
#     def getval2(self): #instance method 
#         self.b = float(input("Enter a Value for b :"))     #instance data member    

#     def operation(self):
#         self.c = self.a + self.b    
#         print(self.c) # print(c) formal varible

# # o1= C1()
# o2 = C2()
# # o1.getval1()
# o2.getval1()
# o2.getval2()
# o2.operation()

#^-----------------------------------------------------------------------------------------------
#!
# class C1:
#     def getval1(self):
#         self.a = float(input("Enter a value for a "))
# class C2(C1):
#     def getval2(self):
#         self.b = float(input("Enter  a value for b "))        

#     def operation(self):
#         o2.getval1()  #self.getval1()
#         o2.getval2()  #self.getval2() 
#         c= self.a+ self.b
#         print( "SUM = ",c)
# #main class    
# o1 = C1()
# o2 = C2()

# o2.operation()

#^-----------------------------------------------------------------------------------------------
#!multilevel inheritance

# class Grandparent:
#     def getGPP(self):
#         self.GPP = int(input("Enter a property of Grandparent "))

# class parent(Grandparent):
#     def getPP(self):
#         self.PP = int(input("Enter a property of parent "))        

# class child(parent):
#     def getCP(self):
#         self.CP = int(input("Enter property value of child"))        

#     def totp(self):
#         self.totp = self.GPP + self.PP +self.CP
#         print("property of Grandparent :",self.PP)
#         print("property of parent ",self.PP)
#         print("property pf child",self.CP)
#         print("total property => ",self.totp)

# # o1= Grandparent()
# # o2 = parent()
# o3 = child()
# o3.getGPP()
# o3.getPP()
# o3.getCP()
# o3.totp()
#^-----------------------------------------------------------------------------------------------

#!multiple inheritance
# class Grandparent:
#     def getGPP(self):
#         self.GPP = int(input("Enter a prperty of Grndparent :"))

# class parent:
#     def getPP(self):
#         self.PP = int(input("Enter property of parent :"))        


# class child (Grandparent,parent):
#     def g1etCP(self):
#         self.cp = int(input("Enter  a priopery od child :"))

#     def totalpro(self):
#         self.totpro = self.GPP+self.PP+self.cp 
#         print("total proerty is this  =>",self.totpro)

# o3=child()  
# o3.getGPP()
# o3.getPP()
# o3.g1etCP()
# o3.totalpro()

#^-----------------------------------------------------------------------------------------------
#!
#todo - when the all Classes instance data member data type is same THEN we return the value    
# class Grandparent:
#     def getGPP(self):
#         self.p = int(input("Enter a Grandparent property "))
#         return self.p

# class parent:
#     def getPP(self):
#         self.p =int(input("Enter a parent property "))        
#         return self.p

# class child(parent,Grandparent):
#     def getCP(self):
#         self.p = int(input("Enter a child property :"))        
#         return self.p

#     def totalprop(self):

#         x=self.getGPP()
#         y=self.getPP()
#         z= self.getCP()
#         total = x + y + z
#         print("Grandparent property :",x)    
#         print("parent property ",y)
#         print("child property ",z)

#         print("Total of the property =>  ",total)

# o3= child()        

# o3.totalprop()
#^-----------------------------------------------------------------------------------------------


#todo - #InhProg8.py
#todo  - 
import mysql.connector
class Grandparent:
    def getGPP(self):
        self.uname = input("Enteer a university name :") 
        self.uloc = input("Enter a university location :")

    def dispGpp(self):
        print("-"*50)
        print("\t\t university Details :")
        print("-" *50)
        print("University Name ",self.uname)
        print("University Location ",self.uloc)

class parent(Grandparent):
    def getPP(self):
        self.cname = input("Enter a Collage name :")     
        self.cloc = input("Enter a Collage location ") 

    def dispPP(self):
        print("-"*50)
        print("\t\tCollage Details ")    
        print("-"*50)
        print("Collage name ",self.cname)    
        print("Collage Location",self.cloc)


class child(parent):
    def getCP(self):
        self.sno   = int(input("Enter a student Number :"))
        self.sname = input("Enter a student name :")
        self.crs = input("Enter a student course:")
    def dispCP (self):
        print("-"*50)
        print("\t\tStudents Details ")    
        print("-"*50)
        print("Students number",self.sno) 
        print("Students name",self.sname)
        print("Students course",self.crs)

    def savedata(self):
        try:
                
            con = mysql.connector.connect(host = "localhost",
                                        user = "root",
                                        passwd = "kunal123456",         
                                        database ="batch9am" )


            cur = con.cursor()
             #Query
            iq="insert into studres values(%d,'%s','%s','%s','%s','%s','%s') "
            cur.execute(iq %(self.sno,self.sname,self.crs,self.cname,self.cloc,self.uname,self.uloc))
            con.commit()
            print("Records successfully inserted",cur.rowcount)
        except mysql.connector.DatabaseError as db:
            print("DataBase Error ",db)

o3 = child()
o3.getGPP()
o3.getPP()
o3.getCP()
o3.dispGpp()
o3.dispPP()
o3.dispCP()
o3.savedata()
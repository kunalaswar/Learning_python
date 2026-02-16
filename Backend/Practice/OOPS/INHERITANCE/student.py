#student.py<----File Name and Module Name
import mysql.connector
from collage import Collage
class student(Collage):
    def getval3(self):

        self.sno =input("Enter a student Number  :")
        self.name =input("Enter a student name :")
        self.crs =input("Enter a student Course :")
        self.getval1()
        self.getval2()
    def disp3(self):
        self.disp1()
        self.disp2()
        print("-"*50)
        print("\t\tstudents Details ")
        print("-"*50)
        print("students number",self.sno)    
        print("Students name",self.name)
        print("students course ",self.crs)

    def savedata(self):
    
        try:
            con = mysql.connector.connect(host ="localhost",
                                         user = "Root",
                                         passwd = "kunal123456",
                                         database = "batch9am")
            cur = con.cursor()                             
            #Query
            iq="insert into studres values(%d,'%s','%s','%s','%s','%s','%s') "
            cur.execute(iq %(self.sno,self.sname,self.crs,self.cname,self.cloc,self.uname,self.uloc))
            con.commit()
            print(f"Data {cur.rowcount} is inserted Check it ")
        except mysql.connector.DatabaseError as db :
            print("DataBase Error ",db)

            
        
# todo - Please write into the main file OR folder please         
s=student()        
s.getval3()
s.disp3()
s.savedata()


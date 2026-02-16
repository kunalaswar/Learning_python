import Createtable as create
import oracledb as orc
def addstudentrecord():
        try:

            conn=orc.connect("system/tiger@localhost/orcl")
            cur=conn.cursor()
            sno=int(input("Enter a students number :"))
            sname=input("Enter a studetns name ")
            marks=float(input("Enter a students marks "))

            aq=f"insert into students(sno,sname,marks) values({sno},'{sname}',{marks})"
            cur.execute(aq)
            conn.commit()
            print("ADD studetns into it")
            print(f"{cur.rowcount} Student added successfully. ")
            
        except ValueError :
            print("Dont Enter a str alnum and special symbols")


        except orc.DatabaseError as db:
            print("problem with database",db)

# addstudentrecord()

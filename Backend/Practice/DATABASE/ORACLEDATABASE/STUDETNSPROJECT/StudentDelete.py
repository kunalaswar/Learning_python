import Createtable as create
import oracledb as orc
def deleterecord():
        try:

            conn=orc.connect("system/tiger@localhost/orcl")
            cur=conn.cursor()
            sno=int(input("Enter a Studetns number to Delete :"))
            dq=f"delete from students where sno={sno} "
            cur.execute(dq)
            conn.commit()
            if cur.rowcount>0:
                print(f"{cur.rowcount}  studetns Record Delete ")
            else:
                print("Record Does not Exist ")    

            # print("DELETE studetns into it")
            # print(f"{cur.rowcount} Student deleted successfully. ")

        except ValueError:
            print("Dont Enter a str alnum and special symbols")

        except orc.DatabaseError as db:
            print("problem with database",db)

# deleterecord()


import oracledb as orc
def getallrecords():
        
    try:

        conn=orc.connect("system/tiger@localhost/orcl")
        cur=conn.cursor()
        sq="select * from students"
        cur.execute(sq)
        print("SEE all record seen successfully")
        metadata=cur.description
        print("--------------------------")
        for val in metadata:
            print(val[0] ,end="\t ")
        print()
        print("--------------------------")
        records=cur.fetchall()
        for record in records:
            for val in record:
                print(val,end="\t")
            print()
    except orc.DatabaseError as db:
        print("problem with your database",db)

# getallrecords()


def getrecord():
           
    try:

        conn=orc.connect("system/tiger@localhost/orcl")
        cur=conn.cursor()
        sno=int(input("Enter a Students number to SEE there record : "))
        sq=f"select * from students where sno={sno}"

        cur.execute(sq)
        # conn.commit()
        # print("")
        print(f"{cur.rowcount} is recode is seen successfully")

        record=cur.fetchall()
        # print(record)
        for val in record:
            print(val,end=" ")

    except orc.DatabaseError as db:
        print("problem with your database",db)

## getrecord()





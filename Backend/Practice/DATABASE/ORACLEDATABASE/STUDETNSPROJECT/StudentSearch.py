import oracledb as orc
def searchrecord():
           
    try:

        conn=orc.connect("system/tiger@localhost/orcl")
        cur=conn.cursor()
        sno=int(input("WHO record you wnat to see input there Studetns number "))
        sq=f"select * from students where sno= {sno}"

        cur.execute(sq)
        # conn.commit()
        print("SEE record seen successfully")
        # print(f"{cur.rowcount} is recode is seen successfully")

        record=cur.fetchall()
        # print(record)
        for val in record:
            print(val,end=" ")
            print()

    except orc.DatabaseError as db:
        print("problem with your database",db)

# searchrecord()

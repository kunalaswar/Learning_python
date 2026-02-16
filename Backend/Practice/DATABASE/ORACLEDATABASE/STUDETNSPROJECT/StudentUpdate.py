import oracledb as orc
def updaterecord():
        
    try:
            
        conn = orc.connect("system/tiger@localhost/orcl")
        cur=conn.cursor()
        sno=int(input("Enter a Studetns number for Updating the record"))
        sname=input("Enter a NEW students name :")
        marks=float(input("Enter a students new marks here :"))
        upq = f"update students set sname='{sname}',marks={marks} where sno={sno}"
        # upq = "UPDATE students SET marks = marks + 30"

        # print("Database is updated successfully ")

        cur.execute(upq)
        if cur.rowcount >0:
            print((f"{cur.rowcount} Studetns record Updated successfully"))
        else:
            print("Record Does not Exist")    
        conn.commit()
        print("Cursor object is create ")
        
    except orc.DatabaseError as db :
        print("Does't connect Database problem with your code ",db)    

# updaterecord()

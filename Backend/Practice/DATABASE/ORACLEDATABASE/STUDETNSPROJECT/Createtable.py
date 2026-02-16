def create():
        
    import oracledb as orc

    try:
            
        conn = orc.connect("system/tiger@localhost/orcl")
        cur=conn.cursor()
        sq="create table student (sno number(2)primary key ,sname varchar(20) not null,marks number(5,2)not null)"
        print("Database is Created")
        cur.execute(sq)
        print("Cursor object is create ")
        
    except orc.DatabaseError:
        print("Does't connect Database problem with your code ")    

# create()

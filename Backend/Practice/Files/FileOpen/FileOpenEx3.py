try:
    with open("stud1.data","r") as fp:
        print("---Inside of with open() as Indentation-----")
        print("File opened in read Mode Successfully ")
        print("Is file closed :",fp.closed)
        print("File opening Modes = ",fp.mode)
        print("File Name = ",fp.name)
        print("Can we READ data from file = ",fp.readable())
        print("Can we WRITE data from file = ",fp.writable())
    print("Come out from Indentation Block = ",fp.closed)    
    print("Is File Closed after out-off with open() ",fp.closed)
except FileNotFoundError:
    print("\t File is Not Found How I can read ")

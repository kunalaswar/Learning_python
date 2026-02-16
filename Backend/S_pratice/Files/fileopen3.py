# #! program to Demostrating to Open  the file 
#* Not closed the file in finally block 
try:
    with open("stud1.data","r") as fp:
        print("---------Inside of with Open as Indentation ")
        print("File open in read moad Succesfully ")
        print("IS File Closed= ",fp.closed)
        print("------------------------------------")
        print("\tFile Opening Mode=",fp.name)
        print("\tFile Opening Mode=",fp.mode)
        print("\tCan we Read the Data from File=",fp.readable())
        print("\tcan we write the Data to the file=",fp.writable())
        print("\tIs File Closed=",fp.closed) #with in the Identation block 
    print("\nIs File Closed after out-off with open() as Identation=",fp.closed)    
    print("IS File Closed= ",fp.closed)
    

except FileNotFoundError:
    print("File is not found ")
    

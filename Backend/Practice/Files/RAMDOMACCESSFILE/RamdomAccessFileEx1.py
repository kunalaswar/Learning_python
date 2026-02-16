 #! program to need for random access file
# with open ("Hyd.data","r") as fp:
#     filedata=fp.read()
#     print(filedata)

with open("Hyd.data","r") as fp:
    print("Initial position of fp= ",fp.tell()) # 0
    filedata=fp.read(3)
    print(filedata)
    print("Now position pointed by fp :",fp.tell())
    filedata=fp.read(8)
    print(filedata)
    print("Now position pointed by fp :",fp.tell())
    filedata=fp.read(7)
    print(filedata)
    #Re-set the file pointer
    fp.seek(0)
    filedata=fp.read(7)
    print(filedata)
    



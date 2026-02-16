try:
    fp=open("stud1.data","w")
    # print(fp,type(fp))
except  FileExistsError:
    print("File already Exit")   



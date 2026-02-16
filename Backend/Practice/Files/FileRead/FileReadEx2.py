def dispfiledata():
    try:
        filedata=input("Enter a file Name :")
        with open(filedata,"r") as fp:
            print(type(filedata))
            file=fp.readlines()
            # print(file)
            for val in file:
                print(val,end="")
    except FileNotFoundError:
        print("File Not found ")    

dispfiledata()        

#*D:\PYTHON FULL STACK\Core python\Class Notes on 8TH NOV 2024-20240812T114336Z-001\Index of Files.txt
#* file che path aahe te pan Double " " inverded madhe yetat
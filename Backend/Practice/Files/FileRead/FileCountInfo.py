
#! write a python program which will read number of lines ,number of words, number of letter form any file
#*program for counting the Lines,words and char form any files
#^---------------------------------------------------------------------------------------------------


# with open("stud2.data","r") as fp:
#     filedata=fp.readlines()
#     print( filedata,type(filedata))
#     print("file line data = ",len(filedata))

with open("stud2.data","r") as fp:
    filedata=fp.readlines()             #! python is
                                        #! oop lang
    nl=0
    nw=0
    nc=0
    print(filedata)
    for line in filedata:
        nl=nl+1
        nw=nw+len(line.split())
        nc=nc+len(line)
            #For Counting Number of Alphabets-use the following Code
            #for ch in line:
            #    if(ch.isalpha()):
            #        nc=nc+1

        # nc=nc+(line)

        print(line)
    else:

        print("----------------------------")
        print("Number of Lines",nl)
        print("Number of words",nw)
        print("Number of Chars",nc)
        print("----------------------------")























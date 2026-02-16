
#!program for copying the contant of one fine into another file

#^---------------------------------------------------------------------------------------------------
def filecopy():
    try:
        srcfile=input("Enter a source file Name :")
        with open(srcfile,"r") as rp: #open the source file in r mode to read the data from file
            dstfile=input("Entera distanation file Name :")
            with open(dstfile,"a") as wp: #open the Distanation file in write mode 
                srcfiledata=rp.read()
                wp.write(srcfiledata)
                print("SRC file data Copid into Destination file---Verify that")

                
    except FileNotFoundError:
        print("Source file is found ")            

filecopy()

























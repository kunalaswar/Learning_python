# StudentMain.py <---file Name or Module Name
import pickle
def getallrecords():
    try:
        with open("NIT.data","rb") as rp:
            print("\tStudents Details ")
            while(True):
                try:
                    # print("*"*50)
                    # print("Students Details")
                    # print("*"*50)
                    record=pickle.load(rp)
                    for val in record:
                        print(f"\t{val}",end="\t")
                    print()    
                except EOFError:
                    print("-"*50)        
                    break


    except FileNotFoundError:
        print("FIles Does not Exist !")



# getallrecords()
def getrecord():
    try:
        with open("NIT.data","rb")as fp:
            records=[]
            while(True):
                    
                try:
                    record=pickle.load(fp)
                    records.append(record)
                except EOFError:
                    break 
            # print(records)
            # get students Number from kbd  to  get abother records    
        try:
                sno=int(input("Enter your Sno number :"))
                for recordi in records:
                    # print(recordii)
                # print(recordii,type(recordii))
                    found=False
                    if sno==records[0]:
                        found=True    
                        break
                if (found)        :
                    print(f"\t students Number{record[0]}")
                    print(f"\t students Name{record[1]}")
                    print(f"\t students Marks{record[2]}")
                else:
                    print("Students Records Does not Exist")
        except ValueError:
                print("Dont Enter str symbol and ")        
    except FileNotFoundError:
        print("file not found error ")                

getrecord()

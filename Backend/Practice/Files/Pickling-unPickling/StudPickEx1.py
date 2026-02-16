import pickle
while(True):
    with open("stud.pick","ab") as fp:
        sno=int(input("Enter a student Number :"))
        sname=input("Enter a student Name")
        smarks=input("Enter a student Marks")

        #cerate  a empty list of add the value
        l=list()
        l.append(sno)
        l.append(sname)
        l.append(smarks)
        # print(l)

        pickle.dump(l,fp)
        print("student Data saved as record")
        ch=input("Do you want to add another recorted (yes/no) :")
        if ch.lower()=="no":
            break



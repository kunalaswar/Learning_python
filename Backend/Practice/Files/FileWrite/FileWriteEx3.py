
x= {10:"Python",20:"Java",30:"C",40:"DSA"} # Here x is called Iterable Object
# x=[10,"rs",45.23,"NL"]
# y=[20,"rs",45,"NL"]
with open ("stud3.data","a") as fp:
    fp.writelines(str(x)+"\n")
    # fp.writelines(str(y)+"\n")

print("Data written to the file ---verify")    


#Program for Writing the Data to the File----writelines()
#FileWriteEx2.py
# x= {10:"Python",20:"Java",30:"C",40:"DSA"} # Here x is called Iterable Object
# with open("stud5.data","a") as fp:
#     fp.writelines(str(x)+"\n")
#     print("Data Written to the File--verify")
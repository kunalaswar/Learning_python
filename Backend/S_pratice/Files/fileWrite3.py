# #!Program for Writing the Data to the File----writelines()
#FileWriteEx2.py
x=[10,"RS",45.67,"NL"]
with open("stud13.data","a") as fp:
    fp.writelines(str(x))
    print("Data written to the file ---Verify your file ")



# #!Program for Writing the Data to the File----writelines()
#FileWriteEx2.py
# with open("stud12.data","a") as fp:
#     fp.writelines(str(list([1,2,3,4,5])))
#     print("Data Written to the File--verify")
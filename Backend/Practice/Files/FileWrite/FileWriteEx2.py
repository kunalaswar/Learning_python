x=[10,"rs",45.23,"NL"]
y=[20,"rs",45,"NL"]
with open ("stud2.data","w") as fp:
    fp.writelines(str(x)+"\n")
    fp.writelines(str(y)+"\n")

print("Data written to the file ---verify")    

#^---------------------------------------------------------------------------------------------------





















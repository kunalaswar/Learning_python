# x=[1,2,3,4,5]
# y=[6,7,8,9,12]
# with open("stud1.data","a") as fp:
#     # print(fp.name)
#     # print(fp.mode)
#     fp.write(str(x)+"\t")
#     fp.write(str(y)+"\n")



#^----------------------------------------------------------------------------------------------------

# empno=int(input("Enter a Emp number :"))
# empname=(input("Enter a Emp Name :"))
# empsalary=float(input("Enter a Emp Salary :"))
# with open("stud1.data","a") as fp:
#     fp.write(str(empno)+"\t")
#     fp.write(empname +"\t")
#     fp.write(str(empsalary)+'\n')
# print("Verify your file or check it")



#^----------------------------------------------------------------------------------------------------
def dispfiledata():
        
    try:
        filedata=input("Enter a file Name ")

        with open(filedata,"r") as fp:
            print(type(filedata))
            filedata=fp.read()
            print("content of the file")
            print(f"{filedata}")

    except FileNotFoundError:
        print("File not found there") 
dispfiledata()


























marks1 = int(input("Enter a mark 1: "))
marks2 = int(input("Enter a mark 2: "))
marks3 = int(input("Enter a mark 3: "))

total_percentage = (100*(marks1+marks2+marks3))/300

if(total_percentage>=40 and marks1>=30 and marks2>=30 and marks3>=30):
    print("You are passed :",total_percentage )
else:
    print("You are fail",total_percentage)
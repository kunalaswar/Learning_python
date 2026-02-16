#! write a program which is generated numtiplication table using module
def mul(n):
    if n<=0:
        print("Invalid input ")
    else:    
        for val in range(1,11):
            print(f"{n} X {val} = {n*val}")
        
##! while(True):
# num=int(input("Enter a number which table you  want : "))
# print()
# mul(num)
# print()





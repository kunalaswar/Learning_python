# #! write  a python program whhich will accept numerical value decide it is prime or not with the use of Module
#  Prime.py ---> a file name  or module name
def decideprime(n):
    if n<=0:
        print("Invalid input ")
    else:
        res="prime"
        for val in range(2,n):
            if n%val==0:
                res= "Not prime"
                break   

        if res=="prime":
            print(f"{n} is prime")        
        else:
            print(f"{n} is Not prime")
    
# n=int(input("Enter a number :"))                
# decideprime(n)


















#?=======================================================================================================


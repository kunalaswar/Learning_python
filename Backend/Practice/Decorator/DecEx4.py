def calculation(kvr):
    def square():
        n=kvr()
        res=n**2
        return n,res
    return square    



@calculation 
def getval():
    return int(input("Enter a Numerical value :"))

n,res=getval()
print(n,"=",res)














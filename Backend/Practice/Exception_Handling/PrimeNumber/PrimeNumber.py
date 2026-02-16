from PrimeExcept import NonprimeError
def prime(num):
    if num==0 or num==1 or num<0:
        raise NonprimeError
    else:
        res=True
        for val in range(2,num//2):
            if num%val==0:
                res=False
        if res:
            print(f"{num} is prime number")      
        else:
            print(f"{num} is not prime")    

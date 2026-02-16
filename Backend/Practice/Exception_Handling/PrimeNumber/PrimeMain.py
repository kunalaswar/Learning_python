from PrimeExcept import NonprimeError
from PrimeNumber import prime
try:
    num=int(input("Enter a number :"))
    prime(num)
except (NonprimeError,ValueError):
    print("\tDont Enter a 1 or 0 or (-VE) number")    
    print("\tDont Enter Str symbols  ")


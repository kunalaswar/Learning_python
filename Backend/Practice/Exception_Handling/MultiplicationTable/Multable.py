from MulExcept import ZeroError,NegativeNumberError

def table(num):
    if num==0:
        raise ZeroError

    elif num<0:
        raise NegativeNumberError
    
    else:
        print("Multiplication table ")
        for i in range(1,11):
            print(f"{num} X {i} = {num*i}")

# num=int(input("Enter number "))
# res=table(num)
# print(res)

# print(res)




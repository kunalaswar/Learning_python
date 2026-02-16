from ATMExcept import DepositError,WithdrawError,InSuffFundError
bal=500
def Deposit():
    damt=int(input("Enter deposit value :"))
    global bal
    if (damt<0):
        raise DepositError
    else:  
        bal=bal + damt
        print(f"Your deposit amount is {damt}")
        print(f"Your add balnace is {bal}")

def Withdraw():
    global bal
    wamt=float(input("Enter HOw many value you want to Withdraw :"))
    if wamt<0:
        raise WithdrawError
    elif (wamt+500>bal):
        raise WithdrawError
    else:
        print(f"Your withdraw balance is {wamt}")
        bal=bal-wamt    
        print(f"and After Withdraw yor amount is {bal}")

def Display():
    global bal
    print("YOUR BALANCE IS THAT ",bal)
    # print()


# Deposit()
# Withdraw()
# Display()


    

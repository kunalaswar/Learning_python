from ATMExcept import DepositError,WithdrawError,InSuffFundError
from 
bal=500
def deposit():
    global bal
    damt=float(input("Enter a Deposit value :")) #*valueError
    if(damt<0):
        raise DepositError
    else:
        bal=bal+damt
        print("Ur Account xxxxxx123 Deposited with INR:{}".format(damt))
        print("Now Ur Account xxxxxx123 Balance INR:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter a Withdraw value :"))
    if(wamt<0):
        raise WithdrawError
    elif(wamt+500>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("Ur Account xxxxxx123 Withdraw with INR:{}".format(wamt))
        print("Now Ur Account xxxxxx123 Balance INR:{}".format(bal))

def balenq():
    print("Now Ur Account xxxxxx123 Balance INR:{}".format(bal))



























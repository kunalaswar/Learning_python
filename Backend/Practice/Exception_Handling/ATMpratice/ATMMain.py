
from ATMmenu import menu
from ATMOperation import Deposit ,Withdraw,Display
from ATMExcept import DepositError,InSuffFundError,WithdrawError
def main():

    while(True):
        menu()
        ch=int(input("Enter a choice :"))
        match(ch):
            case 1:
                try:
                    Deposit()
                except ValueError:
                    print("Dont Enter a str and Alnum")

                except DepositError:
                    print("Dont Enter a Deposit vlaue at a time ")    


            case 2:
                try:
                    Withdraw()
                except WithdrawError:
                    print("Dont Enter Srt or special symbols at a time")    
                except InSuffFundError:
                    print("YOU DONT HAVE ENIF MONEY PLEASE READ PYTHON NOTE")    

            case 3:
                # try:
                    Display() 
                # except value:
                    # print()    
            case 4:
                print("TNX for using this application ")
                break
            case _ :
                print("Dont Enter a invlaid input")    

main()     

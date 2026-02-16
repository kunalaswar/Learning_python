from ATMmenu import menu
from ATMOperations import deposit ,withdraw,balenq
from ATMExcept import DepositError,InSuffFundError,WithdrawError
while (True):
def main():
            
        try:
                
            menu()
            try:
                ch=int(input("Enter a choice number :"))
                match(ch):
                    case 1:
                        try:
                            deposit()
                        except ValueError:
                            print("Dont Enter a STR or SYMBOLS ")
                        except DepositError:
                            print("Dont Enter Negative value Deposit TIME ")        

                    case 2:
                        try:
                            withdraw()
                        except ValueError: #^ String sathi aahe
                            print("Dont Enter a STR or SYMBOLS ")    
                        except WithdrawError: #^Withdraw time Not enter Zero
                            print("Dont Enter Negative Withdraw TIME ")    
                        except InSuffFundError:
                        print("Ur Account xxxxxx123 does not have Suff Funds--Read Python Notes")  
                    case 3:
                        # try:
                            balenq()
                        # except:
                            # print("Dont Enter ")    
                    case 4:
                        print("Tnx for using this Application")
                        break
                    case _:
                        print("Invalid input please input correct choice")    
                    
            except ValueError:
                print("Dont Enter alnum symbols ENTER A PROPER CHOICE ")
        except valueError:
            print("Enter proper CHOICE")

main()
from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount

def main():

    account1 = CheckingAccount("Lily Farris", 300, 200, 120, 499, 123)

    #Test transfer above transfer limit
    account1.transfer_money(500)
    #Works Correctly

    #Test transfer below minimum balance
    account1.transfer_money(110)
    #Works correctly

    #Test successful transfer
    account1.transfer_money(60)
    #Works correctly

main()
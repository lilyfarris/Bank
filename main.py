from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount

def main():

    account1 = CheckingAccount("Lily Farris", 300, 200, 60, 499, 123)

    #Test transfer above transfer limit
    account1.transfer_money(500)
    #Works Correctly

main()
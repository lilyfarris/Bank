from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount

def main():

    checking_account1 = CheckingAccount("Lily Farris", 300, 200, 120, 499, 123)

    #Test transfer above transfer limit
    checking_account1.transfer_money(500)
    #Works Correctly

    #Test transfer below minimum balance
    checking_account1.transfer_money(110)
    #Works correctly

    #Test successful transfer
    checking_account1.transfer_money(60)
    print(checking_account1.current_balance)
    #Works correctly

    checking_account2 = CheckingAccount("Jane Doe", 800, 300, 150, 888, 456)

    #Test withdraw
    checking_account2.withdraw(100)
    print(checking_account2.current_balance)
    #Works Correctly

    #Test transfer after withdrawing
    checking_account2.transfer_money(100)
    print(checking_account2.current_balance)
    #Works correctly

    savings_account1 = SavingsAccount("John Doe", 1000, 400, 0.05, 777, 999)

    #Test interest earned
    savings_account1.interest_earned()
    print(savings_account1.current_balance)
    #Works correctly

    savings_account2 = SavingsAccount("Joe Doe", 2000, 500, 0.03, 333, 222)

    #Test interest earned after depositing
    savings_account2.deposit(500)
    savings_account2.interest_earned()
    print(savings_account2.current_balance)
    #Works correctly



main()
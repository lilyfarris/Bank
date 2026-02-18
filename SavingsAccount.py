from BankAccount import BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest = interest




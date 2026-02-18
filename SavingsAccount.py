from BankAccount import BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest = interest


    def interest_earned(self):
        self.current_balance += self.current_balance * self.interest

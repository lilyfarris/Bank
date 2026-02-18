from BankAccount import BankAccount
class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit, account_number, routing_number):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer_money(self, amount_to_transfer):
        if amount_to_transfer >= self.transfer_limit:
            print("This is above your transfer limit")
        elif self.current_balance - amount_to_transfer < self.minimum_balance:
            print("This is below your minimum balance")
        else:
            self.current_balance -= amount_to_transfer
            print("Transfer successful")
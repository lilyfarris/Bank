class BankAccount:
    title_of_bank = "Wells Fargo"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount_to_deposit):
        self.current_balance += amount_to_deposit

    def withdraw(self, amount_to_withdraw):
        if(self.current_balance - amount_to_withdraw < self.minimum_balance):
            print("You do not have enough money in this account to withdraw that amount.")
        else:
            self.current_balance -= amount_to_withdraw

    def print_customer_information(self):
        print(self.title_of_bank)
        print(self.customer_name)
        print(self.current_balance)
        print(self.minimum_balance)


account1 = BankAccount("Lily", 500, 400)
account1.deposit(100)
print(account1.current_balance)
account1.withdraw(200)
print(account1.current_balance)
account1.print_customer_information()

account2 = BankAccount("Anna", 1000, 400)
account2.deposit(100)
print(account1.current_balance)
account2.withdraw(200)
print(account1.current_balance)
account2.print_customer_information()


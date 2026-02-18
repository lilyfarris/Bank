class BankAccount:
    title_of_bank = "Wells Fargo"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number

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



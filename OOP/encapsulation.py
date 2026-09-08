# Example of Encapsulation

class Account:

    def __init__(self, balance, accNo):
        # Private data
        self.__balance = balance
        self.__accNo = accNo

    # Method to withdraw money
    def debit(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Debited:", amount)

    # Method to add money
    def credit(self, amount):
        self.__balance += amount
        print("Credited:", amount)

    # Method to show balance
    def show_balance(self):
        print("Current balance:", self.__balance)


# Create object
acc1 = Account(1000, 12345)

# Access data through methods
acc1.debit(500)
acc1.credit(200)
acc1.show_balance()
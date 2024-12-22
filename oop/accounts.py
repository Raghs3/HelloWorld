import datetime
import pytz


class Account:
    """Simple account class with balance"""

    def __init__(self, name, balance):  # technically constructor is __new__
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("The amount must be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))


if __name__ == '__main__':
    raghs3 = Account("Raghs3", 0)
    raghs3.show_balance()

    raghs3.deposit(1000)
    # raghs3.show_balance()
    raghs3.withdraw(500)
    # raghs3.show_balance()

    raghs3.withdraw(10000)

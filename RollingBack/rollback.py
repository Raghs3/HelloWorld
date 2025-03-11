import sqlite3

db = sqlite3.connect('accounts.sqlite')
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL")


class Account(object):

    def __init__(self, name: str, opening_balance: int = 0):
        self.name = name
        self._balance = opening_balance
        print(f"Account created for {self.name}", end='')
        self.show_balance()

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._balance += amount
            print(f"{amount/100:.2f} deposited")
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{amount/100:.2f} withdrawn")  # working in cents and pennies instead of dollars or pounds
            return amount / 100
        else:
            print("The amount must be greater than zero and no more than your account balance")
            return 0.0

    def show_balance(self):
        print(f"Balance on account {self.name} is {self._balance/100:.2f}")


if __name__ == "__main__":
    john = Account("John")
    john.deposit(1010)  # now using integers instead of float (pennies and cents)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)  # when working with float we encounter rounding errors and so exact value doesn't show (instead of 10 we get 9.999998)
    john.withdraw(0)  # recurring or some types of issue, lose accuracy with every 0.1
    john.show_balance()  # we can use decimal class (not teaching here) (code in rollback2 though won't understand)

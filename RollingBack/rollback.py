class Account(object):

    def __init__(self, name: str, opening_balance: float = 0.0):
        self.name = name
        self._balance = opening_balance
        print(f"Account created for {self.name}", end='')
        self.show_balance()

    def deposit(self, amount: float) -> float:
        if amount > 0.0:
            self._balance += amount
            print(f"{amount} deposited")
        return self._balance

    def withdraw(self, amount: float) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withdrawn")
            return amount
        else:
            print("The amount must be greater than zero and no more than your account balance")
            return 0.0

    def show_balance(self):
        print(f"Balance on account {self.name} is {self._balance}")


if __name__ == "__main__":
    john = Account("John")
    john.deposit(10.10)
    john.deposit(0.10)
    john.deposit(0.10)
    john.withdraw(0.30)  # when working with float we encounter rounding errors and so exact value doesn't show (instead of 10 we get 9.999998)
    john.withdraw(0)  # recurring or some types of issue, lose accuracy with every 0.1
    john.show_balance()  # we can use decimal class (not teaching here) (code in rollback2 though won't understand)

import datetime


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.now(datetime.UTC)
        return utc_time

    def __init__(self, name, balance):  # technically constructor is __new__
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            # print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))
            print(f"{amount:6} {tran_type} on {date} (local time was {date.astimezone()})")


if __name__ == '__main__':
    raghs3 = Account("Raghs3", 0)
    raghs3.show_balance()

    raghs3.deposit(1000)   # client is whoever uses the class
    # raghs3.show_balance()
    raghs3.withdraw(500)
    # raghs3.show_balance()

    raghs3.withdraw(10000)

    raghs3.show_transaction()

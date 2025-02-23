class Account(object):

    def __init__(self, name: str, opening_balance: float = 0.0):
        self.name = name
        self.balance = opening_balance
        print(f"Account created for {self.name}", end="")
        self.show_balance()

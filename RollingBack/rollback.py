import datetime
import sqlite3

db = sqlite3.connect('accounts.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)  # challenge, save local timezone to the db too
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")  # sqlite commands
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL,"
           " account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))")
# primary keys have to be unique so error when tried creating second Terry in accounts table
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS"
           " SELECT strftime('%d-%m-%Y %H:%M:%f', history.time, 'localtime') AS localtime,"
           " history.account, history.amount FROM history ORDER BY history.time")  # created a view, of local time

class Account(object):

    @staticmethod
    def _current_time():  # dunno if self is req in brackets or not
        # return datetime.datetime.now(datetime.timezone.utc)
        return 1  # integrity error as primary key must be unique

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row is not None:  # can be `if row:` as well
            self.name, self._balance = row  # unpacking tuple if row is found
            print(f"Retrieved record for {self.name}. ", end='')
        else:  # if row not found
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()  # as inserting something, have to commit the change
            print(f"Account created for {self.name}. ", end='')
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Account._current_time()

        try:  # limit code in try
            db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            db.execute("INSERT INTO history VALUES (?, ?, ?)", (deposit_time, self.name, amount))
        except sqlite3.Error:
            db.rollback()
        else:
            self._balance = new_balance  # had to put in else, otherwise output didn't match database
        finally:  # commit should be in else, as otherwise there is nothing to commit
            db.commit()  # error occurs before this so now putting in try block to avoid crashes

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            # new_balance = self._balance + amount
            # deposit_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES (?, ?, ?)", (deposit_time, self.name, amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(amount)
            print(f"{amount/100:.2f} deposited")
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            # new_balance = self._balance - amount
            # withdrawal_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES (?, ?, ?)", (withdrawal_time, self.name, -amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(-amount)
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

    terry = Account("TerryJ")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)
    michael = Account("Michael")
    terryG = Account("TerryG")

    db.close()

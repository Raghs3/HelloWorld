import sqlite3
from datetime import datetime, timezone
import pickle


def convert_datetime(val):
    """Convert ISO 8601 datetime to datetime.datetime object."""
    return datetime.fromisoformat(val.decode())  # iso format req to use astimezone() method


def adapt_datetime_iso(val):
    """Adapt datetime.date to ISO 8601 date."""
    return val.isoformat()


sqlite3.register_adapter(datetime, adapt_datetime_iso)
sqlite3.register_converter("datetime", convert_datetime)

db = sqlite3.connect("accounts_iso.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute(
    "CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute(
    "CREATE TABLE IF NOT EXISTS history (time datetime NOT NULL, account TEXT NOT NULL,"
    " amount INTEGER NOT NULL, PRIMARY KEY (time, account))")
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS"
           " SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
           " history.account, history.amount FROM history ORDER BY history.time")


class Account(object):

    @staticmethod
    def _current_time():
        utc_time = datetime.now(timezone.utc)
        local_time = utc_time.astimezone()
        zone = local_time.tzinfo
        return utc_time, zone

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)",
                            (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}. ".format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {}. ".format(self.name), end='')
        self.show_balance()

    def _save_update_details(self, amount):
        new_balance = self._balance + amount
        deposit_time, zone = Account._current_time()
        local_time = deposit_time.astimezone(
            tz=zone
            # Store this if the actual zone isn't important and you only need the offset.
        )
        pickled_zone = pickle.dumps(zone)

        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)",
                   (new_balance, self.name))
        db.execute(
            "INSERT INTO history VALUES(?, ?, ?)",
            (
                deposit_time,
                self.name,
                amount
            )
        )
        db.commit()
        self._balance = new_balance

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._save_update_details(amount)
            print("{:.2f} deposited".format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._save_update_details(-amount)
            print("{:.2f} withdrawn".format(amount / 100))
            return amount / 100
        else:
            print(
                "The amount must be greater than zero and no more than your account balance")
            return 0.0

    def show_balance(self):
        print("Balance on account {} is {:.2f}".format(self.name, self._balance / 100))


if __name__ == '__main__':
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.show_balance()

    terry = Account("TerryJ")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 700)
    michael = Account("Michael")
    terryG = Account("TerryG")

    # Check what's been stored.
    for record in db.execute('SELECT time, account, amount FROM history;'):
        transaction_time, account, amount = record  # unpack the row fields
        print(f'UTC = {transaction_time}, local time = {transaction_time.astimezone()}, {account=}, {amount=}')
    db.close()


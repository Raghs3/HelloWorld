import sqlite3
# import pytz

# tim old
db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)  # using detect_types makes it so the item is datetime.datetime

for row in db.execute("SELECT strftime('%d-%m-%Y %H:%M:%f', history.time, 'localtime') AS localtime,"
                      " history.account, history.amount FROM history ORDER BY history.time"):  # ("SELECT * FROM history"): # doing this we realised our time is in str
    print(row)

db.close()  # remember to close the connection!

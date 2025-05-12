import sqlite3
import pytz
import pickle

# tim old
db = sqlite3.connect("accounts_tz.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)  # using detect_types makes it so the item is datetime.datetime
# didn't use the datetime function of SQLite as it truncates the second part, SQLite fns in general have accuracy of only 3 decimals
# for row in db.execute("SELECT strftime('%d-%m-%Y %H:%M:%f', history.time, 'localtime') AS localtime,"  # first, output format, second, input, third, timezone
#                       " history.account, history.amount FROM history ORDER BY history.time"):  # ("SELECT * FROM history"): # doing this we realised our time is in str
for row in db.execute("SELECT * FROM history"):
    # print(row)  # that's why used ORDER BY from time column in table to make use of python's precision
    utc_time = row[0]
    pickled_zone = row[3]
    zone = pickle.loads(pickled_zone)
    local_time = pytz.utc.localize(utc_time).astimezone(zone)
    print(f"{utc_time}\t{local_time}\t{local_time.tzinfo}")

db.close()  # remember to close the connection!

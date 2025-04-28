import sqlite3
import pytz

# tim old
db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)  # using detect_types makes it so item is datetime.datetime

for row in db.execute("SELECT * FROM history"):  # doing this we realised our time is in str
    utc_time = row[0]
    local_time = pytz.utc.localize(utc_time).astimezone()  # i'll just use pytz and move on for now ;-;
    print(f"{utc_time}\t{local_time}")  # time is in string datatype

db.close()  # remember to close the connection!

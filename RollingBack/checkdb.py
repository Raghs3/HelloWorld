import sqlite3


db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)  # using detect_types makes it so item is datetime.datetime

for row in db.execute("SELECT * FROM history"):  # doing this we realised our time is in str
    # print(row)
    local_time = row[0]
    print(f"{local_time}\t{type(local_time)}")  # time is in string datatype

db.close()  # remember to close the connection!

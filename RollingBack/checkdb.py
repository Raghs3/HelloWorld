import sqlite3


db = sqlite3.connect("accounts.sqlite")

for row in db.execute("SELECT * FROM history"):
    # print(row)
    local_time = row[0]
    print(f"{local_time}\t{type(local_time)}")  # time is in string datatype
db.close()

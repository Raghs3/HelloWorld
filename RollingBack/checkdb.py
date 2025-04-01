import sqlite3


db = sqlite3.connect("accounts.sqlite")

for row in db.execute("SELECT * FROM history"):  # doing this we realised our time is in str
    # print(row)
    local_time = row[0]
    print(f"{local_time}\t{type(local_time)}")  # time is in string datatype

db.close()

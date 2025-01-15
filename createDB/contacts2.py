import sqlite3

db = sqlite3.connect("contacts.sqlite")
# prints nothing as there is nothing in the db as we didn't commit when inserting data in previous script
for row in db.execute("SELECT * FROM contacts"):  # all data inserted is rolled back when db closed
    print(row)

db.close()

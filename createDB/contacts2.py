import sqlite3
# sqlite wraps insertions and deletions in transaction so entire transaction can be roll backed
db = sqlite3.connect("contacts.sqlite")

for row in db.execute("SELECT * FROM contacts"):  # all data inserted is rolled back when db closed
    print(row)
# prints nothing as there is nothing in the db as we didn't commit when inserting data in previous script
db.close()

import sqlite3
# sqlite wraps insertions and deletions in transaction so entire transaction can be roll backed
db = sqlite3.connect("contacts.sqlite")

for name, phone, email in db.execute("SELECT * FROM contacts"):  # shortcut instead of cursor
    print(name)  # all data inserted is rolled back when db closed unless committed
    print(phone)
    print(email)
    print('-' * 20)
# prints nothing as there is nothing in the db as we didn't commit when inserting data in previous script (now committed)
db.close()

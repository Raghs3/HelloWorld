import sqlite3
# sqlite wraps insertions and deletions in transaction so entire transaction can be roll backed
db = sqlite3.connect("contacts.sqlite")

new_email = "newemail@update.com"
phone = input("Please enter the phone number ")

update_sql = f"UPDATE contacts SET email = '{new_email}' WHERE contacts.phone = {phone}"
print(update_sql)

update_cursor = db.cursor()
update_cursor.executescript(update_sql)  # executescript doesn't set rowcount property
print(f"{update_cursor.rowcount} rows updated")

print()
print(f"Are connections the same: {update_cursor.connection == db}")
print()

update_cursor.connection.commit()  # suggested to commit using cursor rather than db
update_cursor.close()  # remember to close cursor

for name, phone, email in db.execute("SELECT * FROM contacts"):  # shortcut instead of cursor
    print(name)  # all data inserted is rolled back when db closed unless committed
    print(phone)
    print(email)
    print('-' * 20)
# prints nothing as there is nothing in the db as we didn't commit when inserting data in previous script (now committed)
db.close()

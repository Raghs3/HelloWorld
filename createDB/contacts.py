import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6545678, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@myemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())  # returns a list of tuples of rows

print(cursor.fetchone())  # returns next row in cursor
print(cursor.fetchone())
print(cursor.fetchone())  # None as no more rows

for name, phone, email in cursor:  # after fetching no more values left in cursor (it is a generator)
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()
db.commit()  # this time data has been committed
db.close()

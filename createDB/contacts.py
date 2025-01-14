import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE contacts(name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6545678, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@myemail.com')")

db.close()

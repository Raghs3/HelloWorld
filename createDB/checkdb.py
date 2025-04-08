import sqlite3

conn = sqlite3.connect('contacts.sqlite')

name = input("Please enter a name to search for: ")

# for row in conn.execute("SELECT * FROM contacts WHERE contacts.name = ?", (name,)):  # sqlite_master gives everything
for row in conn.execute("SELECT * FROM contacts WHERE contacts.name LIKE ?", (name,)):  # not case-sensitive
    print(row)

conn.close()
# closing database
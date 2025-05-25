import sqlite3

conn = sqlite3.connect('music.db',)

for x in conn.execute("SELECT albums.name FROM albums WHERE albums.artist = ? ORDER BY albums.name", (196,)):
    print(x)

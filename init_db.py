import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO jobs (title, content) VALUES (?, ?)",
            ('First Job', 'Content for the first job')
            )

cur.execute("INSERT INTO jobs (title, content) VALUES (?, ?)",
            ('Second Job', 'Content for the second job')
            )

connection.commit()
connection.close()
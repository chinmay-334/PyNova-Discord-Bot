import datetime
import sqlite3
conn = sqlite3.connect('bank.db')
db = conn.cursor()

# db.execute("DROP TABLE IF EXIST Student")

print("Opened database successfully\n")

db.execute('''CREATE TABLE DANKMEMER
(username INT NOT NULL,
coins INT NOT NULL,
date TIMESTAMP
);''')

print("Table created successfully\n")
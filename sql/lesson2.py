import sqlite3
from pathlib import Path

path_db = Path('sql', "server2.db")
with sqlite3.connect(path_db) as db:
    cursor = db.cursor()

    # cursor.execute("""CREATE TABLE articles(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     author VARCHAR,
    #     topic VARCHAR,
    #     content TEXT
    # )""")

    # values = [
    #     ("Флипик", "Asdfgh", "dsjajagresxz"),
    #     ("zxcvb", "vbnmnm", "mnbvcx"),
    #     ("qwerrt", "yuyiyt", "trewq ")
    # ]

    # cursor.executemany("INSERT INTO articles(author, topic, content) VALUES(?,?,?)", values)

    # cursor.execute("SELECT * FROM articles")
    # print(cursor.__next__())
    # print(cursor.fetchone())
    # print(cursor.fetchall())
    # print(cursor.fetchmany(2))
    # for data in cursor.execute("SELECT * FROM articles"):
    #     print(data)
        
    cursor.execute("""CREATE TABLE email(
        `from` VARCHAR,
        subject VARCHAR,
        content TEXT
    )""")

    cursor.execute("INSERT INTO email VALUES('qwer', 'asdf', 'zxcv')")

    cursor.execute("SELECT `from` FROM email")
    print(cursor.fetchone()[0])
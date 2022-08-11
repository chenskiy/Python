from package.registration import registration
import sqlite3
from pathlib import Path

path_db = Path('Homework','HM8','folder','sql.db')
with sqlite3.connect(path_db) as db:
    cursor = db.cursor()
    qwert = """
    CREATE TABLE IF NOT EXISTS directory(
        id INTEGER PRIMARY KEY,
        name VARCHAR(30),
        surname VARCHAR(30),
        sex VARCHAR(1),
        number INTEGER(12)
    )
    """
    cursor.executescript(qwert)
registration()
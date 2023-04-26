import sqlite3
# from .create import path_db
from .logger import data_logger
from pathlib import Path

path_db = Path('Homework','HM8','folder','sql.db')
def registration():
    name = input('name: ')
    surname = input('surname: ')
    sex = input('sex: ')
    number = int(input('number: '))
    
    try:
        db = sqlite3.connect(path_db)
        cursor = db.cursor()

        cursor.execute("SELECT number FROM directory WHERE number = ?", [number])
        if cursor.fetchone() is None:
            values = [name, surname, sex, number]
            cursor.execute("INSERT INTO directory(name, surname, sex, number) VALUES(?,?,?,?)", values)
            print('Добавлен новый контакт')
            data_logger(name, surname, sex, number)
            db.commit()
        else:
            print('Такой номер уже существует!')
            registration()
    except sqlite3.Error as e:
        print('Error', e)
    finally:
        cursor.close()
        db.close()
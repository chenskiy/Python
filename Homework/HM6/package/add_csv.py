import csv
from pathlib import Path
from package.logger import data_logger

def add_csv():
    path_add = Path("HM6", "classmates.csv")
    yn = input('Хотите добавить данные?(Y/N) ')
    if yn == 'Y':
        # hum = int(input('Сколько человек? '))
        with open(path_add, mode="a", encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
            # file_writer.writerow('')
            # for i in range(hum):
            x = input('Введите фамилию: ')
            y = input('Введите номер: ')
            z = input('Введите город: ')
            file_writer.writerow([x, y, z]) 
            data_logger(x, y, z)
    return yn
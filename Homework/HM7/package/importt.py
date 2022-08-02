import csv
from pathlib import Path


def improt_csv(x):
    ls = []
    path_import = Path("HM6", "classmates.csv")
    with open(path_import, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        count = 0
        for row in file_reader:
            if count == 0:
                ls.append(f'The file contains columns: {",".join(row)}')
            else:
                ls.append(f'{",".join(row)}')
            count += 1
    ls = list(map(str, ls))
    if x == 0: return ls
    if x == 1: return count


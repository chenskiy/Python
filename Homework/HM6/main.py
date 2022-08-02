from package.export import export_xml
from package.add_csv import add_csv

while True:
    add = add_csv()
    if add == 'Y':
        a = input('Добавить след:(Y/N) ')
        if not a == 'Y': break
    else: break

export_xml()
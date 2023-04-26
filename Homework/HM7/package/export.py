from package.importt import improt_csv
from pathlib import Path


def export_xml():
    ls = improt_csv(0)
    count = improt_csv(1)
    xml = '<xml>\n '
    for i in range(count):
        xml += f'{ls[i]}\n'
    
    xml += '</xml>'
    path_export = Path("HM7", "export.xml")
    with open(path_export, 'w') as w_file:
        w_file.write(xml)
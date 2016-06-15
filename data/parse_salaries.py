__author__ = 'laila'


import csv
import json


with open('raw_salario.txt') as f:
    reader = csv.reader(f, dialect='excel-tab')
    dic = {}
    r = next(reader)
    r = next(reader)
    for row in reader:
        dic[row[0]] = int(row[4])
    with open('parsed_salaries', 'w') as f1:
        json.dump(dic, f1, sort_keys=True, indent=4,ensure_ascii=False)
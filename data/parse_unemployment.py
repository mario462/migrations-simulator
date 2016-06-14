__author__ = 'laila'


import csv
import json


with open('unemployment.txt') as f:
    reader = csv.reader(f, dialect='excel-tab')
    dic = {}
    for row in reader:
        dic[row[0]] = float(row[1])
    with open('parsed_unemployment', 'w') as f1:
        json.dump(dic, f1, sort_keys=True, indent=4,ensure_ascii=False)
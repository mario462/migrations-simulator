__author__ = 'laila'


import csv
import json


with open('raw_extension.txt') as f:
    reader = csv.reader(f, dialect='excel-tab')
    dic = {}
    for row in reader:
        dic[row[0]] = float(row[1])
    with open('parsed_extension', 'w') as f1:
        json.dump(dic, f1, sort_keys=True, indent=4,ensure_ascii=False)


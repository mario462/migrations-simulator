__author__ = 'jose'

import pprint
import json

f = open("paises.txt")
lines = f.readlines()
dict = {}
country, coord = "", ""

for i in range(len(lines)):
    line = lines[i]
    if i % 3 == 1:
        country = line
    elif i % 3 == 2:
        coord = line
        arr_coord = coord[1:-2:1].split(',')
        dict[country[0:-1:1]] = [float(x) for x in arr_coord]

# json_result = json.dumps(dict)
d = open("parsed_countries", mode='w')
json.dump(dict, d, sort_keys=True, indent=4, ensure_ascii=False)
# d.write(json_result)
# pprint.pprint(dict)
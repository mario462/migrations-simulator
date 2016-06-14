# -*- coding: latin-1 -*-
__author__ = 'mario'

import json
import pprint

order = ['Total', 'Pinar del Río', 'Artemisa', 'La Habana', 'Mayabeque', 'Matanzas',
         'Villa Clara', 'Cienfuegos', 'Sancti Spíritus', 'Ciego de Ávila', 'Camagüey',
         'Las Tunas', 'Holguín', 'Granma', 'Santiago', 'Guantánamo', 'Isla de la Juventud']

mapping = {}

f = open('censo', 'r', encoding='latin-1')
lines = f.readlines()
i = 0
while i < len(lines) - 17:
    key = lines[i].encode('latin-1').decode('latin-1').replace('\n', '')
    if key not in mapping:
        mapping[key] = {}
        for j in range(1, 18):
            value = lines[i + j].replace(' ', '').replace('\n','')
            other = order[j-1]
            mapping[key][other] = value
    i += 18
dumped = json.dumps(mapping, sort_keys=True, indent=4, ensure_ascii=False)
pprint.pprint(dumped)
g = open('parsed', 'wt')
g.write(dumped)
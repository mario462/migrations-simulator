# -*- coding: latin-1 -*-
__author__ = 'mario'

import json
import pprint

order = ['Total', 'Pinar del Río', 'Artemisa', 'La Habana', 'Mayabeque', 'Matanzas',
         'Villa Clara', 'Cienfuegos', 'Sancti Spíritus', 'Ciego de Ávila', 'Camagüey',
         'Las Tunas', 'Holguín', 'Granma', 'Santiago de Cuba', 'Guantánamo', 'Isla de la Juventud']

mapping = {}

f = open('raw_living_places.txt', 'r', encoding='latin-1')
lines = f.readlines()
i = 0
while i < len(lines) - 17:
    key = lines[i].replace('\n', '')
    if key not in mapping:
        mapping[key] = {}
        for j in range(1, 18):
            value = lines[i + j].replace(' ', '').replace('\n','')
            other = order[j-1]
            mapping[key][other] = int(value)
    i += 18
g = open('parsed_living_places', 'wt')
dumped = json.dump(mapping, g, sort_keys=True, indent=4, ensure_ascii=False)

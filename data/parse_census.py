# -*- coding: latin-1 -*-
__author__ = 'mario'

import json
import pprint

order = ['Total', 'Pinar del R�o', 'Artemisa', 'La Habana', 'Mayabeque', 'Matanzas',
         'Villa Clara', 'Cienfuegos', 'Sancti Sp�ritus', 'Ciego de �vila', 'Camag�ey',
         'Las Tunas', 'Holgu�n', 'Granma', 'Santiago', 'Guant�namo', 'Isla de la Juventud']

mapping = {}

f = open('data/censo', 'r', encoding='latin-1')
lines = f.readlines()
i = 0
while i < len(lines) - 17:
    key = lines[i].encode('latin-1').decode('latin-1').replace('\n', '')
    if key not in mapping:
        mapping[key] = {}
        for j in range(1, 18):
            value = lines[i + j].replace(' ', '').replace('\n','')
            other = order[j-1]
            mapping[key][other] = int(value)
    i += 18
g = open('data/parsed_living_places', 'wt')
dumped = json.dump(mapping, g, sort_keys=True, indent=4, ensure_ascii=False)

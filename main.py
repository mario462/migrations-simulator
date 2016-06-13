__author__ = 'mario'

import json

if __name__ == '__main__':
    loaded = json.load(open('parsed'))
    print(loaded['Artemisa'])
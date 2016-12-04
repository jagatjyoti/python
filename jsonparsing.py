#! /usr/bin/python3.5

import json
from pprint import pprint

with open('gtt.json') as gttval:
    data = json.load(gttval)

pprint(data['limits']['standstill'])

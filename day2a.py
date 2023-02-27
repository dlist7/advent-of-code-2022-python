#!/usr/bin/env python3

import fileinput

scores = {
    'AX': 4,
    'AY': 8,
    'AZ': 3,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 7,
    'CY': 2,
    'CZ': 6,
}

total = 0
for line in fileinput.input():
    total += scores[line[0]+line[2]]

print(total)

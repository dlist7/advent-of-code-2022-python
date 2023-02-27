#!/usr/bin/env python3

import fileinput

scores = {
    'AX': 3,
    'AY': 4,
    'AZ': 8,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 2,
    'CY': 6,
    'CZ': 7,
}

total = 0
for line in fileinput.input():
    total += scores[line[0]+line[2]]

print(total)

#!/usr/bin/env python3

import fileinput
from day3a import get_priority

total_priority = 0
for i,line in enumerate(fileinput.input()):
    if i%3 == 0:
        pack1 = line
    elif i%3 == 1:
        pack2 = line
    else:
        for c in line:
            if c in pack1 and c in pack2:
                total_priority += get_priority(c)
                break

print(total_priority)

#!/usr/bin/env python3

import fileinput
import re

cal_list = []

cal = 0
for line in fileinput.input():
    match = re.match('(\d+)', line)
    if match:
        cal += int(match.group(1))
    else:
        cal_list.append(cal)
        cal = 0

# Get the last elf.
cal_list.append(cal)

cal_list.sort(reverse=True)
print(sum(cal_list[0:3]))

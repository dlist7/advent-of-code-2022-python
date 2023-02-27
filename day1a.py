#!/usr/bin/env python3

import fileinput
import re

max_cal = 0

cal = 0
for line in fileinput.input():
    match = re.match('(\d+)', line)
    if match:
        cal += int(match.group(1))
    else:
        max_cal = max(cal, max_cal)
        cal = 0

# Get the last elf.
max_cal = max(cal, max_cal)

print(max_cal)

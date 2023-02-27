#!/usr/bin/env python3

import fileinput
import re

def main():
    total = 0
    for line in fileinput.input():
        match = re.match('(\d+)-(\d+),(\d+)-(\d+)', line)
        if match:
            a0 = int(match.group(1))
            a1 = int(match.group(2))
            b0 = int(match.group(3))
            b1 = int(match.group(4))
            if (a0 <= b0 <= a1) or (a0 <= b1 <= a1) or (b0 <= a0 <= b1):
                total += 1
    print(total)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import fileinput
import re

x = []

def main():
    x.append(1)

    for line in fileinput.input():
        match = re.match('(addx|noop) ?(-?\d+)?', line)
        if match.group(1) == 'addx':
            n = int(match.group(2))
            x.append(x[-1])
            x.append(x[-1] + n)
        elif match.group(1) == 'noop':
            x.append(x[-1])

    for i in range(0,240):
        if abs(x[i] - i%40) <= 1:
            print('#', end='')
        else:
            print('.', end='')
        if (i+1)%40 == 0:
            print()

if __name__ == '__main__':
    main()

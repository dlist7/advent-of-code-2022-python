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
    print(20*x[19] + 60*x[59] + 100*x[99] + 140*x[139] + 180*x[179] + 220*x[219])

if __name__ == '__main__':
    main()

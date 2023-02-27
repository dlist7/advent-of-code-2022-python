#!/usr/bin/env python3

import fileinput
import re

crates = {}

def setup_crates(line):
    n_stacks = len(line)//4
    for i in range(0, n_stacks):
        crate = line[4*i+1]
        if crate.isalpha():
            stack = str(i + 1)
            if crates.get(stack) is None:
                crates[stack] = []
            crates[stack].insert(0, crate)

def move_crates(n, f, t):
    crates[t] += crates[f][-n:]
    crates[f][-n:] = []

def main():

    for line in fileinput.input():
        match = re.search('\[\w]', line)
        if match:
            setup_crates(line)
        match = re.match('move (\d+) from (\d+) to (\d+)', line)
        if match:
            n = int(match.group(1))
            f = match.group(2)
            t = match.group(3)
            move_crates(n, f, t)

    for key in sorted(crates.keys()):
        print(crates[key][-1], end='')
    print()

if __name__ == '__main__':
    main()

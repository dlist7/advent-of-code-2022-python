#!/usr/bin/env python3

import fileinput
import math
import re

def main():
    dirs = {}
    cwd = []
    for line in fileinput.input():
        match = re.match('\$ cd /', line)
        if match:
            cwd.append('')
            dirs[''] = 0
            continue
        match = re.match('\$ cd \.\.', line)
        if match:
            cwd.pop()
            continue
        match = re.match('\$ cd (\w+)', line)
        if match:
            cwd.append(match.group(1))
            dirs['/'.join(cwd)] = 0
            continue
        match = re.match('(\d+) .*', line)
        if match:
            size = int(match.group(1))
            for i in range(0, len(cwd)):
                dirs['/'.join(cwd[0:i+1])] += size
            continue
    
    min_s = math.inf
    for s in dirs.values():
        if s + 70000000 - dirs[''] > 30000000:
            min_s = min(min_s, s)
    print(min_s)

if __name__ == '__main__':
    main()

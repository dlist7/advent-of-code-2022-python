#!/usr/bin/env python3

import fileinput
import re

def get_map(blizzards):
    blizzard_map = {}
    for blizzard in blizzards.values():
        p = (blizzard['row'],blizzard['col'])
        if blizzard_map.get(p):
            blizzard_map[p] += 1
        else:
            blizzard_map[p] = 1
    return blizzard_map

def print_map(blizzards, start, finish, rows, cols):
    blizzard_map = get_map(blizzards)
    for i in range(0,rows):
        for j in range(0,cols):
            if i == 0:
                if (i,j) == start:
                    print('.', end='')
                else:
                    print('#', end='')
            elif i == rows - 1:
                if (i,j) == finish:
                    print('.', end='')
                else:
                    print('#', end='')
            elif j == 0 or j == cols - 1:
                    print('#', end='')
            else:
                if not blizzard_map.get((i,j)):
                    print('.', end='')
                else:
                    print('x', end='')
        print('')


def advance(blizzards, rows, cols):
    for k,v in blizzards.items():
        if v['direction'] == '^':
            v['row'] -= 1
            if v['row'] < 1:
                v['row'] = rows - 2
        if v['direction'] == '>':
            v['col'] += 1
            if v['col'] > cols - 2:
                v['col'] = 1
        if v['direction'] == 'v':
            v['row'] += 1
            if v['row'] > rows - 2:
                v['row'] = 1
        if v['direction'] == '<':
            v['col'] -= 1
            if v['col'] < 1:
                v['col'] = cols - 2
    return get_map(blizzards)

def main():

    start = None
    finish = None
    rows = None
    cols = None

    blizzards = {}
    blizzard_id = 0
    for i,line in enumerate(fileinput.input()):
        match = re.match('(#+)\.(#+)', line)
        if match:
            if not start:
                start = (i,len(match.group(1)))
            else:
                finish = (i,len(match.group(1)))
        else:
            for j,c in enumerate(line.rstrip()):
                if c in {'^','>','v','<'}:
                    blizzard_id += 1
                    blizzards[blizzard_id] = {'row':i,'col':j,'direction':c}
    rows = i + 1
    cols = len(line) - 1

    paths = [[start]]
    done = False
    while not done and len(paths) > 0:
        blizzard_map = advance(blizzards, rows, cols)
        npaths = []
        pset = set()
        for path in paths:
            p = path[-1]
            r,c = p

            # Wait
            if not blizzard_map.get(p) and p not in pset:
                npath = path[:] + [p]
                npaths.append(npath)
                pset.add(p)

            # North
            np = (r-1,c)
            if r - 1 > 0 and not blizzard_map.get(np) and np not in pset:
                npath = path[:] + [np]
                npaths.append(npath)
                pset.add(np)

            # East
            np = (r,c+1)
            if c + 1 < cols - 1 and r > 0 and not blizzard_map.get(np) and np not in pset:
                npath = path[:] + [np]
                npaths.append(npath)
                pset.add(np)

            # South
            np = (r+1,c)
            if np == finish:
                npath = path[:] + [np]
                done = True
                break
            if r + 1 < rows - 1 and not blizzard_map.get(np) and np not in pset:
                npath = path[:] + [np]
                npaths.append(npath)
                pset.add(np)

            # West
            np = (r,c-1)
            if c - 1 > 0 and r > 0 and not blizzard_map.get(np) and np not in pset:
                npath = path[:] + [np]
                npaths.append(npath)
                pset.add(np)

        paths = npaths

    print(len(npath)-1)

if __name__ == '__main__':
    main()

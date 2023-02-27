#!/usr/bin/env python3

import fileinput
import math

def check_north(rcmap, pos):
    return rcmap.get((pos[0]-1,pos[1]-1)) \
        or rcmap.get((pos[0]-1,pos[1])) \
        or rcmap.get((pos[0]-1,pos[1]+1))

def check_south(rcmap, pos):
    return rcmap.get((pos[0]+1,pos[1]-1)) \
        or rcmap.get((pos[0]+1,pos[1])) \
        or rcmap.get((pos[0]+1,pos[1]+1))

def check_west(rcmap, pos):
    return rcmap.get((pos[0]-1,pos[1]-1)) \
        or rcmap.get((pos[0],pos[1]-1)) \
        or rcmap.get((pos[0]+1,pos[1]-1))

def check_east(rcmap, pos):
    return rcmap.get((pos[0]-1,pos[1]+1)) \
        or rcmap.get((pos[0],pos[1]+1)) \
        or rcmap.get((pos[0]+1,pos[1]+1))

def check_all(rcmap, pos):
    return check_north(rcmap, pos) \
        or check_south(rcmap, pos) \
        or check_west(rcmap, pos) \
        or check_east(rcmap, pos)

def print_map(rcmap):
    row_min = math.inf
    row_max = -math.inf
    col_min = math.inf
    col_max = -math.inf

    for key in rcmap.keys():
        row_min = min(row_min, key[0])
        row_max = max(row_max, key[0])
        col_min = min(col_min, key[1])
        col_max = max(col_max, key[1])

    for i in range(row_min, row_max+1):
        for j in range(col_min, col_max+1):
            if rcmap.get((i,j)):
                print('#', end='')
            else:
                print('.', end='')
        print('')

def count_map(rcmap):
    row_min = math.inf
    row_max = -math.inf
    col_min = math.inf
    col_max = -math.inf

    for key in rcmap.keys():
        row_min = min(row_min, key[0])
        row_max = max(row_max, key[0])
        col_min = min(col_min, key[1])
        col_max = max(col_max, key[1])

    count = 0
    for i in range(row_min, row_max+1):
        for j in range(col_min, col_max+1):
            if not rcmap.get((i,j)):
                count += 1
    return count

def main():
    elf_map = {}
    row = 0
    for line in fileinput.input():
        for i,c in enumerate(line):
            if c == '#':
                elf_map[(row,i)] = '#'
        row += 1
    
    rules = [
        (check_north,(-1,0)),
        (check_south,(1,0)),
        (check_west,(0,-1)),
        (check_east,(0,1))
    ]

    round = 0
    while True:
        propose_map = {}
        elf_map2 = {}
        moves = 0

        # Pass 1
        for elf in elf_map.keys():
            if not check_all(elf_map, elf):
                elf_map2[elf] = '#'
                continue
            for rule in rules:
                if not rule[0](elf_map, elf):
                    proposed_move = (elf[0]+rule[1][0], elf[1]+rule[1][1])
                    if propose_map.get(proposed_move):
                        propose_map[proposed_move] += 1
                    else:
                        propose_map[proposed_move] = 1
                    break
        # Pass 2
        for elf in elf_map.keys():
            moved = False
            for rule in rules:
                if not rule[0](elf_map, elf):
                    proposed_move = (elf[0]+rule[1][0], elf[1]+rule[1][1])
                    if propose_map.get(proposed_move) == 1:
                        elf_map2[proposed_move] = '#'
                        moved = True
                        moves += 1
                    break
            if not moved:
                elf_map2[elf] = '#'

        elf_map = elf_map2
        rules = rules[1:] + [rules[0]]
        round += 1

        if moves == 0:
            break

    print(round)

if __name__ == '__main__':
    main()

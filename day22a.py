#!/usr/bin/env python3

import fileinput
import re

def update_facing(facing, turn):
    if turn == 'L':
        if facing == 3:
            return 2
        elif facing == 0:
            return 3
        elif facing == 1:
            return 0
        elif facing == 2:
            return 1
    elif turn == 'R':
        if facing == 3:
            return 0
        elif facing == 0:
            return 1
        elif facing == 1:
            return 2
        elif facing == 2:
            return 3

def update_north(monkey_map, r0, c0, r, c):
    if r > 0:
        if monkey_map[r-1][c] == '.':
            return (r-1,c)
        elif monkey_map[r-1][c] == '#':
            return (r0,c0)
        else:
            return update_north(monkey_map, r0, c0, r-1, c)
    else:
        if monkey_map[len(monkey_map)-1][c] == '.':
            return (len(monkey_map)-1,c)
        elif monkey_map[len(monkey_map)-1][c] == '#':
            return (r0,c0)
        else:
            return update_north(monkey_map, r0, c0, len(monkey_map)-1, c)

def update_east(monkey_map, r0, c0, r, c):
    if c < len(monkey_map[r]) - 1:
        if monkey_map[r][c+1] == '.':
            return (r,c+1)
        elif monkey_map[r][c+1] == '#':
            return (r0,c0)
        else:
            return update_east(monkey_map, r0, c0, r, c+1)
    else:
        if monkey_map[r][0] == '.':
            return (r,0)
        elif monkey_map[r][0] == '#':
            return (r0,c0)
        else:
            return update_east(monkey_map, r0, c0, r, 0)

def update_south(monkey_map, r0, c0, r, c):
    if r < len(monkey_map) - 1:
        if monkey_map[r+1][c] == '.':
            return (r+1,c)
        elif monkey_map[r+1][c] == '#':
            return (r0,c0)
        else:
            return update_south(monkey_map, r0, c0, r+1, c)
    else:
        if monkey_map[0][c] == '.':
            return (0,c)
        elif monkey_map[0][c] == '#':
            return (r0,c0)
        else:
            return update_south(monkey_map, r0, c0, 0, c)

def update_west(monkey_map, r0, c0, r, c):
    if c > 0:
        if monkey_map[r][c-1] == '.':
            return (r,c-1)
        elif monkey_map[r][c-1] == '#':
            return (r0,c0)
        else:
            return update_west(monkey_map, r0, c0, r, c-1)
    else:
        if monkey_map[r][len(monkey_map[r])-1] == '.':
            return (r,len(monkey_map[r])-1)
        elif monkey_map[r][len(monkey_map[r])-1] == '#':
            return (r0,c0)
        else:
            return update_west(monkey_map, r0, c0, r, len(monkey_map[r])-1)

def update_position(monkey_map, facing, row, col, dist):
    r,c = row,col
    for i in range(0, dist):
        if facing == 3:
            r,c = update_north(monkey_map, r, c, r, c)
        elif facing == 0:
            r,c = update_east(monkey_map, r, c, r, c)
        elif facing == 1:
            r,c = update_south(monkey_map, r, c, r, c)
        elif facing == 2:
            r,c = update_west(monkey_map, r, c, r, c)
    return r,c

def main():
    monkey_map = []
    facing = 0
    row = 0
    col = 0
    max_length = 0
    first = True
    for line in fileinput.input():
        if line.find('.') >= 0 or line.find('#') >= 0:
            max_length = max(max_length, len(line) - 1)
            monkey_map.append([])
            for i,c in enumerate(line):
                if c == '.':
                    monkey_map[-1].append('.')
                    if first:
                        col = i
                        first = False
                elif c == '#':
                    monkey_map[-1].append('#')
                else:
                    monkey_map[-1].append(None)
        if line.find('L') >= 0 or line.find('R') >= 0:
            directions = line.rstrip()

    for i in range(0, len(monkey_map)):
        if len(monkey_map[i]) < max_length:
            monkey_map[i] += [None]*(max_length-len(monkey_map[i]))

    i = 0
    while i < len(directions):
        match = re.match('((L|R)|(\d+))', directions[i:])
        if match:
            if m := match.group(2):
                i += len(m)
                facing = update_facing(facing, m)
            elif m := match.group(3):
                i += len(m)
                row,col = update_position(monkey_map, facing, row, col, int(m))

    print(1000*(row+1) + 4*(col+1) + facing)

if __name__ == '__main__':
    main()

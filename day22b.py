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

def update_north(monkey_map, r, c):
    if 0 <= c < 50 and r == 100:
        if monkey_map[c+50][50] == '.':
            return (c+50,50,0)
        elif monkey_map[c+50][50] == '#':
            return (r,c,3)
    elif 50 <= c < 100 and r == 0:
        if monkey_map[c+100][0] == '.':
            return (c+100,0,0)
        elif monkey_map[c+100][0] == '#':
            return (r,c,3)
    elif 100 <= c < 150 and r == 0:
        if monkey_map[199][c-100] == '.':
            return (199,c-100,3)
        elif monkey_map[199][c-100] == '#':
            return (r,c,3)
    else:
        if monkey_map[r-1][c] == '.':
            return (r-1,c,3)
        elif monkey_map[r-1][c] == '#':
            return (r,c,3)

def update_east(monkey_map, r, c):
    if 0 <= r < 50 and c == 149:
        if monkey_map[149-r][99] == '.':
            return (149-r,99,2)
        elif monkey_map[149-r][99] == '#':
            return (r,c,0)
    elif 50 <= r < 100 and c == 99:
        if monkey_map[49][r+50] == '.':
            return (49,r+50,3)
        elif monkey_map[49][r+50] == '#':
            return (r,c,0)
    elif 100 <= r < 150 and c == 99:
        if monkey_map[149-r][149] == '.':
            return (149-r,149,2)
        elif monkey_map[149-r][149] == '#':
            return (r,c,0)
    elif 150 <= r < 200 and c == 49:
        if monkey_map[149][r-100] == '.':
            return (149,r-100,3)
        elif monkey_map[149][r-100] == '#':
            return (r,c,0)
    else:
        if monkey_map[r][c+1] == '.':
            return (r,c+1,0)
        elif monkey_map[r][c+1] == '#':
            return (r,c,0)
        else:
            raise Exception('east, r: ' + str(r) + ', c: ' + str(c))

def update_south(monkey_map, r, c):
    if 0 <= c < 50 and r == 199:
        if monkey_map[0][c+100] == '.':
            return (0,c+100,1)
        elif monkey_map[0][c+100] == '#':
            return (r,c,1)
    elif 50 <= c < 100 and r == 149:
        if monkey_map[c+100][49] == '.':
            return (c+100,49,2)
        elif monkey_map[c+100][49] == '#':
            return (r,c,1)
    elif 100 <= c < 150 and r == 49:
        if monkey_map[c-50][99] == '.':
            return (c-50,99,2)
        elif monkey_map[c-5][99] == '#':
            return (r,c,1)
    else:
        if monkey_map[r+1][c] == '.':
            return (r+1,c,1)
        elif monkey_map[r+1][c] == '#':
            return (r,c,1)
        else:
            raise Exception('south, r: ' + str(r) + ', c: ' + str(c))

def update_west(monkey_map, r, c):
    if 0 <= r < 50 and c == 50:
        if monkey_map[149-r][0] == '.':
            return (149-r,0,0)
        elif monkey_map[149-r][0] == '#':
            return (r,c,2)
    elif 50 <= r < 100 and c == 50:
        if monkey_map[100][r-50] == '.':
            return (100,r-50,1)
        elif monkey_map[100][r-50] == '#':
            return (r,c,2)
    elif 100 <= r < 150 and c == 0:
        if monkey_map[149-r][50] == '.':
            return (149-r,50,0)
        elif monkey_map[149-r][50] == '#':
            return (r,c,2)
    elif 150 <= r < 200 and c == 0:
        if monkey_map[0][r-100] == '.':
            return (0,r-100,1)
        elif monkey_map[0][r-100] == '#':
            return (r,c,2)
    else:
        if monkey_map[r][c-1] == '.':
            return (r,c-1,2)
        elif monkey_map[r][c-1] == '#':
            return (r,c,2)

def update_position(monkey_map, facing, row, col, dist):
    r,c,f = row,col,facing
    for i in range(0, dist):
        if f == 3:
            r,c,f = update_north(monkey_map, r, c)
        elif f == 0:
            r,c,f = update_east(monkey_map, r, c)
        elif f == 1:
            r,c,f = update_south(monkey_map, r, c)
        elif f == 2:
            r,c,f = update_west(monkey_map, r, c)
    return r,c,f

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
                row,col,facing = update_position(monkey_map, facing, row, col, int(m))

    print(1000*(row+1) + 4*(col+1) + facing)

if __name__ == '__main__':
    main()

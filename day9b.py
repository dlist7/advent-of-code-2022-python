#!/usr/bin/env python3

import fileinput
import re

rope = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
ts = {rope[-1]}

def move_tail(h,t):

    dr = abs(h[0] - t[0])
    dc = abs(h[1] - t[1])
    dm = max(dr, dc)

    if dm > 1:
        if h[0] == t[0]:
            new = (t[0], t[1] + (1 if h[1] > t[1] else -1))
        elif h[1] == t[1]:
            new = (t[0] + (1 if h[0] > t[0] else -1), t[1])
        else:
            new = (t[0] + (1 if h[0] > t[0] else -1), t[1] + (1 if h[1] > t[1] else -1))
        return new

    return t

def move(d, n):
    for i in range(0, n):

        if d == 'U':
            rope[0] = (rope[0][0]-1, rope[0][1])
        elif d == 'D':
            rope[0] = (rope[0][0]+1, rope[0][1])
        elif d == 'L':
            rope[0] = (rope[0][0], rope[0][1]-1)
        elif d == 'R':
            rope[0] = (rope[0][0], rope[0][1]+1)

        for i in range(0, len(rope)-1):
            rope[i+1] = move_tail(rope[i], rope[i+1])

        ts.add(rope[-1])

def main():
    for line in fileinput.input():
        match = re.match('(U|D|L|R) (\d+)', line)
        if match:
            d = match.group(1)
            n = int(match.group(2))
            move(d,n)
    print(len(ts))

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import fileinput
import re

h = (0,0)
t = (0,0)
ts = {t}

def move_tail():
    global t

    dr = abs(h[0] - t[0])
    dc = abs(h[1] - t[1])
    dm = max(dr, dc)

    if dm > 1:
        if h[0] == t[0]:
            t = (t[0], t[1] + (1 if h[1] > t[1] else -1))
        elif h[1] == t[1]:
            t = (t[0] + (1 if h[0] > t[0] else -1), t[1])
        else:
            t = (t[0] + (1 if h[0] > t[0] else -1), t[1] + (1 if h[1] > t[1] else -1))

def move(d, n):
    global h
    for i in range(0, n):
        if d == 'U':
            h = (h[0]-1, h[1])
        elif d == 'D':
            h = (h[0]+1, h[1])
        elif d == 'L':
            h = (h[0], h[1]-1)
        elif d == 'R':
            h = (h[0], h[1]+1)
        move_tail()
        ts.add(t)

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

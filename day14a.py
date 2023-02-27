#!/usr/bin/env python3

import fileinput

map = {}
floor = -1

def draw_segment(map, p0, p1):
    global floor
    x0,y0 = [int(i) for i in p0.split(',')]
    x1,y1 = [int(i) for i in p1.split(',')]

    floor = max(floor, y0, y1)

    if x0 == x1:
        if y0 < y1:
            for i in range(y0, y1 + 1):
                map[(x0,i)] = '#'
        else:
            for i in range(y1, y0 + 1):
                map[(x0,i)] = '#'
    elif y0 == y1:
        if x0 < x1:
            for i in range(x0, x1 + 1):
                map[(i,y0)] = '#'
        else:
            for i in range(x1, x0 + 1):
                map[(i,y0)] = '#'
    else:
        raise Exception('Diagonal Segment')

def next_p(p):
    if not map.get((p[0], p[1] + 1)):
        return (p[0], p[1] + 1)
    elif not map.get((p[0] - 1, p[1] + 1)):
        return (p[0] - 1, p[1] + 1)
    elif not map.get((p[0] + 1, p[1] + 1)):
        return (p[0] + 1, p[1] + 1)
    else:
        return p

def main():
    for line in fileinput.input():
        points = line.rstrip().split(' -> ')
        for i in range(0, len(points) - 1):
            p0 = points[i]
            p1 = points[i+1]
            draw_segment(map, p0, p1)
    
    count = 0
    done = False
    while True:
        p = (500,0)
        while True:
            np = next_p(p)
            if p == np:
                map[p] = 'o'
                count += 1
                break
            elif p[1] > floor:
                done = True
                break
            else:
                p = np
        if done:
            break

    print(count)

if __name__ == '__main__':
    main()

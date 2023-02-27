#!/usr/bin/env python3

import fileinput
import re

#l_max = 20
l_max = 4000000

def get_segment(l, s):
    r = s[2] - abs(l - s[1])
    if r >= 0:
        return (s[0] - r, s[0] + r)
    return None

def find_point(segments):
    segs = sorted(segments)
    seg = list(segs[0])
    if seg[0] > 0:
        return 0
    for i in range(1, len(segs)):
        if segs[i][0] > seg[1] + 1 and seg[1] + 1 <= l_max:
            return seg[1] + 1
        elif seg[1] >= l_max:
            return None
        elif segs[i][1] > seg[1]:
            seg[1] = segs[i][1]
        #print(seg, segs[i])
    return None

def main():
    sensors = []
    beacons_by_line = {}
    for line in fileinput.input():
        match = re.match('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
        if match:
            sx = int(match.group(1))
            sy = int(match.group(2))
            bx = int(match.group(3))
            by = int(match.group(4))
            d = abs(bx - sx) + abs(by - sy)
            sensors.append((sx, sy, d))
            beacons_by_line.setdefault(by, set()).add(bx)

    for i in range(0, l_max + 1):
        #print(i)
        segments = []
        for s in sensors:
            segment = get_segment(i, s)
            if segment:
                segments.append(segment)
        point = find_point(segments)
        if point:
            #print(point)
            break
    print(point*4000000 + i)

if __name__ == '__main__':
    main()

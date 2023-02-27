#!/usr/bin/env python3

import fileinput
import re

#l = 10
l = 2000000

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
    n = set()
    for s in sensors:
        r = s[2] - abs(l - s[1])
        if r >= 0:
            for i in range(s[0] - r, s[0] + r + 1):
                n.add(i)
    beacons = beacons_by_line.get(l)
    for b in beacons if beacons else []:
        n.remove(b)
    print(len(n))

if __name__ == '__main__':
    main()

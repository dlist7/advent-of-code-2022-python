#!/usr/bin/env python3

import fileinput

def main():
    cubes = {}
    for line in fileinput.input():
        x,y,z = [int(n) for n in line.split(',')]
        cubes[(x,y,z)] = True
    exposed = 0
    for cube in cubes.keys():
        if not cubes.get((cube[0]-1,cube[1],cube[2])):
            exposed += 1
        if not cubes.get((cube[0]+1,cube[1],cube[2])):
            exposed += 1
        if not cubes.get((cube[0],cube[1]-1,cube[2])):
            exposed += 1
        if not cubes.get((cube[0],cube[1]+1,cube[2])):
            exposed += 1
        if not cubes.get((cube[0],cube[1],cube[2]-1)):
            exposed += 1
        if not cubes.get((cube[0],cube[1],cube[2]+1)):
            exposed += 1
    print(exposed)

if __name__ == '__main__':
    main()

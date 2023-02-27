#!/usr/bin/env python3

import fileinput

def main():
    cube_map = {}
    for line in fileinput.input():
        x,y,z = [int(n) for n in line.split(',')]
        cube_map[(x,y,z)] = 1
    exposed = 0
    x_min = min([c[0] for c in cube_map.keys()])
    x_max = max([c[0] for c in cube_map.keys()])
    y_min = min([c[1] for c in cube_map.keys()])
    y_max = max([c[1] for c in cube_map.keys()])
    z_min = min([c[2] for c in cube_map.keys()])
    z_max = max([c[2] for c in cube_map.keys()])

    point = (x_min-1,y_min-1,z_min-1)
    points = [point]
    cube_map[point] = 2

    while len(points) > 0:

        point = points.pop(0)
        px = point[0]
        py = point[1]
        pz = point[2]
        if px - 1 >= x_min - 1:
            if not cube_map.get((px-1,py,pz)):
                cube_map[(px-1,py,pz)] = 2
                points.append((px-1,py,pz))
            elif cube_map[(px-1,py,pz)] == 1:
                exposed += 1
        if px + 1 <= x_max + 1:
            if not cube_map.get((px+1,py,pz)):
                cube_map[(px+1,py,pz)] = 2
                points.append((px+1,py,pz))
            elif cube_map[(px+1,py,pz)] == 1:
                exposed += 1
        if py - 1 >= y_min - 1:
            if not cube_map.get((px,py-1,pz)):
                cube_map[(px,py-1,pz)] = 2
                points.append((px,py-1,pz))
            elif cube_map[(px,py-1,pz)] == 1:
                exposed += 1
        if py + 1 <= y_max + 1:
            if not cube_map.get((px,py+1,pz)):
                cube_map[(px,py+1,pz)] = 2
                points.append((px,py+1,pz))
            elif cube_map[(px,py+1,pz)] == 1:
                exposed += 1
        if pz - 1 >= z_min - 1:
            if not cube_map.get((px,py,pz-1)):
                cube_map[(px,py,pz-1)] = 2
                points.append((px,py,pz-1))
            elif cube_map[(px,py,pz-1)] == 1:
                exposed += 1
        if pz + 1 <= z_max + 1:
            if not cube_map.get((px,py,pz+1)):
                cube_map[(px,py,pz+1)] = 2
                points.append((px,py,pz+1))
            elif cube_map[(px,py,pz+1)] == 1:
                exposed += 1

    print(exposed)

if __name__ == '__main__':
    main()

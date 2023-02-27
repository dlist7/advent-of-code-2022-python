#!/usr/bin/env python3

import fileinput

def main():
    heights = 'abcdefghijklmnopqrstuvwxyz'
    map = []
    visited = []
    start = ()
    end = ()
    paths = []

    for line in fileinput.input():
        map.append([])
        visited.append([])
        for i,c in enumerate(line.rstrip()):
            visited[-1].append(False)
            if c == 'S':
                start = (len(map) - 1, i)
                map[-1].append(heights.find('a'))
            elif c == 'E':
                end = (len(map) - 1, i)
                map[-1].append(heights.find('z'))
            else:
                map[-1].append(heights.find(c))

    paths.append([start])
    visited[start[0]][start[1]] = True

    while True:
        path = paths.pop(0)
        point = path[-1]
        current_elevation = map[point[0]][point[1]]

        # North
        if point[0] > 0:
            next_point = (point[0] - 1, point[1])
            next_elevation = map[point[0] - 1][point[1]]
            if next_elevation - current_elevation <= 1:
                if next_point == end:
                    path.append(next_point)
                    break
                elif not visited[point[0] - 1][point[1]]:
                    visited[point[0] - 1][point[1]] = True
                    paths.append(path + [next_point])

        # East
        if point[1] < len(map[point[0]]) - 1:
            next_point = (point[0], point[1] + 1)
            next_elevation = map[point[0]][point[1] + 1]
            if next_elevation - current_elevation <= 1:
                if next_point == end:
                    path.append(next_point)
                    break
                elif not visited[point[0]][point[1] + 1]:
                    visited[point[0]][point[1] + 1] = True
                    paths.append(path + [next_point])

        # South
        if point[0] < len(map) - 1:
            next_point = (point[0] + 1, point[1])
            next_elevation = map[point[0] + 1][point[1]]
            if next_elevation - current_elevation <= 1:
                if next_point == end:
                    path.append(next_point)
                    break
                elif not visited[point[0] + 1][point[1]]:
                    visited[point[0] + 1][point[1]] = True
                    paths.append(path + [next_point])

        # West
        if point[1] > 0:
            next_point = (point[0], point[1] - 1)
            next_elevation = map[point[0]][point[1] - 1]
            if next_elevation - current_elevation <= 1:
                if next_point == end:
                    path.append(next_point)
                    break
                elif not visited[point[0]][point[1] - 1]:
                    visited[point[0]][point[1] - 1] = True
                    paths.append(path + [next_point])

    print(len(path) - 1)

if __name__ == '__main__':
    main()

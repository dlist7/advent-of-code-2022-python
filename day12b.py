#!/usr/bin/env python3

import fileinput
import math

heights = 'abcdefghijklmnopqrstuvwxyz'
map = []
end = ()

def load_map():
    global end
    for line in fileinput.input():
        map.append([])
        for i,c in enumerate(line.rstrip()):
            if c == 'S':
                map[-1].append(heights.find('a'))
            elif c == 'E':
                end = (len(map) - 1, i)
                map[-1].append(heights.find('z'))
            else:
                map[-1].append(heights.find(c))

def init_visited(m):
    visited = []
    for row in m:
        visited.append([])
        visited[-1] = len(row)*[False]
    return visited

def get_path_len(start):
    global end
    visited = init_visited(map)
    paths = []

    paths.append([start])
    visited[start[0]][start[1]] = True

    while True:

        if len(paths) > 0:
            path = paths.pop(0)
        else:
            return math.inf

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

    return len(path) - 1

def main():

    load_map()

    min_path_len = math.inf

    for i,row in enumerate(map):
        for j,col in enumerate(row):
            if col == 0:
                min_path_len = min(min_path_len, get_path_len((i, j)))

    print(min_path_len)

if __name__ == '__main__':
    main()

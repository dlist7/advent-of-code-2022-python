#!/usr/bin/env python3

import fileinput

forest = []
visible = 0

def load_forest():
    for line in fileinput.input():
        row = []
        for c in line[:-1]:
            row.append(int(c))
        forest.append(row)

def is_visible(row, col):
    height = forest[row][col]

    # Check north.
    vis = True
    for r in range(0, row):
        if forest[r][col] >= height:
            vis = False
            break
    if vis == True:
        return True

    # Check east.
    vis = True
    for c in range(col+1, len(forest[row])):
        if forest[row][c] >= height:
            vis = False
            break
    if vis == True:
        return True

    # Check south.
    vis = True
    for r in range(row+1, len(forest)):
        if forest[r][col] >= height:
            vis = False
            break
    if vis == True:
        return True

    # Check west.
    vis = True
    for c in range(0, col):
        if forest[row][c] >= height:
            vis = False
            break
    if vis == True:
        return True

    return False

def main():
    global visible

    load_forest()
    
    # Add all the trees from the edges.
    visible = 2*len(forest) + 2*len(forest[0]) - 4

    # Check the interior trees.
    for row in range(1, len(forest)-1):
        for col in range(1, len(forest[row])-1):
            visible += is_visible(row, col)

    print(visible)

if __name__ == '__main__':
    main()

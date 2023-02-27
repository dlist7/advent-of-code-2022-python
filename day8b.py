#!/usr/bin/env python3

import fileinput

forest = []
max_score = 0

def load_forest():
    for line in fileinput.input():
        row = []
        for c in line[:-1]:
            row.append(int(c))
        forest.append(row)

def get_score(row, col):
    height = forest[row][col]

    # Check north.
    n_score = 0
    for r in range(row-1, -1, -1):
        n_score += 1
        if forest[r][col] >= height:
            break

    # Check east.
    e_score = 0
    for c in range(col+1, len(forest[row])):
        e_score += 1
        if forest[row][c] >= height:
            break

    # Check south.
    s_score = 0
    for r in range(row+1, len(forest)):
        s_score += 1
        if forest[r][col] >= height:
            break

    # Check west.
    w_score = 0
    for c in range(col-1, -1, -1):
        w_score += 1
        if forest[row][c] >= height:
            break

    return n_score*e_score*s_score*w_score

def main():
    global max_score

    load_forest()
    
    # Check the interior trees.
    for row in range(1, len(forest)-1):
        for col in range(1, len(forest[row])-1):
            max_score = max(max_score, get_score(row, col))

    print(max_score)

if __name__ == '__main__':
    main()

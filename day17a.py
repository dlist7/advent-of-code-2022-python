#!/usr/bin/env python3

import fileinput

shapes = [
    {'height': 1, 'width': 4, 'shape': [(0,0),(0,1),(0,2),(0,3)]},
    {'height': 3, 'width': 3, 'shape': [(0,1),(1,0),(1,1),(1,2),(2,1)]},
    {'height': 3, 'width': 3, 'shape': [(0,0),(0,1),(0,2),(1,2),(2,2)]},
    {'height': 4, 'width': 1, 'shape': [(0,0),(1,0),(2,0),(3,0)]},
    {'height': 2, 'width': 2, 'shape': [(0,0),(0,1),(1,0),(1,1)]},
]

def load_jets():
    return fileinput.input().readline().rstrip()

def can_move(shape, pile, row, col, rdelta, cdelta):
    if col + cdelta < 0 or col + cdelta + shape['width'] > 7 or row + rdelta < 0:
        return False
    for r,c in shape['shape']:
        if pile.get((row + r + rdelta, col + c + cdelta)):
            return False
    return True

def write_shape(shape, pile, row, col):
    for r,c in shape['shape']:
        pile[row + r, col + c] = True

def print_pile(pile):
    mx = max([p[0] for p in pile])
    for i in range(mx, -1, -1):
        for j in range(0, 7):
            if pile.get((i,j)):
                print('#', end='')
            else:
                print('.', end='')
        print('')

def main():
    jets = load_jets()
    pile = {}
    row,col = None, None

    i,height = 0,0
    for rock in range(0, 2022):
        shape = shapes[rock%len(shapes)]
        while True:

            # Appear or fall
            if row == None:
                row,col = height + 3,2
            elif can_move(shape, pile, row, col, -1, 0):
                row -= 1
            else:
                write_shape(shape, pile, row, col)
                height = max(height, row + shape['height'])
                row = None
                break
            
            # Push with jet
            jet = jets[i%len(jets)]
            if jet == '<' and can_move(shape, pile, row, col, 0, -1):
                col -= 1
            elif jet == '>' and can_move(shape, pile, row, col, 0, 1):
                col += 1
            i += 1

    print(height)

if __name__ == '__main__':
    main()

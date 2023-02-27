#!/usr/bin/env python3

import fileinput

def main():
    frame = []
    for line in fileinput.input():
        for i,c in enumerate(line):
            if len(set(frame)) == 13 and c not in frame:
                print(i+1)
                break
            frame.append(c)
            if len(frame) == 14:
                frame.pop(0)

if __name__ == '__main__':
    main()

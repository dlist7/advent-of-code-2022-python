#!/usr/bin/env python3

import fileinput

priorities = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_priority(c):
    return priorities.find(c)

def main():
    total_priority = 0
    for line in fileinput.input():
        comp_length = (len(line) - 1)//2
        comp1 = line[0:comp_length]
        comp2 = line[comp_length:-1]
        for c in comp2:
            if c in comp1:
                total_priority += get_priority(c)
                break

    print(total_priority)

if __name__ == '__main__':
    main()

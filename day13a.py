#!/usr/bin/env python3

import ast
import fileinput

def compare_lists(p0, p1):
    for i in range(0, len(p0)):
        if i >= len(p1):
            return 1
        elif type(p0[i]) is list:
            if type(p1[i]) is list:
                comp = compare_lists(p0[i], p1[i])
                if comp:
                    return comp
            else:
                comp = compare_lists(p0[i], [p1[i]])
                if comp:
                    return comp
        else:
            if type(p1[i]) is list:
                comp = compare_lists([p0[i]], p1[i])
                if comp:
                    return comp
            else:
                if p0[i] < p1[i]:
                    return -1
                elif p0[i] > p1[i]:
                    return 1
    if len(p0) < len(p1):
        return -1
    return 0

def main():
    correct = []
    p0 = None
    p1 = None
    pn = 0
    for line in fileinput.input():
        if line.startswith('['):
            p = ast.literal_eval(line)
            if p0 is not None:
                pn += 1
                p1 = p
                if compare_lists(p0, p1) < 0:
                    correct.append(pn)
            else:
                p0 = p
        else:
            p0 = p1 = None
    print(sum(correct))

if __name__ == '__main__':
    main()

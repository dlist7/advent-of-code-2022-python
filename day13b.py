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

    packets = []
    sorted_packets = []

    packets.append([[2]])
    packets.append([[6]])
    for line in fileinput.input():
        if line.startswith('['):
            packets.append(ast.literal_eval(line))

    while len(packets) > 0:
        i_min = 0
        for i in range(1, len(packets)):
            if compare_lists(packets[i_min], packets[i]) > 0:
                i_min = i
        sorted_packets.append(packets.pop(i_min))
    
    for i,packet in enumerate(sorted_packets):
        if str(packet) == '[[2]]':
            i2 = i + 1
        if str(packet) == '[[6]]':
            i6 = i + 1

    print(i2*i6)

if __name__ == '__main__':
    main()

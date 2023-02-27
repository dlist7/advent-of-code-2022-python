#!/usr/bin/env python3

import fileinput

snafu_lookup = {
    '0': 0,
    '1': 1,
    '2': 2,
    '-': -1,
    '=': -2,
}

def snafu2int(snafu):
    result = 0
    mult = 1
    for i in range(len(snafu)-1,-1,-1):
        result += mult*snafu_lookup[snafu[i]]
        mult *= 5
    return result

def base52snafu(base5):
    b5 = [0] + [int(c) for c in list(base5)]
    result = ''
    for i in range(len(b5)-1,0,-1):
        if b5[i] < 3:
            result = str(b5[i]) + result
        elif b5[i] == 3:
            result = '=' + result
            b5[i-1] += 1
        else:
            # b5[i] == 4
            result = '-' + result
            b5[i-1] += 1
    if b5[0]:
        result = '1' + result

    return result

def int2snafu(num):
    n = num
    result = ''
    while True:
        result = str(n%5) + result
        n = n//5
        if n == 0:
            return base52snafu(result)

def main():
    total = 0
    for line in fileinput.input():
        total += snafu2int(line.rstrip())
    print(int2snafu(total))

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import fileinput

decryption_key = 811589153

def mix(sequence):
    for i in range(0,len(sequence)):

        n = sequence[i]['next']
        p = sequence[i]['previous']
        val = sequence[i]['value']%(len(sequence) - 1)

        if val:
            sequence[n]['previous'] = p
            sequence[p]['next'] = n

        if val > 0:
            num = i
            for k in range(0,val):
                num = sequence[num]['next']
            num2 = sequence[num]['next']
            sequence[i]['previous'] = num
            sequence[i]['next'] = num2
            sequence[num2]['previous'] = i
            sequence[num]['next'] = i
        elif val < 0:
            num = i
            for k in range(0,val,-1):
                num = sequence[num]['previous']
            num2 = sequence[num]['previous']
            sequence[i]['next'] = num
            sequence[i]['previous'] = num2
            sequence[num2]['next'] = i
            sequence[num]['previous'] = i

def main():
    sequence = []
    for i,line in enumerate(fileinput.input()):
        sequence.append({'value':int(line.rstrip())*decryption_key,'next':i+1,'previous':i-1})

    sequence[-1]['next'] = 0
    sequence[0]['previous'] = len(sequence) - 1

    for i in range(0,10):
        mix(sequence)

    for i in range(0, len(sequence)):
        if sequence[i]['value'] == 0:
            break
    sum = 0
    for k in range(0,1000):
        i = sequence[i]['next']
    sum += sequence[i]['value']
    for k in range(0,1000):
        i = sequence[i]['next']
    sum += sequence[i]['value']
    for k in range(0,1000):
        i = sequence[i]['next']
    sum += sequence[i]['value']
    print(sum)

if __name__ == '__main__':
    main()

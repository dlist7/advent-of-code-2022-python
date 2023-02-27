#!/usr/bin/env python3

import fileinput
import re

def add(monkeys, m1, m2):
    return lambda: monkeys[m1]() + monkeys[m2]()
def sub(monkeys, m1, m2):
    return lambda: monkeys[m1]() - monkeys[m2]()
def mul(monkeys, m1, m2):
    return lambda: monkeys[m1]() * monkeys[m2]()
def div(monkeys, m1, m2):
    return lambda: monkeys[m1]()/monkeys[m2]()
def num(n):
    return lambda: n

def main():
    monkeys = {}
    for line in fileinput.input():
        match = re.match('(\w+): (\w+)( ([\+\-\*/]) (\w+))?', line)
        if match:
            monkey = match.group(1)
            if match.group(3):
                m1 = match.group(2)
                op = match.group(4)
                m2 = match.group(5)
                if op == '+':
                    monkeys[monkey] = add(monkeys, m1, m2)
                elif op == '-':
                    monkeys[monkey] = sub(monkeys, m1, m2)
                elif op == '*':
                    monkeys[monkey] = mul(monkeys, m1, m2)
                elif op == '/':
                    monkeys[monkey] = div(monkeys, m1, m2)
            else:
                n = int(match.group(2))
                monkeys[monkey] = num(n)
        else:
            raise Exception('Parse error: ' + line)
    print(int(monkeys['root']()))

if __name__ == '__main__':
    main()

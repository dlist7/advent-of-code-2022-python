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

def guess(monkeys, m1, m2, n):
    monkeys['humn'] = num(n)
    return int(monkeys[m1]() - monkeys[m2]())

def main():
    monkeys = {}
    for line in fileinput.input():
        match = re.match('(\w+): (\w+)( ([\+\-\*/]) (\w+))?', line)
        if match:
            monkey = match.group(1)
            if monkey == 'root':
                monkey1 = match.group(2)
                monkey2 = match.group(5)
            else:
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

    if guess(monkeys, monkey1, monkey2, 1) < guess(monkeys, monkey1, monkey2, -1):
        answer = 1
    else:
        answer = -1
    
    while guess(monkeys, monkey1, monkey2, answer) > 0:
        last_answer = answer
        answer *= 2

    while True:
        half_answer = (answer + last_answer)//2
        half_guess = guess(monkeys, monkey1, monkey2, half_answer)
        if abs(half_guess) < 0.5:
            break
        if half_guess > 0:
            last_answer = half_answer
        else:
            answer = half_answer

    print(half_answer)


if __name__ == '__main__':
    main()

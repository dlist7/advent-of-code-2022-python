#!/usr/bin/env python3

import fileinput
import re

def add(n):
    return lambda old: old + n

def mul(n):
    return lambda old: old * n

def test(n):
    return lambda old: old%n == 0

def main():

    monkeys = []
    current_monkey = None

    for line in fileinput.input():

        match = re.match('Monkey (\d+)', line)
        if match:
            if current_monkey:
                monkeys.append(current_monkey)
            current_monkey = {}
            current_monkey['id'] = int(match.group(1))
            current_monkey['items'] = []
            current_monkey['inspections'] = 0

        match = re.match('\s+Starting items: ((\d+, )*(\d+))', line)
        if match:
            current_monkey['items'] = match.group(1).split(', ')

        match = re.match('\s+Operation: new = (\w+) ([\*\+]) (\w+)', line)
        if match:
            if match.group(1) == match.group(3) == 'old':
                current_monkey['operation'] = lambda old: old*old
            elif match.group(2) == '+':
                current_monkey['operation'] = add(int(match.group(3)))
            elif match.group(2) == '*':
                current_monkey['operation'] = mul(int(match.group(3)))

        match = re.match('\s+Test: divisible by (\d+)', line)
        if match:
            current_monkey['test'] = test(int(match.group(1)))

        match = re.match('\s+If true: throw to monkey (\d+)', line)
        if match:
            current_monkey['true'] = int(match.group(1))

        match = re.match('\s+If false: throw to monkey (\d+)', line)
        if match:
            current_monkey['false'] = int(match.group(1))

    monkeys.append(current_monkey)

    for i in range(0, 20):
        for m in monkeys:
            for item in m['items']:
                m['inspections'] += 1
                new_item = m['operation'](int(item))
                new_item //= 3
                if m['test'](new_item):
                    monkeys[m['true']]['items'].append(str(new_item))
                else:
                    monkeys[m['false']]['items'].append(str(new_item))
            m['items'] = []

    sorted_monkeys = sorted(monkeys, key=lambda m: m['inspections'], reverse=True)
    print(sorted_monkeys[0]['inspections']*sorted_monkeys[1]['inspections'])

if __name__ == '__main__':
    main()

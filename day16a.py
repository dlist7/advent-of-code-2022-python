#!/usr/bin/env python3

import fileinput
import re

valves = {}
working_valves = 0
results = {}

def best_pressure(name, minutes, open, score):
    valve = valves[name]
    scores = []
    sorted_open = sorted(open)
    key = name + '|' + str(minutes) + '|' + str(sorted_open) + '|' + str(score)

    if r := results.get(key):
        return r

    if minutes > 1 and len(open) < working_valves:
        for d in valve['dests']:
            if not name in open:
                if valve['rate'] > 0:
                    open_score = (minutes - 1)*valve['rate']
                    scores.append(best_pressure(d, minutes-2, open + [name], score + open_score))
            if minutes > 2:
                scores.append(best_pressure(d, minutes-1, open, score))
    scores.append(score)

    r = max(scores)
    results[key] = r

    return r

def main():
    global working_valves
    for line in fileinput.input():
        match = re.match('Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ((\w+, )*(\w+))', line)
        if match:
            name = match.group(1)
            rate = int(match.group(2))
            dests = match.group(3).split(', ')
            valves[name] = {'rate':rate,'dests':dests}
            if rate > 0:
                working_valves += 1
    print(best_pressure('AA', 30, [], 0))

if __name__ == '__main__':
    main()

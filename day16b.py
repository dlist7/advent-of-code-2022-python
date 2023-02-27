#!/usr/bin/env python3

import fileinput
import re

valves = {}
distances = {}
in_range = []

def load_valves():
    for line in fileinput.input():
        match = re.match('Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ((\w+, )*(\w+))', line)
        if match:
            name = match.group(1)
            rate = int(match.group(2))
            dests = match.group(3).split(', ')
            valves[name] = {'name':name,'rate':rate,'dests':dests}
        else:
            raise Exception('Unexpected format: ' + line)

def get_distances(name):
    dists = {}
    visited = {name}
    paths = [[name]]

    while len(paths) > 0:
        dests = valves[paths[0][-1]]['dests']
        for n in dests:
            if n not in visited:
                p = paths[0][:]
                p.append(n)
                if valves[n]['rate'] > 0:
                    dists[n] = len(p) - 1
                visited.add(n)
                paths.append(p)
        paths.pop(0)

    return dists

def calculate_distances(valves):
    dists = {}
    for name in [v[0] for v in valves.items() if v[1]['rate'] > 0] + ['AA']:
        dists[name] = get_distances(name)
    return dists

def best_pressure(name, minutes, to_visit, score):
    scores = []

    if minutes > 0:
        s = score + minutes*valves[name]['rate']
        if len(to_visit) > 0:
            for v in to_visit:
                distance = distances[name][v]
                tv = to_visit[:]
                tv.remove(v)
                scores.append(best_pressure(v, minutes-distance-1, tv, s))
        else:
            return s
    else:
        return score
    
    return max(scores)

def n_choose_m(n, m):
    result = 1

    for i in range(0, m):
        result = (n - i)*result//(i + 1)

    return result

def get_i_of_n_choose_m(i, list, n, m):
    ml = [0]*m
    for j in range(0, m):
        ml[j] = j
    for j in range(0, i):
        for k in range(0, m):
            if ml[-k-1] < n - 1 - k:
                ml[-k-1] += 1
                for l in range(-k, 0):
                    ml[l] = ml[l-1] + 1
                break
    result = []
    for j in range(0, m):
        result += [list[ml[j]]]
    return result

def n_choose_m_generator(list, m):
    n = len(list)
    ml = [0]*m
    for i in range(0, n_choose_m(n, m)):
        for j in range(0, m):
            ml[j] = j
        for j in range(0, i):
            for k in range(0, m):
                if ml[-k-1] < n - 1 - k:
                    ml[-k-1] += 1
                    for l in range(-k, 0):
                        ml[l] = ml[l-1] + 1
                    break
        result = []
        for j in range(0, m):
            result += [list[ml[j]]]
        yield tuple(result)

def main():
    global distances, in_range

    load_valves()
    distances = calculate_distances(valves)
    to_visit = sorted([d[0] for d in distances['AA'].items()])

    results = {}
    for i in range(0, len(to_visit)):
        for tv in n_choose_m_generator(to_visit, i + 1):
            results[tv] = best_pressure('AA', 26, list(tv), 0)

    results2 = []
    for k in results.keys():
        ik = tuple(sorted([v for v in to_visit if v not in k]))
        if len(ik):
            results2.append(results[k] + results[ik])
        else:
            results2.append(results[k])
    print(max(results2))

if __name__ == '__main__':
    main()

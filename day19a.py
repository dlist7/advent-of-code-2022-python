#!/usr/bin/env python3

import fileinput
import re

def evaluate_blueprint(blueprint, min, orb, crb, obrb, grb, o, c, ob, g):

    if min < 1:
        return g

    results = []

    # Build ore robot
    if o >= blueprint[1] and o < max(blueprint[1], blueprint[2], blueprint[3], blueprint[5]) + 2:
        no = orb + o - blueprint[1]
        nc = crb + c
        nob = obrb + ob
        ng = grb + g
        results.append(evaluate_blueprint(blueprint, min-1, orb+1, crb, obrb, grb, no, nc, nob, ng))
    # Build clay robot
    if o >= blueprint[2] and c < blueprint[4] + 2:
        no = orb + o - blueprint[2]
        nc = crb + c
        nob = obrb + ob
        ng = grb + g
        results.append(evaluate_blueprint(blueprint, min-1, orb, crb+1, obrb, grb, no, nc, nob, ng))
    # Build obsidian robot
    if o >= blueprint[3] and c >= blueprint[4]:
        no = orb + o - blueprint[3]
        nc = crb + c - blueprint[4]
        nob = obrb + ob
        ng = grb + g
        results.append(evaluate_blueprint(blueprint, min-1, orb, crb, obrb+1, grb, no, nc, nob, ng))
    if o >= blueprint[5] and ob >= blueprint[6]:
        no = orb + o - blueprint[5]
        nc = crb + c
        nob = obrb + ob - blueprint[6]
        ng = grb + g
        results.append(evaluate_blueprint(blueprint, min-1, orb, crb, obrb, grb+1, no, nc, nob, ng))
    if o < max(blueprint[1], blueprint[2]) or (o < blueprint[3] and c < blueprint[4]) \
            or (o < blueprint[5] and ob < blueprint[6]):
        no = orb + o
        nc = crb + c
        nob = obrb + ob
        ng = grb + g
        results.append(evaluate_blueprint(blueprint, min-1, orb, crb, obrb, grb, no, nc, nob, ng))

    if len(results):
        return max(results)
    return grb + g


def main():
    blueprints = []
    for line in fileinput.input():
        match = re.match('\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+', line)
        if match:
            blueprint = int(match.group(1))
            ore_cost = int(match.group(2))
            clay_cost = int(match.group(3))
            obs_ore_cost = int(match.group(4))
            obs_clay_cost = int(match.group(5))
            geode_ore_cost = int(match.group(6))
            geode_obs_cost = int(match.group(7))
        else:
            raise Exception('Parse Error: ' + line)
        blueprints.append((blueprint,ore_cost,clay_cost,obs_ore_cost,obs_clay_cost,
            geode_ore_cost,geode_obs_cost))

    sum = 0
    for blueprint in blueprints:
        sum += blueprint[0]*evaluate_blueprint(blueprint, 24, 1, 0, 0, 0, 0, 0, 0, 0)
    print(sum)

if __name__ == '__main__':
    main()

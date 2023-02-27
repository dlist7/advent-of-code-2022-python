#!/usr/bin/env python3

import fileinput
import math
import re

def evaluate_blueprint(blueprint, min, orb, crb, obrb, grb, o, c, ob, g):

    results = []

    # Build ore robot
    dt = math.ceil((blueprint[1] - o)/orb) + 1
    dt = 1 if dt < 1 else dt
    no = dt*orb + o - blueprint[1]
    nc = dt*crb + c
    nob = dt*obrb + ob
    ng = dt*grb + g
    if min - dt > 0 and o < 2 + max(blueprint[1], blueprint[2], blueprint[3], blueprint[5]):
        #print('ore')
        results.append(evaluate_blueprint(blueprint, min-dt, orb+1, crb, obrb, grb, no, nc, nob, ng))

    # Build clay robot
    dt = math.ceil((blueprint[2] - o)/orb) + 1
    dt = 1 if dt < 1 else dt
    no = dt*orb + o - blueprint[2]
    nc = dt*crb + c
    nob = dt*obrb + ob
    ng = dt*grb + g
    if min - dt > 0 and c < 2 + blueprint[4]:
        #print('clay')
        results.append(evaluate_blueprint(blueprint, min-dt, orb, crb+1, obrb, grb, no, nc, nob, ng))

    # Build obsidian robot
    if crb > 0:
        dt = max(math.ceil((blueprint[3] - o)/orb) + 1, math.ceil((blueprint[4] - c)/crb) + 1)
        dt = 1 if dt < 1 else dt
        no = dt*orb + o - blueprint[3]
        nc = dt*crb + c - blueprint[4]
        nob = dt*obrb + ob
        ng = dt*grb + g
        if min - dt > 0 and ob < 2 + blueprint[6]:
            #print('obs')
            results.append(evaluate_blueprint(blueprint, min-dt, orb, crb, obrb+1, grb, no, nc, nob, ng))

    # Build geode robot
    if obrb > 0:
        dt = max(math.ceil((blueprint[5] - o)/orb) + 1, math.ceil((blueprint[6] - ob)/obrb) + 1)
        dt = 1 if dt < 1 else dt
        no = dt*orb + o - blueprint[5]
        nc = dt*crb + c
        nob = dt*obrb + ob - blueprint[6]
        ng = dt*grb + g
        if min - dt > 0:
            #print('geode')
            results.append(evaluate_blueprint(blueprint, min-dt, orb, crb, obrb, grb+1, no, nc, nob, ng))

    if len(results):
        return max(results)

    return min*grb + g


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

    product = 1
    for blueprint in blueprints[0:3]:
        product *= evaluate_blueprint(blueprint, 32, 1, 0, 0, 0, 0, 0, 0, 0)
    print(product)

if __name__ == '__main__':
    main()

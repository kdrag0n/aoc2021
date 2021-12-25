#!/usr/bin/env python3

import sys
import collections
import itertools

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], 'r') as f:
    file_lines = [l for l in f.read().strip().split('\n\n')]


in_nums = []

total = 0
result = 0
other = 0

scs = []
Scanner = collections.namedtuple('Scanner', ['num', 'beacons', 'loc', 'orient', 'rot'])
while True:
    i = 0
    for l in file_lines:
        pts =[]
        for pt in l.split('\n')[1:]:
            pts += [tuple(ints(pt.split(',')))]
        if i == 0:
            sc = Scanner(i, pts, (0,0), '+x', 0)
        else:
            sc = Scanner(i, pts, None, None, None)
        scs += [sc]
        i += 1

        if False:
            total += 1

    break

print(scs)

# 2D
# sc = scs[0]
# for x, y in scs[0].beacons:
#     correct = False
#     for rx, ry in scs[1].beacons:
#         sc1x = x - rx
#         sc1y = y - ry

#         #project
#         resolved = set()
#         for rx, ry in scs[1].beacons:
#             resolved.add((sc1x + rx, sc1y + ry))
#         correct = len(resolved.intersection(set(scs[0].beacons))) >= 3
#     if correct:
#         break

# grid = [['.']*12 for i in range(12)]
# grid[6][6] = 'S'
# for x, y in sc.beacons:
#     grid[y+6][x+6] = 'B'
# grid[sc1y+6][sc1x+6] = 'S'
# for row in grid[::-1]:
#     print(''.join(row))

def apply_orient(beacons, orient):
    inds, xmul, ymul, zmul = orient
    pts = []
    for pt in beacons:
        x, y, z = [pt[i] for i in inds]
        x *= xmul
        y *= ymul
        z *= zmul
        pts += [(x, y, z)]
    return pts

def orientations(beacons):
    x=0
    for inds in itertools.permutations([0,1,2], 3):
        for xmul in [-1, 1]:
            for ymul in [-1, 1]:
                for zmul in [-1, 1]:
                    orient = (inds, xmul, ymul, zmul)
                    pts = []
                    for pt in beacons:
                        x, y, z = [pt[i] for i in inds]
                        x *= xmul
                        y *= ymul
                        z *= zmul
                        pts += [(x, y, z)]
                    yield (pts, orient)

rel_scs = []

sc0 = scs[0]
sc0orient = ((0, 1, 2), 1, 1, 1)
sc_orients = {sc0.num: sc0orient}

sc0s = [(sc0, sc0orient)]
found_scs = set()
while sc0s:
    sc0, sc0orient = sc0s[0]
    sc0s = sc0s[1:]
    for sc1 in scs:
        if sc0 == sc1 or sc1.num == 0 or sc1.num in found_scs:
            continue
        #<sc>
        print(f'{sc0.num} <-> {sc1.num}')

        #for sc0beacons, sc0orient in orientations(sc0.beacons):
        print('o', sc0orient)
        sc0beacons = apply_orient(sc0.beacons, sc0orient)
        sc0beacons_set = set(sc0beacons)
        for sc1beacons, sc1orient in orientations(sc1.beacons):
            #if sc0orient == sc1orient:
            #    continue
            #<orient>

            for x, y, z in sc0beacons:
                correct = False
                for rx, ry, rz in sc1beacons:
                    # print(f'    {x},{y},{z} -> {rx},{ry},{rz}    ({sc1orient})')
                    sc1x = x - rx
                    sc1y = y - ry
                    sc1z = z - rz

                    #project
                    resolved = set()
                    for rx2, ry2, rz2 in sc1beacons:
                        resolved.add((sc1x + rx2, sc1y + ry2, sc1z + rz2))
                    #if sc0.num == 1 and sc1.num == 4:
                    #    print(resolved)
                    correct = len(resolved.intersection(sc0beacons_set)) >= 12
                    if correct:
                        break
                if correct:
                    break
            
            if correct:
                rel_scs += [(sc0, sc1, sc1orient, (sc1x, sc1y, sc1z))]
                sc_orients[sc1.num] = sc1orient
                found_scs.add(sc1.num)
                break
        if correct:
            sc0s += [(sc1, sc1orient)]

print('\n\n\n\nREL')
for sc0, sc1, sc1orient, rpos in rel_scs:
    print(f'    {sc0.num}->{sc1.num}  =  {rpos}    (orientation = {sc1orient})')
print('\n\nORIENT')
print(sc_orients)

scs_abs = {i: None for i in range(len(scs))}
scs_abs[0] = (0, 0, 0)
while any(v is None for v in scs_abs.values()):
    for sc0, sc1, sc1orient, rpos in rel_scs:
        if not scs_abs[sc1.num] and scs_abs[sc0.num]:
            sc0x, sc0y, sc0z = scs_abs[sc0.num]
            rx, ry, rz = rpos
            scs_abs[sc1.num] = (sc0x + rx, sc0y + ry, sc0z + rz)
            print(f'[RESOLVE]    {sc0.num}->{sc1.num}  =  {rpos}    (orientation = {sc1orient})')
print(scs_abs)

beacons = set()
for sc in scs:
    sx, sy, sz = scs_abs[sc.num]
    for rx, ry, rz in apply_orient(sc.beacons, sc_orients[sc.num]):
        beacons.add((sx + rx, sy + ry, sz + rz))
print(len(beacons))

maxd = -1
for sc0 in scs:
    for sc1 in scs:
        sc0x, sc0y, sc0z = scs_abs[sc0.num]
        sc1x, sc1y, sc1z = scs_abs[sc1.num]
        dist = abs(sc1x - sc0x) + abs(sc1y - sc0y) + abs(sc1z - sc0z)
        if dist > maxd:
            maxd = dist
print('maxd', maxd)

print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')


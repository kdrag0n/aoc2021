#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], 'r') as f:
    file_lines = [l for l in f.read().strip().split('\n')]


in_nums = []

total = 0
result = 0
other = 0

steps = []
while True:
    for l in file_lines:
        st, pts = l.split()
        ptd = [ints(x.split('=')[1].split('..')) for x in pts.split(',')]
        steps += [(st == 'on', *ptd)]

        if False:
            total += 1

    break

print(steps)
grid = set()
for st, (xmin, xmax), (ymin, ymax), (zmin, zmax) in steps:
    for x in range(max(xmin, -50), min(xmax, 50)+1):
        for y in range(max(ymin, -50), min(ymax, 50)+1):
            for z in range(max(zmin, -50), min(zmax, 50)+1):
                # if not (x >= -50 and x <= 50 and y >= -50 and y <= 50 and z >= -50 and z <= 50):
                #     continue
                # print(st, x, y, z)
                if st:
                    grid.add((x, y, z))
                elif (x, y, z) in grid:
                    grid.remove((x, y, z))
    # break

print(len(grid))

print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

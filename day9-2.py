#!/usr/bin/env python3

import sys
import collections
def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], 'r') as f:
    file_lines = [l for l in f.read().strip().split('\n')]


in_nums = []

total = 0
result = 0
other = 0

grid=[]
while True:
    for l in file_lines:
        vals = [int(x) for x in list(l)]
        grid += [vals]

    break

lows=[]
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        pts = [
            (x, y-1),
            (x, y+1),
            (x-1, y),
            (x+1, y),
        ]
        adjs = []
        for px, py in pts:
            if px >= 0 and px < len(row) and py >= 0 and py < len(grid):
                adjs += [grid[py][px]]
        if all(cell < adj for adj in adjs):
            lows += [(x, y, cell)]

print(lows)

def find_ns(ns, x, y):
    pts = [
        (x, y-1),
        (x, y+1),
        (x-1, y),
        (x+1, y),
    ]
    #print('NS', x, y, '  -  ', grid[y][x])
    for x, y in pts:
        if x >= 0 and x < len(row) and y >= 0 and y < len(grid) and grid[y][x] != 9 and (x,y) not in ns:
            ns.add((x,y))
            find_ns(ns, x, y)

basins=[]
for lx, ly, lval in lows:
    print('+++++++', lval)
    ns=set()
    find_ns(ns, lx, ly)
    #print('lval', ns)
    print(lval, '----', [grid[y][x] for x,y in ns])
    basins+=[ns]
bs = sorted([len(s) for s in basins])[::-1][:3]
print(bs)
print(bs[0]*bs[1]*bs[2])
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

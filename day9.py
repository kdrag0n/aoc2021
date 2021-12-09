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
        for x, y in pts:
            if x >= 0 and x < len(row) and y >= 0 and y < len(grid):
                adjs += [grid[y][x]]
        if all(cell < adj for adj in adjs):
            lows += [cell]

print(lows)
print(sum(x+1 for x in lows))

print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

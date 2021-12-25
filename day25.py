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
        grid += [list(l)]

        if False:
            total += 1

    break

steps = 0
chgc = 1
while chgc:
    chgs = []
    chgc = 0
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '>':
                fwx = x + 1
                if fwx >= len(row):
                    fwx -= len(row)
                if grid[y][fwx] == '.':
                    chgs += [(x, y, fwx, y)]
    chgc += len(chgs)
    for x0, y0, x1, y1 in chgs:
        grid[y1][x1] = grid[y0][x0]
        grid[y0][x0] = '.'
    chgs = []
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 'v':
                fwy = y + 1
                if fwy >= len(grid):
                    fwy -= len(grid)
                if grid[fwy][x] == '.':
                    chgs += [(x, y, x, fwy)]
    for x0, y0, x1, y1 in chgs:
        grid[y1][x1] = grid[y0][x0]
        grid[y0][x0] = '.'
    chgc += len(chgs)
    steps += 1

print(steps)

print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

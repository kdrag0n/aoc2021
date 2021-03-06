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

grid = [[False] * 2000 for i in range(2000)]
folds = []
while True:
    for l in file_lines:
        if not l:
            continue
        elif l.startswith('fold'):
            _, _, ins = l.split()
            axis, pos = ins.split('=')
            pos = int(pos)
            folds += [(axis, pos)]
        else:
            x, y = map(int, l.split(','))
            grid[y][x] = True

        if False:
            total += 1

    break

def print_grid():
    for r in grid:
        print(''.join(('#' if c else '.') for c in r))

# print_grid()
print(folds)
for axis, pos in folds:
    print(axis, pos)
    if axis == 'x':
        for x2 in range(pos + 1, 2000):
            for y in range(2000):
                if not grid[y][x2]:
                    continue
                refp = pos - (x2 - (pos))
                if refp < 0:
                    continue
                grid[y][refp] = True
                grid[y][x2] = False
    elif axis == 'y':
        for y2 in range(pos + 1, 2000):
            for x in range(2000):
                if not grid[y2][x]:
                    continue
                refp = pos - (y2 - (pos))
                # print(x, y2)
                # print('refp', refp)
                if refp < 0:
                    continue
                grid[refp][x] = True
                grid[y2][x] = False
    # print_grid()
    break

x = 0
for r in grid:
    for c in r:
        if c:
            x += 1
print(x)
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

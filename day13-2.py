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

SIZE = 2000
grid = [[False] * SIZE for i in range(SIZE)]
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

width = SIZE
height = SIZE
# print_grid()
print(folds)
for axis, pos in folds:
    print(axis, pos)
    if axis == 'x':
        for x2 in range(pos + 1, width):
            for y in range(height):
                if not grid[y][x2]:
                    continue
                refp = pos - (x2 - (pos))
                grid[y][refp] = True
                grid[y][x2] = False
                width = pos + 1
    elif axis == 'y':
        for y2 in range(pos + 1, height):
            for x in range(width):
                if not grid[y2][x]:
                    continue
                refp = pos - (y2 - (pos))
                # print(x, y2)
                # print('refp', refp)
                grid[refp][x] = True
                grid[y2][x] = False
                height = pos + 1
    # print_grid()

for r in grid[:height]:
    print(''.join(('#' if c else '.') for c in r[:width]))

print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

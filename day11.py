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

grid = []
while True:
    for l in file_lines:
        vals = [int(x) for x in list(l)]
        grid += [vals]

        if False:
            total += 1

    break

print()
print('start')
for row in grid:
    print(''.join(map(str, row)))
print()
flashes=0
for step in range(100):
    flashed = set()
    if step % 10 == 0:
        print(step)
    for row in grid:
        for x, cell in enumerate(row):
            row[x] += 1
    while True:
        print('ASDi')
        new_flashed = 0
        incd = 0
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell > 9 and (x, y) not in flashed:
                    print('FL', x, y, cell)
                    pts = [
                        (x, y-1),
                        (x, y+1),
                        (x-1, y),
                        (x+1, y),
                        (x-1, y-1),
                        (x+1, y+1),
                        (x-1, y+1),
                        (x+1, y-1),
                    ]
                    new_flashed += 1
                    for px, py in pts:
                        if px >= 0 and px < len(row) and py >= 0 and py < len(grid):
                            print('upd', px, py)
                            grid[py][px] += 1
                            if grid[py][px] > 9:
                                incd += 1
                            flashed.add((x, y))
                    print('new cent', grid[2][2])
        flashes += new_flashed
        if not incd:
            break
    for x, y in flashed:
        grid[y][x] = 0
    print()
    print('step', step)
    for row in grid:
        print(''.join(map(str, row)))
    print()
print(flashes)

print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

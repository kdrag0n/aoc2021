#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    fl = [l for l in f.read().split("\n") if l]



ilist = []
imap = {}

total = 0
result = 0
other = 0

grid = []

lines = []
while True:
    for l in fl:
        print(l)
        p1, _, p2 = l.split()
        p1 = [int(x) for x in p1.split(',')]
        p2 = [int(x) for x in p2.split(',')]

        lines += [(p1, p2)]
        if False:
            total += 1

    break

print(lines)
width = max(max([line[0][0], line[1][0]]) for line in lines) + 1
height = max(max([line[0][1], line[1][1]]) for line in lines) + 1
for y in range(height):
    grid += [[0] * width]

print('width', width, 'heght', height)
for (x1, y1), (x2, y2) in lines:
    print('DRAW', (x1, y1), (x2, y2))
    if x1 == x2:
        if y1 > y2:
            tmp = y1
            y1 = y2
            y2 = tmp
        for y in range(y1, y2 + 1):
            print('  fill', x1, y)
            grid[y][x1] += 1
    elif y1 == y2:
        if x1 > x2:
            tmp = x1
            x1 = x2
            x2 = tmp
        for x in range(x1, x2 + 1):
            print('  fill', x, y1)
            grid[y1][x] += 1
    else:
        print(' diag', (x1, y1), (x2, y2))
        xoff = 0
        for xoff in range(abs(x2 - x1) + 1):
            yoff = xoff
            if y2 - y1 < 0:
                yoff *= -1
            if x2 - x1 < 0:
                xoff *= -1
            x = x1 + xoff
            y = y1 + yoff
            print('  fill', x, y, 'xoff=', xoff, 'yoff=', yoff)
            grid[y][x] += 1

ov = 0
for row in grid:
    for cell in row:
        print(cell % 10 if cell != 0 else '.', end='')
        if cell > 1:
            ov += 1
    print()
print(ov)

print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")

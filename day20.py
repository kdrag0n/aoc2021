#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], 'r') as f:
    file_lines = [l for l in f.read().strip().split('\n')]

filt = file_lines[0]
file_lines = file_lines[2:]
in_nums = []

total = 0
result = 0
other = 0

grid = set()
while True:
    for y, l in enumerate(file_lines):
        chs = [c == '#' for c in l]
        for x, ch in enumerate(chs):
            if ch:
                grid.add((x, y))

        if False:
            total += 1

    break
nfilt = {}
for i, c in enumerate(filt):
    nfilt[i] = c == '#'
filt = nfilt


def print_grid(grid):
    if not grid:
        return
    minx = min(x for x, y in grid)
    maxx = max(x for x, y in grid)
    width=maxx-minx+1

    miny = min(y for x, y in grid)
    maxy = max(y for x, y in grid)
    height=maxy-miny+1
    grid2 = [['.']* width for i in range(height)]
    for y in range(height):
        for x in range(width):
            gx = minx + x
            gy = miny + y
            if (gx, gy) in grid:
                grid2[y][x] = '#'
            # if gx == 2 and gy == 2:
            #     grid2[y][x] = 'X'
    for row in grid2:
        print(''.join(row))
print_grid(grid)
print(grid)
def bools_to_num(bits):
    n = 0
    bns = list(range(len(bits)))[::-1]
    for i in range(len(bits)):
        n |= bits[i] << bns[i]
    return n
new_grid = set()
defer_evals = []
visited = set()
def eval_pt(x, y, defer_rnd=False):
    global defer_evals
    global new_grid
    # if (x, y) in visited:
    #     return
    pts = [
        (x-1, y-1),
        (x, y-1),
        (x+1, y-1),
        (x-1, y),
        (x, y),
        (x+1, y),
        (x-1, y+1),
        (x, y+1),
        (x+1, y+1),
    ]
    #     (x, y)
    #     (x, y-1),
    #     (x, y+1),
    #     (x-1, y),
    #     (x+1, y),
    #     (x-1, y-1),
    #     (x+1, y+1),
    #     (x-1, y+1),
    #     (x+1, y-1),
    # ]
    #scn1
    # nset = 0
    # for px, py in pts:
    #     if (px, py) in grid:
    #         nset += 1
    vs = []
    for px, py in pts:
        if (px, py) in grid:
            vs += [True]
        else:
            vs += [False]
        # if nset:
        #     defer_evals += [(px, py)]
    # if x == 2 and y == 2:
    #     print(vs)
    val = filt[bools_to_num(vs)]
    if val:
        new_grid.add((x, y))
    visited.add((x, y))

for y in range(-200, 200):
    for x in range(-200, 200):
        eval_pt(x, y)
# for x, y in grid:
#     #eval_pt(x, y)
#     pts = [
#         (x-1, y-1),
#         (x, y-1),
#         (x+1, y-1),
#         (x-1, y),
#         (x, y),
#         (x+1, y),
#         (x-1, y+1),
#         (x, y+1),
#         (x+1, y+1),
#     ]
#     for px,py in pts:
#         eval_pt(px,py)
# while defer_evals:
#     x, y = defer_evals[0]
#     defer_evals = defer_evals[1:]
#     eval_pt(x, y, defer_rnd=True)
#     pts = [
#         (x-1, y-1),
#         (x, y-1),
#         (x+1, y-1),
#         (x-1, y),
#         (x, y),
#         (x+1, y),
#         (x-1, y+1),
#         (x, y+1),
#         (x+1, y+1),
#     ]
#     for px,py in pts:
#         eval_pt(px,py)

grid = new_grid


visited = set()
new_grid = set()
defer_evals = []
# for x, y in grid:
#     #eval_pt(x, y)
#     pts = [
#         (x-1, y-1),
#         (x, y-1),
#         (x+1, y-1),
#         (x-1, y),
#         (x, y),
#         (x+1, y),
#         (x-1, y+1),
#         (x, y+1),
#         (x+1, y+1),
#     ]
#     for px,py in pts:
#         eval_pt(px,py)
# while defer_evals:
#     x, y = defer_evals[0]
#     defer_evals = defer_evals[1:]
#     eval_pt(x, y, defer_rnd=True)
#     pts = [
#         (x-1, y-1),
#         (x, y-1),
#         (x+1, y-1),
#         (x-1, y),
#         (x, y),
#         (x+1, y),
#         (x-1, y+1),
#         (x, y+1),
#         (x+1, y+1),
#     ]
#     for px,py in pts:
#         eval_pt(px,py)
for y in range(-200, 200):
    for x in range(-200, 200):
        eval_pt(x, y)

grid = new_grid


minx = min(x for x, y in grid)
maxx = max(x for x, y in grid)
width=maxx-minx+1

miny = min(y for x, y in grid)
maxy = max(y for x, y in grid)
height=maxy-miny+1
ngr = set()
for x, y in grid:
    if x > minx+1 and x < maxx-1 and y > miny+1 and y < maxy-1:
        ngr.add((x,y))
grid = ngr
print(len(grid))
print_grid(grid)
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

#!/usr/bin/env python3

import sys
from heapq import *
from typing import Collection

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], 'r') as f:
    file_lines = [l for l in f.read().strip().split('\n')]


in_nums = []

total = 0
result = 0
other = 0

grid= []
while True:
    for l in file_lines:
        row = ints(list(l))
        grid += [row]

        if False:
            total += 1

    break

tiled = [[0] * len(grid[0]) * 5 for x in range(len(grid) * 5)]
for r in tiled:
    print(''.join(map(str, r)))
for tx in range(5):
    for ty in range(5):
        st_x = tx * len(grid[0])
        st_y = ty * len(grid)
        for gy in range(len(grid)):
            for gx in range(len(grid[0])):
                nv = grid[gy][gx] + tx + ty
                while nv > 9:
                    nv -= 9
                tiled[st_y + gy][st_x + gx] = nv
grid = tiled
for r in grid:
    print(''.join(map(str, r)))
import collections
graph = collections.defaultdict(list)
nodes = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        pt = (x, y)
        w = grid[y][x]
        node = (w, x, y)
        nodes[pt] = node

        if x == 0 and y == 0:
            start_n = node
        elif x == len(grid[0])-1 and y == len(grid)-1:
            end_n = node
for y in range(len(grid)):
    for x in range(len(grid[0])):
        pts = [
            (x, y-1),
            (x, y+1),
            (x-1, y),
            (x+1, y),
        ]
        adjs = []
        node = nodes[(x, y)]
        for px, py in pts:
            if px >= 0 and px < len(grid[0]) and py >= 0 and py < len(grid):
                neigh = nodes[(px, py)]
                graph[node] += [neigh]
# print(graph)

heap = []
dist = {n: 2147483647 for n in nodes.values()}
dist[start_n] = 0
heappush(heap, (0, start_n))
while heap:
    w, n = heappop(heap)
    for neigh in graph[n]:
        neigh_dist = dist[n] + neigh[0]
        if dist[neigh] > neigh_dist:
            dist[neigh] = neigh_dist
            heappush(heap, (dist[neigh], neigh))

print(dist[end_n])

print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

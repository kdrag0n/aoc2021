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

graph = collections.defaultdict(set)

while True:
    for l in file_lines:
        frm, to = l.split('-')
        graph[frm].add(to)
        graph[to].add(frm)

        if False:
            total += 1

    break


res_paths = []
paths = [['start']]
visited = set()
while paths:
    path = paths[0]
    paths = paths[1:]
    node = path[-1]
    if node == 'end':
        print('FOUND', path)
        res_paths += [path]
    
        #if node not in visited:
            #visited.add(node)
    else:
        for p in [path + [n] for n in graph[node]]:
            smalls = collections.defaultdict(lambda: 0)
            for n in path:
                if n != 'start' and n != 'end' and all(c.islower() for c in n):
                    smalls[n] += 1
            #print(smalls    )
            if sum((1 if n == 'start' else 0) for n in path) > 1:
                continue
            if sum((1 if n == 'end' else 0) for n in path) > 1:
                continue
            if all(c < 2 for c in smalls.values()):
                paths += [p]

print(len(res_paths))
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

#!/usr/bin/env python3

import sys
import re

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], 'r') as f:
    file_lines = [l for l in f.read().strip().split('\n')]


pat = list(file_lines[0])


total = 0
result = 0
other = 0

bonds = {}
while True:
    for l in file_lines[2:]:
        pair, _, ins = l.split()
        bonds[tuple(list(pair))] = ins

        if False:
            total += 1

    break

# def rep(match):
#     pair = match.group(1)
#     return pair[0] + bonds[pair] + pair[1]
# for i in range(10):
#     pat = re.sub(r'(?=(' + '|'.join(pair for pair in bonds.keys()) + r'))', rep, pat)
#     print(pat)

import collections
for i in range(10):
    pending = []
    for i, char in enumerate(pat):
        if i == len(pat) - 1:
            break

        pair = (char, pat[i+1])
        if pair in bonds:
            # print(i, pair, bonds[pair])
            pending += [(i, bonds[pair])]
    # print()
    for i, ins in pending[::-1]:
        pat.insert(i+1, ins)
        # print(i, ins, '-', pat)
    #break
    #print(''.join(pat))

    sums = collections.defaultdict(lambda: 0)
    for c in pat:
        sums[c] += 1
    print(i, sums)
print(max(sums.values()) - min(sums.values()))
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

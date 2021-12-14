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

char_counts = collections.defaultdict(lambda: 0)
pair_counts = collections.defaultdict(lambda: 0)
for ch in pat:
    char_counts[ch] += 1
for i, char in enumerate(pat):
    if i == len(pat) - 1:
        break

    pair = (char, pat[i+1])
    if pair in bonds:
        # print(i, pair, bonds[pair])
        pair_counts[pair] += 1
print(char_counts, pair_counts)
for i in range(40):
    if i % 10 == 0:
        print(i)
    new_pairs = collections.defaultdict(lambda: 0)
    new_chars = collections.defaultdict(lambda: 0)
    for k, v in char_counts.items():
        new_chars[k] = v
    for k, v in pair_counts.items():
        new_pairs[k] = v
    for pair, cnt in pair_counts.items():
        if pair in bonds:
            new_ch = bonds[pair]
            # print(pair, '->', new_ch)
            new_chars[new_ch] += cnt
            new_pairs[pair] -= cnt
            new_pairs[(pair[0], new_ch)] += cnt
            new_pairs[(new_ch, pair[1])] += cnt
    pair_counts = new_pairs
    char_counts = new_chars


    # print(i, char_counts, pair_counts)

print(max(char_counts.values()) - min(char_counts.values()))
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

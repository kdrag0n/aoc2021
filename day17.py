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

while True:
    for l in file_lines:
        l1, l2 = l.split()

        if False:
            total += 1

    break



print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

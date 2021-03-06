#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    lines = [l for l in f.read().split("\n") if l]



ilist = []
imap = {}

total = 0
result = 0
other = 0

last = -1

while True:
    for l in lines:
        val = int(l.split()[0])

        if last != -1 and val > last:
            total += 1
        last = val

    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")

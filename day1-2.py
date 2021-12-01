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

last3 = []
last_sum3 = -1

while True:
    for l in lines:
        val = int(l.split()[0])
        print(val)
        last3.append(val)
        if len(last3) > 3:
            last3 = last3[1:]
        print(f'    last={last3}')

        lsum = sum(last3) if len(last3) == 3 else -1
        if last_sum3 != -1 and lsum > last_sum3:
            total += 1
        last_sum3 = lsum

    break



print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")

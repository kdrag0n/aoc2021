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

bit_nums = []

while True:
    for l in lines:
        l1 = l.split()[0]

        bits = [b == '1' for b in l1]
        bit_nums.append(bits)
        print(bits)

        if False:
            total += 1

    break

gamma = [False] * 12
epsilon = [False] * 12
for i in range(12):
    trues = 0
    falses = 0
    for num in bit_nums:
        if num[i]:
            trues += 1
        else:
            falses += 1
    if trues > falses:
        gamma[i] = True
        epsilon[i] = False
    else:
        gamma[i] = False
        epsilon[i] = True

gamma_dec = int(''.join(('1' if b else '0') for b in gamma), 2)
epsilon_dec = int(''.join(('1' if b else '0') for b in epsilon), 2)

print(gamma, epsilon)
print(''.join(('1' if b else '0') for b in gamma), ''.join(('1' if b else '0') for b in epsilon))
print(gamma_dec*epsilon_dec)
print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")

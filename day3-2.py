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

oxy_nums = [i for i in bit_nums]
co2_nums = [i for i in bit_nums]
for i in range(12):
    if len(oxy_nums) > 1:
        trues = 0
        falses = 0
        for num in oxy_nums:
            if num[i]:
                trues += 1
            else:
                falses += 1
        oxy_nums = [bits for bits in oxy_nums if bits[i] == (trues >= falses)]

    if len(co2_nums) > 1:
        trues = 0
        falses = 0
        for num in co2_nums:
            if num[i]:
                trues += 1
            else:
                falses += 1
        if trues < falses:
            co2_nums = [bits for bits in co2_nums if bits[i]]
        else:
            co2_nums = [bits for bits in co2_nums if not bits[i]]

print()
print(oxy_nums)
print(co2_nums)
oxy_dec = int(''.join(('1' if b else '0') for b in oxy_nums[0]), 2)
co2_dec = int(''.join(('1' if b else '0') for b in co2_nums[0]), 2)

print(oxy_dec*co2_dec)

print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")

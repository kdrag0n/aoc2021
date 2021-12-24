#!/usr/bin/env python3

import sys
# import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], 'r') as f:
    file_lines = [l for l in f.read().strip().split('\n')]


vars = {x: 0 for x in 'wxyz'}
in_nums = []

total = 0
result = 0
other = 0

insts = []
while True:
    for l in file_lines:
        parts = l.split()
        insts += [[hash(parts[0]), *parts[1:]]]
        #inst = parts[0]

        if False:
            total += 1

    break

inp_h = hash('inp')
add_h = hash('add')
mul_h = hash('mul')
div_h = hash('div')
mod_h = hash('mod')
eql_h = hash('eql')
def test_num(n):
    ds = ints(n)
    vars = {x: 0 for x in 'wxyz'}
    for parts in insts:
        # print(parts)
        inst = parts[0]
        var = parts[1]
        if inst == inp_h:
            d = ds[0]
            ds = ds[1:]
            vars[var] = d
            continue
        v2 = parts[2]
        if v2 in vars:
            v2 = vars[v2]
        else:
            v2 = int(v2)
        if inst == add_h:
            vars[var] = vars[var] + v2
        elif inst == mul_h:
            vars[var] = vars[var] * v2
        elif inst == div_h:
            if v2 == 0:
                raise ValueError(f'div 0')
            vars[var] = vars[var] // v2
        elif inst == mod_h:
            if vars[var] < 0 or v2 <= 0:
                raise ValueError('mod neg / 0')
            vars[var] = vars[var] % v2
        elif inst == eql_h:
            vars[var] = 1 if vars[var] == v2 else 0
    # print(vars)
    return (vars['z'] == 0, vars['z'])

# xvals = []
# yvals = []
# i = 0
# for n in np.linspace(11111111111111, 99999999999999, 100000, endpoint=True):
#     n = int(n)
#     s = str(n)
#     # print(s)
#     if len(s) != 14:
#         continue
#     if '0' in s:
#         if s[-1] == '0':
#             n += 1
#             s = str(n)
#         else:
#             continue
#     if i % 1000 == 0:
#         print(i)
#     xvals += [n]
#     v = test_num(s)[1]
#     yvals += [v]
#     # print(n, v)
#     if v == 0:
#         print('FOUND', v)
#     i += 1

# plt.scatter(xvals, yvals, s=1)
# plt.axhline(y=0, color='gray')
# plt.show()
while True:
    n = input('> ')
    print(test_num(n))
    print()
print(test_num('13579246899999'))

print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

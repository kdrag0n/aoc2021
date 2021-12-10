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

opn_to_cls = {'(': ')', '[': ']', '{': '}', '<': '>'}
cls_to_opn = {v: k for k, v in opn_to_cls.items()}
scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
scrs = []
while True:
    for l in file_lines:
        stk = []
        syms = list(l)
        err = False
        for sym in syms:
            if sym in list('([{<'):
                stk += [opn_to_cls[sym]]
            elif len(stk) and sym in cls_to_opn:
                if stk[-1] == sym:
                    stk.pop()
                else:
                    err = True
                    break
        if not err:
            scr = 0
            print(''.join(stk[::-1]))
            for sym in stk[::-1]:
                scr *= 5
                scr += scores[sym]
            scrs += [scr]
    break

import statistics
print(statistics.median(scrs))


print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

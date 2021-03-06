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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
while True:
    for l in file_lines:
        stk = []
        syms = list(l)
        err = False
        for sym in syms:
            print(sym)
            if sym in list('([{<'):
                stk += [opn_to_cls[sym]]
            elif len(stk) and sym in cls_to_opn:
                print(stk)
                if stk[-1] == sym:
                    stk.pop()
                else:
                    print('INV', sym)
                    err = True
                    break
        if err:
            total += scores[sym]
    break



print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

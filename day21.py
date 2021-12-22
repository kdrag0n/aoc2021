#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

STARTS = [7, 8]
#STARTS = [4,8]

die=0
rolls = 0
def roll():
    global die
    die+=1
    if die > 100:
        die = 1
    return die
p=0
p_pos = STARTS
scores = [0, 0]
while True:
    x = roll() + roll() + roll()
    rolls += 3
    pos = (p_pos[p] + x - 1) % 10 + 1
    scores[p] += pos
    p_pos[p] = pos
    print(f'p={p+1}  roll={x}  pos={pos}    sc={scores[p]}')

    if scores[0] >= 1000 or scores[1] >= 1000:
        break
    p=int(not p)

print('\n')
lose = sorted(scores)[0]
print(lose * rolls)

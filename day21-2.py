#!/usr/bin/env python3

import sys
import functools

def ints(itr):
    return [int(i) for i in itr]

STARTS = [7, 8]
STARTS = [4,8]

p_pos = STARTS
p_wins = [0, 0]
p=0
@functools.cache
def play(p, p_pos, scores, dseed=0):
    p=0
    scores = [0, 0]
    while True:
        x = roll() + roll() + roll()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    play(p, p_pos, scores, dseed=)
        pos = (p_pos[p] + x - 1) % 10 + 1
        scores[p] += pos
        p_pos[p] = pos
        print(f'p={p+1}  roll={x}  pos={pos}    sc={scores[p]}')

        if scores[0] >= 1000 or scores[1] >= 1000:
            break
        p=int(not p)
    p_wins[p] += 1

print('\n')
lose = sorted(scores)[0]
print(lose * rolls)

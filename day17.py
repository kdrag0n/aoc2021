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

X_MIN = 137
X_MAX = 171
Y_MIN = -98
Y_MAX = -73

# X_MIN = 20
# X_MAX = 30
# Y_MIN = -10
# Y_MAX = -5

x=0
y=0

dx=0
dy=0

maxy = -1e10
brk = False

for dx in range(-250, 250):
    orig_dx = dx
    for dy in range(-250, 250):
        dx = orig_dx
        orig_dy = dy
        x = 0
        y = 0
        brk = False
        #print('TRY', dx, dy)
        run_maxy = -1e10
        for step in range(1000):
            #print('x', x, 'y', y)
            x += dx
            y += dy
            dx = dx + 1 if dx < 0 else dx - 1
            dy -= 1

            if y > run_maxy:
                run_maxy = y
            
            if x >= X_MIN and x <= X_MAX and y >= Y_MIN and y <= Y_MAX:
                print('reached', orig_dx, orig_dy)
                brk = True
                break
        if brk and run_maxy > maxy:
            maxy = run_maxy

print('MAX', maxy)


print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

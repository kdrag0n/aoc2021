#!/usr/bin/env python3

import sys
import collections
import itertools

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], 'r') as f:
    file_lines = [l for l in f.read().strip().split('\n')]


in_nums = []

total = 0
result = 0
other = 0

steps = []
while True:
    for l in file_lines:
        st, pts = l.split()
        ptd = [ints(x.split('=')[1].split('..')) for x in pts.split(',')]
        steps += [(st == 'on', *ptd)]

        if False:
            total += 1

    break

class Rectangle:
    def intersection(self, other):
        a, b = self, other
        x1 = max(min(a.x1, a.x2), min(b.x1, b.x2))
        y1 = max(min(a.y1, a.y2), min(b.y1, b.y2))
        z1 = max(min(a.z1, a.z2), min(b.z1, b.z2))
        x2 = min(max(a.x1, a.x2), max(b.x1, b.x2))
        y2 = min(max(a.y1, a.y2), max(b.y1, b.y2))
        z2 = min(max(a.z1, a.z2), max(b.z1, b.z2))
        if x1<x2 and y1<y2 and z1<z2:
            return type(self)(x1, y1, z1, x2, y2, z2)
    __and__ = intersection

    def difference(self, other):
        inter = self&other
        if not inter:
            yield self
            return
        xs = {self.x1, self.x2}
        ys = {self.y1, self.y2}
        zs = {self.z1, self.z2}
        if self.x1<other.x1<self.x2: xs.add(other.x1)
        if self.x1<other.x2<self.x2: xs.add(other.x2)
        if self.y1<other.y1<self.y2: ys.add(other.y1)
        if self.y1<other.y2<self.y2: ys.add(other.y2)
        if self.z1<other.z1<self.z2: zs.add(other.z1)
        if self.z1<other.z2<self.z2: zs.add(other.z2)
        for (x1, x2), (y1, y2), (z1, z2) in itertools.product(
            pairwise(sorted(xs)), pairwise(sorted(ys)), pairwise(sorted(zs))
        ):
            rect = type(self)(x1, y1, z1, x2, y2, z2)
            if rect!=inter:
                yield rect
    __sub__ = difference

    def __init__(self, x1, y1, z1, x2, y2, z2):
        if x1>x2 or y1>y2 or z1>z2:
            raise ValueError("Coordinates are invalid")
        self.x1, self.y1, self.z1, self.x2, self.y2, self.z2 = x1, y1, z1, x2, y2, z2

    def __iter__(self):
        yield self.x1
        yield self.y1
        yield self.z1
        yield self.x2
        yield self.y2
        yield self.z2

    def __eq__(self, other):
        return isinstance(other, Rectangle) and tuple(self)==tuple(other)
    def __ne__(self, other):
        return not (self==other)

    def __repr__(self):
        return type(self).__name__+repr(tuple(self))
    def __hash__(self):
        return hash(tuple(self))


def pairwise(iterable):
    # https://docs.python.org/dev/library/itertools.html#recipes
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

rects = set()
print(steps)
grid = set()
for si, (st, (x0, x1), (y0, y1), (z0, z1)) in enumerate(steps):
    print(si)
    r = Rectangle(x0, y0, z0, x1 + 1, y1 + 1, z1 + 1)
    if st:
        new_rs = collections.deque([r])
        while new_rs:
            nr = new_rs.popleft()
            pending_inter = None
            rems = []
            found = False
            for r2i, r2 in enumerate(rects):
                inter = nr.intersection(r2)
                if not inter:
                    continue
                # print('inter', nr, r2)
                # print('int', inter)
                diff = list(r2.difference(nr)) + list(nr.difference(r2))
                # print('diff', diff)
                rems += [r2]
                pending_inter = inter
                new_rs.extend(diff)
                # vol = 0
                # for nr in r2.difference(nr):
                    # vol += (nr.x2 - nr.x1) * (nr.y2 - nr.y1) * (nr.z2 - nr.z1)
                # print(vol)
                found = True
            if not found:
                rects.add(nr)
            for r in rems:
                rects.remove(r)
            if pending_inter is not None:
                rects.add(pending_inter)
    else:
        pending = []
        rems = []
        for r2i, r2 in enumerate(rects):
            inter = r.intersection(r2)
            if not inter:
                continue
            rems += [r2]
            df = r2.difference(r)
            if df:
                pending += df
        for r in rems:
            rects.remove(r)
        rects.update(pending)
    # vol = 0
    # for r in rects:
    #     vol += (r.x2 - r.x1) * (r.y2 - r.y1) * (r.z2 - r.z1)
    # print(vol)
    # for rx0, rx1, ry0, ry1, rz0, rz1 in on_regs:
    #     if x0 >= rx0 and x1 <= rx1 and y0 >= ry0 and y1 <= ry1 and z0 >= rz0 and z1 <= rz1:
    #         # completely included
    #         continue
        
    # on_regs += [(x0, x1, y0, y1, z0, z1)]
    # for x in range(xmin, min(xmax, 50)+1):
    #     for y in range(ymin, min(ymax, 50)+1):
    #         for z in range(zmin, min(zmax, 50)+1):
    #             # if not (x >= -50 and x <= 50 and y >= -50 and y <= 50 and z >= -50 and z <= 50):
    #             #     continue
    #             # print(st, x, y, z)
    #             if st:
    #                 grid.add((x, y, z))
    #             elif (x, y, z) in grid:
    #                 grid.remove((x, y, z))
    # break

# inters = 1
# while inters > 0:
#     inters = 0
#     pending = []
#     rems = []
#     for r in rects:
#         for r2 in rects:
#             if r == r2:
#                 continue
#             inter = r.intersection(r2)
#             if inter:
#                 print('inter', r, r2)
#                 inters += 1
#                 #union
#                 pending += [inter, *r2.difference(r)]
#                 rems += [r, r2]
#     for r in rems:
#         if r in rects:
#             rects.remove(r)
#     rects.update(pending)


print(rects)
vol = 0
for r in rects:
    vol += (r.x2 - r.x1) * (r.y2 - r.y1) * (r.z2 - r.z1)
print(vol)
print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

#!/usr/bin/env python3

import sys
# from z3 import *
import itertools

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], 'r') as f:
    file_lines = [l for l in f.read().strip().split('\n')]


# file_lines = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
# file_lines = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''.split('\n')

d_segs = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}
d_segs = {k: sorted(list(v)) for k, v in d_segs.items()}
d_segs_inv = {tuple(v): k for k, v in d_segs.items()}

d_segs_len = {}
for d, segs in d_segs.items():
    dup = False
    for d2, segs2 in d_segs.items():
        if d2 != d and len(segs) == len(segs2):
            dup = True
            break
    if dup:
        continue
    
    d_segs_len[len(segs)] = d

total = 0
result = 0
other = 0

outs = []
seg_to_x = {s: i for i, s in enumerate(list('abcdefg'))}
x_to_seg = {v: k for k, v in seg_to_x.items()}

while True:
    for l in file_lines:
        ten, final = l.split(' | ')
        nums = [list(s) for s in ten.split(' ')]
        fnums = [list(s) for s in final.split(' ')]
        seg_map = {}
        segs_maps = {}
        for segs in nums:
            if len(segs) in d_segs_len:
                real_d = d_segs_len[len(segs)]
                real_segs = d_segs[real_d]
                segs_maps[tuple(segs)] = real_d #tuple(real_segs)
                # for i in range(len(segs)):
                #     cur_seg = segs[i]
                #     real_seg = real_segs[i]
                #     seg_map[cur_seg] = real_seg
        
        # for segs in fnums:
        #     if len(segs) in d_segs_len:
        #         total += 1
        # sv = Solver()
        # for cur_segs, real_segs in segs_maps.items():
        #     conds = []
        #     for s in cur_segs:
        #         src_s = IntVal(seg_to_x[s])
        #         for rs in real_segs:
        #             real_s = seg_to_x[rs]
        #             conds += [src_s == real_s]
        #     sv.add(Or(*conds))
        # sv.check()
        # print(sv.model())
        print(segs_maps)
        for p in itertools.permutations(list('abcdefg')):
            seg_map = {x_to_seg[i]: v for i, v in enumerate(p)}
            #print(f'{p} -> {seg_map}')
            
            val = True
            for segs, real_d in segs_maps.items():
                res_segs = tuple(sorted([seg_map[s] for s in segs]))
                if res_segs not in d_segs_inv or d_segs_inv[res_segs] != real_d:
                    val = False
                    break
                print(f'{segs} -> {real_d}')
            if val:
                try:
                    ds = []
                    for segs in nums:
                        res_segs = [seg_map[s] for s in segs]
                        d = d_segs_inv[tuple(sorted(res_segs))]
                        ds += [d]
                except KeyError:
                    continue
                break
        ds = []
        for segs in fnums:
            res_segs = [seg_map[s] for s in segs]
            d = d_segs_inv[tuple(sorted(res_segs))]
            ds += [d]
        print(seg_map)
        # for seg in list('abcdefg'):
        #     if seg not in seg_map:
        #         print('missing', seg)
        print(ds)
        outs += [ds]

    break


for out in outs:
    print(out)
    dec = int(''.join(map(str, out)))
    total += dec

print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

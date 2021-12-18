#!/usr/bin/env python3

import sys
import math

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], 'r') as f:
    file_lines = [eval(l) for l in f.read().strip().split('\n')]


in_nums = []

total = 0
result = 0
other = 0


n = [[[[[9,8],1],2],3],4]
n = [7,[6,[5,[4,[3,2]]]]]
n = [[6,[5,[4,[3,2]]]],1]
n = [[[[[4,3],4],4],[7,[[8,4],9]]], [1, 1]]
tried_paths = []
# def rec(path):
#     global tried_paths
#     for i, x in enumerate(path[-1][1]):
#         if isinstance(x, list):
#             new_path = path + [(i, x)]
#             tried_paths += [new_path]
#             return rec(new_path)
#     return path
import collections
Num = collections.namedtuple('Num', ['value', 'container', 'index'])
def flatten(n, out):
    # print('rec', n)
    for i, x in enumerate(n):
        if isinstance(x, list):
            flatten(x, out=out)
        else:
            out += [Num(x, n, i)]
    return out
all_tried = []
def rec(path):
    global all_tried
    level_res = []
    for i, x in enumerate(path[-1][1]):
        if isinstance(x, list):
            new_path = path + [(i, x)]
            res = rec(new_path)
            level_res += [res]
    # print('level_res', level_res)
    all_tried.extend(level_res)
    if level_res:
        return level_res[0]
    return path
# def rec(path):
#     for i, x in enumerate(path[-1][1]):
#         if isinstance(x, list):
#             new_path = path + [(i, x)]
#             return rec()
#     return path
def first_reg(path, predicate=lambda x: True, not_past=None):
    global all_tried
    level_res = []
    for i, x in enumerate(path[-1][1]):
        if not_past is not None and x is not_past:
            return None
        elif isinstance(x, list):
            new_path = path + [(i, x)]
            res = first_reg(new_path, predicate=predicate, not_past=not_past)
            if res:
                level_res += [res]
        elif predicate(x):
            return path + [(i, x)]
    all_tried.extend(level_res)
    if level_res :
        return level_res[0]
    return None
def first_reg_rev(path, predicate=lambda x: True, not_past=None):
    print('desc', path)
    for i, x in list(enumerate(path[-1][1]))[::-1]:
        if not_past is not None and x is not_past:
            print('past')
            return None
        elif isinstance(x, list):
            return first_reg_rev(path + [(i, x)], predicate=predicate, not_past=not_past)
    for i, x in list(enumerate(path[-1][1]))[::-1]:
        if isinstance(x, int) and predicate(x):
            return path + [(i, x)]
    return None
def backtrack_path_first_reg(path):
    last_i, last_step = path[-1]
    for pi, (step_i, step_list) in list(enumerate(path[:-1]))[::-1]:
        print('desc', pi, (step_i, step_list))
        for i, x in list(enumerate(step_list)):
            print('chk', i, x)
            if i <= last_i:
                continue
            if isinstance(x, int):
                return step_list, i, x
        last_i = step_i
        last_step = step_list
    return None
def backtrack_path_first_reg_rev(path):
    # print('bk', path)
    last_i, last_step = path[-1]
    for pi, (step_i, step_list) in list(enumerate(path[:-1]))[::-1]:
        # print('desc', pi, (step_i, step_list))
        for i, x in list(enumerate(step_list))[::-1]:
            if i >= last_i:
                continue
            if isinstance(x, int):
                return step_list, i, x
        last_i = step_i
        last_step = step_list
    return None
def reduce_n(n):
    global all_tried
    while True:
        flat_n = []
        flatten(n, flat_n)
        print('flat', [x.value for x in flat_n])
        all_tried = []
        exp_path = rec([(0, n)])
        # print('e', exp_path, len(exp_path))
        # print('tried', all_tried)
        if not (len(exp_path)-1 >= 4):
            found = None
            for path in all_tried:
                if isinstance(path[-1][1], list) and len(path)-1 >= 4:
                    # print('FOUND NEW', path)
                    found = path
                    break
            if found is not None:
                exp_path = found
        if len(exp_path)-1 >= 4:
            exp_i, exp_pair = exp_path[-1]
            print('\nEXP', exp_i, exp_pair)
            exp_l, exp_r = exp_pair

            # reg_l_path = first_reg([(0, n)], not_past=exp_pair)
            # if reg_l_path is not None:
            #     print('  L', reg_l_path)
            #     reg_i, reg_num = reg_l_path[-1]
            #     reg_l_path[-2][1][reg_i] += exp_l

            # reg_r_path = first_reg_rev([(0, n)], not_past=exp_pair)
            # if reg_r_path is not None:
            #     print('  R', reg_r_path)
            #     reg_i, reg_num = reg_r_path[-1]
            #     reg_r_path[-2][1][reg_i] += exp_r

            # reg_l_data = backtrack_path_first_reg_rev(exp_path)
            # if reg_l_data is not None:
            #     print('  L', reg_l_data)
            #     reg_l_list, reg_l_i, reg_l_x = reg_l_data
            #     reg_l_list[reg_l_i] += exp_l

            # reg_r_data = backtrack_path_first_reg(exp_path)
            # if reg_r_data is not None:
            #     print('  R', reg_r_data)
            #     reg_r_list, reg_r_i, reg_r_x = reg_r_data
            #     reg_r_list[reg_r_i] += exp_r
            flat_l_i = None
            flat_l_num = None
            flat_r_i = None
            flat_r_num = None
            for i, num in enumerate(flat_n):
                if num.index == 0 and num.container is exp_pair and num.value == exp_l:
                    flat_l_i = i
                    flat_l_num = num
                if num.index == 1 and num.container is exp_pair and num.value == exp_r:
                    flat_r_i = i
                    flat_r_num = num
            print('FLAT L', flat_l_i, flat_l_num)
            print('FLAT R', flat_r_i, flat_r_num)
            if flat_l_i is not None and flat_l_i > 0:
                print('  L', flat_l_i, flat_l_num)
                reg_l_num = flat_n[flat_l_i - 1]
                reg_l_num.container[reg_l_num.index] += exp_l
            if flat_r_i is not None and flat_r_i < len(flat_n)-1:
                print('  R', flat_r_i, flat_r_num)
                reg_r_num = flat_n[flat_r_i + 1]
                reg_r_num.container[reg_r_num.index] += exp_r
            exp_path[-2][1][exp_i] = 0
            print('RES', n)
            continue

        # all_tried = []
        # first10_path = first_reg([(0, n)], predicate=lambda x: x >= 10)
        # # print('f10 tried', all_tried)
        # if first10_path is not None:
        #     print('\nSPLIT')
        #     i, num = first10_path[-1]
        #     new_pair = [num // 2, int(math.ceil(num / 2))]
        #     first10_path[-2][1][i] = new_pair
        #     print('RES', n)
        #     continue

        found10 = False
        for i, num in enumerate(flat_n):
            if num.value >= 10:
                found10 = True
                break
        if found10:
            print('\nSPLIT')
            new_pair = [num.value // 2, int(math.ceil(num.value / 2))]
            num.container[num.index] = new_pair
            print('RES', n)
            continue
        break
    print('END REC\n')

reduce_n(n)
# exit()
import copy

def calc_mag(pair):
    if isinstance(pair, int):
        return pair
    else:
        return 3 * calc_mag(pair[0]) + 2* calc_mag(pair[1])

max_mag = -1
for l1 in file_lines:
    for l2 in file_lines:
        new_val = [copy.deepcopy(l1), copy.deepcopy(l2)]
        reduce_n(new_val)
        mag = calc_mag(new_val)
        print(l1, '+', l2, '=', mag)
        if mag > max_mag:
            max_mag = mag
print('\n\nMAX MAG', max_mag)

print(f'Total: {total}')
print(f'Result: {result}')
print(f'Other: {other}')

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

def bools_to_num(bits):
    n = 0
    bns = list(range(len(bits)))[::-1]
    for i in range(len(bits)):
        n |= bits[i] << bns[i]
    return n

print('b', bin(int(file_lines[0], 16)))
#root_pkt = [x == '1' for x in bin(int(file_lines[0], 16))[2:]]
root_pkt = []
BITS = {
    '0': list('0000'),
    '1': list('0001'),
    '2': list('0010'),
    '3': list('0011'),
    '4': list('0100'),
    '5': list('0101'),
    '6': list('0110'),
    '7': list('0111'),
    '8': list('1000'),
    '9': list('1001'),
    'A': list('1010'),
    'B': list('1011'),
    'C': list('1100'),
    'D': list('1101'),
    'E': list('1110'),
    'F': list('1111'),
}
for ch in file_lines[0]:
    root_pkt += [x == '1' for x in BITS[ch]]
print(bin(bools_to_num(root_pkt)))
vers = 0
def parse_pkt(pkt):
    global vers
    print('inv - PKT', bin(bools_to_num(pkt)))
    pkt_ver = bools_to_num(pkt[:3])
    pkt_id = bools_to_num(pkt[3:6])
    payload = pkt[6:]
    used = 6

    vers += pkt_ver
    print('ver', pkt_ver)
    print('id', pkt_id)
    if pkt_id == 4:
        nbits = []
        while len(payload) >= 5:
            group = payload[:5]
            nbits += group[1:]
            payload = payload[5:]
            used += 5
            if not group[0]:
                break
        print(bools_to_num(nbits))
    else:
        len_id = payload[0]
        payload = payload[1:]
        used += 1
        print('len id', len_id)
        if not len_id:
            sub_len_bits = bools_to_num(payload[:15])
            print('sub len', sub_len_bits, bin(sub_len_bits))
            payload = payload[15:]
            used += 15

            nx_used = 0
            while len(payload) >= sub_len_bits - nx_used and len(payload) >= 6:
                new_used = parse_pkt(payload)
                payload = payload[new_used:]
                used += new_used
                nx_used += new_used
        else:
            num_subs = bools_to_num(payload[:11])
            print('num subs', num_subs)
            payload = payload[11:]
            used += 11

            for i in range(num_subs):
                new_used = parse_pkt(payload)
                payload = payload[new_used:]
                used += new_used

    print('V', vers)
    return used
parse_pkt(root_pkt)

print(f'Total: {vers}')
print(f'Result: {result}')
print(f'Other: {other}')

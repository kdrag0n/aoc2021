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
#root_pkt = root_pkt[:-6]
print(bin(bools_to_num(root_pkt)))
vers = 0
def parse_pkt(pkt):
    global vers
    orig_len = len(pkt)
    print('inv - PKT', ''.join('1' if x else '0' for x in pkt))
    pkt_ver = bools_to_num(pkt[:3])
    pkt_id = bools_to_num(pkt[3:6])
    payload = pkt[6:]

    vers += pkt_ver
    print('ver', pkt_ver)
    print('id', pkt_id)
    lit = None
    if pkt_id == 4:
        nbits = []
        while len(payload) >= 5:
            group = payload[:5]
            nbits += group[1:]
            payload = payload[5:]
            if not group[0]:
                break
        lit = bools_to_num(nbits)
        print('LIT', lit)
    else:
        len_id = payload[0]
        payload = payload[1:]
        print('len id', len_id)
        sub_lits = []
        if not len_id:
            sub_len_bits = bools_to_num(payload[:15])
            print('sub len', sub_len_bits, bin(sub_len_bits))
            payload = payload[15:]

            nx_used = 0
            while sub_len_bits - nx_used >= 6 and len(payload) >= sub_len_bits - nx_used and len(payload) >= 6:
                print('[] remp', len(payload), ' rem_bits', sub_len_bits - nx_used)
                new_used, new_lit = parse_pkt(payload)
                payload = payload[new_used:]
                nx_used += new_used

                if new_lit is not None:
                    sub_lits += [new_lit]
        else:
            num_subs = bools_to_num(payload[:11])
            print('num subs', num_subs)
            payload = payload[11:]

            for i in range(num_subs):
                if len(payload) < 6:
                    break
                new_used, new_lit = parse_pkt(payload)
                payload = payload[new_used:]

                if new_lit is not None:
                    sub_lits += [new_lit]
        
        if pkt_id == 0:
            lit = sum(sub_lits)
        elif pkt_id == 1:
            n = 1
            for x in sub_lits:
                n *= x
            lit = n
        elif pkt_id == 2:
            lit = min(sub_lits)
        elif pkt_id == 3:
            lit = max(sub_lits)
        elif pkt_id == 5:
            lit = int(sub_lits[0] > sub_lits[1])
        elif pkt_id == 6:
            lit = int(sub_lits[0] < sub_lits[1])
        elif pkt_id == 7:
            lit = int(sub_lits[0] == sub_lits[1])
        else:
            print('UNKNOWN PKT', pkt_id)
            exit()

    print('V', vers)
    return orig_len - len(payload), lit
_, final_num = parse_pkt(root_pkt)
print('FINAL', final_num)

print(f'Total: {vers}')
print(f'Result: {result}')
print(f'Other: {other}')

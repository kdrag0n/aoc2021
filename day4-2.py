#!/usr/bin/env python3

import sys

def ints(itr):
    return [int(i) for i in itr]

with open(sys.argv[1], "r") as f:
    lines = [l for l in f.read().split("\n")]



ilist = []
imap = {}

total = 0
result = 0
other = 0

nums = [int(n) for n in lines[0].split(',')]

boards = []
for bstr in '\n'.join(lines[2:]).strip().split('\n\n'):
    board = []
    for row in bstr.split('\n'):
        cols = [(int(n), False) for n in row.split()]
        board += [cols]
    boards += [board]
    #print(bstr + '\n\n\n')

remove_boards = set()
def hash_board(board):
    n = 1
    for row in board:
        for col in row:
            n += col[0]
            n *= 31
    return n
def loop():
    global winning
    global lastnum

    for num in nums:
        print('L', num)
        for board in boards:
            for row in board:
                print(row)
                for ci, (col, marked) in enumerate(row):
                    if col == num:
                        row[ci] = (col, True)
        
        for board in boards:
            if hash_board(board) in remove_boards:
                continue
            for row in board:
                if all(marked for col, marked in row):
                    print('WIN BY ROW')
                    if (len(boards) - len(remove_boards)) > 1:
                        remove_boards.add(hash_board(board))
                        break
                    else:
                        winning = board
                        outer = True
                        lastnum = num
                        return
            
            if hash_board(board) in remove_boards:
                continue
            for xi in range(5):
                n = 0
                for ri in range(5):
                    if board[ri][xi][1]:
                        n += 1
                if n == 5:
                    print('WIN BY COL')
                    if (len(boards) - len(remove_boards)) > 1:
                        remove_boards.add(hash_board(board))
                        break
                    else:
                        winning = board
                        outer = True
                        lastnum = num
                        return

loop()
s = 0
print(winning)
for row in winning:
    for ci, (col, marked) in enumerate(row):
        if not marked:
            s += col
s *= lastnum
print(s)

print(f"Total: {total}")
print(f"Result: {result}")
print(f"Other: {other}")

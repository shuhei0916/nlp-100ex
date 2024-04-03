from collections import deque
import sys

N = 10

filename = 'popular-names.txt'

def tail(N):
    buf = deque(sys.stdin, N)
    print(''.join(buf))

with open(filename) as f, \
    open('col1.txt', 'w') as f1, open('col2.txt', 'w') as f2:
    for i, line in enumerate(f):
        if i < N:
            print(line)
        else:
            break
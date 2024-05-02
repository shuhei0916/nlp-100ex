from collections import deque
import sys

N = 10

filename = './data/popular-names.txt'

# def tail(N):
#     buf = deque(sys.stdin, N)
#     print(''.join(buf))

# readlines()で全行をメモリに読み込んでから処理するやり方。メモリ効率は悪い
# with open(filename) as f:
#     l = f.readlines()
#     l = l[-N:]
    
#     for i, line in enumerate(l):
#         if i < N:
#             print(line, end="")
#         else:
#             break
        
        
d = deque(['l', 'm', 'n'], 2)
print(d)
        
# with open(filename) as f:
#     d = deque(f, N)
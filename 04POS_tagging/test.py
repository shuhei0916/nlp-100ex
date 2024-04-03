from itertools import groupby
a = [1, 1, 1, 0, 0, 1]

for k, g in groupby(a):
    print(k, list(g))
N = 10

filename = './data/popular-names.txt'

with open(filename) as f, \
    open('col1.txt', 'w') as f1, open('col2.txt', 'w') as f2:
    for i, line in enumerate(f):
        if i < N:
            print(line, end="")
        else:
            break
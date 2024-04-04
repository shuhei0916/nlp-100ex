N = 10

filename = './data/popular-names.txt'

with open(filename) as f: 
    for i, line in enumerate(f):
        if i < N:
            print(line, end="")
        else:
            break
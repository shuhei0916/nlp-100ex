filename = 'popular-names.txt'

with open(filename) as f:
    for line in f:
        print(line.replace('\t', ' '), end = '')

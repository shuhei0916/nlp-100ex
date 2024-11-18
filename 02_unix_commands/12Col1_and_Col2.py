filename = './data/popular-names.txt'

with open(filename) as f, \
    open('./data/col1.txt', 'w') as f1, open('./data/col2.txt', 'w') as f2:
    for line in f:
        cols = line.rstrip('\n').split('\t')
        # print(line.replace('\t', ' '), end = '')
        f1.write(cols[0] + ('\n'))
        f2.write(cols[1] + ('\n'))


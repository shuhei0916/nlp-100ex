filename = './data/popular-names.txt'

with open('./data/col1.txt') as f1, open('./data/col2.txt') as f2, \
    open('./data/merge.txt', 'w') as m:
    for line1, line2 in zip(f1, f2):
        m.write(line1.rstrip('\n') + '\t' + line2.rstrip('\n') + '\n')

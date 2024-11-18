filename = './data/popular-names.txt'

counter = 0
with open(filename) as f:
    lines = f.readlines()
    count = len(lines)
    print(count)
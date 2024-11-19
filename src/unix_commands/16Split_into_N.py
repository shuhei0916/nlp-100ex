N = 10

def main():
    filename = './data/popular-names.txt'
    with open(filename) as f:
        counter = 0
        for line in f:
            print(line)
            counter += 1
        print(counter)
        div = counter / 10
        print(div)


    with open(filename) as f:
        for i in range(N):
            start = int(i * div)
            end = int((i + 1) * div -1)
            print(f'{i} start: {start}, end: {end}')
            with open(f'./data/split_files/popular-names_split{i:02}.txt', 'w') as fo:
                for _ in range(start, end):
                    fo.write(f.readline())

if __name__ =='__main__':
    main()
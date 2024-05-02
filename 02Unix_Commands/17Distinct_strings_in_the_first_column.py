def main():
    filename = './data/popular-names.txt'
    print('hehe')
    with open(filename) as fi:
        for line in fi:
            names = {line.split('\t')[0]}
    print(names)


if __name__ =='__main__':
    main()
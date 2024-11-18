def main():
    filename = './data/popular-names.txt'
    unique_names = set()
    with open(filename) as f:
        for line in f:
            name = line.split(' ')[0]
            unique_names.add(name)
            # print(name)
            # print(type(name))
    print(unique_names)


if __name__ =='__main__':
    main()
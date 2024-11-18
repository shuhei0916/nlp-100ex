def main():
    filename = './data/popular-names.txt'
    with open(filename, 'r') as f:
        a_list = []
        for line in f:
            a_list.append(line.rstrip('\n').split(' '))
            # print(a_list)
    
    # print(a_list)
    sorted_list = sorted(a_list, key=lambda x: int(x[2]), reverse=True)
    print(sorted_list[:10])
    

if __name__ =='__main__':
    main()
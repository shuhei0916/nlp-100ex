def main():
    filename = './data/popular-names.txt'
    with open(filename, 'r') as fi:
        a_list = []
        for i, line in enumerate(fi):
            a_list.append(line.rstrip('\n').split('\t'))
            # print(a_list)
    
    print(a_list)
    print(sorted(a_list, key = lambda name: name[2]))


def sort_test():
    print(sorted([5, 2, 3, 1, 4]))
    s = "This i a test string from Andrew"
    print("This i a test string from Andrew".split())
    print(sorted(s.split(), key = str.lower))

    student_tuples = [
        ('john', 'A', 15), 
        ('jane', 'B', 12), 
        ('dave', 'B', 10), 
    ]
    print(sorted(student_tuples, key=lambda student: student[2]))


if __name__ =='__main__':
    main()
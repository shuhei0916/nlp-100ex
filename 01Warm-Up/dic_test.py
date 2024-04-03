def ngram(seq, n):
    lis = []
    for i in range(len(seq) - n + 1):
        lis.append(seq[i: i + n])
    return lis

if __name__ == '__main__':
    dic = {'I':141, 'you':112}

    print(dic)

    print(dic['I'])

    dic['have'] = 256
    print(dic)
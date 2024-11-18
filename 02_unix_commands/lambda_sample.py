l = ['Charlie', 'Bob', 'Alice']

print((lambda x : x[1])('Alice'))

# 2番目のアルファベット順にソート
l_sorted_second = sorted(l, key=lambda x: x[1])
print(l_sorted_second)
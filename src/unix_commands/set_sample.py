
# setオブジェクトの生成
s = {3, 1, 2, 2, 3, 1, 4}
print(s) # 重複する値は無視される。setは順序を持たない

print(type(s))

s = {i**2 for i in range(10)}
print(s)
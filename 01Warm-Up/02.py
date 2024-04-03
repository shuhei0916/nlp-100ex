# -*- coding: utf-8 -*-
"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」Permalink
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""
s1 = "パトカー"
s2 = "タクシー"

for i in range(len(s1)):
    print(s1[i] + s2[i], end = '')


print('\n別解↓')
for i, j in zip(s1, s2):
    print(i + j, end = '')

print('\n')
a = 'a'
b = 'b'
t = a, b
print(t)

x, y = t
print(x)
print(y)
print(x, y)

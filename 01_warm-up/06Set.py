# -*- coding: utf-8 -*-
"""
06. 集合Permalink
“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""
from dic_test import ngram

def ngram2(seq, n):
    lis = []
    for i in range(len(seq) - n + 1):
        lis.append(seq[i: i + n])
    return lis

x = set(ngram('paraparaparadise', 2))
y = set(ngram('paragraph', 2))
print(x | y)
print(x & y)
print(x - y)
print(y - x)
print('se' in x)
print('se' in y)


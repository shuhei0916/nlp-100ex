# -*- coding: utf-8 -*-
"""
05. n-gramPermalink
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""
str = "I am NLPer"

def ngram(seq, n):
    lis = []
    for i in range(len(seq) - n + 1):
        lis.append(seq[i: i + n])
    return lis

if __name__ == '__main__':
    sent = "I am NLPer"
    words = sent.split(' ')
    lis = ngram(words, 2)
    print(lis)
    lis = ngram(sent, 2)
    print(lis)
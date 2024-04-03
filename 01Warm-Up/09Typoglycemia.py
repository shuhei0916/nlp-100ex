# -*- coding: utf-8 -*-
"""
09. TypoglycemiaPermalink
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．
"""
import random

str = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind."

print(''.join(random.sample(str, len(str))))

sentence_list = []

# print(str.split(' '))

# for i in str.split(' '):
    # print(i)
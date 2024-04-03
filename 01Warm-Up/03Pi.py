# -*- coding: utf-8 -*-
"""
03. 円周率Permalink
“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

tokens = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.".split()
print(tokens)

#　オーソドックスなやり方
num_list = []
for token in tokens:
    num_list.append(len(token.rstrip('.,')))
print(num_list)

#　リスト内包表記
print('\n\nList')
stripped_list = [len(token.rstrip('.,')) for token in tokens]
print(stripped_list)

# ジェネレータ式
print('\n\nGenerator')
stripped_iter = (len(token.rstrip('.,')) for token in tokens)

for token in stripped_iter:
    print(token, end = ' ')


print('\n\nGenerator Function')
#　ジェネレータ関数
def token2lengths(tokens):
    for token in tokens:
        yield len(token.rstrip('.,'))

for token in token2lengths(tokens):
    print(token, end = ' ')
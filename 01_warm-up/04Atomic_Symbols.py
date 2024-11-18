# -*- coding: utf-8 -*-
"""
04. 元素記号Permalink
“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

atomic_list_sample = {"H" : 1, "He" : 2}
# print(atomic_list_sample["H"])

atomic_list = {}
one_ch = [1, 5, 6, 7, 8, 9, 15, 16, 19]

for i, name in enumerate(str.split(' ')):
    if ((i + 1) in one_ch):
        ans = name[:1:]
    else:
        ans = name[:2:]
    # print(name[:2:])
    atomic_list.update({ans:i + 1})
    
print(atomic_list)
    

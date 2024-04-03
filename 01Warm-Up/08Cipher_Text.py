# -*- coding: utf-8 -*-
"""
08. 暗号文Permalink
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

def cipher(txt):
    rep = []
    for i in txt:
        if ord(i) >= 97 and ord(i) <= 122:
            rep.append(chr(219 - ord(i)))
        else:
            rep.append(i)
    # print(rep)
    return ''.join(rep)
        

message = 'the quick brown fox jumps over the lazy dog'
message = cipher(message)
print(message)

message = cipher(message)
print(message)
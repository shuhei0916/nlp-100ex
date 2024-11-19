# -*- coding: utf-8 -*-
"""
07. テンプレートによる文生成Permalink
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
"""
def generate_sentence(x, y, z):
    print(str(x) + "時の" + str(y) + "は" + str(z))
    print('{}時の{}は{}'.format(x, y, z))
    print(f'{x}時の{y}は{z}')
    

generate_sentence(12,"気温", 22.4)
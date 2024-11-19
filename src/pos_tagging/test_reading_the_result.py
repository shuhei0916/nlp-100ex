import unittest
from morph_analyzer import read_mecab_file

class TestMecabParser(unittest.TestCase):
    def test_read_mecab_file(self):
        # テスト用のサンプルデータ
        sample_data = [
            [{'surface': '吾輩', 'base': '吾輩', 'pos': '名詞', 'pos1': '代名詞'},
             {'surface': 'は', 'base': 'は', 'pos': '助詞', 'pos1': '係助詞'},
             {'surface': '猫', 'base': '猫', 'pos': '名詞', 'pos1': '一般'},
             {'surface': 'で', 'base': 'だ', 'pos': '助動詞', 'pos1': ''},
             {'surface': 'ある', 'base': 'ある', 'pos': '助動詞', 'pos1': ''}]
        ]

        # 実際の出力
        result = read_mecab_file("neko.txt.mecab")
        # 一部の行を検証（完全一致が難しい場合）
        self.assertEqual(result[0][0]['surface'], sample_data[0][0]['surface'])
        self.assertEqual(result[0][2]['base'], sample_data[0][2]['base'])
        self.assertEqual(result[0][3]['pos1'], sample_data[0][3]['pos1'])

if __name__ == '__main__':
    unittest.main()

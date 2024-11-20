import unittest
from src.pos_tagging.mecab_reader import read_mecab_file

class TestMecabParser(unittest.TestCase):
    def test_read_mecab_file(self):
        # テスト用のサンプルデータ
        sample_data = [
            [{'surface': '一', 'base': '一', 'pos': '名詞', 'pos1': '数詞'},
             {'surface': '吾輩', 'base': '吾輩', 'pos': '名詞', 'pos1': '普通名詞'},
             {'surface': 'は', 'base': 'は', 'pos': '助詞', 'pos1': '副助詞'},
             {'surface': '猫', 'base': '猫', 'pos': '名詞', 'pos1': '普通名詞'},
             {'surface': 'である', 'base': 'である', 'pos': '判定詞', 'pos1': '*'}]
        ]

        # 実際の出力
        result = read_mecab_file("./data/neko.txt.mecab")
        # 一部の行を検証
        self.assertEqual(result[0][0]['surface'], sample_data[0][0]['surface'])  # 最初の形態素「一」
        self.assertEqual(result[1][0]['surface'], sample_data[0][1]['surface'])  # 吾輩
        self.assertEqual(result[1][2]['base'], sample_data[0][2]['base'])        # は
        self.assertEqual(result[1][3]['base'], sample_data[0][3]['base'])        # 猫
        self.assertEqual(result[1][4]['pos1'], sample_data[0][4]['pos1'])        # 判定詞の品詞細分類1「*」

if __name__ == '__main__':
    unittest.main()

import unittest
import src.warm_up as wu

# 00. 文字列の逆順
class TestStringReversal(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(wu.reverse_string("stressed"), "desserts")

# 01. 「パタトクカシーー」
class TestSubstringExtraction(unittest.TestCase):
    def test_extract_odd_characters(self):
        self.assertEqual(wu.extract_old_characters("パタトクカシーー"), "パトカー")
       
# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」 
class TestInterleaveStrings(unittest.TestCase):
    def test_interleave_strings(self):
        self.assertEqual(wu.interleave_strings("パトカー", "タクシー"), "パタトクカシーー")

#  03. 円周率
class TestWordLengths(unittest.TestCase):
    def test_get_word_lengts(self):
        sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"
        expected = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
        
        self.assertEqual(wu.get_word_lengths(sentence), expected)

# 04. 元素記号
class TestElementDict(unittest.TestCase):
    def test_create_element_dict(self):
        sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
        expected_dict = {
            'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8,
            'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15,
            'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20
        }
        
        result = wu.create_element_dict(sentence)
        self.assertEqual(result, expected_dict)

# 05. n-gram
class TestNgram(unittest.TestCase):
    def test_word_bi_gram(self):
        sentence = "I am an NLPer"
        expected = [["I", "am"], ["am", "an"], ["an", "NLPer"]]
        actual = wu.ngram(sentence.split(), 2)
        self.assertEqual(actual, expected)
        
    def test_char_bi_gram(self):
        sentence = "I am an NLPer"
        expected = ["Ia", "am", "ma", "an", "nN", "NL", "LP", "Pe", "er"]
        actual = wu.ngram(sentence.replace(" ", ""), 2)
        self.assertEqual(actual, expected)

# 06. 集合
class TestBigramOperations(unittest.TestCase):
    def test_generate_bigram_set(self):
        text = "paraparaparadise"
        expected = {"pa", "ar", "ra", "ap", "di", "is", "se", "ad"}#  {"pa", "ar", "ra", "ap", "di", "is", "se"}
        result = wu.generate_bigram_set(text)
        self.assertEqual(result, expected)

    def test_set_operations(self):
        X = {"pa", "ar", "ra", "ap", "di", "is", "se"}
        Y = {"pa", "ar", "ra", "ap", "gr", "ph"}
        union = {"pa", "ar", "ra", "ap", "di", "is", "se", "gr", "ph"}
        intersection = {"pa", "ar", "ra", "ap"}
        difference = {"di", "is", "se"}
        
        self.assertEqual(X | Y, union)  # 和集合
        self.assertEqual(X & Y, intersection)  # 積集合
        self.assertEqual(X - Y, difference)  # 差集合

    def test_contains_bigram(self):
        X = {"pa", "ar", "ra", "ap", "di", "is", "se"}
        self.assertTrue("se" in X)
        self.assertFalse("se" in {"pa", "ar", "ra"})    
        
        
# 07. テンプレートによる文生成
class TestTemplateString(unittest.TestCase):
    def test_template_string(self):
        x = 12
        y = "気温"
        z = 22.4
        expected = "12時の気温は22.4"
        
        self.assertEqual(wu.template_string(x, y, z), expected)

# 08. 暗号文
class TestCipher(unittest.TestCase):
    def test_cipher(self):
        text = "the quick brown fox jumps over the lazy dog"
        expected = "gsv jfrxp yildm ulc qfnkh levi gsv ozab wlt"
        self.assertEqual(wu.cipher(text), expected)
        
        self.assertEqual(wu.cipher(expected), text)

# 09. Typoglycemia
class TestTypoglycemia(unittest.TestCase):
    def test_short_word(self):
        sentence = "I am an"
        self.assertEqual(wu.typoglycemia(sentence), "I am an")
    
    def test_typoglycemia_single_word(self):
        word = "reading"
        result = wu.typoglycemia(word)
        self.assertTrue(result.startswith("r") and result.endswith("g"))
        self.assertEqual(len(result), len(word))
        self.assertNotEqual(result[1:-1], "eadin")  # 中間部分は異なる順序になるべき

    def test_typoglycemia(self):
        text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
        result = wu.typoglycemia(text)
        words = text.split()
        result_words = result.split()
        
        # 単語数が一致していることを確認
        self.assertEqual(len(words), len(result_words))

        for word, result_word in zip(words, result_words):
            if len(word) <= 4:  # 長さが4以下の単語は並び替えられない
                self.assertEqual(word, result_word)
            else:  # 長さが4を超える単語は並び替えられる
                self.assertEqual(word[0], result_word[0])  # 先頭は同じ
                self.assertEqual(word[-1], result_word[-1])  # 末尾は同じ
                self.assertNotEqual(word[1:-1], result_word[1:-1])  # 中間が異なる
    

if __name__ == "__main__":
    unittest.main()
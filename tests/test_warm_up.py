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
    def test_union(self):
        X = set(wu.ngram("paraparaparadise", 2))
        Y = set(wu.ngram("paragraph", 2))
        expected = set(["pa", "ar", "ra", "ap", "ad", "di", "is", "se", "ag", "gr", "ph"])
        
        self.assertEqual(X | Y, expected)
        
    def test_intersection(self):
        X = set(wu.ngram("paraparaparadise", 2))
        Y = set(wu.ngram("paragraph", 2))
        expected = set(["pa", "ra", "ar", "ap"])
        
        self.assertEqual(X & Y, expected)
        
    def test_difference(self):
        X = set(wu.ngram("paraparaparadise", 2))
        Y = set(wu.ngram("paragraph", 2))
        expected = set(["ad", "di", "is", "se"])
        
        self.assertEqual(X - Y, expected)
        
    def test_contains(self):
        X = set(wu.ngram("paraparaparadise", 2))
        Y = set(wu.ngram("paragraph", 2))
        
        self.assertTrue("se" in X)
        self.assertFalse("se" in Y)

if __name__ == "__main__":
    unittest.main()
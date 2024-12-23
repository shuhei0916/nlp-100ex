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
    def test_ngram(self):
        s = "I am an NLPer"
        expected_char_bigram = ["Ia", "am", "ma", "an", "nN", "NL", "LP", "Pe", "er"]
        expected_word_bigram = ["I am", "am an", "an NLPer"]
        
        self.assertEqual(wu.ngram(s, 2, "char"), expected_char_bigram)
        self.assertEqual(wu.ngram(s, 2, "word"), expected_word_bigram) 

        
# class TestNgramSetOperations(unittest.TestCase):
#     def test_ngram_set_operations(self):
#         s1 = "paraparaparadise"
#         s2 = "paragraph"
        
#         bigram_s1 = set(wu.ngram(s1, 2, "char"))
#         bigram_s2 = set(wu.ngram(s2, 2, "char"))
        
#         union = bigram_s1 | bigram_s2
#         intersection = bigram_s1 & bigram_s2
#         difference = bigram_s1 - bigram_s2
        
#         self.assertIn("se", bigram_s1)
#         self.assertNotIn("se", bigram_s2)
        
#         expected_union = {'ar', 'ad', 'ap', 'di', 'gr', 'is', 'pa', 'ph', 'ra', 'se'}
#         expected_intersection = {'ar', 'ap', 'pa', 'ra'}
#         expected_difference = {'ad', 'di', 'is', 'se'}
        
#         self.assertEqual(union, expected_union)
#         self.assertEqual(intersection, expected_intersection)
#         self.assertEqual(difference, expected_difference)


if __name__ == "__main__":
    unittest.main()
import unittest
import src.warm_up as wu

class TestStringReversal(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(wu.reverse_string("stressed"), "desserts")
    
class TestSubstringExtraction(unittest.TestCase):
    def test_extract_odd_characters(self):
        self.assertEqual(wu.extract_old_characters("パタトクカシーー"), "パトカー")
        
class TestInterleaveStrings(unittest.TestCase):
    def test_interleave_strings(self):
        self.assertEqual(wu.interleave_strings("パトカー", "タクシー"), "パタトクカシーー")

class TestWordLengths(unittest.TestCase):
    def test_get_word_lengts(self):
        sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"
        expected = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
        
        self.assertEqual(wu.get_word_lengths(sentence), expected)


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



if __name__ == "__main__":
    unittest.main()
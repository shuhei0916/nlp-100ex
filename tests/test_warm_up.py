import unittest
from src.warm_up import reverse_string, extract_old_characters, interleave_strings, get_word_lengths

class TestStringReversal(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("stressed"), "desserts")
    
class TestSubstringExtraction(unittest.TestCase):
    def test_extract_odd_characters(self):
        self.assertEqual(extract_old_characters("パタトクカシーー"), "パトカー")
        
class TestInterleaveStrings(unittest.TestCase):
    def test_interleave_strings(self):
        self.assertEqual(interleave_strings("パトカー", "タクシー"), "パタトクカシーー")

class TestWordLengths(unittest.TestCase):
    def test_get_word_lengts(self):
        sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"
        expected = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]
        
        self.assertEqual(get_word_lengths(sentence), expected)

if __name__ == "__main__":
    unittest.main()
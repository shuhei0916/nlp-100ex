import unittest
from src.warm_up import reverse_string, extract_old_characters, interleave_strings

class TestStringReversal(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("stressed"), "desserts")
    
class TestSubstringExtraction(unittest.TestCase):
    def test_extract_odd_characters(self):
        self.assertEqual(extract_old_characters("パタトクカシーー"), "パトカー")
        
class TestInterleaveStrings(unittest.TestCase):
    def test_interleave_strings(self):
        self.assertEqual(interleave_strings("パトカー", "タクシー"), "パタトクカシーー")

if __name__ == "__main__":
    unittest.main()
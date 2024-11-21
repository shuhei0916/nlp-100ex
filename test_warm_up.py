import unittest
from src.warm_up import reverse_string

class TestStringReversal(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("stressed"), "desserts")
    
    
if __name__ == "__main__":
    unittest.main()
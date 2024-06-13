import unittest
from main import count_words

class TestCountWordsExtra(unittest.TestCase):
    def test_mixed_case(self):
        text = "Hello hello HELLO HeLLo"
        expected_output = {'hello': 4}
        self.assertEqual(count_words(text), expected_output)

if __name__ == '__main__':
    unittest.main()

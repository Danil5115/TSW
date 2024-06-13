import unittest
from main import count_words, most_common_word

class TestCountWords(unittest.TestCase):
    def test_count_words(self):
        text = "Hello world! Hello, how are you world?"
        expected_output = {
            'hello': 2,
            'world': 2,
            'how': 1,
            'are': 1,
            'you': 1
        }
        self.assertEqual(count_words(text), expected_output)

    def test_empty_string(self):
        text = ""
        expected_output = {}
        self.assertEqual(count_words(text), expected_output)

    def test_punctuation(self):
        text = "Hello! Hello."
        expected_output = {
            'hello': 2
        }
        self.assertEqual(count_words(text), expected_output)

class TestMostCommonWord(unittest.TestCase):
    def test_most_common_word(self):
        text = "Hello world! Hello, how are you world?"
        expected_output = 'hello'
        self.assertEqual(most_common_word(text), expected_output)

    def test_empty_string(self):
        text = ""
        with self.assertRaises(ValueError):
            most_common_word(text)

if __name__ == '__main__':
    unittest.main()

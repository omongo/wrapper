import unittest
from wrapper import Wrapper

class TestWrapper(unittest.TestCase):
    def test_i_am_a_programmer(self):
        actual = Wrapper.wrap('I am a programmer.', 5)
        expected = 'I am\na\nprogr\nammer\n.'
        self.assertEqual(actual, expected)

    def test_this_is_a_book(self):
        actual = Wrapper.wrap('This is a book.', 3)
        expected = 'Thi\ns\nis\na\nboo\nk.'
        self.assertEqual(actual, expected)

    def test_the_zen_of_python(self):
        actual = Wrapper.wrap('The Zen of Python, by Tim Peters', 7)
        expected = 'The\nZen of\nPython,\n by\nTim\nPeters'
        self.assertEqual(actual, expected)

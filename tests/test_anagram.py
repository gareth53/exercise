import unittest
from exercises.anagram import anagram_pair

class TestAnagramPair(unittest.TestCase):

	def test_simple_match(self):
		self.assertTrue(anagram_pair("This Is A Test", "This Is A Test"))

	def test_simple_mismatch(self):
		self.assertFalse(anagram_pair("This Is A Test", "This Is Not A Test"))

	def test_true_anagram(self):
		self.assertTrue(anagram_pair("abcdefghijklm", "mkljihgfedcba"))

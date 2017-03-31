import unittest
from exercises.anagram import SOLUTIONS


class TestAnagramPair(unittest.TestCase):

	msg = "Failed with solution #{}"

	def test_simple_match(self):
		for solution in SOLUTIONS:
			self.assertTrue(solution("This Is A Test", "This Is A Test"), self.msg.format(x+1))

	def test_simple_mismatch(self):
		for solution in SOLUTIONS:
			self.assertFalse(solution("This Is A Test", "This Is Not A Test"), self.msg.format(x+1))

	def test_true_anagram(self):
		for x, solution in enumerate(SOLUTIONS):
			self.assertTrue(solution("abcdefghijklm", "mkljihgfedcba"), self.msg.format(x+1))

	def test_repeated_characters_handled(self):
		for x, solution in enumerate(SOLUTIONS):
			self.assertTrue(solution("aaam", "maaa"), self.msg.format(x+1))
			self.assertFalse(solution("maam", "maaa"), self.msg.format(x+1))
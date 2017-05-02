import unittest
from exercises.sorting.radix_tree import RadixTree

A_WORDS = ["a", "abandon", "abandoned", "ability", "able", "about", "above", "abroad", "absence", "absent", "absolute", "absolutely", "absorb", "abuse", "abuse", "academic", "accent", "accept", "acceptable", "access", "accident", "accidental", "accidentally", "accommodation", "accompany", "according to", "account", "account for", "accurate", "accurately", "accuse", "achieve", "achievement", "acid", "acknowledge", "a couple", "acquire", "across", "act", "action", "active", "actively", "activity", "actor", "actress", "actual", "actually"]

class TestRadixTree(unittest.TestCase):

	def test_simple_creation(self):
		rt = RadixTree()
		self.assertEqual(rt.children, [])
		self.assertEqual(rt.value, "")
		self.assertEqual(rt.full_value, "")

	def test_add_word(self):
		rt = RadixTree()
		rt.add_word("Be")
		self.assertEqual(rt.children[0].value, "b")

	def test_add_word_repeated_calls(self):
		rt = RadixTree()
		self.assertTrue(rt.add_word("Bear"))
		self.assertFalse(rt.add_word("Bear"))
		self.assertTrue(rt.add_word("Bearable"))
		# this one doesnlt create new Nodes, but should stil return True
		self.assertTrue(rt.add_word("Bea"))
		self.assertFalse(rt.add_word("Bea"))

	def test_search(self):
		rt = RadixTree()
		add = rt.add_word("Gruesome")
		self.assertTrue(add)
		self.assertTrue(rt.check_word("gruesome"))
		self.assertFalse(rt.check_word("gruesomes"))

	def test_word_search_vs_prefix(self):
		rt = RadixTree()
		add = rt.add_word("Gruesome")
		self.assertTrue(rt.check_word("gruesome"))
		self.assertFalse(rt.check_word("gruesom"))
		self.assertTrue(rt.check_word("gruesom", prefix=True))

	def test_search_with_more_words(self):
		rt = RadixTree()
		for word in A_WORDS:
			rt.add_word(word)
		for term in ["accurately", "acknowledge", "actively"]:
			self.assertTrue(rt.check_word(term))
			self.assertTrue(rt.check_word(term.upper()))
import unittest
from exercises.palindrome import PalindromeFinder

class TestPDfinder(unittest.TestCase):

	def test_is_palindrome_method(self):
		pdf = PalindromeFinder()
		self.assertTrue(pdf._is_palindrome('madam'))
		self.assertTrue(pdf._is_palindrome('madadam'))
		self.assertTrue(pdf._is_palindrome('maam'))
		self.assertFalse(pdf._is_palindrome('madame'))
		self.assertFalse(pdf._is_palindrome('madamel'))
		self.assertFalse(pdf._is_palindrome('adam'))

	def test_is_palindrom_only_1st_andl_last_difference(self):
		pdf = PalindromeFinder()
		self.assertFalse(pdf._is_palindrome('letter'))


	def test_is_palindrom_short_words(self):
		pdf = PalindromeFinder()
		self.assertFalse(pdf._is_palindrome('two'))
		self.assertTrue(pdf._is_palindrome('i'))

	def test_clean_word_method(self):
		pdf = PalindromeFinder()
		self.assertEquals(pdf._clean_word("!madam"), "madam")
		self.assertEquals(pdf._clean_word("madam,"), "madam")
		self.assertEquals(pdf._clean_word("'madam',"), "madam")
		self.assertEquals(pdf._clean_word("Groovy!"), "groovy")
		self.assertEquals(pdf._clean_word("I'm"), "i'm")

	def test_finding_one_simple_palindrome(self):
		pdf = PalindromeFinder()
		self.assertEquals(pdf.find_in("madam I'm Adam"), ["madam"])

	def test_finding_two_palindromes(self):
		pdf = PalindromeFinder()
		self.assertEquals(pdf.find_in("I ama containing two three letter palindromes: dud"), ["i", "ama", "dud"])

	def test_whole_string_is_palindromes(self):
		pdf = PalindromeFinder()
		self.assertEquals(pdf.find_in("palindromeemordnilap"), ["palindromeemordnilap"])
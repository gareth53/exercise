import unittest
import math
import re
from collections import deque
"""
find the longest palindrome in a string. 
"""


class PalindromeFinder:

	def find_in(self, string):
		# loop through strings from pos 1 to len -2
		# look back, look fwd, store palindromic patterns in an list
		# return list
		palindromes = []
		words = string.split(' ')
		for word in words:
			word = self._clean_word(word)
			if self._is_palindrome(word):
				palindromes.append(word)
		return palindromes

	@staticmethod
	def _clean_word(word):
		"""
		lowercase, remove punctuation
		"""
		word = word.lower()
		# ah, this is a case for a regex
		word = re.sub(r'^[^0-9a-z]*', "", word)
		word = re.sub(r'[^0-9a-z]*$', "", word)
		return word

	@staticmethod
	def _is_palindrome(str):
		chars = deque(str)
		try:
			if chars.pop() != chars.popleft():
				return False
		except IndexError:
			return True
		return True

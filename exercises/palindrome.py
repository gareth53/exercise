import unittest
import math
import re
"""
find the longest palindrome in a string. 
"""

tests = [
	("madam I'm Adam", 										["madam"]), 				# one palindrome
	("I ama containing two three letter palindromes: dud", 	["ama", 'dud']),			# two
	("palindromeemordnilap", 								["palindromeemordnilap"]), 	# whole string
	("A longnol palindrom and a short oneno", 				["longnol"]),				# two palindroms, one longer
	("pop dood mum, eve",									['dood']),								
]


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
		strlen = len(str)
		midpoint_lft = midpoint_rght = int(math.ceil(strlen/2))
		even = strlen % 2
		if not even:
			midpoint_lft -= 1
		for x in range(0, midpoint_lft+1):
			back  = str[midpoint_lft-x]
			forwd = str[midpoint_rght+x]
			if back != forwd:
				return False
		return True






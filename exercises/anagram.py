"""
what's the most performant way of determing whether a string is a permutation of a second string?
"""

def anagram_pair(str1, str2):
	if len(str1) != len(str2):
		return False
	if str1 == str2:
		return True

	def sorted_list(string):
		ord = list(string)
		ord.sort()
		return ord

	if sorted_list(str1) == sorted_list(str2):
		return True

	return False

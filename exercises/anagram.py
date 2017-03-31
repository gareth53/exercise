"""
BOOK: "Cracking The Coding Interview" by Gayle Laakman McDowell
P90
what's the most performant way of determing whether a string is a permutation of a second string?

HINTS:
#44:  try a hash table
#84:  one solution is O(N log N) another is O(N) but uses more space 
#122: could a hash table be useful?
#131: can you make the orders the same?
"""
import timeit
from datetime import datetime


def do_basic_checks(func):

	def func_wrapper(str1, str2):
		if str1 == str2:
			return True

		if len(str1) != len(str2):
			return False

		return func(str1, str2)

	return func_wrapper

@do_basic_checks
def anagram_pair_simple(str1, str2):
	return sorted(str1) == sorted(str2)


@do_basic_checks
def anagram_pair(str1, str2):

	def sorted_list(string):
		li = list(string)
		li.sort()
		return li

	if sorted_list(str1) == sorted_list(str2):
		return True

	return False

@do_basic_checks
def anagram_pair_hashtable_try(str1, str2):
	ht = {}
	for char in str1:
		ht.setdefault(char, 0)
		ht[char] = ht[char] + 1
	for char in str2:
		try:
			ht[char] = ht[char] - 1
			if ht[char] < 0:
				return False
		except KeyError:
			return False
	if sum(ht.values()) > 0:
		return False
	return True

@do_basic_checks
def anagram_pair_hashtable_get(str1, str2):
	ht = {}
	for char in str1:
		count = ht.get(char, 0)
		ht[char] = count + 1
	for char in str2:
		if ht.get(char, -1) < 0:
			return False
		ht[char] = ht[char] - 1
	if sum(ht.values()) > 0:
		return False
	return True

@do_basic_checks
def anagram_pair_find_and_replace(str1, str2):
	for char in str2:
		found = str1.find(char)
		if found == -1:
			return False
		str1 = str1[:found] + str1[found+1:]
	if str1 == "":
		return True
	return False

@do_basic_checks
def anagram_pair_replace(str1, str2):
	for x, char in enumerate(str1):
		pre_replace = str1 + ""
		str1 = str1.replace(char, "", 1)
	if str1 == pre_replace:
		return False
	return True


@do_basic_checks
def anagram_pair_manual_list_build(str1, str2):
	"""
	assume str1 and str2 are equal length
	"""
	arr1 = []
	arr2 = []
	for x in range(0, len(str1)):
		arr1.append(str1[x])
		arr2.append(str2[x])
	arr1.sort()
	arr2.sort()
	if arr1 == arr2:
		return True
	return False

@do_basic_checks
def anagram_pair_list_comprehension(str1, str2):
	"""
	assume str1 and str2 are equal length
	"""
	arr1 = [x for x in str1]
	arr2 = [y for y in str2]
	arr1.sort()
	arr2.sort()
	if arr1 == arr2:
		return True
	return False


SOLUTIONS = (
	anagram_pair,
	anagram_pair_simple,
	anagram_pair_hashtable_try,
	anagram_pair_hashtable_get,
	anagram_pair_find_and_replace,
	anagram_pair_replace,
	anagram_pair_manual_list_build,
	anagram_pair_list_comprehension
)



# For comparing performance
def test(func, tests=1):
	st = datetime.now()
	ROOT = "abcdefg"
	ANAG = "cbagfed"
	NOT =  "abcdefh"

	testcases = [
		(ROOT, ROOT),
		(ROOT * 200, ROOT * 200),
		(ROOT * 300, ROOT * 300),
		(ROOT, ANAG),
		(ROOT * 200, ANAG * 200),
		(ROOT * 300, ANAG * 300),
		(ROOT, NOT),
		(ROOT * 200, NOT * 200),
		(ROOT * 300, NOT * 300),
	]
	for t in testcases * tests:
		func(t[0], t[1])
	end = datetime.now()
	total = (end - st).total_seconds()
	return total

if __name__ == "__main__":
	for x, func in enumerate(SOLUTIONS):
		print(x, test(func, 1000))
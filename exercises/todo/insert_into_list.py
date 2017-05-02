import math



# taks: add an entry to the list at the correct point
# this is an implementation of a binary search

def insert(list, val):
	"""
	return li with val inserted at correct point
	"""
	def get_comparison_indices(start, stop):
		# return tow values to compare
		diff = stop - start
		midpoint = stop + int(diff/2)
		return midpoint, midpoint+1

	examine = int(len(list)/2)

	compare1 = list[examine]
	compare2 = list[examine+1]
	if val < compare2 and val < compare1:
		#val needs to go left

	if val > compare2 and val > compare1:
		#val needs to go right

	if val >= compare1 and val <= compare2:
		#val goes between these two
		return list[:compare1] + [val] + list[compare1:]
	return list





def check_order(list):
	for x in range(1, len(list)):
		if list[x-1] > list[x]:
			return False
	return True

import unittest


class TestCheckOrder(unittest.TestCase):

	def test_simple(self):
		assert check_order([1,2,3,4,5]) == True

	def test_simple2(self):
		assert check_order([1,1,1,1]) == True

	def test_fail(self):
		assert check_order([1,2,1,4,5]) == False

	def test_fail2(self):
		assert check_order([1,2,3,4,3]) == False


class TestInsert(unittest.TestCase):

	def test_simple(self):
		li = [0, 11, 22, 33, 44, 55, 66, 78, 89, 90, 110, 120, 130, 140]
		val = 60
		res = insert(li, val)
		assert len(res) == len(li) + 1



if __name__ == "__main__":
	unittest.main()

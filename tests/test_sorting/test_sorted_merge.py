from unittest import TestCase

from exercises.sorting.combine_sorted_lists import sorted_merge


class TestSortedMerge(TestCase):

	def test_simple_list_addition(self):
		a = [0, 1, 2, 3, 4]
		b = [5, 6, 7, 8, 9]
		c = sorted_merge(a, b)

		self.assertEqual(c, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
		self.assertEqual(b, [5, 6, 7, 8, 9])

	def test_simple_list_addition2(self):
		a = [10, 11, 12, 13, 14]
		b = [5, 6, 7, 8, 9]
		c = sorted_merge(a, b)

		self.assertEqual(c, [5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
		self.assertEqual(a, [10, 11, 12, 13, 14])
		self.assertEqual(b, [5, 6, 7, 8, 9])

	def test_simple_insert(self):
		a = [10, 20]
		b = [15]
		c = sorted_merge(a, b)
		self.assertEqual(c, [10, 15, 20])

	def test_simple_multiple_inserts(self):
		a = [10, 20]
		b = [15, 16, 17, 18, 19]
		c = sorted_merge(a, b)
		self.assertEqual(c, [10, 15, 16, 17, 18, 19, 20])

	def test_leftover_elements_added(self):
		a = [10, 20]
		b = [15, 30, 40]
		c = sorted_merge(a, b)
		self.assertEqual(c, [10, 15, 20, 30, 40])

	def test_second_list_starts_lower(self):
		a = [10, 20]
		b = [5, 15, 25]
		c = sorted_merge(a, b)
		self.assertEqual(c, [5, 10, 15, 20, 25])

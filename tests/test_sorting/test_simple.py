import unittest
from exercises.sorting.implementations import bubblesort, selectionsort, mergesort

class TestBubbleSorter(unittest.TestCase):

	def test_simple_ints(self):
		simple = [2, 7, 3, 1, 9, 12, 6, 8, 9, 2, 4, 3, 8, 9, 12, 12, 1]
		actual = bubblesort(simple)
		self.assertEqual(actual, sorted(simple))


class TestSelectionSorter(unittest.TestCase):

	def test_simple_ints(self):
		simple = [2, 7, 3, 1, 9, 12, 6, 8, 9, 2, 4, 3, 8, 9, 12, 12, 1]
		actual = selectionsort(simple)
		self.assertEqual(actual, sorted(simple))


class TestMergeSort(unittest.TestCase):

	def test_simple_ints(self):
		simple = [2, 7, 3, 1, 9, 12, 6, 8, 9, 2, 4, 3, 8, 9, 12, 12, 1]
		actual = mergesort(simple)
		self.assertEqual(actual, sorted(simple))


import unittest
import random
from exercises.sorting.implementations import bubblesort, selectionsort, mergesort, sort_dict

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


class TestDictSort(unittest.TestCase):
	
	def setUp(self):
		self.data = [{'id': int(random.random() * 10), 'name': 'data%s' % x} for x in range(1, 11)]

	def test_simple_int_key(self):
		sorted_data = sort_dict(self.data, 'id')
		last = None
		for d in sorted_data:
			if last is not None:
				self.assertTrue(d['id'] >= last)
			last = d['id']

	def test_text_key(self):
		sorted_data = sort_dict(self.data, 'name')
		last = None
		for d in sorted_data:
			if last is not None:
				self.assertTrue(d['name'] >= last)
			last = d['name']

	def test_combining_keys(self):
		li = [
			{
				'date': '2017-08-22',
				'name': 'Aardvaark'
			},
			{
				'date': '2017-08-21',
				'name': 'Horse'
			},
			{
				'date': '2017-08-21',
				'name': 'Zebra'
			},
			{
				'date': '2017-08-22',
				'name': 'Wolf'
			}
		]
		expected_order = ('Horse', 'Zebra', 'Aardvaark', 'Wolf')
		ordered_dict = sort_dict(li, sort_keys=['date', 'name'])
		for x, d in enumerate(ordered_dict):
			self.assertEqual(expected_order[x], d['name'])

	def test_no_sort_spec_supplied(self):
		data = [{'foo': True}, {'bar': False}, {'grr': 0}, {'trump': []}]
		sorted_data = sort_dict(data)
		self.assertEqual(data, sorted_data)


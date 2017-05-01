from unittest import TestCase

from exercises.sorting.heap import Heap


class TestHeap(TestCase):

	def test_pop(self):
		heap = Heap([1, 3, 5, 7, 0, 2, 4, 6])
		self.assertEqual(heap.pop(), 0)

	def test_push(self):
		heap = Heap([1, 3, 5])
		self.assertEqual(heap.push(2), 4)

	def test_push_pop(self):
		heap = Heap()
		for x in range(0, 50, 10):
			heap.push(x)
		for x in range(60, 35, -5):
			heap.push(x)
		self.assertEqual(heap.pop(), 0)

	def test_string(self):
		heap = Heap()
		for x in [0, 2, 8, 100, 10, 90, 16, 50, 25, 200]:
			heap.push(x)
		self.assertEqual(str(heap), '[0, 2, 8, 25, 10, 90, 16, 100, 50, 200]')

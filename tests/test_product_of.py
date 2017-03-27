import unittest
from exercises.product_of import get_products_tuned, get_products


class TestProductOf():

	@staticmethod
	def func_under_test(data):
		raise NotImplementedError

	def test_given_example(self):
		data = [1, 7, 3, 4]
		expect = [84, 12, 28, 21]
		self.assertEqual(self.func_under_test(data), expect)

	def test_list_contains_a_zero(self):
		data = [2, 2, 0, 2]
		expect = [0, 0, 8, 0]
		self.assertEqual(self.func_under_test(data), expect)

	def test_list_has_1_item(self):
		data = [2],
		expect = []
		self.assertEqual(self.func_under_test(data), expect)

	def test_empty_list(self):
		data = [],
		expect = []
		self.assertEqual(self.func_under_test(data), expect)


class TestDumbSolution(unittest.TestCase, TestProductOf):

	@staticmethod
	def func_under_test(data):
		return get_products(data)


class TestTunedSolution(unittest.TestCase, TestProductOf):

	@staticmethod
	def func_under_test(data):
		return get_products_tuned(data)

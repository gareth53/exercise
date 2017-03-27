import unittest
from exercises.highest_product import get_highest_product, get_highest_product2


class TestHighestProduct():

	@staticmethod
	def func_under_test(data):
		raise NotImplementedError

	def test_simplest_example(self):
		data = [0, 1, 2, 3]
		expect = 6

	def test_shortest_list_a_zero_kaiboshes_all(self):
		data = [0, 1, 2]
		expect = 0

	def test_shortest_list_with_a_negative_number(self):
		data = [-1, 1, 2]
		expect = -2

	def test_negative_numbers(self):
		data = [-10, -10, 1, 2, 3]
		expect = 300

	def test_long_list(self):
		data = [0, 1, 2, 3]
		expect = 6

	def test_list_with_descending_values(self):
		input =[10, 9, 2, 1]
		expect =180

	def test_really_long_list(self):
		data = 20 * [10, 9, 2, 1]
		expect = 1000


class TestDumbSolution(unittest.TestCase, TestHighestProduct):

	@staticmethod
	def func_under_test(data):
		return get_highest_product(data)


class TestTunedSolution(unittest.TestCase, TestHighestProduct):

	@staticmethod
	def func_under_test(data):
		return get_highest_product2(data)
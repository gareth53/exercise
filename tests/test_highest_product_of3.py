import unittest
from exercises.product_of_3 import highest_product_of3


class TestHighestProductOf3(unittest.TestCase):

	def test_given_example(self):
		"""
		given [-10, -10, 1, 3, 2] we should return 300 (which we get by taking -10 * -10 * 3).
		"""
		data = [-10, -10, 1, 3, 2]
		expct = 300
		self.assertEqual(highest_product_of3(data), expct)


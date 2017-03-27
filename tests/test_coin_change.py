import unittest
from exercises.coin_change import ChangeCalculator


class TestMethodGetBiggestCoins(unittest.TestCase):

	def test_simple(self):
		denominations = [1, 2]
		amount = 4
		expect = [2, 2], 0
		cc = ChangeCalculator(denominations)
		self.assertEqual(cc._get_biggest_coins(denominations, amount), expect)

	def test_leftovers(self):
		denominations = [1, 2]
		amount = 7
		expect = [2, 2, 2], 1
		cc = ChangeCalculator(denominations)
		self.assertEqual(cc._get_biggest_coins(denominations, amount), expect)


class TestMethodGetBestSolution(unittest.TestCase):

	def test_simple_2coin_solution(self):
		denominations = [1, 2]
		amount = 7
		expect = [2, 2, 2, 1]
		cc = ChangeCalculator(denominations)
		self.assertEqual(cc._get_best_solution(amount), expect)


	def test_multi_coin_solution(self):
		denominations = [1, 2, 5, 10, 20, 50, 100]
		amount = 198
		expect = [100, 50, 20, 20, 5, 2, 1]
		cc = ChangeCalculator(denominations)
		self.assertEqual(cc._get_best_solution(amount), expect)


class TestSolution:
	def test_simple2(self):
		assert True
#		'denominations': [1, 2],
#		'amount': 5,
#		'expect': 4,
#		'workings': """
#			1 1 1 1 1
#			2 1 1 1
#			2 2 1
#			5
#		"""
#	},
#	{
	def test_simple_GBP_example(self):
		assert True
#		'denominations': [1, 2, 5, 10, 20, 50, 100, 200],
#		'amount': 12,
#		'expect': 15,
#		'workings': """
#			1 1 1 1 1 1 1 1 1 1 1 1
#			2 1 1 1 1 1 1 1 1 1 1
#			2 2 1 1 1 1 1 1 1 1
#			2 2 2 1 1 1 1 1 1
#			2 2 2 2 1 1 1 1
#			2 2 2 2 2 1 1
#			2 2 2 2 2 2
#			5 1 1 1 1 1 1 1
#			5 2 1 1 1 1 1
#			5 2 2 1 1 1
#			5 2 2 2 1
#			5 5 1 1
#			5 5 2
#			10 1 1
#			10 2
#		"""
#	},

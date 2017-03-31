"""
Imagine you landed a new job as a cashier...
Your quirky boss found out that you're a programmer and has a weird request about something they've 
been wondering for a long time.

Write a function that, given:

- an amount of money
- a list of coin denominations
- computes the number of ways to make amount of money with coins of the available denominations.

Example: for amount=44 (44p) and denominations=[1,2,3] (1p, 2p and 3p), 
your program would output 44 - the number of ways to make 44p with those denominations:

1 = 44 x 1p
2 = 42 x 1p, 1 x 2p
3 = 40 x 1p, 2 x 2p
...
12 = 2 x 1p, 21 x 2p
13 = 0 x 1p, 22 x 2p

14 = 41 x 1p, 1 x 3p
15 = 38 x 1p, 2 x 3p
...
26 =  6 x 1p, 13 x 3p
27 =  3 x 1p, 14 x 3p

28 = 14 x 3p, 1 x 2p


Example: for the ammout 12p and denominations [1, 2, 5]

1 = 12 x 1
2 = 10 x 1, 1 x 2
3 = 8 x 1, 2 x 2
4 = 6 x 1, 3 x 2
5 = 4 x 1, 4 x 2
6 = 2 x 1, 5 x 2

7 = 6 x 2

8 = 2 x 5, 2 x 1
9 = 2 x 5, 1 x 2
10 = 1 x 5, 3 x 2, 1 x 1
11 = 1 x 5, 2 x 2, 3 x 1
12 = 1 x 5, 1 x 2, 5 x 1



"""

import copy

class ChangeCalculator:

	def __init__(self, denominations):
		denominations.sort()
		denominations.reverse()
		# TODO: this on a single pass
		self.denominations = denominations
		self.coin_substitutions = {}

	def _generate_coin_substitutions(self)
		"""
		first cut: how can coins be replaced by the 2 next smallest currencies?
		we want the output to look so:
		{
			1: [],
			2: [[1, 1]],
			5: [[2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]],
			10:[[5, 5], [2, 2, 2, 2, 2]],
			20:[[10, 10], [10, 5, 5], [5, 5, 5, 5],
			50:[[20, 20, 10], [20, 10, 10, 10]]
		}
		we could then generate all possible replacements of a coin with a recursive calculation
		"""
		coin_map = {}
		subs = []
		return coin_map

	def _generate_coin_substitution(self, coin)
		"""
		"""
		return []

	def get_all_combinations(self, target):
		return []

	def _replace_coins(self, coins):
		"""
		replace all the occurrences of the larger coins
		with all potential smaler patterns
		"""
		return coins

	def _get_biggest_coins(self, denominations, target):
		"""
		gets the biggest coins + leftover
		"""
		for val in denominations:
			if val <= target:
				coins = [val] * (target/val)
				leftover = target % val
				return coins, leftover
		raise Exception("Something bad. Assumptions incorrect. No 1p coin?")

	def _get_best_solution(self, target):
		"""
		calculate the number of combinations of numbers that would
		add up to the target

		assume: denominations are highest value first
		assume: we always have a 1p coin
		"""
		all_coins = []
		leftover = target
		denominations = copy.copy(self.denominations)
		while leftover > 0:
			coins, leftover = self._get_biggest_coins(denominations, leftover)
			all_coins =  all_coins + coins
			if leftover == 0:
				return all_coins
			# remove biggest coin
			denominations = denominations[1:]
		return all_coins

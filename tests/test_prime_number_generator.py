import unittest
from exercises.prime_number_generator import PrimeGenerator

KNOWN_PRIMES = [
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 
83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 
179, 181, 191, 193, 197, 199
]


class TestPrimeGenerator(unittest.TestCase):

	def setUp(self):
		self.g = PrimeGenerator()

	def test_with_pregenerated_primes(self):
		res = self.g.generate(0, 11)
		self.assertEqual(res, [2, 3, 5, 7, 11])

	def test_start_param_respected(self):
		res = self.g.generate(7, 11)
		self.assertEqual(res, [7, 11])

	def test_with_generated_prime(self):
		res = self.g.generate(0, 13)
		self.assertEqual(res, [2, 3, 5, 7, 11, 13])

	def test_with_known_primes(self):
		st = 17
		end = 42
		res = self.g.generate(st, end)
		xpected = [a for a in KNOWN_PRIMES if a>=st and a<=end]
		self.assertEqual(res, xpected)

	def test_with_all_known_primes(self):
		res = self.g.generate(0, 200)
		self.assertEqual(KNOWN_PRIMES, res)

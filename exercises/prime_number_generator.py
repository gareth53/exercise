import math

class PrimeGenerator:

	_known_primes = [2, 3]

	def _is_non_prime(self, primes, val):
		"""
		We're going to tackle the problem from a different angle....
		we can exploit the following property of a non-prime number:
		a non-prime number alwatys has a factor that is prime

		this func assumes that primes includes all prime numbers that are <= sqrt of val
		"""
		limit = math.sqrt(val)
		for prime in primes:
			if prime > limit:
				break
			if val % prime == 0:
				return True
		return False

	def _generate_next_prime(self):
		i = self._known_primes[-1]
		while True:
			i = i + 2
			if not self._is_non_prime(self._known_primes, i):
				yield i


	def generate(self, start, end):
		"""
		returns prime numbers that are >= st and <= end
		"""
		i = max(start, self._known_primes[-1])
		while i <= end:
			i = self._generate_next_prime()
			self._known_primes.append(i)
		# TODO: optimize this...
		return_list = [a for a in self._known_primes if a>= start and a<= end]			
		return return_list

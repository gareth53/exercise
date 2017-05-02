"""
This is a demo task.

A zero-indexed array A consisting of N integers is given. An equilibrium index of this array is any integer P such that 0 ≤ P < N and the sum of elements of lower indices is equal to the sum of elements of higher indices, i.e. 
A[0] + A[1] + ... + A[P−1] = A[P+1] + ... + A[N−2] + A[N−1].
Sum of zero elements is assumed to be equal to 0. This can happen if P = 0 or if P = N−1.

"""
import unittest


def find_equilibrium_simple(input):
	"""
	find equilibrium index such that the sum of elements of lower indices is equal to the sum of elements of higher indices
	"""
	for i in range(1, len(input)-1):
		if sum(input[:i]) == sum(input[i+1:]):
			return i 
	return -1


def find_equilibrium(input):
	"""
	findi equilibrium index such that the sum of elements of 
	lower indices is equal to the sum of elements of higher indices
	minimise loops
	"""
	if len(input) < 3:
		return -1
	left = input[0]
	right = sum(input[2:])
	for i in range(1, len(input)-1):
		if left == right:
			return i
		left += input[i]
		right = right - input[i+1]
	return -1


class TestSolution(unittest.TestCase):

	def test_simple(self):
		input = [1, 1, 1, 1, 1]
		expect = 2
		self.assertEqual(find_equilibrium(input), expect)


	def test_no_equilibrium(self):
		input = [1, 2, 3]
		expect = -1
		self.assertEqual(find_equilibrium(input), expect)


	def test_three_equilibriums(self):
		input = [-1, 3, -4, 5, 1, -6, 2, 1]
		expect = 1
		self.assertEqual(find_equilibrium(input), expect)

	def test_equilibrium_is_penultimate_value(self):
		input = [1, 1, 1, 1, 1, 1, 1, 0, 7]
		expect = 7
		self.assertEqual(find_equilibrium(input), expect)

	def test_array_too_short_for_equlibrium(self):
		input = [1, 1]
		expect = -1
		self.assertEqual(find_equilibrium(input), expect)


if __name__ == "__main__":
	unittest.main()
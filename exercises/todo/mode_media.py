import unittest

"""
mean and medain can be done by Python;s inbuilt statistics package.
e.g.

	from statistics import mean, median
	data = [0,1,2,3,4,5,6,7]
	mean(data)
	median(data)

but for argument's sake... and for fun... let's do this from scratch

"""

def find_mode(data):
	vals = {}
	for val in data:
		count = vals.get(val, 0)
		vals[val] = count + 1
	highest_occurrence = max(vals.values())
	return [key for key, val in vals.items() if val == highest_occurrence]


def find_median(data):
	data = sorted(data)
	lngth = len(data)
	if lngth % 2 == 1:
		return data[(lngth-1)/2]
	# TODO: take midpoint between the two central values...
	return None


class TestMode(unittest.TestCase):

	def test_find_modes(self):
		tests = [
			([0], [0]),
			([0, 1, 1], [1]),
			([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
			([0, 1, 1, 2, 3, 4], [1]),
		]
		for test in tests:
			self.assertEquals(find_mode(test[0]), test[1])


class TestMedian(unittest.TestCase):

	def test_find_media(self):
		tests = [
			([0], 0),
			([0, 1, 1], 1),
			([1, 2, 3, 4, 5], 3),
			([0, 1, 1, 2, 3, 4], None),
			([5, 4, 3, 2, 1], 3),
			([3, 1, 5, 2, 4], 3),
		]
		for test in tests:
			self.assertEquals(find_median(test[0]), test[1])


if __name__ == "__main__":
	unittest.main()
from datetime import datetime
"""
Given a list_of_ints, find the highest_product you can get from three of the integers.
The input list_of_ints will always have at least three integers.
"""

testcases = [
	{
		'desc': "Simplest example",
		'input': [0, 1, 2, 3],
		'expect': 6
	},
	{
		'desc': "Shortest list, a zero kaiboshes all",
		'input': [0, 1, 2],
		'expect': 0
	},
	{
		'desc': "Shortest list, with a negative number",
		'input': [-1, 1, 2],
		'expect': -2
	},
	{
		'desc': "Negative Numbers",
		'input': [-10, -10, 1, 2, 3],
		'expect': 300
	},
	{
		'desc': "Long list",
		'input': [0, 1, 2, 3],
		'expect': 6
	},
	{
		'desc': "list with descending values",
		'input': [10, 9, 2, 1],
		'expect': 180
	},
	{
		'desc': "Really long list",
		'input': 20 * [10, 9, 2, 1],
		'expect': 1000
	}

]

def get_highest_product(numbers):
	"""
	returns the highest product of three numbers in a list
	the dumb, brute-force way
	"""
	output = None

	for x, num1 in enumerate(numbers):
		for y, num2 in enumerate(numbers):
			for z, num3 in enumerate(numbers):
				if x != y and x != z and y != z:
					product = num1*num2*num3
					if not output or product > output:
						output = product
	return output


def get_highest_product2(numbers):
	"""
	returns the highest product of three numbers in a list
	a more performant way than the brute force...
	"""
	# order the list largest number first
	order = sorted(numbers)
	highs = order[-3:]
	# check for negatives
	if order[0] < 0 and order[1] < 0:
		if abs(order[0]) > highs[0] and abs(order[1]) >= highs[0]:
			highs = highs[1:] + order[:1]
	# so we now have either a list of 3 or 4
	output = None
	for x, num1 in enumerate(order):
		for y, num2 in enumerate(order):
			for z, num3 in enumerate(order):
				if x != y and x != z and y != z:
					product = num1*num2*num3
					if not output or product > output:
						output = product
	return output






def test(func):
	for test in testcases:
		st = datetime.now()
		actual = func(test['input'])
		end = datetime.now()
		res = actual ==  test['expect']
		if res:
			print "%s: OK (%sms)" % (test['desc'], (end - st).microseconds)
		else:
			print "%s: FAIL, expected: %s, actual: %s" % (test['desc'], test['expect'], actual)


test(get_highest_product2)

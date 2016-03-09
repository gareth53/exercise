"""
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7*3*4, 1*3*4, 1*7*4, 1*7*3]

Do not use division in your solution.
"""

testcases = [
	{
		'desc': 'Given example',
		'input': [1, 7, 3, 4],
		'expect': [84, 12, 28, 21]
	},
	{
		'desc': 'List contains a zero',
		'input': [2, 2, 0, 2],
		'expect': [0, 0, 8, 0]
	},
	{
		'desc': 'List has 1 item',
		'input': [2],
		'expect': []
	},
	{
		'desc': 'Empty list',
		'input': [],
		'expect': []
	}
]

def get_products_of_all_ints_except_at_index(num_list):
	"""
	this is the slow, long-winded approach
	"""
	results = []
	for x, num in enumerate(num_list):
		product = None
		for y, num in enumerate(num_list):
			if x != y:
				if product is None:
					product = num
				else:
					product = product*num
				if product == 0:
					break
		if product is not None:
			results.append(product)
	return results

def get_products_of_all_ints_except_at_index_tuned(num_list):
	"""
	we're doing lots of repeated calculations
	so let's do those up front....
	Given:
		input = [1, 2, 3, 4, 5]
		output = [2*3*4*5, 1*3*4*5, 1*2*4*5]

	We can store the repeaetd calculations
			behind:
				[1, 1*2, 1*2*3, 1*2*3*4, 1*2*3*4*5]
				[1, 2, 6, 24, 120]
			beyond:
				[1*2*3*4*5, 2*3*4*5, 3*4*5, 4*5, 5]
				[120, 120, 60, 20, 5]

	so now, output for index 0:
		2*3*4*5 = beyond[1]

	output for index 1:
		1*3*4*5 = behind[0] * beyond[2]

	output for index 2:
		1*2*4*5 = behind[1] * beyond[3]

	"""
	if len(num_list) < 2:
		return []
	def cumulative_products(num_list):
		products = [num_list[0]]
		for x in range(1, len(num_list)):
			products.append(products[x-1]*num_list[x])
		return products

	behind = cumulative_products(num_list)
	num_list.reverse()
	beyond = cumulative_products(num_list)
	beyond.reverse()
	# so now we loop through the list, multiplying the before and after figures
	products = []
	list_len = len(num_list)
	for x in range(0, list_len):
		pre = behind[x-1] if x > 0 else 1
		post = beyond[x+1] if x+1 < list_len else 1
		products.append(pre*post)
	return products



def test(func):
	for test in testcases:
		actual = func(test['input'])
		if actual == test['expect']:
			print "OK", test['desc']
		else:
			print "FAIL", test['desc']
			print "Expected", test['expect']
			print "Actual", actual

test(get_products_of_all_ints_except_at_index)
test(get_products_of_all_ints_except_at_index_tuned)

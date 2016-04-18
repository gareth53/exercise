"""
Imagine you landed a new job as a cashier...
Your quirky boss found out that you're a programmer and has a weird request about something they've 
been wondering for a long time.

Write a function that, given:

- an amount of money
- a list of coin denominations
- computes the number of ways to make amount of money with coins of the available denominations.

Example: for amount=44 (44p) and denominations=[1,2,3][1,2,3] (11p, 22p and 33p), 
your program would output 44 - the number of ways to make 44p with those denominations:

1p, 1p, 1p, 1p
1p, 1p, 2p
1p, 3p
2p, 2p
"""
from datetime import datetime

testcases = [
	{
		'description': "Super simple example #1",
		'denominations': [1, 2],
		'amount': 4,
		'expect': 3,
		'workings': """
			1 1 1 1
			1 1 2
			2 2
		"""
	},
#	{
#		'description': "Super simple example #2",
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
#		'description': "Simple GBP example",
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
]

def count_combos(denominations, target):
	combos = get_combos(denominations, target)
	return len(combos)

def get_combos(denominations, target):
	"""
	calculate the number of combinations of numbers that would
	add up to the target
	"""
	print target
	denominations.sort()
	combos = set()
	# to begin with let's do the simple, single value calculations
	for val in denominations:
		if val < target:
			leftover = target % val
			strrepr = (str(val) + "-") * (target/val)
			if leftover == 0:
				combos.add(strrepr)
			else:
				# we need to figure out how to make up the leftover
				leftover_combos = get_combos(denominations, leftover)
				for combo in leftover_combos:
					combos.add(strrepr + combo)
			# now we need to take away 1 coin each iteration and calculate the number
			# of ways to make up the leftover
		else:
			break
	return combos


def test(func):
	for test in testcases:
		st = datetime.now()
		actual = func(test['denominations'], test['amount'])
		end = datetime.now()
		res = actual ==  test['expect']
		if res:
			print "OK: %s (%sms)" % (test['description'], (end - st).microseconds)
		else:
			print "FAIL: %s expected: %s, actual: %s" % (test['description'], test['expect'], actual)

test(count_combos)


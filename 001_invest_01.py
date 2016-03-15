
"""
https://www.interviewcake.com/question/python/stock-price

Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

You must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass)
"""

testcases = [
	{
		'desc': 'constant rise',
		'input': [1,2,3,4,5,6,7,8,9,10],
		'expect': (0, 9, 9)
	},
	{
		'desc': 'constant fall',
		'input': [10,9,7,5,3,1],
		'expect': (0, 1, -1)
	},
	{
		'desc': 'zero profit',
		'input': [20,19,19,15,13,11,9],
		'expect': (1, 2, 0)
	},
	{
		'desc': 'invest in first (high) wave',
		'input': [8,10,12,1,2,3],
		'expect': (0, 2, 4)
	},
	{
		'desc': 'invest in second wave',
		'input': [1,2,3,4,3,2,3,4,5,4],
		'expect': (0, 8, 4)
	},
	{
		'desc': 'invest late on a wobbly day',
		'input': [10, 10, 2, 20, 3, 12, 1, 20, 1, 19],
		'expect': (6, 7, 19)
	},
	{
		'desc': 'low before peak',
		'input': [1,4,5,6,9,10,12,11,9,4,20,19,2],
		'expect': (0, 10, 19)
	},
	{
		'desc': 'peak before low',
		'input': [7,8,9,10,9,8,7,6,5,4,5,4,5,6],
		'expect': (0, 3, 3)
	}
]

def compare_all_possible_tactics(prices):
	"""
	this solution has a nested for loop
	it's a brute-force approach
	"""
	profits = []
	for x, price in enumerate(prices):
		for sell_time in xrange(x+1, len(prices)):
			profits.append({
				'buy_time': x,
				'buy': price,
				'sell_time': sell_time,
				'sell': prices[sell_time],
				'profit':  prices[sell_time] - price
			})
	ordered_profits = sorted(profits, key=lambda k: k['profit'])
	optimal = ordered_profits[-1]
	return optimal['buy_time'], optimal['sell_time'], optimal['profit']

def analyse_in_single_loop(prices):
	"""
	given a list of share prices
	returns the best time to buy, sell & the profit
	only a single for loop!
	"""

	def profit(buy, sell):
	    return prices[sell] - prices[buy]

	buy = 0
	sell = 1
	potential_buy = 0

	for x in range(1, len(prices)):
		curr_profit = profit(buy, sell)
		# simple case to update sell
		if profit(buy, x) > curr_profit:
		    sell = x
		# this *might* be a better point to buy
		if prices[x-1] < prices[potential_buy]:
		    potential_buy = x-1
		# maybe the potential buy point has paid off
		if profit(potential_buy, x) > curr_profit:
		    buy = potential_buy
		    sell = x

	return buy, sell, profit(buy, sell)
    

def test(func):
	for test in testcases:
		actual = func(test['input'])
		if actual == test['expect']:
			print "OK", test['desc']
		else:
			print "FAIL", test['desc']
			print "Expected", test['expect']
			print "Actual", actual

test(compare_all_possible_tactics)
test(analyse_in_single_loop)
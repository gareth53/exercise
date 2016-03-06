
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
	'desc': 'second wave',
	'input': [1,2,3,4,3,2,3,4,5,4],
	'expect': (0, 8, 4)
	},
	{
	'desc': 'invest late',
	'input': [2,3,4,5,3,1,4,5,4],
	'expect': (5, 7, 4)
	},
	{
	'desc': 'price drops, but doesn\'t reocver',
	'input': [8,10,12,1,2,3],
	'expect': (0, 2, 4)
	},
	{
	'desc': 'invest late on a wobbly day',
	'input': [10, 10, 2, 20, 3, 12, 1, 20, 1, 19],
	'expect': (6, 7, 19)
	},
]

def profit(prices, buy, sell):
    return prices[sell] - prices[buy]

def best_invest(prices):
	"""
	given a list of share prices
	returns the best time to buy, sell & the profit
	"""
    buy = 0
    sell = 1
    potential_buy = 0
    for x in range(2, len(prices)):
    	curr_profit = profit(prices, buy, sell)
        # simlpe case
        if profit(prices, buy, x) > curr_profit:
            sell = x
        # this *might* be a better point to buy
        if prices[x] < prices[buy]:
            potential_buy = x
        # maybe the potential buy point has paid off
        elif profit(prices, potential_buy, x) > curr_profit:
            buy = potential_buy
            sell = x

    return buy, sell, profit(prices, buy, sell)
    

def test(func):
	for test in testcases:
		actual = func(test['input'])
		if actual == test['expect']:
			print "OK", test['desc']
		else:
			print "FAIL", test['desc']
			print "Expected", test['expect']
			print "Actual", actual

test(best_invest)
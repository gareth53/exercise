
"""
https://www.interviewcake.com/question/python/stock-price

Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made
from 1 purchase and 1 sale of 1 Apple stock yesterday.

You must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass)
"""



def compare_all_possible_tactics(prices):
    """
    :arg prices = list of numbers
    :returns tuple of buy_time, sll_time & profit

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
    :arg prices = list of numbers
    :returns tuple of buy_time, sll_time & profit

    only a single for loop!
    """

    def profit(buy_time, sell_time):
        return prices[sell_time] - prices[buy_time]

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
    

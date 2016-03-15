def highest_product_of3(arg):
    """
    given a list of integers/floats, returns the highest product
    of 3 of those numbers
    the numbers may be negative.
    """
    high = max(arg[0], arg[1])
    low = min(arg[0], arg[1])
    # high2
    high2 = arg[0] * arg[1]
    # lowest_product_of_2
    low2 = arg[0] * arg[1]
    high3 = arg[0] * arg[1] * arg[2]
    for x in arg[2:]:
        high3 = max(high3, high2*x, low2*x)
        high2 = max(high2, high*x, low*x)
        low2 = min(low2, low*x)
        high = max(high, x)
        low = min(low, x)
    return high3

print highest_product_of3([-10, 2, -3, 5, 1, 5])
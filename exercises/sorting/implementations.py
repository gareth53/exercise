from copy import copy
import math

def bubblesort(arr):
	"""
	run through the array, swapping pairs of values
	keep doing it untik you donlt have to do it no more
	"""

	edit = True
	while edit:
		edit = False
		for x in range(0, len(arr) - 1):
			lft = arr[x]
			rght = arr[x+1]
			if rght < lft:
				arr[x] = rght
				arr[x+1] = lft
				edit = True
	return arr


def selectionsort(arr):
	"""
	the multiple scan to find the smallest
	a scan that each time yields the smallest value
	"""
	arr = copy(arr)
	new_arr = []
	while arr:
		lowest = None
		for idx, x in enumerate(arr):
			if lowest is None or x < lowest:
				lowest = x
				lowest_idx = idx
		new_arr.append(arr.pop(lowest_idx))
	return new_arr


def mergesort(arr):
	"""
	divide the list into equal-sized sublists
	i.e. the left and right
	recursively do this until you have lists of one (which will be sorted)
	"""

	def merge(left, right):
		result = []

		while left and right:
		    if left[0] <= right[0]:
		        result.append(left.pop(0))
		    else:
		        result.append(right.pop(0))
		# Either list may have elements left, we just add them...
		return result + left + right


    # list of zero or one elements needs no sorting
	if len(arr) <= 1:
	    return arr

	half = int(math.floor(len(arr)/2))
	left = arr[:half]
	right = arr[half:]

	#Recursively sort both sublists.
	left = mergesort(left)
	right = mergesort(right)

	# merge the now-sorted sublists.
	return merge(left, right)


def sort_dict(dict_list, sort_key=None, sort_keys=None):
	"""
	:param dict_list: <list> of <dict>s [{}, {}]
	:param sort_keys: <list> of <str>
	:return: <list>
	"""
	if sort_key:
		return sorted(dict_list, key=lambda x: x[sort_key])
	elif sort_keys:
		return sorted(dict_list, key=lambda x: "".join([x[key] for key in sort_keys]))
	return dict_list


if __name__ == "__main__":
	# some benchmarking
	import time
	li = range(0, 8000)
	li.reverse()

	def timeit(method):
	    def timed(*args, **kw):
	        ts = time.time()
	        result = method(*args, **kw)
	        te = time.time()
	        print('%r %2.2f sec' % (method.__name__, te-ts))
	        return result
	    return timed

	@timeit
	def bubble(li):
		return bubblesort(li)

	@timeit
	def selection(li):
		return selectionsort(li)

	@timeit
	def merge(li):
		return mergesort(li)

	@timeit
	def builtin(li):
		return sorted(li)

	bubble(li)
	selection(li)
	merge(li)
	builtin(li)

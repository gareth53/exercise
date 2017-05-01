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


def selectionsort_old(arr):
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


def selectionsort(arr):
	"""
	this one quicker since it doesn't do a pop
	just edits the arr that's passed in
	"""
	limit = len(arr)
	for i in range(0, limit):
		smallest = arr[i]
		smallest_idx = i
		for x in range(i+1, limit):
			this_val = arr[x]
			if this_val < smallest:
				smallest = this_val
				smallest_idx = x
		arr[i], arr[smallest_idx] = this_val, arr[i]
	return arr



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


def insertionsort(arr):
	for i in range(1, len(arr)):
		for j in range(i, 0, -1):
			if arr[j] < arr[j-1]:
				arr[j], arr[j-1] = arr[j-1], arr[j]
			else:
				break
	return arr


def bucketsort(arr, n=10):
	"""
	n = bucket_size
	"""
	buckets = {}
	for a in arr:
		idx = int(math.floor(a/n))
		bucket = buckets.get(idx, [])
		bucket.append(a)
		buckets[idx] = bucket
	return_li = []
	for b in sorted(buckets.keys()):
		return_li = return_li + insertionsort(buckets[b])
	return return_li


if __name__ == "__main__":
	# some benchmarking
	import time
	li = list(range(0, 8000))
	li.reverse()

	def timeit(method):
	    def timed(*args, **kw):
	        ts = time.time()
	        result = method(*args, **kw)
	        te = time.time()
	        print('%2.2f sec' % (te-ts))
	        return result
	    return timed

	@timeit
	def run_algo(algorithm):
		print(algorithm.__name__)
		return algorithm(li)

	for algorithm in [selectionsort, mergesort, insertionsort, bucketsort, sorted]:
		run_algo(algorithm)
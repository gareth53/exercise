"""
Sorted Merge
You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. 
Write a method to merge B into A in a sorted order.
Question from "Cracking The Coding Interview" by Gayle Laakmann McDowell

"""


def sorted_merge(a, b):
	"""
	:param a: <list> (sorted)
	:param b: <list> (sorted)
	:returns: <list>
	"""
	if a[-1] < b[0]:
		return a + b
	if b[-1] < a[0]:
		return b + a
	b_inserts = 0
	for a_indx in range(0, len(a)):
		a_el = a[a_indx + b_inserts]
		for b_indx in range(b_inserts, len(b)):
			b_el = b[b_indx]
			if b_el < a_el:
				a = a[:a_indx+b_inserts] + [b_el] + a[a_indx+b_inserts:]
				b_inserts = b_inserts + 1
			else:
				break
		# we may have some elemnts we haven;t inserted
		# check that
	if b_inserts < len(b):
		a = a + b[b_inserts:]
	return a

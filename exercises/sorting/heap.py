import heapq

"""
Simple interface for the functio alitu in the heapq modulw
"""

class Heap:

	def __init__(self, initial_list=None):
		if not initial_list:
			initial_list = []
		heapq.heapify(initial_list)
		self.data = initial_list

	def push(self, val):
		heapq.heappush(self.data, val)
		heapq.heapify(self.data)
		return len(self.data)

	def pop(self):
		return heapq.heappop(self.data)

	def __str__(self):
		return str(self.data)


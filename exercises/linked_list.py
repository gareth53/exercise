from datetime import datetime

class LinkedListSingle:

	def __init__(self, payload):
		"""
		init method creats the first node
		"""
		self.head = Node(payload)

	def update_head(self, node):
		self.head = node

	def append(self, payload):
		new_node = Node(payload)
		n = self.head
		while(n.next != None):
			n = n.next
		n.next = new_node

	def list_values(self):
		return [node.payload for node in self.nodes()]

	def nodes(self):
		vals = []
		node = self.head
		while self.head:
			if not node:
				return
			this_node = node
			node = node.next
			yield this_node

	def _insert_node(self, new_payload, preceding_node=None):
		"""
		if preceding_node is None, we insert at the beginning
		"""
		if not preceding_node:
			new_node = Node(new_payload, self.head)
			self.head = new_node
		else:
			new_node = Node(new_payload, preceding_node.next)
			preceding_node.next = new_node

	def insert_in_order(self, payload):
		"""
		let's assume the payloads are integers
		"""
		preceding_node = None
		for node in self.nodes():
			if node.payload > payload:
				break
			preceding_node = node
		self._insert_node(payload, preceding_node)



class Node:

	def __init__(self, payload, next_node=None):
		self.payload = payload
		self.next = next_node



if __name__ == "__main__":
	# some benchmarking
	# create a list of X entries
	# then insert some values
	# compare LinkedList Vs list.append() and list.sort()
	def setup(limit):
		li = range(0, limit)
		linked_list = LinkedListSingle(0)
		for x in li[1:]:
			linked_list.append(x)
		return li, linked_list

	def timeit(method):
	    def timed(*args, **kw):
	        ts = time.time()
	        result = method(*args, **kw)
	        te = time.time()
	        print('%r %2.2f sec' % (method.__name__, te-ts))
	        return result
	    return timed

	@timeit
	def managing_order_in_a_list(li, vals):
		for x in vals:
			li.append(x)
			li.sort()
		return li

	@timeit
	def managing_order_in_a_linked_list(linked_list, vals):
		for x in vals:
			linked_list.insert_in_order(x)
		return linked_list

	import time


	lim = 20000
	print("setup")
	li, linked_list = setup(lim)
	print("creating insertion values")
	insertion_vals = range(0, lim, 3)
	print("testing list " + str(datetime.now()))
	li_result = managing_order_in_a_list(li, insertion_vals)
	print("testing linked list " + str(datetime.now()))
	linked_list_result = managing_order_in_a_linked_list(linked_list, insertion_vals)

#	print("comparing output: " + str(datetime.now()))
#	assert li_result == linked_list_result.list_values()





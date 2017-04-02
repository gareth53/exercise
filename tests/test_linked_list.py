import unittest
from exercises.linked_list import LinkedListSingle, Node

class X(unittest.TestCase):
	"""
	tests:
		- setup
		- inserting a node
		- removing a node
		- appending a node
	"""
	def test_creating_linkedlist(self):
		li = LinkedListSingle(payload=2)
		self.assertEqual(li.head.payload, 2)
		self.assertEqual(li.head.next, None)

	def test_appending_linkedlist(self):
		li = LinkedListSingle(payload=2)
		li.append(4)
		self.assertNotEqual(li.head.next, None)
		self.assertEqual(li.head.payload, 2)
		self.assertEqual(li.head.next.payload, 4)

	def test_list_values(self):
		li = LinkedListSingle(payload=2)
		li.append(4)
		li.append(5)
		li.append(10)
		self.assertEqual(li.list_values(), [2, 4, 5, 10])

	def test_insert_node(self):
		li = LinkedListSingle(payload=2)
		li._insert_node(1)
		self.assertEqual(li.list_values(), [1, 2])

	def test_insert_in_order(self):
		li = LinkedListSingle(payload=2)
		li.append(4)
		li.append(6)
		li.append(8)
		li.insert_in_order(5)
		self.assertEqual(li.list_values(), [2, 4, 5, 6, 8])
		li.insert_in_order(50)
		self.assertEqual(li.list_values(), [2, 4, 5, 6, 8, 50])
		li.insert_in_order(0)
		self.assertEqual(li.list_values(), [0, 2, 4, 5, 6, 8, 50])

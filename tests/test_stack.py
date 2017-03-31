import unittest
from exercises.stack import Stack


class TestStack(unittest.TestCase):

	def test_init(self):
		s = Stack()
		self.assertTrue(s)

	def test_iint_with_vals(self):
		s = Stack(9, 8, 8)
		self.assertTrue(s)
		self.assertEquals(s.data, [9, 8, 8])

	def test_push(self):
		s = Stack()
		s.push(2)
		self.assertEquals(s.data, [2])

	def test_pop(self):
		s = Stack()
		s.push(2)
		val = s.pop()
		self.assertEquals(val, 2)

	def test_is_empty(self):
		s = Stack()
		self.assertTrue(s.is_empty())
		s.push(2)
		self.assertFalse(s.is_empty())

	def test_peek_in_empty(self):
		s = Stack()
		self.assertEquals(s.peek(), None)

	def test_peek(self):
		s = Stack(1,2,3,4,5,6)
		self.assertEquals(s.peek(), 6)
		s.pop()
		self.assertEquals(s.peek(), 5)

	def test_repr_empty(self):
		s = Stack()
		self.assertEquals(str(s), "Stack {0}")

	def test_repr_small(self):
		s = Stack(1, 2, 3, 4, 5)
		self.assertEquals(str(s), "Stack {5} [1, 2, 3, 4, 5]")

	def test_repr_large(self):
		vals = [1, 2, 3, 4, 5] * 200
		s = Stack(*vals)
		self.assertEquals(str(s), "Stack {1000} [1, 2, 3, 4, 5, 1, 2, 3, 4, 5 ...]")

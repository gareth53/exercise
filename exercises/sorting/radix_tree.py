

class Node:

	def __init__(self, value, parent):
		self.value = value.lower()
		self.parent = parent
		self.children = []
		self.full_value = self._calculate_full_value()
		self.full_word = False

	def add_node(self, value):
		node = Node(value, self)
		self.children.append(node)
		return node

	def _calculate_full_value(self):
		values = [self.value]
		node = self.parent
		while node:
			values.append(node.value)
			node = node.parent
		values.reverse()
		return "".join(values)

	def find_child(self, char):
		for node in self.children:
			if node.value == char:
				return node
		return None

	def mark_as_word(self):
		self.full_word = True

	def __repr__(self):
		return "<Node '%s'>" % self.full_value


class RadixTree(Node):

	def __init__(self):
		self.children = []
		self.value = ""
		self.full_value = ""
		self.parent = None

	def add_word(self, word):
		curr_node = self
		created = False
		for char in word.lower():
			child = curr_node.find_child(char)
			if child:
				curr_node = child
			else:
				curr_node = curr_node.add_node(char)
				created = True
		if curr_node.full_word:
			return False
		curr_node.mark_as_word()
		return True

	def check_word(self, word, prefix=False):
		curr_node = self
		for char in word.lower():
			child = curr_node.find_child(char)
			if not child:
				return False
			curr_node = child
		return prefix or curr_node.full_word
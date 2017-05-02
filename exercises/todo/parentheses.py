import unittest


def strip_parentheses(input, chars="()"):
	"""
	this one walks through the string char by char
	"""
	open_char = chars[0]
	close_char = chars[-1]
	opens = []
	closes = []
	cuts = []
	for i, char in enumerate(input):
		if char == open_char:
			opens.append(i)
		if char == close_char:
			closes.append(i)
		if opens and closes:
			if len(opens) == len(closes):
				st = opens[0]
				end = closes[-1]
				if st < end:
					cuts.append((st, end))
				opens = []
				closes = []
	output = input
	# do the snipping in reverse to preserve integrity of the indices
	cuts.reverse()
	for cut in cuts:
		output = output[:cut[0]].rstrip() + output[cut[1]+1:]
	return output


class TestStripParetheses(unittest.TestCase):
	tests = [
		# input, expected, open/close chars
		("A null op", "A null op", "()"),
		("This Is Simplest (Case)", "This Is Simplest", "()"),
		("(All Bracketed)", "", "()"),
		("Empty Brackets ()", "Empty Brackets", "()"),
		("This Has Two (Parentheses) That Need Stripping (OK?)", "This Has Two That Need Stripping", "()"),
		("A Simple (Nested (Example))", "A Simple", "()"),
		("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.", "Sometimes they get confusing.", "()"),
		("No(Spaces)", "No", "()"),
		("No(Spaces)Here", "NoHere", "()"),

		# 'Error' cases
		("Here (We Should (Just) return the string", "Here (We Should (Just) return the string", "()"),
		("Inverted )Brackets(", "Inverted )Brackets(", "()"),
		("Nested (bracket (incrroect Nesting)", "Nested (bracket (incrroect Nesting)", "()"),

		# don;t be over-zealous correcting whitespace
		(" Protect (Whitespace) ", " Protect ", "()"),
		("Protect  My (Whitespace#2)", "Protect  My", "()"),
		("Protect (Whitespace#3) ", "Protect ", "()"),

		# testing other brackets
		(" Protect {Whitespace} ", " Protect ", "{}"),
		("Protect  My [Whitespace#2]", "Protect  My", "[]"),
		("Protect <Whitespace#3> ", "Protect ", "<>")

	]

	def test_all_cases(self):
		for test in self.tests:
			res = strip_parentheses(test[0], test[2])
			self.assertEquals(res, test[1])

	def test_no_specified_chars(self):
		# final test with no chars arg
		self.assertEquals(strip_parentheses("Don't You (Forget About Me)"), "Don't You")

if __name__ == "__main__":
	unittest.main()

import unittest
from exercises.meeting_times import condense_meeting_times


class TestTimeCondenser(unittest.TestCase):

	def test_meetings_simultaneous_equal_in_length(self):
		data = [(0, 1), (0, 1)]
		expect = [(0, 1)]
		self.assertEqual(condense_meeting_times(data), expect)

	def test_meetings_overlap(self):
		data = [(0, 2), (1, 3)]
		expect = [(0, 3)]
		self.assertEqual(condense_meeting_times(data), expect)

	def test_meetings_overlap_2nd_meeting_starts_earlier(self):
		data = [(2, 4), (0, 3)]
		expect = [(0, 4)]
		self.assertEqual(condense_meeting_times(data), expect)

	def test_first_meeting_encompasses_a_subsequent_meeting(self):
		data = [(0, 4), (1, 3)]
		expect = [(0, 4)]
		self.assertEqual(condense_meeting_times(data), expect)

	def test_meeting_encompasses_a_previous_meeting(self):
		data = [(1, 3), (0, 4)]
		expect = [(0, 4)]
		self.assertEqual(condense_meeting_times(data), expect)

	def test_meetings_in_an_unhelpful_order(self):
		data = [(1, 3), (0, 4), (0, 1), (13, 14), (5, 6), (15, 16), (12, 13)]
		expect = [(0, 4), (5, 6), (12, 14), (15, 16)]
		self.assertEqual(condense_meeting_times(data), expect)

	def test_meetings_that_dont_overlap_but_run_into_each_other(self):
		data = [(0, 4), (4, 6)]
		expect = [(0, 6)]
		self.assertEqual(condense_meeting_times(data), expect)

	def test_meeting_joins_two_meetings_that_didnt_poreviously_overlap(self):
		data = [(0, 1), (3, 6), (1, 3)]
		expect = [(0, 6)]
		self.assertEqual(condense_meeting_times(data), expect)

	def test_we_account_for_a_break(self):
		data = [(0, 1), (3, 6), (7, 8)]
		expect = [(0, 1), (3, 6), (7, 8)]
		self.assertEqual(condense_meeting_times(data), expect)

	def test_given_testcase(self):
		data = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
		expect = [(0, 1), (3, 8), (9, 12)]
		self.assertEqual(condense_meeting_times(data), expect)

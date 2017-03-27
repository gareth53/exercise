import sys
import os
sys.path.append(os.getcwd())

import unittest
#from tracker import TempTracker
from tracker import CounterTracker as TempTracker


class TestTrackerInsert(unittest.TestCase):

	def test_insert(self):
		tr = TempTracker()
		tr.insert(25)
		self.assertEqual(tr._get_temps(), [25,])

	def test_multiple_inserts(self):
		y = 10
		tr = TempTracker()
		for x in range(0, y):
			tr.insert(x)
		self.assertEqual(len(tr._get_temps()), 10)


class TestTrackerMax(unittest.TestCase):

	def test_max_returns_none(self):
		tr = TempTracker()
		self.assertEqual(tr.get_max(), None)


	def test_max(self):
		tr = TempTracker()
		for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6]:
			tr.insert(x)
		self.assertEqual(tr.get_max(), 9)


class TestTrackerMin(unittest.TestCase):

	def test_min_returns_none(self):
		tr = TempTracker()
		self.assertEqual(tr.get_min(), None)


	def test_min(self):
		tr = TempTracker()
		for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 0, 5, 6]:
			tr.insert(x)
		self.assertEqual(tr.get_min(), 0)


class TestTrackerMode(unittest.TestCase):

	def test_mode_returns_none(self):
		tr = TempTracker()
		self.assertEqual(tr.get_mode(), None)

	def test_mode_one_single_value(self):
		tr = TempTracker()
		tr.insert(2)
		self.assertEqual(tr.get_mode(), 2)

	def test_mode_one_multiple_value(self):
		tr = TempTracker()
		for x in [0, 1, 2, 3, 4, 5, 4]:
			tr.insert(x)
		self.assertEqual(tr.get_mode(), 4)

	def test_mode_multiple_modes(self):
		tr = TempTracker()
		for x in [5, 0, 1, 2, 3, 4, 5, 4]:
			tr.insert(x)
		self.assertTrue(tr.get_mode() in [4, 5])


class TestTrackerMean(unittest.TestCase):

	def test_no_mean_val(self):
		tr = TempTracker()
		self.assertEqual(tr.get_mean(), None)

	def test_get_mean_singel_value(self):
		tr = TempTracker()
		tr.insert(50)
		self.assertEqual(tr.get_mean(), 50.0)

	def test_get_mean_mulit_value(self):
		tr = TempTracker()
		for x in [0, 5, 10, 5]:
			tr.insert(x)
		self.assertEqual(tr.get_mean(), 5.0)


if __name__ == "__main__":
	unittest.main()
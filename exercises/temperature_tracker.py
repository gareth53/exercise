"""
You decide to test if your oddly-mathematical heating company is fulfilling its
All-Time Max, Min, Mean and Mode Temperature Guarantee(TM).
Write a class TempTracker with these methods:

insert() - records a new temperature
get_max() - returns the highest temp we've seen so far
get_min() - returns the lowest temp we've seen so far
get_mean() - returns the mean of all temps we've seen so far
get_mode() - returns the mode of all temps we've seen so far

Optimize for space and time. Favor speeding up the getter functions (get_max(),
get_min(), get_mean(), and get_mode()) over speeding up the insert() function.

get_mean() should return a float, but the rest of the getter functions can
return integers.
Temperatures will all be inserted as integers. We'll record
our temperatures in Fahrenheit, so we can assume they'll all be in the range
0..110.

If there is more than one mode, return any of the modes.

(mode = most occurrent value)
"""

from collections import Counter

class CounterTracker:
    """
    this implementation uses the python Counter class from collections
    """

    def __init__(self):
        self._temps = []
        self._mode = None
        self._mean = None
        self._max = None
        self._min = None

    def insert(self, temp):
        self._temps.append(temp)
        self._update_calculations()

    def _update_calculations(self):
        vals = self._temps
        self._mean = self._get_mean(vals)
        self._mode = self._get_mode(vals)
        self._max, self._min = self._get_max_min(vals)

    @staticmethod
    def _get_mean(vals):
        return sum(vals) / len(vals)

    @staticmethod
    def _get_mode(vals):
        return Counter(vals).most_common()[0][0]

    @staticmethod
    def _get_max_min(vals):
        return max(vals), min(vals)

    def _get_temps(self):
        return self._temps

    def get_max(self):
        return self._max

    def get_min(self):
        return self._min

    def get_mode(self):
        return self._mode

    def get_mean(self):
        return self._mean




class TempTracker:
    """
    this is pure Python implementation
    """

    def __init__(self):
        self._temps = []
        self.total = 0
        self.mean = None
        self.mode = set()
        self.modes = {}

    def _get_temps(self):
        return self._temps

    def _update_mode(self, temp):
        count = self.modes.get(temp, 0) + 1
        self.modes[temp] = count
        if not self.mode:
            self.mode = {temp}
            return
        curr_mode_count = self.modes[list(self.mode)[0]]
        if count == curr_mode_count:
            self.mode.add(temp)
            return
        if count > curr_mode_count:
            self.mode = {temp}

    def _update_mean(self, temp):
        self.total += temp
        self.mean = self.total / len(self._temps)

    def insert(self, temp):
        self._temps.append(temp)
        self._temps = sorted(self._temps)
        self._update_mode(temp)
        self._update_mean(temp)

    def get_max(self):
        if self._temps:
            return self._temps[-1]
        return None

    def get_min(self):
        if self._temps:
            return self._temps[0]
        return None

    def get_mean(self):
        return self.mean

    def get_mode(self):
        if self.mode:
            return list(self.mode)[-1]
        return None

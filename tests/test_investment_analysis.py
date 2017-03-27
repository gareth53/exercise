import unittest
from exercises.investment_analysis import compare_all_possible_tactics, analyse_in_single_loop


class AllTestCases:
    """
    Abstract class that is inherited by classes
    that test specific implementations
    """

    @staticmethod
    def func_under_test(data):
        raise NotImplementedError

    def test_constant_rise(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expect = (0, 9, 9)
        self.assertEquals(self.func_under_test(data), expect)

    def test_constant_fall(self):
        data = [10, 9, 7, 5, 3, 1]
        expect = (0, 1, -1)
        self.assertEquals(self.func_under_test(data), expect)

    def test_zero_profit(self):
        data = [20, 19, 19, 15, 13, 11, 9]
        expect = (1, 2, 0)
        self.assertEquals(self.func_under_test(data), expect)

    def test_invest_in_first_high_wave(self):
        data = [8, 10, 12, 1, 2, 3]
        expect = (0, 2, 4)
        self.assertEquals(self.func_under_test(data), expect)

    def test_invest_in_second_wave(self):
        data = [1, 2, 3, 4, 3, 2, 3, 4, 5, 4]
        expect = (0, 8, 4)
        self.assertEquals(self.func_under_test(data), expect)

    def test_invest_late_on_a_wobbly_day(self):
        data = [10, 10, 2, 20, 3, 12, 1, 20, 1, 19]
        expect = (6, 7, 19)
        self.assertEquals(self.func_under_test(data), expect)

    def test_low_before_peak(self):
        data = [1, 4, 5, 6, 9, 10, 12, 11, 9, 4, 20, 19, 2]
        expect = (0, 10, 19)
        self.assertEquals(self.func_under_test(data), expect)

    def test_peak_before_low(self):
        data = [7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 5, 4, 5, 6]
        expect = (0, 3, 3) 
        self.assertEquals(self.func_under_test(data), expect)


class TestPossibleTactics(unittest.TestCase, AllTestCases):

    @staticmethod
    def func_under_test(data):
        return compare_all_possible_tactics(data)


class TestSingleLoop(unittest.TestCase, AllTestCases):

    @staticmethod
    def func_under_test(data):
        return analyse_in_single_loop(data)

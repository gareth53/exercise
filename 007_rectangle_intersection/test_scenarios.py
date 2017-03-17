import unittest
from rectangle import find_intersection, Rect


class TestCases(unittest.TestCase):

    def test_no_intersection(self):
        rect1 = { 'left_x': 1, 'bottom_y': 4, 'width': 3, 'height': 3 }
        rect2 = { 'left_x': 5, 'bottom_y': 8, 'width': 3, 'height': 3 }
        rslt = find_intersection(rect1, rect2)
        self.assertEquals(rslt, None)

    def test_negative_coods(self):
        """
        Rect 1 bottom left of rect 2 - negative numbers
        """
        rect1 = { 'left_x': -4, 'bottom_y': 1, 'width': 2, 'height': 2 }
        rect2 = { 'left_x': -3, 'bottom_y': 0, 'width': 2, 'height': 2 }
        expect = { 'left_x': -3, 'bottom_y': 0, 'width': 1,  'height': 1 }
        actual = find_intersection(rect1, rect2)
        self.assertEquals(actual, expect)

    def test_rect1_top_left(self):
        """
        Simple overlap rect 1 top left of rect 2
        """
        rect1 = { 'left_x': 1, 'bottom_y': 5, 'width': 4, 'height': 4 }
        rect2 = { 'left_x': 2, 'bottom_y': 6, 'width': 4, 'height': 4 }
        rslt =  { 'left_x': 2, 'bottom_y': 5, 'width': 3,  'height': 3 }
        actual = find_intersection(rect1, rect2)
        self.assertEquals(actual, rslt)

    def test__rect1_bottom_right(self):
        """
        Simple overlap rect 2 top left of rect 1',
        """
        rect1 = { 'left_x': 2, 'bottom_y': 6, 'width': 4, 'height': 4 }
        rect2 = { 'left_x': 1, 'bottom_y': 5, 'width': 4, 'height': 4 }
        rslt = { 'left_x': 2, 'bottom_y': 5, 'width': 3,  'height': 3 }
        actual = find_intersection(rect1, rect2)
        self.assertEquals(actual, rslt)

    def test_rect1_top_right(self):
        """
        Rect 1 top right of rect 2',
        """
        rect1 = { 'left_x': 5, 'bottom_y': 5, 'width': 5, 'height': 5 }
        rect2 = { 'left_x': 0, 'bottom_y': 6, 'width': 6, 'height': 2 }
        rslt = { 'left_x': 5, 'bottom_y': 5, 'width': 1,  'height': 1 }
        actual = find_intersection(rect1, rect2)
        self.assertEquals(actual, rslt)

    def test_rect_btm_right(self):
        """
        Rect 1 bottom right of rect 2',
        """
        rect1 = { 'left_x': 3, 'bottom_y': 7, 'width': 4, 'height': 4 }
        rect2 = { 'left_x': 0, 'bottom_y': 4, 'width': 4, 'height': 4 }
        rslt = { 'left_x': 3, 'bottom_y': 4, 'width': 1,  'height': 1 }
        actual = find_intersection(rect1, rect2)
        self.assertEquals(actual, rslt)

    def test_rect1_btm_left(self):
        """
        Rect 1 bottom left of rect 2',
        """
        rect1 = { 'left_x': 0, 'bottom_y': 5, 'width': 2, 'height': 2 }
        rect2 = { 'left_x': 1, 'bottom_y': 4, 'width': 2, 'height': 2 }
        rslt = { 'left_x': 1, 'bottom_y': 4, 'width': 1,  'height': 1 }
        actual = find_intersection(rect1, rect2)
        self.assertEquals(actual, rslt)

    def test_rect1_left_smaller(self):
        """
        Rect 1 left of rect 2, shallower',
        """
        rect1 = { 'left_x': 0, 'bottom_y': 3, 'width': 2, 'height': 2 }
        rect2 = { 'left_x': 1, 'bottom_y': 4, 'width': 4, 'height': 4 }
        rslt = { 'left_x': 1, 'bottom_y': 3, 'width': 1,  'height': 2 }
        actual = find_intersection(rect1, rect2)
        self.assertEquals(actual, rslt)

    def test_rect1_subset(self):
        """
        rect2 subset of rect1',
        """
        rect1 = { 'left_x': 1, 'bottom_y': 10, 'width': 6, 'height': 9 }
        rect2 = { 'left_x': 2, 'bottom_y': 6, 'width': 4, 'height': 4 }
        rslt = { 'left_x': 2, 'bottom_y': 6, 'width': 4,  'height': 4 }
        actual = find_intersection(rect1, rect2)
        self.assertEquals(actual, rslt)

    def test_rect2_subset(self):
        """
        rect1 subset of rect2
        """
        rect1 = { 'left_x': 2, 'bottom_y': 6, 'width': 4, 'height': 4 }
        rect2 = { 'left_x': 1, 'bottom_y': 10, 'width': 6, 'height': 9 }
        rslt = { 'left_x': 2, 'bottom_y': 6, 'width': 4,  'height': 4 }
        actual = find_intersection(rect1, rect2)
        self.assertEquals(actual, rslt)

    def test_boundaries_touch(self):
        """
        two rects butting up to each other
        """
        rect1 = { 'left_x': 2, 'bottom_y': 6, 'width': 4, 'height': 4 }
        rect2 = { 'left_x': 6, 'bottom_y': 6, 'width': 6, 'height': 6 }
        actual = find_intersection(rect1, rect2)
        self.assertEquals(actual, None)


if __name__ == '__main__':
    unittest.main()

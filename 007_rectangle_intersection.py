"""

Write a function to find the rectangular intersection of two given rectangles.

Rectangles are always "straight" and never "diagonal." More rigorously: each
side is parallel with either the x-axis or the y-axis.

They are defined as dictionaries like this:

my_rectangle = {
    'left_x': 1,
    'bottom_y': 5,
    'width': 10,
    'height': 4,
}

Your output rectangle should use this format as well.
"""
from datetime import datetime

testcases = [
    {
        'description': 'Simple overlap rect 1 top left of rect 2',
        'rect1': { 'left_x': 1, 'bottom_y': 5, 'width': 4, 'height': 4 },
        'rect2': { 'left_x': 2, 'bottom_y': 6, 'width': 4, 'height': 4 },
        'reslt': { 'left_x': 2, 'bottom_y': 5, 'width': 3,  'height': 3 }
    },
    {
        'description': 'Simple overlap rect 2 top left of rect 1',
        'rect2': { 'left_x': 1, 'bottom_y': 5, 'width': 4, 'height': 4 },
        'rect1': { 'left_x': 2, 'bottom_y': 6, 'width': 4, 'height': 4 },
        'reslt': { 'left_x': 2, 'bottom_y': 5, 'width': 3,  'height': 3 }
    },
    {
        'description': 'Rect 1 top right of rect 2',
        'rect1': { 'left_x': 5, 'bottom_y': 5, 'width': 5, 'height': 5 },
        'rect2': { 'left_x': 0, 'bottom_y': 6, 'width': 6, 'height': 2 },
        'reslt': { 'left_x': 5, 'bottom_y': 5, 'width': 1,  'height': 1 }
    },
    {
        'description': 'Rect 1 bottom right of rect 2',
        'rect1': { 'left_x': 3, 'bottom_y': 7, 'width': 4, 'height': 4 },
        'rect2': { 'left_x': 0, 'bottom_y': 4, 'width': 4, 'height': 4 },
        'reslt': { 'left_x': 3, 'bottom_y': 4, 'width': 1,  'height': 1 }
    },
    {
        'description': 'Rect 1 bottom left of rect 2',
        'rect1': { 'left_x': 0, 'bottom_y': 5, 'width': 2, 'height': 2 },
        'rect2': { 'left_x': 1, 'bottom_y': 4, 'width': 2, 'height': 2 },
        'reslt': { 'left_x': 1, 'bottom_y': 4, 'width': 1,  'height': 1 }
    },
    {
        'description': 'Rect 1 left of rect 2, shallower',
        'rect1': { 'left_x': 0, 'bottom_y': 3, 'width': 2, 'height': 2 },
        'rect2': { 'left_x': 1, 'bottom_y': 4, 'width': 4, 'height': 4 },
        'reslt': { 'left_x': 1, 'bottom_y': 3, 'width': 1,  'height': 2 }
    },
    {
        'description': 'rect2 subset of rect1',
        'rect1': { 'left_x': 1, 'bottom_y': 10, 'width': 6, 'height': 9 },
        'rect2': { 'left_x': 2, 'bottom_y': 6, 'width': 4, 'height': 4 },
        'reslt': { 'left_x': 2, 'bottom_y': 6, 'width': 4,  'height': 4 }
    },
    {
        'description': 'rect1 subset of rect2',
        'rect2': { 'left_x': 1, 'bottom_y': 10, 'width': 6, 'height': 9 },
        'rect1': { 'left_x': 2, 'bottom_y': 6, 'width': 4, 'height': 4 },
        'reslt': { 'left_x': 2, 'bottom_y': 6, 'width': 4,  'height': 4 }
    },
    {
        'description': 'Rect 1 bottom left of rect 2 - negative numbers',
        'rect1': { 'left_x': -4, 'bottom_y': 1, 'width': 2, 'height': 2 },
        'rect2': { 'left_x': -3, 'bottom_y': 0, 'width': 2, 'height': 2 },
        'reslt': { 'left_x': -3, 'bottom_y': 0, 'width': 1,  'height': 1 }
    },
    {
        'description': 'no intersection',
        'rect2': { 'left_x': 1, 'bottom_y': 4, 'width': 3, 'height': 3 },
        'rect1': { 'left_x': 5, 'bottom_y': 8, 'width': 3, 'height': 3 },
        'reslt': None
    },

]


class Rect:

    def __init__(self, rect):
        self.rect_dict = rect
        self.left = rect['left_x']
        self.right = rect['left_x'] + rect['width']
        self.bottom = rect['bottom_y']
        self.top = rect['bottom_y'] - rect['height']
        self.area = rect['width'] * rect['height']

    @property
    def corners(self):
        return [
            [self.left, self.top],
            [self.right, self.top],
            [self.right, self.bottom],
            [self.left, self.bottom]
        ]

    def contains_points(self, points):
        """
        points: list/tuple of [x, y]
        returns true if ANY point is within the rectangle
        """
        for point in points:
            x, y = point
            x_in = x >= self.left and x <= self.right
            y_in = y >= self.top and y <= self.bottom
            return x_in and y_in
        return False

def find_intersection(rect1, rect2):
    r1 = Rect(rect1)
    r2 = Rect(rect2)
    # ensure an intersection exists
    intersect = False
    # TODO: tidy this into a class method and use an OR
    if r2.contains_points(r1.corners) or r1.contains_points(r2.corners):
        # we have intersection!
        # TODO: classmethod
        left = max(r1.left, r2.left)
        top = max(r1.top, r2.top)
        right = min(r1.right, r2.right)
        bottom = min(r1.bottom, r2.bottom)
        return {
            'left_x': left,
            'bottom_y': bottom,
            'width': right - left,
            'height': bottom - top
        }
    return None

def test(func):
	for test in testcases:
		st = datetime.now()
		actual = func(test['rect1'], test['rect2'])
		end = datetime.now()
		res = actual ==  test['reslt']
		if res:
			print "OK: %s (%sms)" % (test['description'], (end - st).microseconds)
		else:
			print "FAIL: %s expected: %s, actual: %s" % (test['description'], test['reslt'], actual)

test(find_intersection)

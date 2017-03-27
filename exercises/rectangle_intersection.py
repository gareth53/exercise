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

What if there is no intersection? Does your function do something reasonable
in that case?

What if one rectangle is entirely contained in the other? Does your function do
something reasonable in that case?

What if the rectangles don't really intersect but share an edge? Does your
function do something reasonable in that case?

Do some parts of your function seem very similar? Can they be refactored so
you repeat yourself less?
"""

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
        points: list/tuple of [x, y] lists
        returns true if ANY point is within the rectangle
        """
        for point in points:
            x, y = point
            x_in = x > self.left and x < self.right
            y_in = y > self.top and y < self.bottom
            if x_in and y_in:
                return True
        return False

    def get_intersection(self, other):
        if self.contains_points(other.corners) or other.contains_points(self.corners):
            # we have intersection!
            left = max(self.left, other.left)
            top = max(self.top, other.top)
            right = min(self.right, other.right)
            bottom = min(self.bottom, other.bottom)
            return Rect({
                'left_x': left,
                'bottom_y': bottom,
                'width': right - left,
                'height': bottom - top
            })
        return None

def find_intersection(rect1, rect2):
    intersect = Rect(rect1).get_intersection(Rect(rect2))
    return intersect.rect_dict if intersect else None

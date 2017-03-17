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

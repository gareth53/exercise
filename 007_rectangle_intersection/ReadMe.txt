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

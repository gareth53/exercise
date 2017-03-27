"""
https://www.interviewcake.com/question/python/balanced-binary-tree

Write a function to see if a binary tree is "superbalanced" (a new tree
property we just made up).
A tree is "superbalanced" if the difference between the depths of any two
leaf nodes is no greater than one.

Gotchas
Your first thought might be to write a recursive function, thinking, "the tree
is balanced if the left subtree is balanced and the right subtree is balanced."
This kind of approach works well for some other tree problems.

But this isn't quite true. Counterexample: suppose that from the root of our
tree:

The left subtree only has leaves at depths 10 and 11.
The right subtree only has leaves at depths 11 and 12.
Both subtrees are balanced, but from the root we will have leaves at 3 different
 depths.

We could instead have our recursive function get the list of distinct leaf
depths for each subtree. That could work fine. But let's come up with an
iterative solution instead. It's usually better to use an iterative solution
instead of a recursive one because it avoids stack overflow.
"""

class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(x, y, length):
            if length == 1:
                return Node(grid[x][y], True)

            length //= 2

            top_left = helper(x, y, length)
            top_right = helper(x, y + length, length)
            bot_left = helper(x + length, y, length)
            bot_right = helper(x + length, y + length, length)

            children_are_leaves = top_left.isLeaf and top_right.isLeaf and bot_left.isLeaf and bot_right.isLeaf

            same_values = top_left.val == top_right.val == bot_left.val == bot_right.val

            if children_are_leaves and same_values:
                return Node(top_left.val, True)
            
            return Node(1, False, top_left, top_right, bot_left, bot_right)
        
        return helper(0, 0, len(grid))

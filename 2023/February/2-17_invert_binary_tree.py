# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time | O(n) space
    # In the worst case, the queue will contain all the leaf nodes of a full binary tree (i.e. n / 2)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        while queue:
            node = queue.popleft()

            if not node:
                continue
            
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)

        return root

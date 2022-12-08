class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = self.getLeaves(root1, [])
        leaves2 = self.getLeaves(root2, [])
        return leaves1 == leaves2

    def getLeaves(self, root, leaves):
        if root:
            self.getLeaves(root.left, leaves)

            if not root.left and not root.right:
                leaves.append(root.val)

            self.getLeaves(root.right, leaves)

        return leaves

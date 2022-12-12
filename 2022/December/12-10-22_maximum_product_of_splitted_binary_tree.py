class Solution:
    # O(N) time | O(N) space
    # Notice that the function does two things:
    #   1) Finds the subtree sum rooted at node.
    #   2) Updates the max product seen so far.
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.total = 0

        def subtreeSum(node):
            if not node:
                return 0
            left = subtreeSum(node.left)
            right = subtreeSum(node.right)
            subtree_sum = node.val + left + right
            self.ans = max(self.ans, subtree_sum * (self.total - subtree_sum))
            return subtree_sum
        
        self.total = subtreeSum(root)
        subtreeSum(root)
        MOD = 10**9 + 7
        return self.ans % MOD

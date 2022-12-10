class Solution:
    # O(n) time | O(n) space
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def subtreeSum(root):
            total = 0
            stack = [root]

            while stack:
                node = stack.pop()
                if not node:
                    continue
                total += node.val
                stack.append(node.left)
                stack.append(node.right)

            return total

        total = subtreeSum(root)
        
        def findMaxProduct(node):
            subtree_sum = 0
            if not node:
                return subtree_sum

            left_sum = findMaxProduct(node.left)
            right_sum = findMaxProduct(node.right)

            subtree_sum = node.val + left_sum + right_sum
            product = (total - subtree_sum) * subtree_sum
            self.ans = max(self.ans, product)

            return subtree_sum

        self.ans = 0
        MOD = 10**9 + 7
        findMaxProduct(root)
        return self.ans % MOD

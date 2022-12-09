class Solution:
    # O(n) time | O(n) space
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def getMaxDiff(root, _min, _max):
            if not root:
                return _max - _min
            
            val = root.val
            _min = min(_min, val)
            _max = max(_max, val)

            left = getMaxDiff(root.left, _min, _max)
            right = getMaxDiff(root.right, _min, _max)

            return max(left, right)

        return getMaxDiff(root, root.val, root.val)

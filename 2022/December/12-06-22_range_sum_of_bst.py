# O(n) time | O(n) space
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    stack = [root]
    ans = 0

    while stack:
        node = stack.pop()
        
        if not node:
            continue

        val = node.val
        if low <= val:
            stack.append(node.left)
        if val <= high:
            stack.append(node.right)
        
        if low <= val <= high:
            ans += val
    
    return ans

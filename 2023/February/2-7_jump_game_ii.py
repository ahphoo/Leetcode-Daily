class Solution:
    # O(n) time | O(1) space
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        window_end = 0
        max_idx = 0
        ans = 0

        for i in range(n - 1):
            max_idx = max(max_idx, i + nums[i])

            if i == window_end:
                window_end = max_idx
                ans += 1
        
        return ans

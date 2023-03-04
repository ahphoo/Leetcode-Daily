class Solution:
    # O(n) time | O(1) space
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        minKIdx, maxKIdx, badIdx = -1, -1, -1
        n = len(nums)

        for i in range(n):
            num = nums[i]

            if not minK <= num <= maxK:
                badIdx = i
            if num == minK:
                minKIdx = i
            if num == maxK:
                maxKIdx = i
            
            count = max(0, min(minKIdx, maxKIdx) - badIdx)
            ans += count

        return ans

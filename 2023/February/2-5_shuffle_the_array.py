class Solution:
    # O(n) time | O(n) space
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if n <= 1:
            return nums
        
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        
        return res

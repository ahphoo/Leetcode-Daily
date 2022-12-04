class Solution:
    # O(n) time | O(1) space
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        
        min_diff = float('inf')
        min_idx = 0
        prefix_sum = 0
        
        for i in range(n):
            prefix_sum += nums[i]
            
            first = prefix_sum // (i + 1)
            last = total - prefix_sum
            if i != (n - 1):
                last //= (n - i - 1)
                
            current_diff = abs(first - last)
            
            if current_diff < min_diff:
                min_diff = current_diff
                min_idx = i
        
        return min_idx

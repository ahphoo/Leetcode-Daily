class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        min_sum = float('inf')
        cur_sum_max = float('-inf')
        cur_sum_min = float('inf')
        _sum = 0

        for num in nums:
            cur_sum_max = max(cur_sum_max + num, num)
            max_sum = max(max_sum, cur_sum_max)

            cur_sum_min = min(cur_sum_min + num, num)
            min_sum = min(min_sum, cur_sum_min)

            _sum += num
        
        if min_sum == _sum:
            return max_sum

        return max(max_sum, _sum - min_sum)

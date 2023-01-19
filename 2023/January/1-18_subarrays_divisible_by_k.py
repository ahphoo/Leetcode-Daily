class Solution:
    # O(k + n) time | O(k) space
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        prefix_remainder = 0
        num_subarrays_with_remainder = [0] * k
        num_subarrays_with_remainder[0] = 1

        for i in range(n):
            prefix_remainder = (prefix_remainder + (nums[i] % k + k)) % k
            res += num_subarrays_with_remainder[prefix_remainder]
            num_subarrays_with_remainder[prefix_remainder] += 1
        
        return res

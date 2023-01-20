class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        seq = [[nums[0]]]
        _set = set()

        for i in range(1, n):
            new_seq = []

            for s in seq:
                comb = s + [nums[i]]
                key = tuple(comb)
                if key not in _set and nums[i] >= s[-1]:
                    new_seq.append(comb)
                    _set.add(key)

            seq += [[nums[i]]]
            seq += new_seq
        
        ans = []
        for s in seq:
            if len(s) >= 2:
                ans.append(s)

        return ans

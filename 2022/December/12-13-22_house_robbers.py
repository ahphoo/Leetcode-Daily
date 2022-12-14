class Solution:
    # O(N) time | O(1) space
    def rob(self, nums: List[int]) -> int:
        two_house = 0
        one_house = 0

        for num in nums:
            one_house, two_house = max(num + two_house, one_house), one_house
        
        return one_house

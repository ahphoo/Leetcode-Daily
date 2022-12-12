class Solution:
    # O(n) time | O(1) space
    def climbStairs(self, n: int) -> int:
        one_step = 1
        two_step = 1

        for i in range(1, n):
            one_step, two_step = two_step, one_step + two_step 

        return two_step

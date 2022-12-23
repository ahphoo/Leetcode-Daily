class Solution:
    # O(n) time | O(1) space
    def maxProfit(self, prices: List[int]) -> int:
        sold = float('-inf')
        held = float('-inf')
        reset = 0

        for price in prices:
            sold, held, reset = held + price, max(reset - price, held), max(reset, sold)

        return max(sold, reset)

class Solution:
    # O(rows * cols) time | O(cols) space
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1) + 1
        cols = len(text2) + 1
        dp = [[0] * cols for _ in range(2)]

        for i in range(1, rows):
            for j in range(1, cols):
                if text1[i - 1] == text2[j - 1]:
                    dp[i % 2][j] = dp[(i % 2) - 1][j - 1] + 1
                else:
                    dp[i % 2][j] = max(dp[(i % 2) - 1][j], dp[i % 2][j - 1])

        return dp[(rows % 2) == 0][cols - 1]

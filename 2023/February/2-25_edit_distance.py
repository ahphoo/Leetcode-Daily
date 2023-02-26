class Solution:
    # O(M * N) time | O(min(M, N)) space - space optimized version.
    # M is the length of word1. N is the length of word2.
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == "":
            return len(word2)
        if word2 == "":
            return len(word1)

        rows = len(word1) + 1
        cols = len(word2) + 1

        dp = [[0] * cols for _ in range(2)]

        for i in range(2):
            dp[i][0] = i

        for j in range(cols):
            dp[0][j] = j
        
        for i in range(1, rows):
            if i > 1:
                dp[i % 2][0] = i

            for j in range(1, cols):
                if word1[i - 1] == word2[j - 1]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1]
                else:
                    insert = dp[i % 2][j - 1]
                    delete = dp[(i - 1) % 2][j]
                    replace = dp[(i - 1) % 2][j - 1]
                    dp[i % 2][j] = min(insert, delete, replace) + 1
        
        return dp[(rows - 1) % 2][-1]

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]

        for j in range(cols):
            dp[0][j] = matrix[0][j]

        for i in range(1, rows):
            for j in range(cols):
                if j == 0:
                    min_path = min(dp[i - 1][j], dp[i - 1][j + 1])
                elif j == cols - 1:
                    min_path = min(dp[i - 1][j - 1], dp[i - 1][j])
                else:
                    min_path = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])

                dp[i][j] = min_path + matrix[i][j]
        
        return min(dp[rows - 1])

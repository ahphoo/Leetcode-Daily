class Solution:
    # O(n^2) time | O(n^2) space
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        dp = [[-1] * n for _ in range(n)]
        pairs = [None] * n

        for i in range(n):
            pairs[i] = (ages[i], scores[i])

        pairs.sort()

        def findBestScore(prev: int, i: int) -> int:
            if i >= n:
                return 0
            if dp[prev + 1][i] != -1:
                return dp[prev + 1][i]

            prev_score = pairs[prev][1]
            curr_score = pairs[i][1]
            
            if prev == -1 or prev_score <= curr_score:
                dp[prev + 1][i] = max(findBestScore(prev, i + 1), curr_score + findBestScore(i, i + 1))
                return dp[prev + 1][i]
            
            dp[prev + 1][i] = findBestScore(prev, i + 1)
            return dp[prev + 1][i]
            

        return findBestScore(-1, 0)

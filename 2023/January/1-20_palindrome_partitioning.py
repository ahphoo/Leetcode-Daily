class Solution:
    # O(N * 2^N) time | O(N^2) space
    # In the worst case, there could be 2^N substrings. Each substring takes O(N) time to build.
    # We use a 2-D dp array of size N * N.
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        dp = [[False] * n for _ in range(n)]
        
        def backtrack(s, start, part, dp):
            if start >= n:
                res.append(part.copy())

            for end in range(start, n):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    part.append(s[start:end + 1])
                    backtrack(s, end + 1, part, dp)
                    part.pop()
        
        backtrack(s, 0, [], dp)
        return res

class Solution:
    # O(N) time | O(N) space
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1

        score = [0] * n

        for a, b in trust:
            score[a - 1] -= 1
            score[b - 1] += 1

        for i in range(n):
            if score[i] == n - 1:
                return i + 1
        
        return -1

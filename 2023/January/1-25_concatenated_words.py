class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        s = set(words)

        for word in words:
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):
                if i == n:
                    start = 1
                else:
                    start = 0
                
                for j in range(start, i + 1):
                    dp[i] = dp[i] or (dp[j] and (word[j:i] in s))
            
            if dp[n]:
                res.append(word)
                
        return res 

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(s)
        adj = [[] for _ in range(n)]
        ans = 0

        for i in range(1, n):
            adj[parent[i]].append(i)

        def dfs(node, parent):
            nonlocal ans

            longestChain = 0
            secondLongestChain = 0

            for child in adj[node]:
                chain = dfs(child, node)

                if s[child] == s[node]:
                    continue
                if chain > longestChain:
                    longestChain, secondLongestChain = chain, longestChain
                elif chain > secondLongestChain:
                    secondLongestChain = chain

            ans = max(ans, longestChain + 1 + secondLongestChain)
            return longestChain + 1

        dfs(0, -1)
        return ans

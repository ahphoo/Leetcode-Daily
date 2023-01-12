class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = defaultdict(list)
        ans = [0] * n
    
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
    
        def dfs(node: int, parent: int):
            cnt = Counter(labels[node])
            for child in g[node]:
                if child != parent:
                    cnt += dfs(child, node)
            ans[node] = cnt[labels[node]]
            return cnt
            
        dfs(0, -1)
        return ans

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        fuel = 0
    
        def dfs(node, parent, adj, seats):
            nonlocal fuel
            representatives = 1

            for child in adj[node]:
                if child != parent:
                    representatives += dfs(child, node, adj, seats)
    
            if node != 0:
                fuel += ceil(representatives / seats)

            return representatives
    
        n = len(roads) + 1
        adj = [[] for _ in range(n)]

        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)

        dfs(0, -1, adj, seats)
        return fuel

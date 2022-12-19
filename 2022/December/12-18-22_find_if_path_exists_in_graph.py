class Solution:
    # O(V + E) time | O(V + E) space
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        seen = [False] * n
        stack = [source]

        while stack:
            node = stack.pop()

            if node == destination:
                return True
            if seen[node]:
                continue
            
            seen[node] = True

            for neighbor in adj_list[node]:
                stack.append(neighbor)
            
        return seen[destination]

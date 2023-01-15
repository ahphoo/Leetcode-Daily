class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        adj = defaultdict(list)
        val_to_nodes = defaultdict(list)
        uf = [i for i in range(n)]
        rank = [0] * n

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        for i in range(n):
            val_to_nodes[vals[i]].append(i)
            
        def find(x: int) -> int:
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x: int, y: int) -> None:
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return
            elif rank[root_x] < rank[root_y]:
                uf[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                uf[root_y] = root_x
            else:
                uf[root_y] = root_x
                rank[root_x] += 1

        ans = 0

        for _, nodes in sorted(val_to_nodes.items()):
            for node in nodes:
                for neig in adj[node]:
                    if vals[node] >= vals[neig]:
                        union(node, neig)

            group = defaultdict(int)

            for node in nodes:
                root = find(node)
                group[root] += 1

            for _, size in group.items():
                print(size)
                ans += (size * (size + 1)) // 2

        return ans

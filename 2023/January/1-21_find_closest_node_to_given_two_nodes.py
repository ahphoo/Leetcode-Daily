class Solution:
    # O(N) time | O(N) space - N is the number of nodes in the graph
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [float('inf')] * n
        dist2 = [float('inf')] * n
        dist1[node1] = 0
        dist2[node2] = 0
        minimum_dist = float('inf')
        ans = -1

        adj = defaultdict(list)
        for i in range(n):
            j = edges[i]
            if j == -1:
                continue
            adj[i].append(j)
        
        def bfs(node: int, dist: List[int], length: int) -> None:
            queue = deque([node])
            seen = set()

            while queue:
                curr = queue.popleft()
                seen.add(curr)

                length += 1

                for neigh in adj[curr]:
                    if neigh in seen:
                        continue
                    queue.append(neigh)
                    dist[neigh] = length

        bfs(node1, dist1, 0)
        bfs(node2, dist2, 0)

        for i in range(n):
            current_dist = max(dist1[i], dist2[i])

            if current_dist < minimum_dist:
                minimum_dist = current_dist
                ans = i
            elif current_dist == minimum_dist:
                ans = min(ans, i)
        
        return ans

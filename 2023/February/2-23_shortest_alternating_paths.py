class Solution:
    # O(n + e) time | O(n + e) space
    # n is the number of nodes, e is the number of edges
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a, b in redEdges:
            graph[a].append((b, "red"))
        for a, b in blueEdges:
            graph[a].append((b, "blue"))

        ans = [-1] * n
        queue = deque([ (0, "no_color", 0) ])
        seen = { (0, "red"), (0, "blue") }

        while queue:
            node, prev_color, length = queue.popleft()

            if ans[node] == -1:
                ans[node] = length

            length += 1

            for neighbor, color in graph[node]:
                if (neighbor, color) in seen:
                    continue
                if prev_color == color:
                    continue
                queue.append((neighbor, color, length))
                seen.add((neighbor, color))

        return ans

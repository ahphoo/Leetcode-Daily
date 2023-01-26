class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for start, end, price in flights:
            adj[start].append((end, price))

        stops = [float('inf')] * n

        pq = [(0, src, 0)]

        while pq:
            total_cost, city, steps = heapq.heappop(pq)

            if city == dst:
                return total_cost

            if steps > stops[city] or steps > k:
                continue

            stops[city] = steps
            for neigh, cost in adj[city]:
                heapq.heappush(pq, (total_cost + cost, neigh, steps + 1))

        return -1

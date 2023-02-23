class Solution:
    # O(nlogn) time | O(n) space
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        min_heap = [(capital[i], profits[i], i) for i in range(n)]
        heapify(min_heap)
        max_heap = []

        for _ in range(min(k, n)):

            while min_heap and min_heap[0][0] <= w:
                _, profit, i = heappop(min_heap)
                heappush(max_heap, (-profit, i))

            if max_heap:
                w += -heappop(max_heap)[0]
        
        return w

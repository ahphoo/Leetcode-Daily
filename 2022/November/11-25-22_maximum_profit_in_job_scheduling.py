class Solution:
    # O(nlogn) time | O(n) space
    # sorting + priority queue
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(list(zip(startTime, endTime, profit)))
        pq = []
        max_profit = 0
        n = len(jobs)
        
        for i in range(n):
            start, end, profit = jobs[i]
            
            while pq and pq[0][0] <= start:
                _, chain_profit = heappop(pq)
                max_profit = max(chain_profit, max_profit)
                
            heappush(pq, (end, max_profit + profit))
            
        while pq:
            _, chain_profit = heappop(pq)
            max_profit = max(chain_profit, max_profit)
            
        return max_profit

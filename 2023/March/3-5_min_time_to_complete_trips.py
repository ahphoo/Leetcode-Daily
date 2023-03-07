class Solution:
    # O(nlog(n)) time | O(1) space
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lo = 1
        hi = max(time) * totalTrips

        while lo < hi:
            mid = lo + (hi - lo) // 2

            trips = sum(mid // t for t in time)

            if trips < totalTrips:
                lo = mid + 1
            else:
                hi = mid
        
        return hi

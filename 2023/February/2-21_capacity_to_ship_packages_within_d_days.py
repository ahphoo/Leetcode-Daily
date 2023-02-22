class Solution:
    # O(n) time | O(1) space
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(capacity: int, current_days: int) -> bool:
            load = 0

            for weight in weights:
                load += weight
                if load > capacity:
                    load = weight
                    current_days -= 1
                    if current_days <= 0:
                        return False
            
            return True
        
        lo = max(weights)
        hi = sum(weights)

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if canShip(mid, days):
                hi = mid
            else:
                lo = mid + 1

        return lo

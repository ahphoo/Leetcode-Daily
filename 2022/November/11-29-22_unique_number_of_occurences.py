class Solution:
    # O(n) time | O(n) space
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        s = set()
        
        for num in count:
            if count[num] in s:
                return False
            s.add(count[num])
            
        return True

class Solution:
    # O(n) time | O(1) space - sliding window
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i, j = 0, 0

        while j < n:
            chars[i] = chars[j]
            count = 0

            while j < n and chars[i] == chars[j]:
                count += 1
                j += 1
            
            i += 1

            if count <= 1:
                continue

            for digit in str(count):
                chars[i] = digit
                i += 1
        
        return i

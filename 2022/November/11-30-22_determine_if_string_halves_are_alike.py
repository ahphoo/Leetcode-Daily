class Solution:
    # O(n) time | O(1) space
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        freq = 0
        vowels = set('aeiouAEIOU')
        
        for i in range(n // 2):
            if s[i] in vowels:
                freq += 1
        
        for i in range(n // 2, n):
            if s[i] in vowels:
                freq -= 1
        
        return freq == 0

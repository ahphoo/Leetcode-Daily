class Solution:
    # O(n) time | O(1) space
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        same_chars = freq1.keys() == freq2.keys()
        same_freq = Counter(freq1.values()) == Counter(freq2.values())
        
        return same_chars and same_freq

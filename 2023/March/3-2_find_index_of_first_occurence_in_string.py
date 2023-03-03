class Solution:
    # O(n) time | O(n) space - KMP (Knuth-Morris-Pratt)
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        def getLongestPrefixSuffix(s, m):
            prevLps = 0
            i = 1
            lps = [0] * m
    
            while i < m:
                if s[i] == s[prevLps]:
                    lps[i] = prevLps + 1
                    prevLps += 1
                    i += 1
                elif prevLps != 0:
                    prevLps = lps[prevLps - 1]
                else:
                    i += 1
    
            return lps

        lps = getLongestPrefixSuffix(needle, m)

        i, j = 0, 0
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j != 0:
                j = lps[j - 1]
            else:
                i += 1
            
            if j == m:
                return i - m
        
        return -1


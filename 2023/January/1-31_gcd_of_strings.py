class Solution:
    # O(m + n) time | O(m + n) space.
    # m is the length of str1. n is the length of str2.
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        n = gcd(len(str1), len(str2))
        return str1[:n]

class Solution:
    # O(m + n) time | O(1) space
    # m is the length of a. n is the length of b.
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y != 0:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]

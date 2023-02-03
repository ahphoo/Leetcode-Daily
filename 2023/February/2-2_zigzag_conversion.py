class Solution:
    # O(n) time | O(1) space
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = ''
        n = len(s)
        charsInSection = 2 * (numRows - 1)

        for row in range(numRows):
            middle_row = 0 < row < numRows - 1

            for i in range(row, n, charsInSection):
                ans += s[i]

                if not middle_row:
                    continue

                charsAbove = 2 * row
                charsBetween = charsInSection - charsAbove
                j = i + charsBetween

                if j < n:
                    ans += s[j]
        
        return ans

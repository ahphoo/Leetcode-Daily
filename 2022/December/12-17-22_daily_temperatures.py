class Solution:
    # O(n) time | O(n) space
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, idx = stack.pop()
                ans[idx] = i - idx
            stack.append([temp, i])

        return ans

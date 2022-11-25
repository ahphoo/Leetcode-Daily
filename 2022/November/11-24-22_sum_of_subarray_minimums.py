class Solution:
    # O(n) time | O(n) space
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        n = len(arr)
        stack = [0]
        res = [0] * n
        
        for i in range(n):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
                
            j = stack[-1]
            res[i] = res[j] + (i - j) * arr[i]
            stack.append(i)
        
        return sum(res) % (10**9 + 7)

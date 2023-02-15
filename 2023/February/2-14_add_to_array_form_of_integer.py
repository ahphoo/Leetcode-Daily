class Solution:
    # O(n) time | O(1) space
    # n is the length of num.
    # Note: k is at most 10^4, which is 5 digits, so in the case when k > 0 it is O(1) to
    # convert k into an array-form integer.
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num) - 1, -1, -1):
            k += num[i]
            num[i] = k % 10
            k //= 10
        
        if k > 0:
            return [int(i) for i in str(k)] + num
            
        return num

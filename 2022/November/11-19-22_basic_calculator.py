class Solution:
    # O(n) time | O(n) space
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        operand = 0
        res = 0
        
        for c in s:
            if c.isdigit():
                operand = (operand * 10) + int(c)
            elif c == '+':
                res += sign * operand
                sign = 1
                operand = 0
            elif c == '-':
                res += sign * operand
                sign = -1
                operand = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif c == ')':
                res += sign * operand
                res *= stack.pop()
                res += stack.pop()
                operand = 0

        
        return res + sign * operand

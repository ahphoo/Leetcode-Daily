class Solution:
    # O(n) time | O(n) space
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']

        def evaluate(a, b, op):
            if op == '+':
                return a + b
            if op == '-':
                return a - b
            if op == '*':
                return a * b
                
            return int(a / b)

        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(evaluate(a, b, token))
            else:
                stack.append(int(token))
        
        return stack.pop()

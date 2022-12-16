class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    # O(1) time | O(n) space
    def push(self, x: int) -> None:
        self.in_stack.append(x)

    # O(1) amortized time | O(1) space
    def pop(self) -> int:
        if not self.out_stack:
            self.transfer()
        return self.out_stack.pop()

    # O(1) amortized time | O(1) space
    def peek(self) -> int:
        if not self.out_stack:
            self.transfer()
        return self.out_stack[-1]

    # O(n) time | O(n) space
    def transfer(self) -> None:
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    # O(1) time | O(1) space
    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

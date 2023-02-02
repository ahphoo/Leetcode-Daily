class Solution:
    # O(w) time | O(1) space.
    # w is the length of the longest string in words. Since the length of order is always 26, space complexity is constant.
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m = len(words)
        n = len(order)

        if m == 1:
            return True

        position = [0] * n
        for i in range(n):
            char = order[i]
            position[ord(char) - ord('a')] = i

        def inOrder(a: str, b: str) -> bool:
            len_a = len(a)
            len_b = len(b)

            for i in range(len_a):
                if i >= len_b:
                    return False

                char_a = ord(a[i]) - ord('a')
                char_b = ord(b[i]) - ord('a')

                if position[char_a] < position[char_b]:
                    return True
                if position[char_a] > position[char_b]:
                    return False

            return True
            
        for i in range(m - 1):
            w1 = words[i]
            w2 = words[i + 1]
            if not inOrder(w1, w2):
                return False
        
        return True

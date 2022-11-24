class Solution:
    # O(m*n*3^k) time | O(k) space - m is the # of rows, n is the # of cols, k is the length of the word
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        n = len(word)
        
        def dfs(i, j, k):
            if i < 0 or j < 0 or i >= rows or j >= cols: 
                return False
            if board[i][j] != word[k]:
                return False
            
            letter, board[i][j] = board[i][j], '*'
            k += 1
            
            ans = (k == n) \
                or dfs(i + 1, j, k) \
                or dfs(i - 1, j, k) \
                or dfs(i, j + 1, k) \
                or dfs(i, j - 1, k)
            
            board[i][j] = letter
            return ans
            
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
                
        return False

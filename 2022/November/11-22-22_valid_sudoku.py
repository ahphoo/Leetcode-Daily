class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                
                if n == '.':
                    continue
                
                k = (3*(i // 3)) + (j // 3)
                if n in row_set[i] or n in col_set[j] or n in box_set[k]:
                    return False
                
                row_set[i].add(n)
                col_set[j].add(n)
                box_set[k].add(n)
                
        return True

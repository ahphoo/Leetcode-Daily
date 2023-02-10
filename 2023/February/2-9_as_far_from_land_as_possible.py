class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque([])
        distance = -1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q.append((i, j))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for x, y in neighbors:
                    if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] >= 1:
                        continue
                    q.append((x, y))
                    grid[x][y] = 1
            distance += 1    
        
        if distance == 0:
            return -1
            
        return distance

class Solution:
    # O(mn) time | O(max(m, n)) space - m is the # of rows, n is the # of cols
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        r, c = entrance
        
        queue = deque([(r, c, 0)])
        
        while queue:
            x, y, steps = queue.popleft()
            
            if x < 0 or y < 0 or x >= rows or y >= cols or maze[x][y] == '+':
                continue
            if (x in [0, rows - 1] or y in [0, cols - 1]) and (x, y) != (r, c):
                return steps
            
            maze[x][y] = '+'
            steps += 1

            queue.append((x - 1, y, steps));
            queue.append((x + 1, y, steps));
            queue.append((x, y - 1, steps));
            queue.append((x, y + 1, steps));
        
        return -1

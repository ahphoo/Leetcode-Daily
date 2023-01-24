class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [0] * (n**2 + 1)
        ans = float('inf')
        queue = deque([1])
        i = 1

        forwards = list(range(0, n))
        backwards = list(range(n - 1, -1, -1))
        direction = 1

        for row in range(n - 1, -1, -1):
            if direction == 1:
                columns = forwards
            else:
                columns = backwards

            for col in columns:
                cells[i] = (row, col)
                i += 1

            direction *= -1

        dist = [-1] * (n**2 + 1)
        dist[1] = 0

        while queue:
            curr = queue.popleft()

            for square in range(curr + 1, min(curr + 6, n**2) + 1):
                row, col = cells[square]
                dest = board[row][col]
                if dest == -1:
                    dest = square

                if dist[dest] == -1:
                    dist[dest] = dist[curr] + 1
                    queue.append(dest)
        
        return dist[n**2]

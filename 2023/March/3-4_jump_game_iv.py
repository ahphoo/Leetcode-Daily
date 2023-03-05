class Solution:
    # O(n) time | O(n) space - Modified BFS
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        nei = defaultdict(list)

        for i in range(n):
            nei[arr[i]].append(i)

        idx_visited, nums_visited = {-1, n}, set()
        queue = deque([(0, 0)])

        while queue:
            idx, steps = queue.popleft()

            if idx == n - 1:
                return steps
            if idx in idx_visited:
                continue
            idx_visited.add(idx)
                
            steps += 1
            queue.append((idx - 1, steps))
            queue.append((idx + 1, steps))

            num = arr[idx]

            if num in nums_visited:
                continue
            nums_visited.add(num)

            for i in nei[num]:
                if i not in idx_visited:
                    queue.append((i, steps))
            
        return -1

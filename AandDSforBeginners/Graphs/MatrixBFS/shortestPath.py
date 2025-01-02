class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        N = len(grid)
        visit = set()
        queue = deque([(0, 0, 1)])
        visit.add((0, 0))
        neighbors = [[0, 1], [0, -1], [1, 1], [1, -1], [-1, -1], [-1, 1], [1, 0], [-1, 0]]

        while queue:
            r, c, length = queue.popleft()
            if (min(r, c) < 0 or
            max(r, c) >= N or grid[r][c]):
                continue

            if r == N - 1 and c == N - 1:
                return length

            for dr, dc in neighbors:
                if (r + dr, c + dc) not in visit:
                    queue.append((r + dr, c + dc, length + 1))
                    visit.add((r + dr, c + dc))

        return -1

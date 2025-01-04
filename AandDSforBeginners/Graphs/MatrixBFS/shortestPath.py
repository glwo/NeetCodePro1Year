class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        seen = set()
        q.append((0, 0, 1))
        seen.add((0, 0))

        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        while q:
            r, c, length = q.popleft()

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 1:
                continue

            if r == ROWS - 1 and c == COLS - 1:
                return length

            for dr, dc in neighbors:
                if (r + dr, c + dc) not in seen:
                    q.append((r + dr, c + dc, length + 1))
                    seen.add((r + dr, c + dc))

        return -1

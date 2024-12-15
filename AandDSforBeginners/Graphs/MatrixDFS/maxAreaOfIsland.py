class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def dfs(grid, r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            count = 1

            count += dfs(grid, r + 1, c)
            count += dfs(grid, r - 1, c)
            count += dfs(grid, r, c + 1)
            count += dfs(grid, r, c - 1)

            return count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num = dfs(grid, r, c)
                    maxArea = max(maxArea, num)

        return maxArea

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def dfs_iterative(grid, start_r, start_c):
            stack = [(start_r, start_c)]
            area = 0
            while stack:
                r, c = stack.pop()
                if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                    continue
                grid[r][c] = 0
                area += 1
                stack.append((r + 1, c))
                stack.append((r - 1, c))
                stack.append((r, c + 1))
                stack.append((r, c - 1))
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs_iterative(grid, r, c)
                    maxArea = max(maxArea, area)

        return maxArea

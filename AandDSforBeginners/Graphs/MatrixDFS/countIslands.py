class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(grid, r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(grid, r, c)
                    count += 1

        return count

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs_iterative(grid, start_r, start_c):
            stack = [(start_r, start_c)]
            while stack:
                r, c = stack.pop()
                if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                    continue
                grid[r][c] = "0"
                stack.append((r + 1, c))
                stack.append((r - 1, c))
                stack.append((r, c + 1))
                stack.append((r, c - 1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs_iterative(grid, r, c)
                    count += 1

        return count

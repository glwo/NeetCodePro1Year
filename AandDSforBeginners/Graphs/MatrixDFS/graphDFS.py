class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def helper(grid: List[List[int]], r: int, c: int, visit: set) -> int:
            if (min(r, c) < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == 1):
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            visit.add((r, c))

            count = 0
            count += helper(grid, r + 1, c, visit)
            count += helper(grid, r - 1, c, visit)
            count += helper(grid, r, c + 1, visit)
            count += helper(grid, r, c - 1, visit)

            visit.remove((r, c))
            return count

        return helper(grid, 0, 0, set())

    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        stack = [(0, 0, set())]
        path_count = 0

        while stack:
            r, c, visit = stack.pop()

            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1):
                continue
            if r == ROWS - 1 and c == COLS - 1:
                path_count += 1
                continue

            new_visit = visit.copy()
            new_visit.add((r, c))

            stack.append((r + 1, c, new_visit))
            stack.append((r - 1, c, new_visit))
            stack.append((r, c + 1, new_visit))
            stack.append((r, c - 1, new_visit))

        return path_count

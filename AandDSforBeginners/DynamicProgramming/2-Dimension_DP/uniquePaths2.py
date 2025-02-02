# Top down dp
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = {(M - 1, N - 1): 1}

        def dfs(r, c):
            if r == M or c == N or grid[r][c]:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[(r, c)]

        return dfs(0, 0)

# Bottom up dp
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[M - 1][N - 1] == 1:
            return 0
        dp = [[0] * (N + 1) for _ in range(M + 1)]


        dp[M - 1][N - 1] = 1

        for r in range(M - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if grid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] += dp[r + 1][c]
                    dp[r][c] += dp[r][c + 1]

        return dp[0][0]

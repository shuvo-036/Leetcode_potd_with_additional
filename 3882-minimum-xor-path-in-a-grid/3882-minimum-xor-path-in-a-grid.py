class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[set() for j in range(n)] for i in range(m)]

        dp[0][0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                up = set()
                left = set()

                if i > 0:
                    up = dp[i-1][j]

                if j > 0:
                    left = dp[i][j-1]

                combined = up | left

                for xorVal in combined:
                    resultXorVal = xorVal ^ grid[i][j]
                    dp[i][j].add(resultXorVal)

        for xorVal in range(1024):
            if xorVal in dp[m-1][n-1]:
                return xorVal

        return -1

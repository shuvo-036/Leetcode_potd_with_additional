class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        
        m= len(grid)
        n = len(grid[0])
        dp = [[[-1] * 2 for _ in range(n)] for _ in range(m)]
        mod = 10 **9+7

        def dfs(i,j,d):
            if i < 0 or j < 0 or i>=m or j >=n:
                return 0
            
            if i == m-1 and j == n-1:
                return 1
            
            if i>= m or j >= n:
                return 0
            
            if dp[i][j][d] != -1:
                return dp[i][j][d]

            if grid[i][j] == 1:
                if d == 0:
                    dp[i][j][d] = dfs(i + 1, j, 1)
                else:
                    dp[i][j][d] = dfs(i, j + 1, 0)
            else:
                dp[i][j][d] = (
                        dfs(i, j + 1, 0) + dfs(i + 1, j, 1)
                    ) % mod
            return dp[i][j][d]
        return dfs(0, 0, 0)
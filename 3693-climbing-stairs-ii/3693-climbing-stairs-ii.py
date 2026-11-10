class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        dp = [-1] * (n + 1)

        def solve(i):

            if i == n:
                return 0

            if dp[i] != -1:
                return dp[i]

            ans = float('inf')

            if i + 1 <= n:
                ans = min(ans, costs[i] + 1 + solve(i + 1))

            if i + 2 <= n:
                ans = min(ans, costs[i + 1] + 4 + solve(i + 2))

            if i + 3 <= n:
                ans = min(ans, costs[i + 2] + 9 + solve(i + 3))

            dp[i] = ans
            return dp[i]

        return solve(0)
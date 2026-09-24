class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0] * (n+1)
        def ways(n):
            if n == 1 or n < 1:
                return 1
            if dp[n]:
                return dp[n]
            
            dp[n] = ways(n-1) + ways(n-2)
            return dp[n]

        return ways(n)
        
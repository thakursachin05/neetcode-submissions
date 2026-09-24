class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)
        def dfs(i):
            if i >= len(cost):
                return 0
            if dp[i]:
                return dp[i]
            if i == 0:
                dp[i] = min(cost[i] + min(dfs(i+1), dfs(i+2)), cost[i+1] + min(dfs(i+2), dfs(i+3)))
                return dp[i]
            
            dp[i] = cost[i] + min(dfs(i+1), dfs(i+2))
                
            return dp[i]

        return dfs(0)
        
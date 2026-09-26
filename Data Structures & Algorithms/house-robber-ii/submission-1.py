class Solution:
    def rob(self, nums: List[int]) -> int:
    
        def dfs(i, limit, dp):
            if i >= limit:
                return 0

            if dp[i] != -1:
                return dp[i]

            dp[i] = max(nums[i] + dfs(i+2, limit,dp), dfs(i+1, limit,dp))
            return dp[i]
        
        n = len(nums)
        dp = [-1] * (n+1)
        first = dfs(0, n-1, dp)
        dp1 = [-1] * (n+1)
        second = dfs(1,n,dp1)


        return max(first, second, nums[0])
        
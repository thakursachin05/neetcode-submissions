class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [[-1] * (n + 1) for _ in range(n)]
        
        def dfs(i, prev):
            if i >= len(nums):
                return 0
            res = 0
            
            if dp[i][prev + 1] != -1:
                return dp[i][prev+ 1]
            
            if prev == -1 or nums[i] > nums[prev]:
                 res = max(res, 1 + dfs(i + 1, i))
            
            # Choice 2: Skip the current element (prev stays exactly the same!)
            res = max(res, dfs(i + 1, prev))
            dp[i][prev + 1] = res 
            return res
        
        return dfs(0, -1)
        
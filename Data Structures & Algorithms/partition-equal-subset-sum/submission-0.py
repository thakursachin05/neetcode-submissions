class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum1 = 0
        for num in nums:
            sum1 += num
        if sum1%2 != 0:
            return False
        dp = [[-1] * (50001) for _ in range(len(nums)+1)]
        def dfs(i, sum2):
            if i >= len(nums) or sum2 < 0:
                return False
            
            if sum2 == 0:
                return True
            
            if dp[i][sum2]!=-1:
                return dp[i][sum2]
            
            dp[i][sum2] = dfs(i+1, sum2-nums[i]) or dfs(i+1, sum2)
            return dp[i][sum2]

        
        return dfs(0, sum1//2)
        
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return nums[0]

        dp = [0] * (len(nums) + 1)
        dp[0], dp[1] = nums[0], max(nums[1], nums[0])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+ dp[i-2], max(dp[i-1], dp[i-2]))
        
        return max(dp[len(nums)-1], dp[len(nums)])
        
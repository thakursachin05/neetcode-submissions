class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        subset = []

        def dfs(i, currentSum):
            if i < len(nums) and currentSum == target:
                result.append(subset.copy())
                return
            if i >= len(nums) or currentSum > target:
                return
            subset.append(nums[i])
            dfs(i, currentSum + nums[i])
            subset.pop()
            dfs(i+1, currentSum)
        
        dfs(0,0)
        return result
            
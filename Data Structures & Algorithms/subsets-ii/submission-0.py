class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        
        dfs(0)

        unique_tuples = set(tuple(x) for x in res)
    

        return [list(x) for x in unique_tuples]
            
        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        visited = {nums[0]}
        for i in range(1,len(nums)):
            print(nums[i])
            if nums[i] in visited:
                return True
            visited.add(nums[i])
        return False
        
        
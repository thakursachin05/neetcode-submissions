class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        prefix[0] = nums[0]
        
        suffix[len(nums)-1] = nums[len(nums)-1]
        print(suffix)
        
        for i in range(len(nums) -1):
            prefix[i+1] = prefix[i] * nums[i+1]

        print(prefix)

        for i in range(len(nums) -1, 0, -1):
            suffix[i-1] = suffix[i] * nums[i-1]

        print(suffix)
        for i in range(len(nums)):
            left = prefix[i-1] if i > 0 else 1
            right = suffix[i+1] if i < len(nums)-1 else 1

            res[i] = left * right

        return res

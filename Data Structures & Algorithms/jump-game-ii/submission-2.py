class Solution:
    def jump(self, nums: List[int]) -> int:
        minSteps = float('inf')
        steps = [float('inf')] * len(nums)
        steps[0] = 0

        for i in range(len(nums) - 1):
            l = i+1
            r = min(i + nums[i], len(nums)-1)
            while l <= r:
                # print(l, r) 
                steps[l] = min(steps[i] + 1, steps[l])
                l += 1
        # print(steps)
        return steps[len(nums)-1]
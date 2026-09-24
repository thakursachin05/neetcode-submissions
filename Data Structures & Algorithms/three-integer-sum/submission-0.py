class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i>0 and a == nums[i-1]:
                continue

            target = -nums[i]
            l,r = i+1, len(nums)-1

            while l<r:
                sum = nums[l] + nums[r]
                if sum < target:
                    l += 1
                elif sum > target:
                    r -=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res

        
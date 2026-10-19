class Solution:
    def merge(self, nums1, nums2):
        l = r = 0
        temp = []
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                temp.append(nums1[l])
                l+=1
            else:
                temp.append(nums2[r])
                r+=1
        
        while l < len(nums1):
            temp.append(nums1[l])
            l+=1

        while r < len(nums2):
            temp.append(nums2[r])
            r += 1
        return temp


    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        lo, hi = 0, len(nums)-1
        print(lo, hi, nums)

        
        mid = (lo+hi)//2

        left = self.sortArray(nums[lo : mid + 1])
        right = self.sortArray(nums[mid + 1 : hi + 1])
        return self.merge(left,right)
        
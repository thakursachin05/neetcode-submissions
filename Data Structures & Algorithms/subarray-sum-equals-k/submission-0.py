class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        curr = 0
        res = 0
        for num in nums:
            curr += num
            if mp.get(curr-k,0):
                res += mp[curr-k]
            mp[curr] = 1 + mp.get(curr,0)
        return res
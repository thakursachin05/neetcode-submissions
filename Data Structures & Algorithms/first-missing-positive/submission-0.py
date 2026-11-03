class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        seen = [False] * (n + 1)
        for num in nums:
            if num > 0 and num <= n:
                seen[num] = True

        for num in range(1, n + 1):
            if not seen[num]:
                return num

        return n + 1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestSum = float('-inf')
        summ = 0
        for num in nums:
            summ += num
            bestSum = max(bestSum, summ)
            if summ < 0:
                summ = 0
        return bestSum
        
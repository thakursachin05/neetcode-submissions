class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        res = 0
        for num in prices:
            res = max(res, num-minPrice)
            minPrice = min(minPrice, num)
        return res
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        maxSuffixArr = [0]*n
        maxSuffixArr[n-1] = heights[n-1]
        for i in range(1, n):
            maxSuffixArr[n-i-1] = max(maxSuffixArr[n-i], heights[n-i-1])
        result = []
        for i in range(n):
            if heights[i] >= maxSuffixArr[i] and heights[i] > heights[i+1] if i+1 < n else True:
                result.append(i)

        return result
        
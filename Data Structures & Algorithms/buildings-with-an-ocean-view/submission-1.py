class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        i = n-1
        result = []
        maxH = 0
        while i >= 0:
            if heights[i] > maxH:
                result.append(i)
            maxH = max(maxH, heights[i])
            i -= 1
            
        return result[:][::-1]



        
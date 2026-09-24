class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [[0, heights[0]]]
        maxArea = -float('inf')
        for h in range(1, len(heights)):
            left = h
            while len(stack) and stack[-1][1] > heights[h]:
                area = stack[-1][1] * (h - stack[-1][0])
                # print('area', area, stack)
                maxArea = max(area, maxArea)
                left = stack[-1][0]
                stack.pop()
            stack.append([left, heights[h]])
            # print("final stack", stack)
         
        while len(stack):
            area = stack[-1][1] * (len(heights) - stack[-1][0])
            # print('area', area, stack)
            maxArea = max(area, maxArea)
            stack.pop()

        return maxArea
        
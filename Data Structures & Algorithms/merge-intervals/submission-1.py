class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            newInterval = intervals[i]
            if newInterval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], newInterval[1])
            else:
                result.append(intervals[i])
        return result
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] > intervals[i][0]:
                res[-1][1] = min(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return len(intervals) - len(res)
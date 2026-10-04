class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            heapq.heappush(minHeap, ((x**2 + y**2), [x,y]))
        result = []
        while k:
            dist, pair = heapq.heappop(minHeap)
            # print(dist, pair)
            result.append(pair)
            k -= 1
        return result



        
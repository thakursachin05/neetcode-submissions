class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-1 * x for x in stones]
        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            x, y = -heapq.heappop(minHeap), -heapq.heappop(minHeap)
            if x == y:
                continue
            else:
                heapq.heappush(minHeap, -(x-y))
        return -minHeap[0] if len(minHeap) > 0 else 0
        
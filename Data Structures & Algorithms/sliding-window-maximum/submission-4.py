import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        result = []
        max_heap = []
        for i in range(left, k):
            heapq.heappush(max_heap, (-nums[i], i))
        left = k
        while left < len(nums):
            maxElement, pos = max_heap[0]
            # print(max_heap, left, left-k, maxElement, pos, pos < left-k)
            while max_heap and (pos < left-k):
                heapq.heappop(max_heap)
                maxElement, pos = max_heap[0]
                
            result.append(-maxElement)
            heapq.heappush(max_heap, (-nums[left], left))
            left += 1
        maxElement, pos = max_heap[0]
        # print(max_heap, left, left-k, maxElement, pos)
        while max_heap and (pos < left-k):
            maxElement, pos = heapq.heappop(max_heap)
        result.append(-maxElement)
        return result
        
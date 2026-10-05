class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        minHeap = [[-y, x] for x, y in count.items()]

        heapq.heapify(minHeap)

        queue = deque()

        time = 0

        while minHeap or queue:
            time += 1
            if queue and time == queue[0][0]:
                heapq.heappush(minHeap, queue[0][1])
                queue.popleft()
            if minHeap:
                freq, ele = heapq.heappop(minHeap)
                new_freq = freq + 1
                if new_freq < 0:
                    queue.append((time + n + 1, [new_freq, ele]))
        
        return time


        
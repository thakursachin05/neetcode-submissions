class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = {i: [] for i in range(n)}
        min_stops = [float('inf')] * n
        for src1, dst1, cost in flights:
            adjList[src1].append([dst1, cost])
        
        minHeap = [[0, src, 0]]
        visited = set()
        while minHeap:
            # print(minHeap)
            cost1, node, stops = heapq.heappop(minHeap)
            # print(cost1, node, stops)

            if node == dst:
                return cost1
            
            if stops > k or stops >= min_stops[node]:
                continue
            
            min_stops[node] = stops
            

            for nei, cost2 in adjList[node]:
                heapq.heappush(minHeap, [cost1+cost2, nei, stops+1])

        return -1

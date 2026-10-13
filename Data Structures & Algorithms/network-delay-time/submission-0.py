class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = [[] for i in range(n+1)]

        for u, v, w in times:
            adjList[u].append((v,w))

        minHeap = [(0,k)]
        visited = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = w1
            for n2, w2  in adjList[n1]:
                heapq.heappush(minHeap, [w1+w2, n2])
        return t if len(visited) == n else -1



        
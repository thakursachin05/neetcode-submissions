class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                adj[i].append([cost, j])
                adj[j].append([cost, i])
        
        minHeap = [[0,0]]
        visited = set()
        res = 0
        while len(visited) != N:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            res += cost 
            visited.add(node)
            for cost1, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, [cost1, nei])
        
        return res

        
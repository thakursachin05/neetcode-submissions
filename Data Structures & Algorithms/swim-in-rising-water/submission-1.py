class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        visited.add((0,0))
        N = len(grid)

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            
            if r == N-1 and c == N-1:
                return t
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr == N or nc == N or ((nr,nc) in visited):
                    continue
                visited.add((nr,nc))
                heapq.heappush(minHeap, [max(t,grid[nr][nc]), nr, nc])

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        freshOranges = 0
        queue = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    freshOranges += 1
        minutes = 0
        while queue and freshOranges:
            minutes += 1
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for x, y in directions:
                    nr, nc = r+x, c+y
                    
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        freshOranges -= 1
                        queue.append((nr,nc))
                        
        return minutes if freshOranges == 0 else -1
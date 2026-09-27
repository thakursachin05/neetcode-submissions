class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        
        def dfs(i,j):
            if i < 0 or i >= len(grid) or j <0 or j>=len(grid[0]) or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            
            current_area = 1
            for x,y in directions:
                current_area += dfs(i+x,j+y)

            return current_area
        
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = max(area,dfs(i,j))
        
        return area
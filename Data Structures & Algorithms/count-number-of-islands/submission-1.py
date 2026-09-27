class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        
        def dfs(i,j):
            if i < 0 or i >= len(grid) or j <0 or j>=len(grid[0]) or grid[i][j] == '0':
                return 
            
            grid[i][j] = '0'
            

            for x,y in directions:
                dfs(i+x,j+y)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count+=1
                    dfs(i,j)
        
        return count
